import copy
# ?     WORKING NO ERRORS :)


board = [[0 for _ in range(3)] for _ in range(3)]
class listNode():
    def __init__(self, board, score  = 0):
        self.board = copy.deepcopy(board)
        self.score = score
        self.children = []
        
def score(board):
    maxScore = 0
    minScore = 0
    for i in range(3):
        if(board[i][0] == board[i][1] == board[i][2]):
            if(board[i] == "O"):
                minScore += 1
            elif(board[i] == "X"):
                maxScore += 1
    for j in range(3):
        if(board[0][j] == board[1][j] == board[2][j]):  
            if board[0][j] == "O":
                minScore += 1
            elif board[0][j] == "X":
                maxScore += 1
    if(board[0][0] == board[1][1] == board[2][2]):
        if(board[0][0] == "O"):
            minScore += 1
        elif(board[0][0] == "X"):
            maxScore += 1
            
    if(board[2][0] == board[1][1] == board[0][2]):
        if(board[0][2] == "O"):
            minScore += 1
        elif(board[0][2] == "X"):
            maxScore += 1
    score = minScore + maxScore
    return score  
    
def minimax(Node, depth, maximizing):
    # need to find out how to make end condition if all possible nox    x           
        

    if(maximizing):
        #loop condition bad never gets over first square something happens and makes it to where nothing else works
        bestScore = float('-inf')
        for i in range(3):
            for j in range(3):
                if Node.board[i][j] == 0:
                    tempBoard = copy.deepcopy(Node. board)
                    tempBoard[i][j] = "X"
                    prev = listNode(tempBoard)
                    Node.children.append(prev)
                    prev = minimax(prev,depth - 1, not maximizing)
                    tempScore = prev.score
                    bestScore = max(bestScore, tempScore)
        Node.score = bestScore
        return bestScore

        
    else:
        bestScore = float('inf')
        for i in range(3):
            for j in range(3):
                if(Node.board[i][j] == 0):
                    tempBoard = copy.deepcopy(Node.board)
                    tempBoard[i][j] = "O"
                    prev = listNode(tempBoard)
                    Node.children.append(prev)
                    prev = minimax(prev, depth - 1, maximizing)
                    tempScore = prev.score
                    bestScore = min(bestScore, tempScore)
        Node.score = bestScore
        return bestScore


def getUserInput(depth):
    if(depth % 2 == 0):
        user = True
        if(user):
            x = input('enter x location to place.')
            y = input('enter y location to place.')
            x = int(x)
            y = int(y)
        board[x][y] = 'O'
            
def checkWinner(board):
    for x in range(3):
        temp = board[x][0]
        if temp != 0:
            if temp == board[x][1] == board[x][2]:
                return temp
    for y in range(3):
        temp = board[0][y]
        if(temp != 0 and temp == board[1][y] == board[2][y]):
            return temp
    if(board[0][0] != 0):
        temp = board[0][0]
        if(temp == board[1][1] == board[2][2]):
            return temp
    if(board[2][0] != 0):
        temp = board[2][0]
        if(temp == board[1][1] == board[0][2]):
            return temp


board[0][0] = "X"

def main(board):
    depth = 0
    while depth <= 8:   
        if(depth % 2 == 0):
            getUserInput(depth)
            depth += 1
        else:
            for x in range(3):
                for y in range(3):
                    minimax(listNode(board), depth, True)
                    
            depth += 1
            for i in range(3):
                print(board[i])
main(board)  
