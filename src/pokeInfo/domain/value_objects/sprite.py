class Sprite:
    
    def __init__(self, path: str):
        if(type(path)==str & path.endswith(".png")): 
            self.path = path
        else:
            raise ValueError("Argument parsed is not allowed.")
        
    def __eq__(self, other):
        if(isinstance(other, Sprite)):
            return self.path==other.path
        return False