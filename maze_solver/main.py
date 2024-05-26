import re
import string

with open('./input.txt', 'r') as f:
  input = f.readlines()
  mazes = []
  current_maze = []
  isMaze = False
  instructions = []
  for line in input: # getting the mazes out of the file, putting them into the 'mazes' list
    if re.match(".\n", line):
      isMaze = True
      current_maze = []
      continue
    if line == "\n" or line == "":
      isMaze = False
      mazes.append(current_maze)
    line = line.replace("\n", "")
    line = line.replace(" ", "")
    line = list(line)
    if(isMaze):
      current_maze.append(line)
  mazes.append(current_maze)

newMazes = []
for maze in mazes: # this piece of code is getting the distance to the goal on every walkable field
  startingpoint = []
  current_maze = []
  while any("." in row for row in maze):
    for rowIndex in range(len(maze)):
      for colIndex in range(len(maze[rowIndex])):
        if maze[rowIndex][colIndex] == 'S':
          startingpoint = [rowIndex, colIndex]
          maze[rowIndex][colIndex] = "."
        if maze[rowIndex][colIndex] == "G":
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
  current_pos = startingpoint
  current_maze_instructions = "S"
  while maze[current_pos[0]][current_pos[1]] != "G":  # Here, after getting the distance to the goal from each field, the character moves always in the direction of the smallest number until it reaches its testination
    nearby_numbers = []
    if isinstance(maze[current_pos[0] + 1][current_pos[1]], int):
      nearby_numbers.append(maze[current_pos[0] + 1][current_pos[1]])
    if isinstance(maze[current_pos[0] - 1][current_pos[1]], int):
      nearby_numbers.append(maze[current_pos[0] - 1][current_pos[1]])
    if isinstance(maze[current_pos[0]][current_pos[1] + 1], int):
      nearby_numbers.append(maze[current_pos[0]][current_pos[1] + 1])
    if isinstance(maze[current_pos[0]][current_pos[1] - 1], int):
      nearby_numbers.append(maze[current_pos[0]][current_pos[1] - 1])

    if maze[current_pos[0] - 1][current_pos[1]] == "G": # Initially this criteria was in the same if statement where the program checks for where is the smallest number,
      current_pos = [current_pos[0] - 1, current_pos[1]] # but the code would prioritize to go in the direction of the smallest number instead of the goal and by that it would create an endless cycle
      current_maze_instructions += "U"
      continue
    if maze[current_pos[0] + 1][current_pos[1]] == "G":
      current_pos = [current_pos[0] + 1, current_pos[1]]
      current_maze_instructions += "D"
      continue
    if maze[current_pos[0]][current_pos[1] - 1] == "G":
      current_pos = [current_pos[0], current_pos[1] - 1]
      current_maze_instructions += "L"
      continue
    if maze[current_pos[0]][current_pos[1] + 1] == "G":
      current_pos = [current_pos[0], current_pos[1] + 1]
      current_maze_instructions += "R"
      continue
        
    if maze[current_pos[0] - 1][current_pos[1]] == min(nearby_numbers):
      current_pos = [current_pos[0] - 1, current_pos[1]]
      current_maze_instructions += "U"
    if maze[current_pos[0] + 1][current_pos[1]] == min(nearby_numbers):
      current_pos = [current_pos[0] + 1, current_pos[1]]
      current_maze_instructions += "D"
    if maze[current_pos[0]][current_pos[1] - 1] == min(nearby_numbers):
      current_pos = [current_pos[0], current_pos[1] - 1]
      current_maze_instructions += "L"
    if maze[current_pos[0]][current_pos[1] + 1] == min(nearby_numbers):
      current_pos = [current_pos[0], current_pos[1] + 1]
      current_maze_instructions += "R"
  current_maze_instructions += "G"
  current_maze_instructions = " ".join(char for char in current_maze_instructions)
  instructions.append(current_maze_instructions)

for i in range(len(instructions)):
  print(string.ascii_uppercase[i] + "\n" + instructions[i] + "\n")