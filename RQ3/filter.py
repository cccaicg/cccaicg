import os
import re
import shutil

reg_no_match = "No results matched your search"
reg_warning = 'ERROR_TYPE_RESULTS_INCOMPLETE'
reg_error = "regular expressions must be surrounded by slashes."
reg_failed = "failed"
reg_file_count = 'Box-sc-g0xbh4-0 cgQapc'
star_range = ['4_8','8_16','2048_4096']

for i in star_range:
    print(f"Processing... {i}")
    html_path = 'html/%s/' % i

    counter = 0
    counter_total = 0
    valid_file_list = []

    for f in os.listdir(html_path):
        html_file = open(html_path + f, 'r', encoding='utf-8', errors='ignore')
        content = html_file.read()
        html_file.close()

        # print(content.find(reg_warning))
        if content.find(reg_warning) != -1:
            os.remove(html_path + f)
            # print(f)
            continue

        if content.find(reg_error) != -1:
            # print(f)
            os.remove(html_path + f)
            continue

        if content.find(reg_failed) != -1:
            # print(f)
            os.remove(html_path + f)
            continue

        idx = content.find(reg_file_count)
        if idx != -1:
            # print(f)

            content = content[idx + 41:idx + 50]
            if content[0] == "M":
                # More than 100 files..
                os.remove(html_path + f)

                continue

            first_whitespace = content.find(" ")
            content = content[:first_whitespace]

            # if int(content) > 20:
            #     # os.remove(html_path + f)
            #     # print(content)
            #     # print(f)
            #     # continue

            # print(content)
            counter_total += 1


            if int(content) != 0:
                # print(f)

                valid_file_list.append(f)
                counter += 1
                continue
        else:
            print(f)

    # if not os.path.exists(f"download_html/{i}"):
    #     os.makedirs(f"download_html/{i}")
    # for f in valid_file_list:
    #     shutil.copy(os.path.join(html_path,f), os.path.join(f"download_html/{i}/", f))

    print(counter_total)