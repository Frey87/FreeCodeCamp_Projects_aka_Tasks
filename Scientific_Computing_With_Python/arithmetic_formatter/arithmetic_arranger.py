def arithmetic_arranger(problem, h=False):
  #1 error -  too many problems
  if len(problem) > 5:
    return print("Error: Too many problems.")
  elements = [item.split() for item in problem]

  elements_flat = [item for l in elements for item in l] 

  for parts in  elements_flat:  
    #2 error -  no more than four digits
    if len(parts)>4:
      return print("Error: Numbers cannot be more than four digits.")
    #3 error -  only digits
    if parts.isalpha():
      return print("Error: Numbers must only contain digits.") 
    #4 error - function accept only addition and subtraction.
    elif parts == "/":
      return print("Error: Operator must be '+' or '-'.")
    elif parts == "*":
      return print("Error: Operator must be '+' or '-'.")
  
  con_elements = [] 
  con_elements1 = []
  con_elements2 = []
  con_elements3 = []
  con_elements4 = []

  # create new list of splited problems
  try:
    new_elements1 = elements[0]
    new_elements2 = elements[1]
    new_elements3 = elements[2]
    new_elements4 = elements[3]
    new_elements5 = elements[4]
  except (IndexError, UnboundLocalError):
    pass


  try:
    a = new_elements1[0]
    a = int(a)
    a1 = new_elements1[1]
    a2 = new_elements1[2]
    a2 = int(a2)
    if a1 == "+":
      a4 = a + a2
    elif a1 != "+":
      a4 = a - a2
      
    con_elements.append(a)
    con_elements1.append(a1)
    con_elements2.append(a2)
    con_elements3.append(a4)
    b = new_elements2[0]
    b = int(b)
    b1 = new_elements2[1]
    b2 = new_elements2[2]
    b2 = int(b2)
    if b1 == "+":
      b4 = b + b2
    elif b1 != "+":
      b4 = b - b2
  
    con_elements.append(b)
    con_elements1.append(b1)
    con_elements2.append(b2)
    con_elements3.append(b4)

    c = new_elements3[0]
    c = int(c)
    c1 = new_elements3[1]
    c2 = new_elements3[2]
    c2 = int(c2)
    if c1 == "+":
      c4 = c + c2
    elif c1 != "+":
      c4 = c - c2
    
    con_elements.append(c)
    con_elements1.append(c1)
    con_elements2.append(c2)
    con_elements3.append(c4)

    d = new_elements4[0]
    d = int(d)
    d1 = new_elements4[1]
    d2 = new_elements4[2]
    d2 = int(d2)
    if d1 == "+":
      d4 = d + d2
    elif d1 != "+":
      d4 = d - d2
    
    con_elements.append(d)
    con_elements1.append(d1)
    con_elements2.append(d2)
    con_elements3.append(d4)
    
    f = new_elements5[0]
    f1 = new_elements5[1]
    f2 = new_elements5[2]
    f2 = int(f2)
    if f1 == "+":
      f4 = f + f2
    elif f1 != "+":
      f4 = f - f2
    con_elements.append(f)
    con_elements1.append(f1)
    con_elements2.append(f2)
    con_elements3.append(f4)
  except (IndexError, UnboundLocalError, ValueError):
    pass


  # 4 rule dashes should run along the entire length of each problem individually
  e = "_"
  # add two variables to the new list, found the max lenght of numbers and add 2 for operator and one free space
  try:
    numbers = [] 
    numbers.append(con_elements[0])
    numbers.append(con_elements2[0]) 
    max_number = max(numbers)
    dashes_len = len(str(max_number))+2
    dashes = (e*dashes_len)
    
    numbers1 = [] 
    numbers1.append(con_elements[1])
    numbers1.append(con_elements2[1]) 
    max_number1 = max(numbers1)
    dashes_len1 = len(str(max_number1))+2
    dashes1 = (e*dashes_len1)
    
    numbers2 = [] 
    numbers2.append(con_elements[2])
    numbers2.append(con_elements2[2]) 
    max_number2 = max(numbers2)
    dashes_len2 = len(str(max_number2))+2
    dashes2 = (e*dashes_len2)
    
    numbers3 = [] 
    numbers3.append(con_elements[3])
    numbers3.append(con_elements2[3]) 
    max_number3 = max(numbers3)
    dashes_len3 = len(str(max_number3))+2
    dashes3 = (e*dashes_len3)
    
    numbers4 = [] 
    numbers4.append(con_elements[4])
    numbers4.append(con_elements2[4]) 
    max_number4 = max(numbers3)
    dashes_len4 = len(str(max_number4))+2
    dashes4 = (e*dashes_len4)
  except IndexError:
    pass
  #Output result with 
  #                  right-aligned numbers
  #                  spaces between each problem
  #                  operator will be on the same line as the second operand
  #                  both operands will be in the same order as provided 
  if len(problem) == 1:
    # first line
    print("{:>10}".format(con_elements[0]))
    # second line
    print("{:>5}{:>5}".format(con_elements1[0], con_elements2[0]))
    # third line
    print("{:>10}".format(dashes))
    # dashes
    print("{:>10}".format(con_elements3[0]))
  elif len(problem) == 2:
    # first line
    print("{:>10}{:>10}".format(con_elements[0], con_elements[1]))
    # second line
    print("{:>5}{:>5}{:>5}{:>5}".format(con_elements1[0], con_elements2[0], con_elements1[1], con_elements2[1]))
    # third line
    print("{:>10}{:>10}".format(dashes, dashes1))
    # dashes
    print("{:>10}{:>10}".format(con_elements3[0], con_elements3[1]))
  elif len(problem) == 3:
    # first line
    print("{:>10}{:>10}{:>10}".format(con_elements[0], con_elements[1], con_elements[2]))
    # second line
    print("{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}".format(con_elements1[0], con_elements2[0], con_elements1[1], con_elements2[1], con_elements1[2], con_elements2[2]))
    # third line
    print("{:>10}{:>10}{:>10}".format(dashes, dashes1, dashes2))
    # dashes
    print("{:>10}{:>10}{:>10}".format(con_elements3[0], con_elements3[1], con_elements3[2]))
  elif len(problem) == 4:
    # first line
    print("{:>10}{:>10}{:>10}{:>10}".format(con_elements[0], con_elements[1], con_elements[2], con_elements[3]))
    # second line
    print("{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}".format(con_elements1[0], con_elements2[0], con_elements1[1], con_elements2[1], con_elements1[2], con_elements2[2], con_elements1[3], con_elements2[3]))
    # third line
    print("{:>10}{:>10}{:>10}{:>10}".format(dashes, dashes1, dashes2, dashes3))
    # dashes
    print("{:>10}{:>10}{:>10}{:>10}".format(con_elements3[0], con_elements3[1], con_elements3[2], con_elements3[3]))
  elif len(problem) == 5:
    # first line
    print("{:>10}{:>10}{:>10}{:>10}{:>10}".format(con_elements[0], con_elements[1], con_elements[2], con_elements[3], con_elements[4]))
    # second line
    print("{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}".format(con_elements1[0], con_elements2[0], con_elements1[1], con_elements2[1], con_elements1[2], con_elements2[2], con_elements1[3], con_elements2[3], con_elements1[4], con_elements2[4]))
    # third line
    print("{:>10}{:>10}{:>10}{:>10}{:>10}".format(dashes, dashes1, dashes2, dashes3, dashes4))
    # dashes
    print("{:>10}{:>10}{:>10}{:>10}{:>10}".format(con_elements3[0], con_elements3[1], con_elements3[2], con_elements3[3], con_elements3[4]))
    
