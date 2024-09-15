import csv
import os
import xml.dom.minidom
import re
import numpy as np
from tqdm import tqdm
from tree_sitter import Language, Parser

Language.build_library(
    'build/my-languages.so',

    [
        'vendor/tree-sitter-java',
        'vendor/tree-sitter-c',
        'vendor/tree-sitter-python'
    ]
)


def tree_to_token_index(root_node):
    if (len(root_node.children) == 0 or root_node.type.find('string') != -1) and root_node.type != 'comment':
        return [(root_node.start_point, root_node.end_point)]
    else:
        code_tokens = []
        for child in root_node.children:
            code_tokens += tree_to_token_index(child)
        return code_tokens


def index_to_code_token(index, code):
    start_point = index[0]
    end_point = index[1]
    if start_point[0] == end_point[0]:
        s = code[start_point[0]][start_point[1]:end_point[1]]
    else:
        s = ""
        s += code[start_point[0]][start_point[1]:]
        for i in range(start_point[0] + 1, end_point[0]):
            s += code[i]
        s += code[end_point[0]][:end_point[1]]
    return s


def getTokens(parser, code_snippet):
    tree = parser.parse(bytes(code_snippet, "utf8"))
    root_node = tree.root_node

    tokens_index = tree_to_token_index(root_node)

    loc = code_snippet.split('\n')

    tokens = [index_to_code_token(x, loc) for x in tokens_index]
    if tokens.__contains__(""):
        tokens.remove("")

    return tokens


def find_common_tokens(dp, s, t, flag):
    i = len(s)
    j = len(t)
    common_tokens = []

    while i > 0 and j > 0:
        if flag[i][j] == 1:
            common_tokens.append(s[i - 1])
            i -= 1
            j -= 1
        elif flag[i][j] == 2:
            i -= 1
        else:
            j -= 1

    common_tokens.reverse()

    return common_tokens


def lcs(s, t):
    len_1 = len(s)
    len_2 = len(t)

    res = np.zeros((len_1 + 1, len_2 + 1))
    flag = np.zeros((len_1 + 1, len_2 + 1))
    for i in range(1, len_1 + 1):
        for j in range(1, len_2 + 1):
            if s[i - 1] == t[j - 1]:
                res[i][j] = 1 + res[i - 1][j - 1]
                flag[i][j] = 1
            else:
                res[i][j] = max(res[i - 1][j], res[i][j - 1])
                if (res[i - 1][j] > res[i][j - 1]):
                    flag[i][j] = 2
                else:
                    flag[i][j] = 3

    return res, flag


def process_xml(xml_path):
    xml = open(xml_path, 'r+', encoding='utf-8', errors='ignore')

    original = ["&", '>', "<", ]
    target = ["&amp;", "&gt;", "&lt;"]

    content = xml.read()

    if content.startswith("<root>"):
        print("XML is well formatted")
        xml.close()
        return

    xml.seek(0)
    xml.truncate()

    results = re.finditer('</*source[^\n]*>', content, re.I | re.S | re.U)

    for item in results:
        old_str = item.group()
        new_str = 'RandomCharacterL' + old_str[1:-1] + 'RandomCharacterR'
        content = content.replace(old_str, new_str)

    for i in range(len(original)):
        content = content.replace(original[i], target[i])

    # print(content)
    content = content.replace('RandomCharacterL', '<')
    content = content.replace('RandomCharacterR', '>')
    content = '<root>\n' + content + '\n</root>'

    xml.write(content)
    xml.close()


def find_longest_function(code):
    function_length_count = dict()
    for i in range(len(code)):
        path = code[i].attributes["file"].value
        start_line = int(code[i].attributes['startline'].value)
        end_line = int(code[i].attributes['endline'].value)

        if path.__contains__("prompt") or path.__contains__("syn"):
            # synthetic code
            if tool != "copilot":
                repo_num = int(path.split('/')[-1][7:12])
            else:
                repo_num = path.split('/')[-2].split('_')[-1]
                cur_res = path.split('/')[-1]
                repo_num = repo_num + "_" + cur_res
        else:
            # source code.
            repo_num = int(path.split('/')[3].split('.')[0])

        if function_length_count.__contains__(repo_num):
            function_length_count[repo_num] = max(function_length_count[repo_num], end_line - start_line)
        else:
            function_length_count.update({repo_num: end_line - start_line})

    return function_length_count


def extract_syn_numbers(base_path):
    return [x[7:12] for x in os.listdir(base_path)]


def extract_syn_numbers_cop(base_path):
    # return [ x.split('_')[-1] for x in os.listdir(base_path)]
    syn_numbers = set()
    for root, dirs, files in os.walk(base_path):
        if len(files) != 0:
            for f in files:
                repo_num = root.split('syn_')[1]
                syn_numbers.add(repo_num + "_" + f)
    return syn_numbers


star_idx = [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 9000000]
if __name__ == "__main__":
    languages = ['java', 'c', 'python']
    tool = "gpt4o"  # copilot, gpt4o, cw
    csv.field_size_limit(500 * 1024 * 1024)

    for lang in languages:
        LANGUAGE = Language('build/my-languages.so', lang)
        parser = Parser()
        parser.set_language(LANGUAGE)
        for k in range(len(star_idx) - 1):
            left = star_idx[k]
            right = star_idx[k + 1]

            if lang == "python":
                lang = 'py'
            source_code_xml_path = f"./data/{tool}/{lang}/Type-2 xml/{tool}_1000_{lang}_{left}_{right}_functions-blind-crossclones/source_functions-blind.xml"
            syn_code_xml_path = f"./data/{tool}/{lang}/Type-2 xml/{tool}_1000_{lang}_{left}_{right}_functions-blind-crossclones/" \
                                + f"{tool}_1000_{lang}_{left}_{right}_functions-blind.xml"
            csv_path = f"./data/{tool}/{lang}/Type-4 csv/{left}_{right}.csv"

            delete_type1_path = f"./data/{tool}/{lang}/Type-1 clones/{left}_{right}/"
            delete_type2_path = f"./data/{tool}/{lang}/Type-2 clones/{left}_{right}/"

            if lang == 'py':
                lang = "python"

            if not os.path.exists(syn_code_xml_path):
                # print(syn_code_xml_path)
                continue

            print('+'*50)
            print(f"Tool {tool} language {lang} interval {left}_{right} is processing...")

            # Format xml
            process_xml(syn_code_xml_path)
            process_xml(source_code_xml_path)

            if tool != "copilot":
                type_1_repo = extract_syn_numbers(delete_type1_path)
                type_2_repo = extract_syn_numbers(delete_type2_path)
            else:
                type_1_repo = extract_syn_numbers_cop(delete_type1_path)
                type_2_repo = extract_syn_numbers_cop(delete_type2_path)

            type_4_dict = dict()

            # Read Type-4 csv
            with open(csv_path, encoding='utf_8_sig', errors='ignore') as f:
                for row in csv.DictReader(f, skipinitialspace=True):
                    pred = row['predictions']
                    repo = row['repo']

                    # test_test_list.append(repo)
                    if lang == "python":
                        if pred == "1":
                            pred = "True"
                        elif pred == "0":
                            pred = "False"
                        else:
                            continue

                    pred = pred.lower()

                    if tool != "copilot":
                        if str(repo).zfill(5) not in type_2_repo and str(repo).zfill(5) not in type_1_repo:
                            type_4_dict.update({repo: pred})
                    else:
                        if repo not in type_2_repo and repo not in type_1_repo:
                            type_4_dict.update({repo: pred})

            DOMTree_source = xml.dom.minidom.parse(source_code_xml_path)
            DOMTree_syn = xml.dom.minidom.parse(syn_code_xml_path)

            source = DOMTree_source.documentElement
            syn = DOMTree_syn.documentElement

            sources_code = source.getElementsByTagName("source")
            syn_code = syn.getElementsByTagName("source")

            source_count = find_longest_function(sources_code)
            syn_count = find_longest_function(syn_code)

            weakly_type_3 = 0
            moderate_type_3 = 0
            strong_type_3 = 0
            very_strong_type_3 = 0

            for i in tqdm(range(len(sources_code))):
                source_path = sources_code[i].attributes["file"].value
                s = sources_code[i].childNodes[0].nodeValue.strip()
                start_line = int(sources_code[i].attributes['startline'].value)
                end_line = int(sources_code[i].attributes['endline'].value)

                source_repo_num = int(source_path.split('/')[3].split('.')[0])

                if source_count[source_repo_num] != end_line - start_line:
                    continue

                if tool != "copilot":
                    if not type_4_dict.__contains__(str(source_repo_num)) or type_4_dict[str(source_repo_num)] == 'false':
                        continue

                # Remove the function signature which is provided in the prompt.
                if lang == 'c' or lang == 'java':
                    s = s[s.find('{') + 2:len(s) - 2]
                elif lang == 'python':
                    s = s[s.find(':') + 9:len(s) - 7]

                source_lines = s.split('\n')
                source_token = getTokens(parser, s)

                for j in range(len(syn_code)):
                    syn_path = syn_code[j].attributes["file"].value
                    start_line = int(syn_code[j].attributes['startline'].value)
                    end_line = int(syn_code[j].attributes['endline'].value)

                    if tool != "copilot":
                        cur_syn_num = int(syn_path.split('/')[-1][7:12])

                        if not cur_syn_num == source_repo_num or syn_count[cur_syn_num] != end_line - start_line:
                            continue
                    else:
                        cur_syn_num = int(syn_path.split('/')[-2].split('_')[1])

                        if not cur_syn_num == source_repo_num:
                            continue

                        cur_res = syn_path.split('/')[4]

                        full_res = str(source_repo_num) + "_" + cur_res
                        if syn_count[full_res] != end_line - start_line:
                            continue
                        if not type_4_dict.__contains__(full_res) or type_4_dict[full_res] == 'false':
                            continue

                    if lang != "python":
                        try:
                            res = syn_code[j].childNodes[0].nodeValue.strip()
                            reg = r"\{(.*\n)*\}"
                            code_content = re.search(reg, res)
                            if code_content.group().count('\n') - 1 < 2:
                                continue
                        except AttributeError:
                            pass
                    else:
                        res = syn_code[j].childNodes[0].nodeValue.strip()
                        code_content = res[res.find(":") + 9:len(res) - 7]
                        if code_content.count("\n") == 0:
                            continue

                    res = syn_code[j].childNodes[0].nodeValue.strip()

                    if lang == 'c' or lang == 'java':
                        res = res[res.find('{') + 2:len(res) - 2]
                    elif lang == 'python':
                        res = res[res.find(':') + 9:len(res) - 7]


                    res_lines = res.split('\n')
                    res_token = getTokens(parser, res)

                    line_dp, line_flag = lcs(source_lines, res_lines)
                    similar_lines_num = line_dp[-1][-1]

                    token_dp, token_flag = lcs(source_token, res_token)
                    common_tokens = find_common_tokens(token_dp, source_token, res_token, token_flag)

                    similar_tokens = token_dp[-1][-1]

                    max_token_num = max(len(source_token), len(res_token))
                    s_length = len(s.split('\n'))
                    res_length = len(res.split('\n'))

                    line_similarity = similar_lines_num / max(s_length, res_length)
                    token_similarity = float('{:.6f}'.format(similar_tokens / max_token_num))

                    syntax_similarity = min(token_similarity, line_similarity)

                    # print(syntax_similarity)
                    if syntax_similarity < 0.5:
                        weakly_type_3 += 1
                    elif syntax_similarity >= 0.5 and syntax_similarity < 0.7:
                        moderate_type_3 += 1
                    elif syntax_similarity >= 0.7 and syntax_similarity < 0.9:
                        strong_type_3 += 1
                    elif syntax_similarity != 1.0:
                        very_strong_type_3 += 1
                    else:
                        #print("Type-1 or Type-2 clones, skip")
                        continue

            pairs_count = len(syn_count) / 100
            # You can print the results you want
            print("Type-1 clone rate is %.2f" % (len(type_1_repo) / pairs_count))
            print("Type-2 clone rate is %.2f" % ((len(type_2_repo) - len(type_1_repo)) / pairs_count))
            print("Very Strong type 3 rate is %.2f" % (very_strong_type_3 / pairs_count))
            print("Strong type 3 rate is %.2f" % (strong_type_3 / pairs_count))
            print("Moderate Type 3 rate is %.2f" % (moderate_type_3 / pairs_count))
            print("Weakly Type 3 rate is %.2f" % (weakly_type_3 / pairs_count))
