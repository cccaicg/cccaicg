import os
import re

reg = "href=\"https://github.com/[^\"]*\.java"

star_range = ['4_8','8_16','2048_4096']
counter = 0
for i in star_range:

    file_path = "valid_html/%s/" % i
    for fi in os.listdir(file_path):
        # print(f)
        f = open(file_path + fi, 'r', encoding='utf-8', errors='ignore')
        content = f.read()
        list = re.findall(reg, content)

        download_set = set()
        for l in list:
            # print(l)
            l = l[6:len(l)]
            l = l.replace("github.com", "raw.githubusercontent.com")
            l = l.replace("/blob", "")
            download_set.add(l)

        if len(download_set) == 0:
            continue

        # print(str(i) + str(download_set))
        cur_file = "download_file/%s/" % i + fi.split('.html')[0]
        print(cur_file)
        if not os.path.exists(cur_file):
            os.makedirs(cur_file)

        for cur_item in download_set:
            cmd = "wget -P %s " % cur_file + cur_item + " --no-check-certificate"
            os.system(cmd)
            pass

        counter += 1
