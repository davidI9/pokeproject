class StatsList:
    
    def __init__(self, stats: dict):
        self.stats = stats
    
    def __eq__(self, other):
        if(isinstance(other, StatsList)):
            return self.stats==other.stats
        return False