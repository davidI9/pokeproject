class AbilitiesList:
    
    def __init__(self, abilities: dict):
        self.abilities = abilities
        
    def __eq__(self, other):
        if(isinstance(other, AbilitiesList)):
            return self.abilities==other.abilitiess
        return False