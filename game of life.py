# Ryan Korsrud
# UCID: 30173204
# TUT: T11

CRITTER = '*'
EMPTY = ' '

def oneEmpty():
    world = []
    for row in range(10):
        world.append([EMPTY for i in range(10)])
    return world

def twoSingleCritter():
    world = [["*"," ", " "," ", " ", " ", " ", " ", " ", " "]]
    for row in range(9):
        world.append([EMPTY for i in range(10)])

def threeSingleBirth():
    return[[" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " ","*", " ", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "]]

def fourthSimpleBirth():
    return[[" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", "*","*", " ", " ", " ", " ", " ", " "],
     [" ","*", " ","*", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     ["*"," ", " "," ", " ", " ", " ", " ", " ", " "]]

def fifthCreateListEdgeCases():
    return [["*"," ", "*"," ", " ", " ", " ", " ", " ", "*"],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     ["*"," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", " ", " ", " ", " ", " "],
     ["*"," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", "*"],
     [" "," ", " "," ", " ", " ", " ", " ", "*", " "],
     ["*","*", " "," ", " ", " ", " ", " ", " ", "*"]]

def sixthComplexCases():
    return [[" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", "*", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", "*", " ", " ", " ", " "],
     [" "," ", " ","*", "*", "*", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     ["*"," ", " "," ", " ", " ", " ", " ", " ", " "]]

# gets the user to select a file, ensures the file is valid, and parses the file to create the world
# args(None)
# returns(oldWorld: List[List[String]])
def sevenCustomCase():
    newLine, fileOk, oldWorld, blank = '\n', False, [], 0
    while not fileOk:
        try:
            fileName = input('Enter file name: ')
            f = open(fileName, 'r')
            file = f.readlines()
            if len(file) == blank:
                print('File %s is empty' %(fileName))
            else:
                for row in range(len(file)):
                    oldWorld.append([])
                    for character in range(len(file[row])):
                        if file[row][character] != newLine:
                            oldWorld[row].append(file[row][character])
                f.close()
                fileOk = True # exits while loop
        except:
            print('There was a problem reading file %s' %fileName)
            fileOk = False    
    return  oldWorld


# displays the turn number, old world, and new world
# args(turn: int, oldWorld: List[List[String]], newWorld: List[List[String]])
# returns(None)
def display(turn, oldWorld, newWorld):
    columnLength = len(oldWorld[0])
    seperator = columnLength*2-4
    totalRows = len(oldWorld)
    print('\nTurn #%d\nBEFORE%sAFTER' %(turn,' '*seperator + '\t\t'))
    for row in range(0, totalRows):
        print(' -'*columnLength, end=' #\t\t')          # prints line of dashes above oldWorld
        print(' -'*columnLength, end=' #\n')            # prints line of dashes above newWorld
        print('', end='|')                              # prints a | before the oldWorld row
        print(*oldWorld[row], sep='|', end='|#\t\t|')   # prints a row from oldWorld, seperates each item with a "|", and ends the row with "|#          "
        print(*newWorld[row], sep='|', end='|#\n')      # prints a row from newWorld, seperates each item with a "|", and ends the row with "|#" and a new line
    print(' -'*columnLength, end=' #\t\t')      # prints a line of dashes below oldWorld
    print(' -'*columnLength, end=' #\n\n')      # prints a line of dashes below newWorld


# creates a deep copy of a world
# args(world: List[List[String]])
# returns(copy_world: List[List[String]])
def copy(world):
    copy_world = []
    for r in range(len(world)):
        copy_world.append([])
        for c in range(len(world[0])):
            copy_world[r].append(world[r][c])
    return copy_world


# gets the number of neighbouring critters for world[r][c]
# args(r: int, c: int, world: List[List[String]])
# returns(count: int)
def getCritterCount(r, c, world):
    cols, rows, count = len(world[0]) - 1, len(world) - 1, 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i != 0 or j != 0) and 0 <= r+i <= rows and 0 <= c+j <= cols:
                if world[r+i][c+j] == CRITTER:
                    count += 1
    return count
                

# updates the world based on the rules of the game
# args(debugOn: bool, oldWorld: List[List[String]])
# returns(newWorld: List[List[String]])
def update(debugOn, oldWorld):
    newWorld, lonely, crowded = [], 1, 4
    for r in range(len(oldWorld)):
        newWorld.append([])
        for c in range(len(oldWorld[0])):
            critterCount = getCritterCount(r, c, oldWorld)
            if (oldWorld[r][c] == EMPTY and critterCount != 3) or (oldWorld[r][c] == CRITTER and critterCount <= lonely or critterCount >= crowded):
                newWorld[r].append(EMPTY)
                if debugOn and oldWorld[r][c] == CRITTER:
                    print("The critter in row %s cell %s died because it had %s neighbouring critters" %(r+1, c+1, critterCount))
            else:
                newWorld[r].append(CRITTER)
                if debugOn and oldWorld[r][c] == EMPTY:
                    print("A critter in row %s cell %s is born because it had %s neighbouring critters" %(r+1, c+1, critterCount))
    return newWorld
                

# gets the user to select a starting world
# args(None)
# returns(world: List[List[String]])
def getStartingWorld():
    choices = [oneEmpty, twoSingleCritter, threeSingleBirth, fourthSimpleBirth, fifthCreateListEdgeCases, sixthComplexCases, sevenCustomCase]
    try:
        index = int(input('1. Empty\n2. Single Critter\n3. Single Birth\n4. Simple Birth\n5. Edge Cases\n6. Complex Case\n7. Custom\nSelect a starting world[1-6]: ')) - 1
        if 0 <= index <= 6: #checks that the choice is in valid range
            return choices[index]()
        print('selection must be between 1 and 7...\n')
    except:
        print('invalid selection...\n')
    return getStartingWorld()


# games main function
# args(None)
# returns(None)
def main():
    oldWorld, newWorld, turn, playing, debugOn = getStartingWorld(), [], 0, True, False # initalizes games variables
    #games main loop
    while playing:
        turn += 1
        newWorld = update(debugOn, oldWorld)
        display(turn,oldWorld,newWorld)
        cont = input("Press enter to continue or 'q' to quit... ")
        if cont == 'q' or cont == 'Q':
            print('game quit...')
            playing = False
        elif cont == 'd' or cont == 'Q':
            debugOn = not debugOn
        oldWorld = copy(newWorld)
        
main()
