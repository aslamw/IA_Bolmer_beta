"""
 author: Marcos Wagner
 data: 11/01/2023 06:14
"""
import os, datetime, gc, logging
from fala import test_speack
from dados_sistema import mySystem, typeSystem
from securyt import generate_key

class Bolmer(mySystem, typeSystem):
    
    def __init__(self) -> None:
        mySystem.__init__(self)
        typeSystem.__init__(self)
        
        self.name :str = 'Bolmer'
        self.age :datetime = datetime.datetime.now()
        self.happy :int = 0
        self.sadness :int = 0
        self.doubt :int = 10
        self.state_mode :str = 'speack'
        self.key = generate_key('marcos1999',b"1234567890123456")
        
    def speack(self) -> str:
        
        match self.state_mode:
            case 'speack': 
                data :str = test_speack()
        
                print(data)
            case 'to type':
                print('de boa')
                
    
if __name__ == '__main__':
    while True:
        #(I := Bolmer().speack())
        print((I := Bolmer().speack()))
        print('start')
        #gc.collect()