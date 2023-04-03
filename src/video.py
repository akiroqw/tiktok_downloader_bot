from config import*

class Video:
    def __init__(self, url, extension) -> None:
        self.url = url
        self.name = uuid.uuid4()
        self.extension = extension
        self.path = self.name + self.extension
        
    def get_video(self):
        with open(self.path, 'rb') as video:
            return video

    def __del__(self):
        os.remove(self.path)
