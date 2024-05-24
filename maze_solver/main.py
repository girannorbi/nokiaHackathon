import re
import string

with open('./input.txt', 'r') as f:
  input = f.readlines()
  mazes = []
  currentMaze = []
  isMaze = False
  instructions = []
  for line in input: # getting the mazes out of the file, putting them into the 'mazes' list
    if re.match(".\n", line):
      isMaze = True
      currentMaze = []
      continue
    if line == "\n" or line == "":
      isMaze = False
      mazes.append(currentMaze)
    line = line.replace("\n", "")
    line = line.replace(" ", "")
    line = list(line)
    if(isMaze):
      currentMaze.append(line)
  mazes.append(currentMaze)

newMazes = []
for maze in mazes: # this piece of code is getting the distance from the goal on every field
  startingpoint = []
  currentMaze = []
  while any("." in row for row in maze):
    for rowIndex in range(len(maze)):
      for colIndex in range(len(maze[rowIndex])):
        if maze[rowIndex][colIndex] == 'S':
          startingpoint = [rowIndex, colIndex]
          maze[rowIndex][colIndex] = "."
        if maze[rowIndex][colIndex] == 'G':
          if maze[rowIndex-1][colIndex] == ".":
            maze[rowIndex-1][colIndex] = 1
          if maze[rowIndex+1][colIndex] == ".":
            maze[rowIndex+1][colIndex] = 1
          if maze[rowIndex][colIndex+1] == ".":
            maze[rowIndex][colIndex+1] = 1
          if maze[rowIndex][colIndex-1] == ".":
            maze[rowIndex][colIndex-1] = 1
        if isinstance(maze[rowIndex][colIndex], int):
          if maze[rowIndex-1][colIndex] == ".":
            maze[rowIndex-1][colIndex] = maze[rowIndex][colIndex]+1
          if maze[rowIndex+1][colIndex] == ".":
            maze[rowIndex+1][colIndex] = maze[rowIndex][colIndex]+1
          if maze[rowIndex][colIndex+1] == ".":
            maze[rowIndex][colIndex+1] = maze[rowIndex][colIndex]+1
          if maze[rowIndex][colIndex-1] == ".":
            maze[rowIndex][colIndex-1] = maze[rowIndex][colIndex]+1
  maze[startingpoint[0]][startingpoint[1]] = "S"
  currentPos = startingpoint
  currentMazeInstructions = "S"
  while maze[currentPos[0]][currentPos[1]] != "G":
    nearbyNumbers = []
    if isinstance(maze[currentPos[0]+1][currentPos[1]], int):
      nearbyNumbers.append(maze[currentPos[0]+1][currentPos[1]])
    if isinstance(maze[currentPos[0]-1][currentPos[1]], int):
      nearbyNumbers.append(maze[currentPos[0]-1][currentPos[1]])
    if isinstance(maze[currentPos[0]][currentPos[1]+1], int):
      nearbyNumbers.append(maze[currentPos[0]][currentPos[1]+1])
    if isinstance(maze[currentPos[0]][currentPos[1]-1], int):
      nearbyNumbers.append(maze[currentPos[0]][currentPos[1]-1])

    if maze[currentPos[0]-1][currentPos[1]] == "G":
      currentPos = [currentPos[0]-1, currentPos[1]]
      currentMazeInstructions += "U"
      continue
    if maze[currentPos[0]+1][currentPos[1]] == "G":
      currentPos = [currentPos[0]+1, currentPos[1]]
      currentMazeInstructions += "D"
      continue
    if maze[currentPos[0]][currentPos[1]-1] == "G":
      currentPos = [currentPos[0], currentPos[1]-1]
      currentMazeInstructions += "L"
      continue
    if maze[currentPos[0]][currentPos[1]+1] == "G":
      currentPos = [currentPos[0], currentPos[1]+1]
      currentMazeInstructions += "R"
      continue
        
    if maze[currentPos[0]-1][currentPos[1]] == "G" or maze[currentPos[0]-1][currentPos[1]] == min(nearbyNumbers):
      currentPos = [currentPos[0]-1, currentPos[1]]
      currentMazeInstructions += "U"
    if maze[currentPos[0]+1][currentPos[1]] == "G" or maze[currentPos[0]+1][currentPos[1]] == min(nearbyNumbers):
      currentPos = [currentPos[0]+1, currentPos[1]]
      currentMazeInstructions += "D"
    if maze[currentPos[0]][currentPos[1]-1] == "G" or maze[currentPos[0]][currentPos[1]-1] == min(nearbyNumbers):
      currentPos = [currentPos[0], currentPos[1]-1]
      currentMazeInstructions += "L"
    if maze[currentPos[0]][currentPos[1]+1] == "G" or maze[currentPos[0]][currentPos[1]+1] == min(nearbyNumbers):
      currentPos = [currentPos[0], currentPos[1]+1]
      currentMazeInstructions += "R"
  currentMazeInstructions += "G"
  currentMazeInstructions = " ".join(char for char in currentMazeInstructions)
  instructions.append(currentMazeInstructions)
  
for i in range(len(instructions)):
  print(string.ascii_uppercase[i] + "\n" + instructions[i])