def num_check(question):
    valid = False
    while not valid:

        error = "please enter a number more then zero"

        try:
            
            response = float(input("enter a number: ")) 

            if response > 0:
                return response
            

            else:
                print(error)
                print()
        
        except ValueError:
            print(error) 