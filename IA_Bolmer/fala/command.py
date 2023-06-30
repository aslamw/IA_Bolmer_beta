import os, time, sys
def commands():
    jj = {}
    with open('teste.dll','r') as arq:
        dados = arq.read()
        
    for item in dados.split('\n'):
        item = item.split(':')
        
        jj[item[0]] = item[1]
        
    exec(jj['limpar'])
    
    
commands()

def mult_commands():
    jj = {}
    with open('teste_mult.dll','r') as arq:
        dados = arq.read()
        
    for item in dados.split('</>'):
        if item:
            item = item.split('<>')
           
            jj[item[0]] = item[1]
        
            exec(jj['contar'])
mult_commands()