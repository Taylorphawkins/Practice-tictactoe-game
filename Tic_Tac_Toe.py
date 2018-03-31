import random

def game():
    
    # creat the list of valid moves
    valMove = [x for x in range(1,10)]
    allMoves = [x for x in range(1,10)]
    player_1 = []
    player_2 = []
    players = [player_1, player_2]
    # draw the board
    board(valMove)
    # get the players choice of X or O
    pawn = playerChoice()
    # ask for move and check for a win
    checkWin(valMove, pawn, allMoves, player_1, players)
    

        


def playerChoice():
    
    # setting the player as either X or O
    player = []
    pawn = input("'Do you want to play as X's or O's?: ")
    pawn = pawn.lower()

    if pawn == "x":
        player = "X"
    elif pawn == "o":
        player = "O"
    else:
        # if you chose something other then X or O
        print ("Please Choose X or O.")
        return(playerChoice())
    print ("You are '" + player + "'")
    # send the result of the choice to the game
    return(player)




def playerMove(valMove, pawn, allMoves, player_1):
    
    # Choosing a space to place the player's pawn
    playerInput = input("Choose a number: ")
    playersMove = int(playerInput)
    if playersMove in valMove:
        # checking for if the space chosen is free and if so
        # then replace the number with the plawers pawn
        print ('you chose ' + playerInput)
        pos = valMove.index(playersMove)
        valMove.insert(pos, pawn)
        valMove.remove(playersMove)
        allMoves.remove(playersMove)
        player_1.append(playersMove)
        
        print (random.randint(allMoves,valMove))
        
        # send the resulting player's move to to the game
        return(playersMove)
        
    else:
        # if its not a free space choose another
        print ("try again")
        return(playerMove(valMove, pawn))
    





def ai():
    

    import random
    for x in range(10):
        print (random.randint(1,101))
    
   # play to win
   # play to block
   # play to get 2 in a row






def checkWin(valMove, pawn, allMoves, player_1, players):
    
    someoneWon = False
    
    while someoneWon == False:
        
        print ("no win yet")
        playerMove(valMove, pawn, allMoves, player_1)
        board(valMove)
        
        if not allMoves:
            print ("no more moves")
            break
        
        for i in players:
         
            if 1 and 2 and 3 in i:
                
                someoneWon = True
                break
            
            elif 4 and 5 and 6 in i:
                    
                someoneWon = True
                break
            
            elif 7 and 8 and 9 in i:
                    
                someoneWon = True
                break
            
            elif 7 and 5 and 3 in i:
                    
                someoneWon = True
                break
            
            elif 1 and 5 and 9 in i:
                    
                someoneWon = True
                break
            
            else:
                continue
        
        
    return(someoneWon)





def board(space):
    
    # Print out the board placing the valid moves in each space
    print ("   |   |   ")
    print (" {} | {} | {}".format(space[0], space[1], space[2]))
    print ("___|___|___") 
    print ("   |   |   ")
    print (" {} | {} | {}".format(space[3], space[4], space[5]))
    print ("___|___|___") 
    print ("   |   |   ")
    print (" {} | {} | {}".format(space[6], space[7], space[8]))
    print ("   |   |   ")

game()

