import json
import os

import modify_tools

def create_folder(s):
    if not os.path.exists(s):
        os.makedirs(s)


def raw_output_prompt(file_name,comemnt,signature,lang):
    with open(file_name,'w',encoding='utf-8',errors='ignore') as tar_file:
        if lang in ['c','java']:
            whole_prompt = comemnt.strip() + '\n' + signature  + '\n{'
        elif lang=='python':
            whole_prompt = signature + '    ' + comemnt.replace('\n','\n    ') + '\n'
        tar_file.write(whole_prompt)

# This function may output some warnings.
def check_output_prompt(file_name,comemnt,signature,lang,warning=False):
    if comemnt==None or signature==None:
        with open('information/error_convert.txt', 'a', encoding='utf-8', errors='ignores') as error_file:
            error_file.write(file_name+'\n')
        return True

    if comemnt=='*no_need*' and signature=='*no_need*':
        return False

    if warning:
        with open('information/warning.txt','a',encoding='utf-8',errors='ignores') as warning:
            warning.write(file_name+'\n')

    raw_output_prompt(file_name,comemnt,signature,lang)
    return False


# modify_mdoe:
# 0-paraphrase the comment
# 1-modify the function name 
# 2-modify the parameter names 
# 3-change the parameter order
# modify_option-turn on/of the specific modification
modify_option = (False,True,True,True)
star_idxs = [0,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,9000000]
language = 'python' # c/java/python
data_folder = './data/'# should put a character '/' at last
output_folder = 'modify_outputs/' # the folder to store new prompts
json_folder = 'new_func/' # the folder that stores the source code  json
info_folder = 'information/' # the folder to store some informations such as warinings and errors
if language is None or language not in ['c','java','python']:
    print('please check the language')
    exit()
if not os.path.exists(data_folder):
    print('data_folder not exists')
    exit()




file_postfix = language if language!='python' else 'py'
language_folder = output_folder + language + '/'

create_folder(output_folder)
create_folder(language_folder)
create_folder(info_folder)

with open('information/error_convert.txt', 'w'):
    pass

with open('information/error_word.txt','w'):
    pass

with open('information/warning.txt','w'):
    pass

paraphrase_count = 0

if __name__=='__main__':
    for i in range(len(star_idxs)-1):
        star_range_folder = '%s_%s/'%(star_idxs[i],star_idxs[i+1])
        print('---------'+star_range_folder+'---------')
        clone_folder = data_folder + star_range_folder
        print(clone_folder)
        if not os.path.exists(clone_folder):
            continue

        range_folder = language_folder + star_range_folder
        create_folder(range_folder)

        json_file_path = json_folder + language + '/' + language + '_func_star_%d_%d.json' % (star_idxs[i], star_idxs[i + 1])
        json_file = open(json_file_path,encoding='utf-8',errors='ignore')
        json_lines = json_file.readlines()
        json_file.close()

        clone_prompt_fileNames = os.listdir(clone_folder)
        print(len(clone_prompt_fileNames))
        # paraphrase comment
        if modify_option[0]:
            print('+++' + 'paraphrase comment' + '+++')
            specified_folder = range_folder + 'comment/'
            create_folder(specified_folder)
            for prompt_fileName in clone_prompt_fileNames:
                prompt_id = int(prompt_fileName.split('.')[0].split('_')[-1])
                id_str = '%05d'%(prompt_id)
                prompt_name = specified_folder + 'comment_' + id_str + '.' + file_postfix
                if os.path.exists(prompt_name):
                    continue
                
                json_line = json_lines[prompt_id]
                func_dict = json.loads(json_line)
                old_comment = func_dict['docstring']
                old_signature = func_dict['func_signal']
                new_comment,new_siganture = modify_tools.modify_prompt(old_comment,old_signature,language,0,count_key=paraphrase_count)
                paraphrase_count += 1
                
                check_output_prompt(prompt_name,new_comment,new_siganture,language)
            pass
        # modify function name
        if modify_option[1]:
            print('+++' + 'modify function name' + '+++')
            specified_folder = range_folder + 'funcName/'
            create_folder(specified_folder)
            for prompt_fileName in clone_prompt_fileNames:
                prompt_id = int(prompt_fileName.split('.')[0].split('_')[-1])
                json_line = json_lines[prompt_id]
                func_dict = json.loads(json_line)
                old_comment = func_dict['docstring']
                old_signature = func_dict['func_signal']
                for tar_type in range(3):
                    new_comment, new_siganture,warnning = modify_tools.modify_prompt(old_comment, old_signature, language, 1,tar_type)
                    prompt_name = specified_folder + 'funcName%d_' % (tar_type) + '%05d'%prompt_id + '.' + file_postfix
                    flag = check_output_prompt(prompt_name, new_comment, new_siganture, language, warnning)
                    if flag:
                        raw_output_prompt(prompt_name,old_comment,old_signature,language)
            pass
        # modify parameter name
        if modify_option[2]:
            print('+++' + 'modify parameter name' + '+++')
            specified_folder = range_folder + 'paramName/'
            create_folder(specified_folder)
            for prompt_fileName in clone_prompt_fileNames:
                prompt_id = int(prompt_fileName.split('.')[0].split('_')[-1])
                json_line = json_lines[prompt_id]
                func_dict = json.loads(json_line)
                old_comment = func_dict['docstring']
                old_signature = func_dict['func_signal']
                for tar_type in range(3):
                    new_comment, new_siganture,warnning = modify_tools.modify_prompt(old_comment, old_signature, language, 2,
                                                                            tar_type)
                    prompt_name = specified_folder + 'paramName%d_' % (tar_type) + '%05d'%prompt_id + '.' + file_postfix
                    flag = check_output_prompt(prompt_name, new_comment, new_siganture, language,warnning)
                    if flag:
                        raw_output_prompt(prompt_name,old_comment,old_signature,language)
            pass
        # change parameter order
        if modify_option[3]:
            print('+++' + 'change parameter order' + '+++')
            specified_folder = range_folder + 'paramOrder/'
            create_folder(specified_folder)
            for prompt_fileName in clone_prompt_fileNames:
                prompt_id = int(prompt_fileName.split('.')[0].split('_')[-1])
                json_line = json_lines[prompt_id]
                func_dict = json.loads(json_line)
                old_comment = func_dict['docstring']
                old_signature = func_dict['func_signal']
                
                prompts = modify_tools.modify_prompt(old_comment, old_signature, language, 3)
                for no, prompt in enumerate(prompts):
                    new_comment, new_siganture, order_warning = prompt
                    prompt_name = specified_folder + 'paramOrder%d_' % no + '%05d'%prompt_id + '.' + file_postfix
                    flag = check_output_prompt(prompt_name, new_comment, new_siganture, language, order_warning)
                    if flag:
                        raw_output_prompt(prompt_name,old_comment,old_signature,language)
            pass
