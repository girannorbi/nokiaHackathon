import re
import string

with open('./input.txt', 'r') as f:
  input = f.readlines()

  results = []
  matrices = []
  operations = []

  isMatrix = False
  currentMatrix = []
  isAnOperation = False
  for line in input:
    line = line.replace("\n", "")
    if len(line) == 1:
      currentMatrix.append(line[0])
      isMatrix = True
      continue
    if line == "" and isMatrix:
      matrices.append(currentMatrix)
      currentMatrix = []
      isMatrix = False
    if isMatrix:
      line.strip()
      line = re.sub(' +', ' ', line)
      currentMatrix.append(line.split(" "))

    if line == "operations":
      isAnOperation = True
      continue

    if isAnOperation and line != "":
      operations.append(line)

# making the operations
  def getMatrix(matrixName):
    for matrix in matrices:
      if matrix[0] == matrixName:
        return matrix
    return False
  def addMatrices(matrix1, matrix2):
    newmatrix = [""]
    currentrow = []
    if (len(matrix1) == len(matrix2) and len(matrix1[1]) == len(matrix2[1])):
      for i in range(1, len(matrix1)):
        for j in range(len(matrix1[i])):
          currentrow.append(int(matrix1[i][j]) + int(matrix2[i][j]))
        newmatrix.append(currentrow)
        currentrow = []
      return newmatrix
    else:
      print("A mátrixok nem adhatóak össze egymással!")
      exit(1)

  def multiplyMatrices(matrix1, matrix2):
    newmatrix = [""]
    matrix1.pop(0)
    matrix2.pop(0)
    if (len(matrix1[0]) == len(matrix2)):
      for row in matrix1:
        currentrow = []
        for col in range(len(matrix2[0])):
          total = 0
          for i in range(len(row)):
            total += int(row[i]) * int(matrix2[i][col])
          currentrow.append(total)
        newmatrix.append(currentrow)
    return newmatrix

  for operation in operations:
    operation = operation.replace(" ", "")
    processedMatrices = []
    processedOperations = []
    for char in operation:
      if char.isalpha():
        processedOperations.append(getMatrix(char))
      else:
        processedOperations.append(char)

    while "*" in processedOperations:
      for i in range(len(processedOperations)):
        if processedOperations[i] == "*":
          multipliedMatrices = multiplyMatrices(processedOperations[i-1], processedOperations[i+1])
          processedOperations.pop(i+1)
          processedOperations.insert(i, multipliedMatrices)
          processedOperations.pop(i+1)
          processedOperations.pop(i-1)
          break
    # adding
    while "+" in processedOperations:
      for i in range(len(processedOperations)):
        if processedOperations[i] == "+":
          addedMatrices = addMatrices(processedOperations[i-1], processedOperations[i+1])
          processedOperations.pop(i+1)
          processedOperations.insert(i, addedMatrices)
          processedOperations.pop(i+1)
          processedOperations.pop(i-1)
          break

    processedOperations.insert(0, operation.replace("", " ").strip())
    results.append(processedOperations)
for i in results:
  for j in i:
    if isinstance(j, str):
      print(j)
    else:
      for row in j:
        print(" ".join(str(number) for number in row))
  print("")