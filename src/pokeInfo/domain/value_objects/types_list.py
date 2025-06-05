class TypesList:
    
    def __init__(self, types: list):
        self.types = types
    
    def __eq__(self, other):
        if(isinstance(other, TypesList)):
            return self.types==other.types
        return False