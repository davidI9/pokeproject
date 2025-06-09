class Sprite:
    def __init__(self, path: str):
        self.path = path
        
    def __eq__(self, other):
        if(isinstance(other, Sprite)):
            return self.path==other.path
        return False