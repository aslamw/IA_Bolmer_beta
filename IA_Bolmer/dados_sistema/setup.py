import platform, os
    
class typeSystem(object):
    
    def __init__(self) -> None:
        self.system :str = platform.system()
        self.command :str = self.get_comands()
    
    def get_comands(self):
        if not os.path.exists('./data/syswin.dll'):
            with open('./data/syswin.dll','w') as arq:
                arq.write('')
        
        match self.system:
            case "Windows":
                with open("./data/syswin.dll" , "r") as arq:
                    return arq.read()
                
if __name__ == "__main__":
    print(typeSystem().command)
        