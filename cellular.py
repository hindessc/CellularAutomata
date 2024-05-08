import random

WIDTH = 60

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

def getAdjacency(grid, i, j):
    adjacent = 0
    for d in adjacencies:
        a = i + d[0]
        b = j + d[1]
        try:
            adjacent += grid[a][b]
        except IndexError:
            adjacent += 0
    return adjacent

def convert(row):
    return str(list(map(lambda x: "█" if x == 1 else " ", row))).replace("[", "").replace("'", "").replace(",", "").replace("]", "")

curr = []
for i in range(20):
    msg = []
    for j in range(WIDTH):
        msg.append(1 if random.choice(range(0, 3)) == 2 and i in range(8, 12) and j in range(28, 32) else 0)
    curr.append(msg)

while True:
    _ = input()
    next = []
    for i in range(20):
        msg = []
        for j in range(WIDTH):
            count = getAdjacency(curr, i, j)
            if count < 2:
                msg.append(0)
            elif (count == 2 or count == 3) and curr[i][j] == 1:
                msg.append(1)
            elif count == 3:
                msg.append(1)
            else:
                msg.append(0)
        next.append(msg)
    curr = next
    for i in range(20):
        print(convert(curr[i]))
    print("--------------------------------------------")