print(''' 
1) Addition
2) Subtraction
3) Multiplication
4) Division

Other:

5) Writing even numbers 
''')



# Selecting
selectOne = int(input("Select One: "))

#If selectOne == {number of category}   Example:
# print ("{Category Name}")   
#     {Variable 1} = int(input("First Number: "))
#     {Variable 2} = int(input("Second Number: "))
#     {Variable 3} = {Variable 1} {+, -, /, *} {Variable 2}
#     print(f"Result: {result}")


if selectOne == 1:
    
    print('-'*50)
    print ("Addition")
    numberA = int(input("First Number: "))
    numberAA = int(input("Second Number: "))
    result = numberA + numberAA
    print(f"Result: {result}")
# Subtraction
elif selectOne == 2:
   
    print("-"*50)
    print("Subtraction")
    numberS = int(input("First Number: "))
    numberSS = int(input("Second Number: "))
    result = numberS - numberSS
    print(f"Result: {result}")
# Multiplication
elif selectOne == 3:
   
    print("-"*50)
    print("Multiplication")
    numberM = int(input("First Number: "))
    numberMM = int(input("Second Number: "))
    result = numberM * numberMM
    print(f"Result: {result}")
# Division
elif selectOne == 4:
    
    print("-"*50)
    print("Division")
    numberD = int(input("First Number: "))
    numberDD = int(input("Second Number: "))
    result = numberD / numberDD
    print(f"Result: {result}")
# Writin even numbers 
elif selectOne == 5:
    evenQuestion = int(input("Where do you want to write even number? "))
    calcEven = 0
    while evenQuestion > calcEven:
        if calcEven % 2 == 0:
            print(calcEven)
        calcEven += 1

# Quiting
keynumber = int(1)

while keynumber > 0:
    question = input("If you want to exit program write q: ")
    if question == "q":
        print("Exiting...")
        keynumber -= 1





