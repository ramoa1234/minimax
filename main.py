

grid = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

def main():
    game = True
    count = 0
    checkGame()
    while(game):
        print(grid[0])
        print(grid[1])
        print(grid[2])
        if(count % 2== 0):
            X = input("enter x location:")
            Y = input("enter y location:")
            grid[X][Y] = X
        else:
            pass
            #logic for algorithm

def checkGame():
    pass
    #check the game hasn't ended

def miniMax():
    for i in range(3):
        temp = grid[i]
        for j in range(3):
            if():
                pass
    for i in range(3):
        pass
            

main()


