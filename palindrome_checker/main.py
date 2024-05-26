with open('./input.txt', 'r') as f:
  input = f.readlines()
  for line in input:
    isPalindrome = True
    unique_charachters = 0
    line.replace("\n", "")
    line = "".join(filter(str.isalnum, line))
    line = line.lower()
    for offset in range(len(line)):
      if line[offset] != line[len(line)-1 - offset]: # checks if the carachter from the front is equals to the character in the back, while moving inside
        isPalindrome = False
      if line[offset] not in line[0:offset]:
        unique_charachters += 1
    if isPalindrome:
      print(f"YES, {unique_charachters}")
    else:
      print(f"NO, -1")