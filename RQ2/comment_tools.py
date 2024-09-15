import time
import requests

class APIError(Exception):
    def __init__(self, msg):
        self.msg = 'please fill the Open-AI api_key'
    
    def __str__(self):
        return self.msg

def split_comment(comment):
    result_parts = []
    rest_comment = comment
    lines = comment.split('\n')

    cur_part = ''
    if_param = False
    for line in lines:
        if '@param' in line:
            result_parts.append(cur_part)
            if_param = True
            cur_part = ''
        elif '@return' in line and if_param or '*/' in line and if_param:
            result_parts.append(cur_part)
            if_param = False
            cur_part = ''
        cur_part += line + '\n'
    result_parts.append(cur_part)
    return result_parts

def modify_comment_by_model(comment, model, tokenizer, torch_device):
    batch = tokenizer([comment], truncation=True, padding='longest', max_length=60, return_tensors="pt").to(
        torch_device)
    translated = model.generate(**batch, max_length=60, num_beams=6, num_return_sequences=3,
                                temperature=1.5)
    modified_comments = tokenizer.batch_decode(translated, skip_special_tokens=True)
    for m_c in modified_comments:
        if m_c != comment:
            return (m_c,True)
    return (comment,False)

def modify_comment_by_gpt4o(comment,count_key):
    time.sleep(0.1)
    model_name = 'gpt-4o-2024-08-06'
    api_key = ""
    if api_key=="":
        raise APIError
    while True:

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        payload = {
            "model": model_name,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": 'Paraphrase the code comment and keep the comment style:\n' + comment
                        },
                    ]
                }
            ],
            "max_tokens": 300
        }

        try:
            response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload, timeout=10)

            
        except Exception as e:
            print(e)
            print("ERROR: Time Limit Exceed!")
            time.sleep(5)
            continue

        response_json = response.json()
        try:
            new_comment = response_json['choices'][0]['message']['content']
        except:
            print(response_json['error'])
            exit()
        
        break
    
    print(new_comment)
    
    return new_comment
