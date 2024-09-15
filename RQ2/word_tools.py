
import enchant


def single_word_convert(s, s_type):
    if s_type == "SingleWord":
        if s[0].isupper():
            s = s[0].lower() + s[1:]
        elif s[0].islower():
            s = s[0].upper() + s[1:]

        return s
    else:
        print("No need to Convert!")

def convert_to_upper_camel(s, s_type):
    if s_type == 1:
        return s
    elif s_type == 0:
        s = s[0].upper() + s[1:]
        return s
    elif s_type == 2:
        words = s.split("_")
        res = ""
        for word in words:
            if word=='':
                continue
            res += word[0].upper() + word[1:]
        return res

def convert_to_lower_camel(s, s_type):
    if s_type == 1:
        s = s[0].lower() + s[1:]
        return s
    elif s_type == 0:
        return s
    elif s_type == 2:
        words = s.split("_")
        res = ""
        for k in range(len(words)):
            if k == 0:
                res += words[k][0] + words[k][1:]
                continue
            if words[k]=='':
                continue
            res += words[k][0].upper() + words[k][1:]
            
        return res

def convert_to_underscore(s, s_type):
    if s_type == 1:
        words = []
        last = 0
        for i in range(len(s)):
            if s[i].isupper() and i != 0:
                words.append(s[last:i])
                last = i
            if i == len(s) - 1:
                words.append(s[last:i + 1])

        if len(words) == 1:
            return None

        new_s = ""
        for i in range(len(words)):
            word = words[i]
            if i != len(words) - 1:
                new_s += word.lower() + "_"
            else:
                new_s += word.lower()

        return new_s

    elif s_type == 0:
        words = []
        last = 0
        for i in range(len(s)):
            if s[i].isupper() and i != 0:
                words.append(s[last:i])
                last = i
            if i == len(s) - 1:
                words.append(s[last:i + 1])

        if len(words) == 1:
            return None

        new_s = ""
        for i in range(len(words)):
            word = words[i]
            if i != len(words) - 1:
                new_s += word.lower() + "_"
            else:
                new_s += word.lower()

        return new_s

    elif s_type == 2:
        return s

# return 0-lower camel, 1-upper camel, 2-underline,3-error
def distinguish_type(word):
    s = word.strip()
    for char in s:
        if not char in ([chr(i) for i in range(ord('a'),ord('a')+26)] + [chr(i) for i in range(ord('A'),ord('A')+26)] + ['_']):
            with open('information/error_word.txt', 'a', encoding='utf-8') as err_words:
                err_words.write(s + '\n')
            return 3
    try:
        if s[0] not in [chr(i) for i in range(ord('a'),ord('a')+26)] + [chr(i) for i in range(ord('A'),ord('A')+26)]:
            return 3
    except:
        return 3
    
    if s[0].isupper():
        return 1
    
    elif s[0].islower() and s.find("_")==-1:
        for c in s:
            if c.isupper():
                return 0
        d = enchant.DictWithPWL('en-us','my_dict.txt')
        if d.check(s):
            return 0
        else:
            with open('information/error_word.txt','a',encoding='utf-8') as err_words:
                err_words.write(s+'\n')
    elif s.find("_")!=-1:
        return 2

    return 3


def modify_word(word,target):
    # modify words
    # target: 0-lower camel, 1-upper camel, 2-underline,3-error
    type = distinguish_type(word)
    if type==3:
        print('error word type: %s'%word.strip())
        return (None,None)
    # lower camel
    if target==0:
        if type in [1,2]:
            return convert_to_lower_camel(word,type),len(word) <= 2
        else:
            return word,False
    # upper camel
    elif target==1:
        if type in [0,2]:
            return convert_to_upper_camel(word,type),len(word) <= 2
        else:
            return word,False
    # underline
    elif target==2:

        if type==0 and sum([c.isupper() for c in word])>0:
            return convert_to_underscore(word,type),len(word) <= 2

        elif type==1 and sum([c.isupper() for c in word])>1:
            return convert_to_underscore(word,type),len(word) <= 2
        else:
            return word,False

