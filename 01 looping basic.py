def num_check(question):
    valid = False
    while not valid:


        response = float(input("enter a number: "))

        if response > 0:
            valid = True
        

        else:
            print("please enter a number more then zero")
            print()
    