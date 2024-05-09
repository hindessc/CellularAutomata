import random
import sys

def display(grid):
    for i in range(HEIGHT):
        print(convert(grid[i]))
    print("-"*WIDTH)
    
def addRooms(grid, number = 1):
    rooms = []
    while len(rooms) < number:
        i = random.randint(1, HEIGHT-1)
        j = random.randint(1, WIDTH-1)
        iDim = random.randint(4, 8)
        jDim = random.randint(4, 8)
        skip = False
        
        for (i_, iDim_, j_, jDim_) in rooms:
            if range(max(i, i_), min(i+iDim, i_+iDim_+1)) and range(max(j, j_), min(j+jDim, j_+jDim_+1)):
                skip = True
        
        if not skip:
            rooms.append((i, iDim, j, jDim))    
        
    for (i, iDim, j, jDim) in rooms:
        for a in range(iDim):
            print(a)
            for b in range(jDim):
                if i+a < HEIGHT-1 and j+b < WIDTH-1:
                    grid[i+a][j+b] = 1
                    print(i+a, j+b)
    return grid
    
def getAdjacency(grid, i, j):
    adjacent = 0
    for d in adjacencies:
        a = i + d[0]
        b = j + d[1]
        if (0 <= a and a < HEIGHT) and (0 <= b and b < WIDTH):
            adjacent += grid[a][b]
    return adjacent

def convert(row):
    return str(list(map(conversion, row))).replace("[", "").replace("'", "").replace(",", "").replace("]", "")

def conversion(num):
    match num:
        case 0:
            return "█"
        case 1:
            return " "

WIDTH = 40
HEIGHT = 20

adjacencies = [
      [-1, -1]
    , [-1, 0]
    , [-1, 1]
    , [0, -1]
    , [0, 1]
    , [1, -1]
    , [1, 0]
    , [1, 1]   
    ]

def getRuleset(key):
    if not key.endswith(".txt"):
        ruleset = key
    else:
        with open(key) as file:
            ruleset = file.read()

    for rule in ruleset.split("/"):
        match rule[0]:
            case 'B':
                born = list(map(int, rule[1:]))
            case 'S':
                survive = list(map(int, rule[1:]))
            case _:
                print("Invalid ruleset")
                born, survive = None
    return ruleset, born, survive
    
while True:
    ruleset, born, survive = getRuleset(input("Enter a ruleset: "))
    curr = []
    for i in range(HEIGHT):
        msg = []
        for j in range(WIDTH):
            msg.append(1 if random.choice(range(0, 2)) == 1 and i in range(int(HEIGHT/2-2), int(HEIGHT/2+2)) and j in range(int(WIDTH/2-2), int(WIDTH/2+2)) else 0)
        curr.append(msg)

    while True:
        match input().lower().split():
            case [":q"] | [":quit"]:
                sys.exit()
            case [":h"] | [":help"] | ["help"]:
                print("Your options are:\n"
                      ":h to brin up this help menu\n"
                      "press enter to update the state of the system"
                      ":q to quit\n"
                      ":p to print the current ruleset\n"
                      ":r <ruleset> to update the current ruleset\n"
                      ":w <filepath> to write the current ruleset to a file\n"
                      ":a <number> to add a number of rooms"
                      )
            case [":p" ] | [":printruleset"]:
                print(ruleset)
            case [":r", rule] | [":updateruleset", rule]:
                ruleset, born, survive = getRuleset(rule)
            case [":w", path] | [":write", path]:
                try:
                    with open(path.strip(), "x") as file:
                        file.write(ruleset)
                except FileExistsError:
                    match input("File exists, are you sure you want to overwrite it (y/n)"):
                        case "y":
                            file.write(ruleset)
            case [":a", value]:
                number = int(value)
                curr = addRooms(curr, number)
                display(curr) 
            case _:
                    
                next = []
                for i in range(HEIGHT):
                    msg = []
                    for j in range(WIDTH):
                        count = getAdjacency(curr, i, j)
                        if i == 0 or i == HEIGHT-1 or j == 0 or j == WIDTH-1:
                            msg.append(0)
                        elif count in survive and curr[i][j] == 1:
                            msg.append(1)
                        elif count in born:
                            msg.append(1)
                        else:
                            msg.append(0)
                    next.append(msg)
                curr = next
                display(curr)