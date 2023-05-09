"""
 author: Marcos Wagner
 data: 11/01/2023 06:14
"""
import os, datetime, gc, logging
from fala import test_speack
from dados_sistema import mySystem,typeSystem
from .securyt import generate_key

class Bolmer(mySystem, typeSystem):
    
    def __init__(self) -> None:
        mySystem.__init__(self)
        typeSystem.__init__(self)
        
        self.name :str = 'Bolmer'
        self.age :datetime = datetime.datetime.now()
        self.happy :int = 0
        self.sadness :int = 0
        self.doubt :int = 10
        self.key = generate_key('','')
        
    def speack(self) -> str:
        data :str = test_speack()
        print(data)
        
        if data == 'memória ram total':
            print(self.memory_total)
    
if __name__ == '__main__':
    while True:
        #(I := Bolmer().speack())
        print((I := Bolmer().command))
        print('start')
        gc.collect()