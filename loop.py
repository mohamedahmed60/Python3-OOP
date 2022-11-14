print('''
      Select Opreation:
        1- Addition
        2- Subtract
        3- Multiply
        4- Dividu

        ''')

while True:
    choice = int(input('Enter Choice : 1, 2, 3, 4 :  '))
                            

    if choice in (1,2,3,4):
       num1 = int(input("Enter First Number: "))
       num2 = int(input("Enter Second Number: "))
       if choice == 1:
           result = num1 + num2
           print(f"{num1} + {num2} = {result}")
       elif choice == 2:
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
       elif choice == 3:
            result = num1 * num2
            print(f"{num1} * {num2} ={result}")
       elif choice == 4:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
       else:
            print("Error, Enter choice 1,2,3,4: ")
       nextcaculation = input("Let's do next caculation (y / n)").lower()
       if nextcaculation == "n":
            break
    else:
        print("Error")
      
