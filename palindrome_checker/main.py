with open('./input.txt', 'r') as f:
  input = f.readlines()
  for line in input:
    isPalindrome = True
    uniqueCharachters = 0
    line = line.replace("\n", "") # filters newline
    line = "".join(filter(str.isalnum, line)) # filters non-alphanumeric characters from line
    line = line.lower()
    for offset in range(len(line)):
      if line[offset] != line[len(line)-1 - offset]: # checks if the carachter from the front is equals to the character in the back, while moving inside
        isPalindrome = False
      if line[offset] not in line[0:offset]:
        uniqueCharachters += 1
    if isPalindrome:
      print(f"YES, {uniqueCharachters}")
    else:
      print(f"NO, -1")