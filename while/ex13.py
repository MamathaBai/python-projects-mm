while True:
    age = input("Enter the age:(or type 'quit to stop)")
    if age == 'quit':
        break
    age = int(age)
    if age<3:
        print("free to kids")
    elif age<=12:
        print("the ticket is $10")
    else:
        print("the ticket is $15")