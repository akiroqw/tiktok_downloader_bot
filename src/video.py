from config import*

class Video:
    def __init__(self, url, name , extension) -> None:
        self.url = url
        self.name = name
        self.extension = extension
        self.path = self.name + self.extension
        
    def __del__(self):
        os.remove(self.path)
