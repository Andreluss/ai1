print("assadfsdf")
class State:
    def __init__(self):
        pass
    """hahaha"""
    def next_state(self, move):
        pass
    def possible_moves(self):
        pass
    def probability(self):
        pass
    def evaluate(self):
        pass
# asdflkdnflksjaflkdjf 
# dalkfjsdlkgjslsdkfj skdjf dlkfj sdkfj lsdkjflskdjflkjsd
# dlskfksdjf
class Move:
    pass #p  ass

max_depth = 4
def minmax(state, depth):
    if depth == max_depth:
        return state.evaluate()
    value = 0
    for move in state.possible_moves():
        value = max(value, 1-minmax(state.next_state(move), depth+1))
    return value
# lksdjflksjdfl kjsdfl kdsjflkdsjlkfjsdlkfj lkdsjfl sd
# kjdfiajdoifjs dfoisjdko fi
# ijoifjoifsjiossf[isfidsf
# zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
# zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz