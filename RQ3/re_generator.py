import csv
import re
import xml.dom.minidom
import os


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


def convert_to_reg(content):
    content = content.replace(" [", r"\[")
    content = content.replace("]", r"\]")
    content = content.replace("(", r"\(")
    content = content.replace(")", r"\)")
    content = content.replace("*", r"\*")
    content = content.replace("- 1", r"-[0-9]+")
    content = content.replace("1", r"[0-9]+")
    content = content.replace(" {", r"(\s)*\{(\s)*")
    content = content.replace("}", r"(\s)*\}(\s)*")
    content = content.replace(" ++", r"\+\+")
    content = content.replace(" +", r' \+')

    content = content.replace("|", r"\|")
    content = content.replace(".", r"\.")
    content = content.replace("\"x\"", "\".*\"")
    content = content.replace("x --", r"[^ .;()]+--")
    content = content.replace(r"x \(", r"[^ .;()]+\(")
    content = content.replace("x", "[^ .;()]+")

    return content


if __name__ == "__main__":
    csv.field_size_limit(500 * 1024 * 1024)
    star_idxs = [4, 8]
    key_count = 0

    for i in range(len(star_idxs) - 1):
        left = star_idxs[i]
        right = star_idxs[i + 1]
        xml_path = "Type-2 xml/cw_1000_java_%d_%d_functions-blind.xml" % (left, right)

        if not os.path.exists(xml_path):
            # print("Skip")
            continue
        process_xml(xml_path)

        csv_path = "Type-4 csv/%d_%d.csv" % (left, right)

        false_dict = dict()
        with open(csv_path, encoding='utf_8_sig', errors='ignore') as f:
            for row in csv.DictReader(f, skipinitialspace=True):
                pred = row['predictions']
                repo = row['repo']

                if pred == "False":
                    false_dict.update({int(repo): pred})

        DOMTree = xml.dom.minidom.parse(xml_path)
        clones = DOMTree.documentElement
        classes = clones.getElementsByTagName("class")

        counter = 0
        sources = DOMTree.getElementsByTagName('source')

        test_list = []
        for i in range(len(sources)):
            s = sources[i].childNodes[0].nodeValue.strip()
            source_path = sources[i].attributes["file"].value

            repo = int(source_path.split("/")[-1].split(".")[0].split("_")[1])

            if not false_dict.__contains__(repo):
                # print(false_dict[repo])
                continue

            function_body = s[s.find("{") + 1:s.rfind("}") - 1]
            # print(s)
            if function_body.strip().count("\n") == 0:
                # print(s)
                continue
            code_content = s.split('\n')

            code_fragment = ""
            skip_head = False
            Length_exceed = False
            for (j, line) in enumerate(code_content):
                if line.__contains__("@"):
                    continue
                if not skip_head:
                    line = convert_to_reg(line)
                    code_fragment += '/' + line
                    skip_head = True
                    continue

                line = line.strip()
                line = convert_to_reg(line)

                if len(line) == 0:
                    continue
                if j == len(code_content) - 2 and code_content[j + 1] == "}":
                    code_fragment += line.strip()
                else:
                    code_fragment += line.strip() + r"[\s]*"

            if not os.path.exists("reg_txt"):
                os.makedirs("reg_txt")

            print(f"Writing to reg_txt/{left}_{right}.txt")
            f = open("reg_txt/%d_%d.txt" % (left, right), "a", encoding='utf-8')

            code_fragment = code_fragment + '/'

            f.write(str(repo) + ".java " + code_fragment + " language:Java \n")
