class MoveList:
    
    def __init__(self, moves: list):
        self.moves = moves
    
    def __eq__(self, other):
        if(isinstance(other, MoveList)):
            return self.moves==other.moves
        return False