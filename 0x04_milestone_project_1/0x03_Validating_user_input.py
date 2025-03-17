# The user of isdigit() for validating
def user_choice():
    while True:
        choice = 'WRONG'
        acceptable_range = range(0,10)
        within_range = False

        while choice.isdigit()==False or within_range ==False:
            choice = input("Please enter a number (0-10): ")

            #Digit Check
            if choice.isdigit() ==False:
                print("Sorry that is not a digit!")

            #Range Check
            if choice.isdigit() == True:
                if int(choice) in acceptable_range:
                    within_range = True
                else:
                    within_range= False
        return int(choice)



print(user_choice())