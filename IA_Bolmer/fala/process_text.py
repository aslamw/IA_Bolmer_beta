import os

def process_text(menssage,data_speack=False,data_comand=False):
    data_text :dict = {}
    if data_speack:
        
        for item in data_speack.split('\n'):
            item = item.split(':')
            data_text[item[0]] = item[1].split(',')
    elif data_comand:
        
        for item in data_speack.split('<>'):
            data_text[item[0]] = item[1].split('</>')
        
    try:
        
        print(menssage)
        print(data_text)
    except: 
        pass
