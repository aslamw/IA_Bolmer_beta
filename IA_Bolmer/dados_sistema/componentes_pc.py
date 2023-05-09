import psutil

class mySystem (object):
    
    def __init__(self):
        self.memory_used :int = round(psutil.virtual_memory().used /1024/1024/1024 , 2)
        self.memory_free :int = round(psutil.virtual_memory().free /1024/1024/1024 , 2)
        self.memory_total :int = round(psutil.virtual_memory().total /1024/1024/1024 , 2)
        self.memory_percent :int = psutil.virtual_memory().percent

        self.cpu :int = psutil.cpu_percent()
        self.cpu_all :int = psutil.cpu_freq().max
    def securyt_system(self):
        pass

if __name__ == "__main__":
    print(mySystem().memory_free)
    