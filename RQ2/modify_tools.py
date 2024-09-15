
import re

import numpy as np
import word_tools
import comment_tools

chars = [chr(ord('a')+ i)  for i in range(26)] + [chr(ord('A')+ i)  for i in range(26)] + [chr(ord('0')+ i)  for i in range(10)]

# 检查某个单词是否合法
def my_check(s,d):
    return d.check(s)



# 找到函数签名中的所有形参
def find_params(signature,lang,only_name):
    if lang in ['c','java']:
        params_result = re.search('\(([ \n\t]*[^ \t\n(),]+[ \n\t]+[^ \t\n,)]+[ \n\t]*[,]*)+[ \n\t]*\)', signature,
                                  re.I | re.S | re.U)

        if params_result != None:
            params = []
            params_str = params_result.group()[1:-1].strip()
            params_str_len = len(params_str)
            # 要针对泛型处理
            genericity = 0
            words = []
            cur_word = ''
            last_space_idx = -1
            last_head_idx = 0
            meet_character = False
            # 从后往前找
            for idx,c in enumerate(params_str):
                if c=='<':
                    genericity += 1
                if c=='>':
                    genericity -= 1
                if  idx==params_str_len-1:
                    name = params_str[last_space_idx + 1:]
                    type = params_str[last_head_idx:last_space_idx]
                    params.append((type, name))
                    last_head_idx = idx + 1
                    continue
                elif (c==',' and genericity==0):
                    name = params_str[last_space_idx+1:idx]
                    type = params_str[last_head_idx:last_space_idx]
                    params.append((type, name))
                    last_head_idx = idx+1
                    continue
                if c in [' ','\t','\n']:
                    last_space_idx = idx



            # type_id_pairs = params_str[1:-1].split(',')
            # for type_id in type_id_pairs:
            #     tem = type_id.strip().split(' ')
            #     type = " ".join(tem[:-1])
            #     param = tem[-1]
            #     params.append((type,param))
            return params
        else:
            return  []
    elif lang=='python':
        params_result = re.search('\(([ \n\t]*[^ \n\t]+[ \n\t]*[,]*)+[ \n\t]*\)', signature,
                                  re.I | re.S | re.U)
        if params_result != None:

            params_str = params_result.group()
            params_str= params_str[1:-1]
            params = []

            layer = 0
            param_begin = 0

            for i in range(len(params_str)):
                if params_str[i]=='(':
                    layer += 1
                elif params_str[i]==')':
                    layer -= 1
                elif params_str[i]==',' and layer==0:
                    cur_p = params_str[param_begin:i]
                    if only_name:
                        idx = cur_p.find('=')
                        params.append(('Placeholder',cur_p.strip() if idx==-1 else cur_p[:idx].strip()))
                    else:
                        params.append(('Placeholder',cur_p.strip()))
                    param_begin = i + 1
            cur_p = params_str[param_begin:]
            if only_name:
                idx = cur_p.find('=')
                params.append(('Placeholder',cur_p.strip() if idx == -1 else cur_p[:idx].strip()))
            else:
                params.append(('Placeholder',cur_p.strip()))

            return params
        else:
            return []

        pass

# 找到函数签名中的函数名
def find_funcName(signature):
    funcName_result = re.search('([ \t\n]|^)[^ \t\n@]+[ \t\n]*\(',signature,re.I | re.S | re.U)

    func_name = None

    if funcName_result!=None:
        func_name = funcName_result.group()[:-1].strip()

    if func_name==None:
        print('debug: 3')
        print(signature)
    return func_name

# 得到参数顺序全排列
def get_param_orders(signature,lang):
    params = find_params(signature,lang,False)
    params_num = len(params)
    if params_num <= 1:
        return []

    if lang == 'python':
        if params_num <= 2 and params[0] == 'self':
            return []
        cur_flags = [1] * params_num # 标记python函数中各参数的形式：self(0)、普通(1)、默认参数(2)
        for i in range(params_num):
            if params[i] == 'self':
                cur_flags[i] = 0
            elif params[i].find('=') != -1:
                cur_flags[i] = 2
        if cur_flags.count(1) <= 1 and cur_flags.count(2) <= 1:
            return []

    result_orders = []

    cur_order = list(range(params_num))


    while True:
        # 找到下一个字典序
        cur_idx = -1
        for i in range(1, len(cur_order)):
            if cur_order[i] > cur_order[i - 1]:
                cur_idx = i - 1

        if cur_idx < 0:
            break
        if cur_order == 0:
            break

        for i in range(len(cur_order) - 1, 0, -1):
            if cur_order[i] > cur_order[cur_idx]:
                tem = cur_order[cur_idx]
                cur_order[cur_idx] = cur_order[i]
                cur_order[i] = tem

                if lang=='python':
                    tem = cur_flags[cur_idx]
                    cur_flags[cur_idx] = cur_flags[i]
                    cur_flags[i] = tem
                break

        tem_order = cur_order[cur_idx + 1:]
        tem_order.reverse()
        cur_order = cur_order[:cur_idx + 1]
        cur_order.extend(tem_order)

        if lang=='python':
            tem_flags = cur_flags[cur_idx + 1:]
            tem_flags.reverse()
            cur_flags = cur_flags[:cur_idx + 1]
            cur_flags.extend(tem_flags)


        # python需要处理self和默认参数，根据cur_flags的递增性
        check_ok = True
        if lang == 'python':
            for i in range(params_num-1):
                if cur_flags[i+1] < cur_flags[i]:
                    check_ok = False
                    break

        if not check_ok:
            continue

        result_orders.append(cur_order)

    return result_orders

# 得到新排列
def get_new_order(signature,lang):
    params = find_params(signature, lang, False)
    params_num = len(params)
    if params_num <= 1:
        return []
    if lang == 'python':
        if params_num <= 2 and params[0] == 'self':
            return []
        cur_flags = [1] * params_num  # 标记python函数中各参数的形式：self(0)、普通(1)、默认参数(2)
        for i in range(params_num):
            if params[i][1] == 'self':
                cur_flags[i] = 0
            elif params[i][1].find('=') != -1:
                cur_flags[i] = 2
        if cur_flags.count(1) <= 1 and cur_flags.count(2) <= 1:
            return []
        old_order = list(range(params_num))
        while True:
            new_order = []
            if cur_flags[0]==0:
                new_order.append(0)

            if 1 in cur_flags:
                begin_1 = cur_flags.index(1)
            else:
                begin_1 = -1

            if 2 in cur_flags:
                begin_2 = cur_flags.index(2)
            else:
                begin_2 = -1

            if begin_1 != -1:
                end_1 = begin_2 if begin_2!=-1 else -1
                if end_1!=-1:
                    t1 = old_order[begin_1:end_1]
                    np.random.shuffle(t1)
                    new_order.extend(t1)
                else:
                    t1 = old_order[begin_1:]
                    np.random.shuffle(t1)
                    new_order.extend(t1)
            if begin_2 != -1:
                t1 = old_order[begin_2:]
                np.random.shuffle(t1)
                new_order.extend(t1)
            if new_order!=old_order:
                break
    else:
        old_order = list(range(params_num))
        new_order = list(range(params_num))
        while new_order==old_order:
            np.random.shuffle(new_order)
    return [new_order]

# 修改函数的prompt
# comment：注释
# signature：函数签名
# lang：c、java、python
# mode：修改注释——0、修改函数名——1、修改参数名——2、修改参数顺序——3
# word_type：修改函数名和参数名时的目标标识符形式：0——小驼峰、1——大驼峰、2——连字符
# 返回值：prompt(comment+signature)，但是调换顺序时会返回一个列表，修改ID名时会返回一个警告信息
def modify_prompt(comment, signature, lang, modify_mode,tar_word_type=None,count_key=0):
    # 修改注释
    if modify_mode == 0:
        return (comment_tools.modify_comment_by_gpt4o(comment,count_key),signature)
    # 修改函数名
    elif modify_mode == 1:
        cur_fun_name = find_funcName(signature)
        new_fun_name,warning = word_tools.modify_word(cur_fun_name,tar_word_type)
        if new_fun_name==None:
            return (None,None,None)
        if new_fun_name==cur_fun_name:
            return ('*no_need*','*no_need*',warning)
        new_signature = signature.replace(cur_fun_name,new_fun_name)
        new_comment = comment.replace(cur_fun_name,new_fun_name)
        return (new_comment,new_signature,warning)
    # 修改参数名
    elif modify_mode == 2:
        cur_params = find_params(signature,lang,True)

        new_params = []
        have_diff = False
        modify_warning = False
        for item in cur_params:

            cur_param = item[1].lstrip('*')
            star_num = item[1].find(cur_param)
            if '=' in cur_param:
                print('aaaaaaaaaaaaaaa')
            new_param,warning = word_tools.modify_word(cur_param,tar_word_type)
            
            if new_param==None:
                return (None,None,None)
            if new_param!=cur_param:
                have_diff = True
            if warning:
                modify_warning = True
            new_params.append('*'*star_num+new_param)

        if not have_diff:
            return ('*no_need*','*no_need*',modify_warning)
        else:
            new_comment = comment
            new_signature = signature
            for i in range(len(cur_params)):
                new_comment = new_comment.replace(cur_params[i][1],new_params[i])
                new_signature = new_signature.replace(cur_params[i][1], new_params[i])

            return (new_comment,new_signature,warning)
    # 修改参数顺序
    elif modify_mode == 3:
        # print(lang)
        comment_parts = comment_tools.split_comment(comment)
        comment_parts_flag = [-1]*len(comment_parts) # 标记该部分是否对应参数
        params = find_params(signature,lang,False)
        param_names = [item[1].strip() for item in params]

        order_warning = False
        param_in_comment_idxs = [] # 记录原注释中参数出现的顺序即参数下标

        # 寻找注释与参数间的对应关系
        for comment_part_idx,comment_part in enumerate(comment_parts):
            for param_idx,param_name in enumerate(param_names):
                equ_idx = param_name.find('=')
                if equ_idx!= -1:
                    param_name = param_name[:equ_idx]

                param_name = param_name.replace('*','').strip()

                if word_tools.distinguish_type(param_name)==3:
                    return [(None,None,order_warning)]

                re_expression = '@param[ \t\n]+%s'%param_name
                if re.search(re_expression,comment_part,re.U | re.S)!=None:
                    param_in_comment_idxs.append(param_idx)
                    comment_parts_flag[comment_part_idx] = param_idx
                    break

        new_orders = get_new_order(signature,lang)
        # new_orders = get_param_orders(signature,lang)

        begin_idx = signature.find('(') # 第一个'('的位置
        end_idx =  len(signature) - signature[::-1].find(')') -1 # 最后一个'('的位置

        new_prompts = []
        for new_order in new_orders:
            
            param_str = ''
            new_comment = ''
            comment_param_id = 0
            comment_param_order = []

            for param_idx in new_order:
                if param_idx in param_in_comment_idxs:
                    comment_param_order.append(param_idx)

            if lang in ['c','java']:
                try:
                    # 组建参数列表
                    for idx in new_order:
                        param_str += params[idx][0].strip() + ' ' + params[idx][1].strip() + ', '

                    if comment_param_order != param_in_comment_idxs:
                        # 组建注释
                        for part_idx in range(len(comment_parts)):
                            if comment_parts_flag[part_idx]!=-1:
                                comment_part_idx = comment_parts_flag.index(comment_param_order[comment_param_id])
                                new_comment = new_comment + comment_parts[comment_part_idx]
                                comment_param_id += 1
                                pass
                            else:
                                new_comment +=  comment_parts[part_idx]
                        new_comment = new_comment[:-1]
                    else:
                        new_comment = comment
                    new_signature = signature[:begin_idx + 1] + param_str[:-2] + signature[end_idx:]
                except:
                    new_comment, new_signature = None, None

            elif lang=='python':
                # for idx in new_order:
                #     param_str += params[idx] + ', '
                #     new_comment += '\n' + comment_parts[idx-1 if have_self else + 1]
                # new_signature = signature[:begin_idx + 1] + param_str[:-2] + signature[end_idx:]
                try:
                # 组建参数列表
                    for idx in new_order:
                        param_str += params[idx][0].strip() + ' ' + params[idx][1].strip() + ', '

                    if comment_param_order != param_in_comment_idxs:
                        # 组建注释
                        for part_idx in range(len(comment_parts)):
                            if comment_parts_flag[part_idx] != -1:
                                comment_part_idx = comment_parts_flag.index(comment_param_order[comment_param_id])
                                new_comment += '\n' + comment_parts[comment_part_idx]
                                comment_param_id += 1
                                pass
                            else:
                                new_comment += '\n' + comment_parts[part_idx]
                    else:
                        new_comment = comment
                    print(param_str)
                    new_signature = (signature[:begin_idx + 1] + param_str[:-2] + signature[end_idx:]).replace('Placeholder ','').replace('Placeholder','')
                    print(new_signature)
                except:
                    new_comment, new_signature = None, None

            new_prompts.append((new_comment,new_signature,order_warning))


        return new_prompts


if __name__=='__main__':

    comment = '// Public API.\n'
    signature = '@SuppressWarnings(String assetPath, "WeakerAccess")\npublic AssetPathFetcher(AssetManager assetManager)'

    print(find_params('@SuppressWarnings(String assetPath, "WeakerAccess")\npublic AssetPathFetcher(AssetManager assetManager)','java',False))

    result = re.search('a[ \t\n]+b','a\t   b') 
    if result!=None:
        print(result.group())