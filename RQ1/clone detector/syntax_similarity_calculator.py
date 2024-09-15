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
        source_path = code[i].attributes["file"].value
        start_line = int(code[i].attributes['startline'].value)
        end_line = int(code[i].attributes['endline'].value)


        if source_path.__contains__("prompt"):
            # synthetic code
            repo_num = int(source_path.split('/')[3].split('_')[1].split(".java")[0])
        else:
            # source code.
            print(source_path)
            repo_num = int(source_path.split('/')[3].split('.')[0])

        if function_length_count.__contains__(repo_num):
            function_length_count[repo_num] = max(function_length_count[repo_num], end_line - start_line)
        else:
            function_length_count.update({repo_num: end_line - start_line})

    return function_length_count


if __name__ == "__main__":
    # This script is a basic implementation of syntax similarity calculator.
    lang = "java"

    LANGUAGE = Language('build/my-languages.so', lang)
    parser = Parser()
    parser.set_language(LANGUAGE)

    # warning: the xml file should be consistent with the csv file.
    syn_code_xml_path = "example/Type-2 xml/cw_1000_java_4_8_functions-blind-crossclones/cw_1000_java_4_8_functions-blind.xml"
    source_code_xml_path = "example/Type-2 xml/cw_1000_java_4_8_functions-blind-crossclones/source_functions-blind.xml"
    csv_path = "example/Type-4 csv/4_8.csv"

    # Format xml
    process_xml(syn_code_xml_path)
    process_xml(source_code_xml_path)

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

        if not type_4_dict.__contains__(str(source_repo_num)) or type_4_dict[str(source_repo_num)] == 'false':
            # print("skip")
            continue

        # Remove the function signature which is provided in the prompt.
        if lang == 'c' or lang == 'java':
            s = s[s.find('{') + 2:len(s) - 2]
        elif lang == 'python':
            s = s[s.find(':') + 9:len(s) - 7]

        source_lines = s.split('\n')
        source_token = getTokens(parser, s)

        # print(len(syn_code))
        for j in range(len(syn_code)):
            syn_path = syn_code[j].attributes["file"].value
            start_line = int(syn_code[j].attributes['startline'].value)
            end_line = int(syn_code[j].attributes['endline'].value)

            cur_syn_num = int(syn_path.split('/')[3].split('_')[1].split(".java")[0])
            if not cur_syn_num == source_repo_num or syn_count[cur_syn_num] != end_line - start_line:
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

            # print("----")
            # print(res)
            # print(s)
            # print("---")

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
                # print("Type-1 or Type-2 clones, skip")
                continue

    # You can print the results you want
    print("Weakly Type 3 Count = %d" % weakly_type_3)
    print("Moderate Type 3 Count = %d" % moderate_type_3)
    print("Strong type 3 count = %d" % strong_type_3)
    print("Very Strong type 3 count = %d" % very_strong_type_3)