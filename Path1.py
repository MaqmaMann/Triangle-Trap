from random import *

turnsP1 = randint(1,2)
turnsP2 = randint(1,2)

print('Turns; P1:', turnsP1, 'P2:', turnsP2)     #For TroubleShooting
print('')   #Spacing
from math import *

from graphics import GraphicsWindow

###Setting up the board
board = GraphicsWindow(525, 525)
c = board.canvas()
c.setOutline('maroon')
c.drawRect(0, 0, 500, 500) #The Boarder
c.setOutline('black')
c.drawLine(250, 250, 250, 230) #The Starting (inverse) triangle
c.drawLine(250, 250, 250 + sqrt(300), 260)
c.drawLine(250, 250, 250 - sqrt(300), 260)

###Initalizing and cataloging the playable points
playablePoints = [[250, 230],               #(x, y) coordinate pairs. (two columns)
                  [250 + sqrt(300), 260],
                  [250 - sqrt(300), 260]]
RowsPP = len(playablePoints) #Initializing handles for the "playablePoints" table
ColumnsPP = 1

nonPlayablePoints = [[250, 250]]

playedLines = [[250, 250, 250, 230],        #Two points aranged as (x, y) coordinate pairs. (four columns)
               [250, 250, 250 + sqrt(300), 260],
               [250, 250, 250 - sqrt(300), 260]]

##def notTakenTest():
##    if endPoint in playablePoints or nonPlayablePoints:
##        return False

while turnsP1 != 0:
    choice = randint(0, RowsPP - 1)
    startPoint = [playablePoints[choice][0], playablePoints[choice][1]]
    options = randint(1, 5)
    print('Option Selected:', options)

    ### Add a for loop to test which orientations are valid plays
    options = randint(1, 6)     #Parameter to work with the part of the unfinished code that works; The above three lines will be uncommented when everything works

    if options == 1:
        newX = startPoint[0] + sqrt(300)
        newY = startPoint[1] + 10
        turnsP1 = turnsP1 - 1
    elif options == 2:
        newX = startPoint[0] - sqrt(300)
        newY = startPoint[1] + 10
        turnsP1 = turnsP1 - 1
    elif options == 3:
        newX = startPoint[0] - sqrt(300)
        newY = startPoint[1] - 10
        turnsP1 = turnsP1 - 1
    elif options == 4:
        newX = startPoint[0] + sqrt(300)
        newY = startPoint[1] - 10
        turnsP1 = turnsP1 - 1
    elif options == 5:
        newX = startPoint[0]
        newY = startPoint[1] + 20
        turnsP1 = turnsP1 - 1
    elif options == 6:
        newX = startPoint[0]
        newY = startPoint[1] - 20
        turnsP1 = turnsP1 - 1


        
    playablePoints.append([newX, newY])

    endPoint = [[newX, newY]]
    
    play = [startPoint[0], startPoint[1], newX, newY]
    
    playedLines.append(play)
    
    print('The Played line:', play)     #For TroubleShooting
    print('')   #Spacing
    print('Played Lines now consist of:', playedLines)
    print('')
    print('Playable Points after play', playablePoints)  
    print('')   

    c.drawLine(play[0], play[1], newX, newY) #Actually draws the line

    ###Visualization of playable points
    for R in range(len(playablePoints)):
        c.drawOval(playablePoints[R][0]-2.5, playablePoints[R][1]-2.5, 5, 5)

    
    
