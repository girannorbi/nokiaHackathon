import re

with open('./input.txt', 'r') as f:
  input = f.readlines()

  results = []
  matrices = [] # structure -> ['name of the matrix', [row1], [row2]...]]
  operations = []

  operations_block_index = 0 # the start of the instructions block at the end of the file
  for line_index in range(len(input)):
    line = input[line_index]
    line = line.replace("\n", "")
    line = re.sub(" +", " ", line)
    if line == "operations":
      operations_block_index = line_index
      break
    if line == "" or line == "matrices":
      continue

    if len(line) == 1:
      matrices.append([line])
    else:
      matrices[len(matrices)-1].append(line.split(" "))

  for line_index in range(operations_block_index, len(input)):
    line = input[line_index]
    line = line.replace("\n", "")
    line = re.sub(" +", " ", line)
    if line == "" or line == "operations":
      continue
    operations.append(line)

# making the operations
  def getMatrix(matrix_name):
    for matrix in matrices:
      if matrix[0] == matrix_name:
        provided_matrix = matrix
        return provided_matrix 
    print("Hiba a mátrixlekérdezésben!")
    print("Kapott név: " + matrix_name)
    exit(1)
  def addMatrices(matrix1, matrix2):
    if len(matrix1) == len(matrix2) and len(matrix1[1]) == len(matrix2[1]):
      new_matrix = [""]
      matrix1 = matrix1[1:len(matrix1)]
      matrix2 = matrix2[1:len(matrix2)]
      for i in range(len(matrix1)):
        current_row = []
        for j in range(len(matrix1[i])):
          current_row.append(int(matrix1[i][j]) + int(matrix2[i][j]))
        new_matrix.append(current_row)
      return new_matrix
    else:
      print("A mátrixok nem adhatóak össze egymással! \n"
            "Összeadott mátrixok: ")
      for row in matrix1:
        print(row)
      for row in matrix2:
        print(row)
      exit(1)

  def multiplyMatrices(matrix1, matrix2):
    if (len(matrix1[1]) == len(matrix2)-1):
      new_matrix = [""]
      matrix1 = matrix1[1:len(matrix1)]
      matrix2 = matrix2[1:len(matrix2)]
      for row in matrix1:
        currentrow = []
        for col in range(len(matrix2[0])):
          total = 0
          for i in range(len(row)):
            total += int(row[i]) * int(matrix2[i][col])
          currentrow.append(total)
        new_matrix.append(currentrow)
      return new_matrix
    else:
      print("A mátrixok nem szorozhatóak egymással! \n"
            "Összeszorzott mátrixok: ")
      for row in matrix1:
        print(row)
      for row in matrix2:
        print(row)
      exit(1)

  for operation in operations:
    operation = operation.replace(" ", "")
    processed_operations = [] # the same operations as in the "operation" variable, but the letters are replaced by the real matrices
    for charachter in operation:
      if charachter.isalpha():
        processed_operations.append(getMatrix(charachter))
      else:
        processed_operations.append(charachter)

    while "*" in processed_operations:
      for i in range(len(processed_operations)):
        if processed_operations[i] == "*":
          multipliedMatrices = multiplyMatrices(processed_operations[i - 1], processed_operations[i + 1])
          processed_operations.pop(i + 1)
          processed_operations.insert(i, multipliedMatrices)
          processed_operations.pop(i + 1)
          processed_operations.pop(i - 1)
          break

    while "+" in processed_operations:
      for i in range(len(processed_operations)):
        if processed_operations[i] == "+":
          addedMatrices = addMatrices(processed_operations[i - 1], processed_operations[i + 1])
          processed_operations.pop(i + 1)
          processed_operations.insert(i, addedMatrices)
          processed_operations.pop(i + 1)
          processed_operations.pop(i - 1)
          break

    processed_operations.insert(0, operation.replace("", " ").strip())
    results.append(processed_operations)

for i in results:
  for j in i:
    if isinstance(j, str):
      print(j)
    else:
      j.pop(0)
      for row in j:
        print(" ".join(str(number) for number in row))
      print("")