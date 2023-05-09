import platform
    
class typeSystem(object):
    
    def __init__(self) -> None:
        self.system :str = platform.system()
        self.command :str = self.get_comands()
    
    def get_comands(self):
        
        match self.system:
            case "Windows":
                with open("./dados/syswin.dll" , "r") as arq:
                    return arq.read()
                
if __name__ == "__main__":
    print(typeSystem().command)
        