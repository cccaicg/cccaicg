import json
import re
import os
import xml.dom.minidom
import lizard
import scipy.stats

# import matplotlib.pyplot as plt
from tree_sitter import Language, Parser

Language.build_library(
    'build/my-languages.so',

    [
        'vendor/tree-sitter-java',
        'vendor/tree-sitter-c',
        'vendor/tree-sitter-python'
    ]
)


def clear_code(code_str,lang):
    if lang in ['c','java']:
        comment_reg = "([ \t]*((\/\*(?:\*(?!\/)|[^\*])*\*\/\n)|(//[^\n]*\n)))+"
    elif lang == 'python':
        comment_reg = '([ \t]*((#[^\n]*)|(\'\'\'(\'(?!(\'\'))|[^\'])*\'\'\')|(\"\"\"(\"(?!(\"\"))|[^\"])*\"\"\"))(\n|$)*)+'
    else:
        print("Language Error!")
        return
    comment_list = re.finditer(comment_reg, code_str, re.I | re.S | re.U)

    for item in comment_list:
        code_str = code_str.replace(item.group(),'\n')

    res = ""
    for l in code_str.split("\n"):
        if len(l.strip()) != 0:
            res += l + "\n"
    res = res.strip()

    return res


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
    tree = parser.parse(bytes(code_snippet, "utf_8"))
    root_node = tree.root_node

    tokens_index = tree_to_token_index(root_node)
    loc = code_snippet.split('\n')
    tokens = [index_to_code_token(x, loc) for x in tokens_index]
    if tokens.__contains__(""):
        tokens.remove("")

    return tokens


def get_search_code_similarity():
    # This function is used to calculate the code similarity which is searched in RQ3.
    for interval in star_idxs:
        xml_path = f"source/xml/{interval}_functions-blind-crossclones/{interval}_functions-blind-crossclones-0.00-classes-withsource.xml"

        DOMTree = xml.dom.minidom.parse(xml_path)
        element = DOMTree.documentElement
        code = element.getElementsByTagName("source")

        search_code_list = []
        search_dict = dict()
        syn_dict = dict()
        for j in range(len(code)):
            code_path = code[j].attributes["file"].value

            s = code[j].childNodes[0].nodeValue.strip()
            if code_path.split("/")[1] == "search_results":
                cur_repo = code_path.split("/")[2]
                search_code_list.append(s)
                search_dict.update({s: int(cur_repo)})
            else:
                cur_repo = code_path.split("/")[-1].split(".java")[0].split("prompt_")[1]
                syn_dict.update({s: int(cur_repo)})

        for syn_code in syn_dict.keys():
            cur_repo = syn_dict[syn_code]

            if f"{interval}_{cur_repo}" not in t2_comment_length_dict.keys():
                continue
            # print("Current interval %d-%d" % (left, right))
            # print(cur_repo)
            counter = 0
            score = 0
            for c in search_code_list:
                if search_dict[c] == cur_repo:
                    # print(syn_code)
                    syn_code = clear_code(syn_code, "java")

                    syn_tokens = getTokens(parser, syn_code)
                    cur_code_tokens = getTokens(parser, c)
                    match_token = 0

                    #print(c)
                    if syn_tokens.__contains__("") and len(syn_tokens) != len(cur_code_tokens):
                        syn_tokens.remove("")
                    if cur_code_tokens.__contains__("") and len(syn_tokens) != len(cur_code_tokens):
                        cur_code_tokens.remove("")

                    if len(syn_tokens) != len(cur_code_tokens):
                        # Normally, the searched code should have the same tokens with the results.
                        # However, Sometimes the results will match another completion results in the dataset.
                        print("ERROR... two code fragment do not match...")
                        continue

                    for i in range(len(syn_tokens)):
                        if syn_tokens[i] == cur_code_tokens[i]:
                            match_token += 1

                    score += match_token / len(syn_tokens)
                    counter += 1
            # print(counter)
            print(f"{interval}_{cur_repo}")
            cur_comment = comment_dict[f"{interval}_{cur_repo}"]
            x.append(cur_comment)
            y.append(score)


def get_proxy_dataset_code_similarity():
    for interval in star_idxs:
        for f in os.listdir(f"dataset/type2/RQ1/{interval}"):
            file_name = f.split("prompt_")[1]
            cur_repo = int(f.split("prompt_")[1].split(".java")[0])

            # the code file in RQ1/ is the Type-2 clones we collect from RQ1
            # They have been applied exact search through GitHub to confirm they are real Type-2.
            source_code = open(f"source/code/{interval}/{file_name}", 'r',encoding='utf-8').read()
            syn_code = open(f"dataset/type2/RQ1/{interval}/{f}",'r',encoding='utf-8').read()

            source_code = clear_code(source_code, 'java')
            syn_code = clear_code(syn_code, 'java')

            syn_tokens = getTokens(parser, syn_code)
            source_code_tokens = getTokens(parser, source_code)
            match_token = 0

            if syn_tokens.__contains__("") and len(syn_tokens) != len(source_code_tokens):
                syn_tokens.remove("")
            if source_code_tokens.__contains__("") and len(syn_tokens) != len(source_code_tokens):
                source_code_tokens.remove("")

            for i in range(len(syn_tokens)):
                if syn_tokens[i] == source_code_tokens[i]:
                    match_token += 1

            score = match_token / len(syn_tokens)

            cur_comment = comment_dict[f"{interval}_{cur_repo}"]
            x.append(cur_comment)
            y.append(score)



if __name__ == "__main__":
    x = []
    y = []
    code_file = "dataset/"

    lang = 'java'
    LANGUAGE = Language('build/my-languages.so', lang)

    parser = Parser()
    parser.set_language(LANGUAGE)
    star_idxs = ['4_8', '8_16', '2048_4096']
    comment_dict = dict()
    t2_comment_length_dict = dict()

    for interval in star_idxs:
        json_file = open(f"new_func/java/java_func_star_{interval}.json", 'r' ,encoding='utf-8')


        for (i,l) in enumerate(json_file.readlines()):
            comment = json.loads(l)['docstring']
            comment_dict.update({f"{interval}_{i}": len(comment)})

    for roots, dirs, files in os.walk(code_file):
        for f in files:
            cur_file = roots + "/" + f

            cur_repo = int(f.split(".java")[0].split("_")[1])
            cur_interval = roots.split("\\")[-1]

            # print(cur_file)
            if roots.find("no_clone") != -1:
                x.append(comment_dict[f"{cur_interval}_{cur_repo}"])
                # x.append(int(lizard.analyze_file(cur_file).average_cyclomatic_complexity))
                y.append(0)
                continue
            if roots.find("type1") != -1:
                x.append(comment_dict[f"{cur_interval}_{cur_repo}"])
                y.append(1)
                continue

            t2_comment_length_dict.update({f"{cur_interval}_{cur_repo}": comment_dict[f"{cur_interval}_{cur_repo}"]})

    get_search_code_similarity()
    get_proxy_dataset_code_similarity()
    print(len(x))
    print(len(y))
    print(scipy.stats.spearmanr(x, y))
