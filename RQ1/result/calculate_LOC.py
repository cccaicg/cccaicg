import os
import re
from collections import Counter

def clear_code(code_str, lang):
    if lang in ['c', 'java']:
        comment_reg = "([ \t]*((\/\*(?:\*(?!\/)|[^\*])*\*\/\n)|(//[^\n]*\n)))+"
    elif lang == 'python':
        comment_reg = '([ \t]*((#[^\n]*)|(\'\'\'(\'(?!(\'\'))|[^\'])*\'\'\')|(\"\"\"(\"(?!(\"\"))|[^\"])*\"\"\"))(\n|$)*)+'
    else:
        print("Language Error!")
        return
    comment_list = re.finditer(comment_reg, code_str, re.I | re.S | re.U)

    for item in comment_list:
        code_str = code_str.replace(item.group(), '\n')

    res = ""
    for l in code_str.split("\n"):
        if len(l.strip()) != 0:
            res += l + "\n"

    res = res.strip()

    return res


def find_func_body(code):
    begin_idx = code.find('{')
    end_idx = code.rfind('}')
    return code[begin_idx:end_idx + 1]


def calculate_more_than_5_LOC(counter):
    more_than_five_LOC = 0
    for data in counter.keys():
        if data >= 5:
            more_than_five_LOC += counter[data]

    return more_than_five_LOC


tool = "cw"
lang = "java"

global_longer_count = 0
global_file_count = 0

clear_comment_iter_list = []
syn_path = f"data/{tool}/{lang}/Type-1 clones/"

keep_comment_list = []
clear_comment_list = []

test_count = 0
file_count = 0
for root, dirs, file in os.walk(syn_path):

    if len(file) == 0:
        continue

    for f in file:
        syn_file = root + "/" + f
        content = open(syn_file, 'r', encoding='utf-8').read()

        if lang == "py":
            clear_comment_code = clear_code(content, 'python')
            func_body = clear_comment_code[clear_comment_code.find(":") + 1:len(clear_comment_code)]
            generated_LOC_clear_comment = len(func_body.strip().split("\n"))


        elif lang == "c":
            fun_body = find_func_body(content)
            generated_LOC_clear_comment = (find_func_body(clear_code(content, "c")).count("\n") - 1)


        else:
            fun_body = find_func_body(content)
            generated_LOC_clear_comment = (find_func_body(clear_code(content, "java")).count("\n") - 1)
            #print(find_func_body(clear_code(content, "java")))
            # rint(fun_body)
            #print(generated_LOC_clear_comment)

            if generated_LOC_clear_comment >= 5:
                test_count += 1


        file_count += 1

        clear_comment_list.append(generated_LOC_clear_comment)


clear_comment_counter = Counter(clear_comment_list)
global_longer_count += calculate_more_than_5_LOC(clear_comment_counter)
global_file_count += file_count

print(global_longer_count)
print(global_file_count)
print(global_longer_count / global_file_count)
