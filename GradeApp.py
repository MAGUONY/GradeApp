def main():

    print("Hello, this app tells you betweeen what numbers is your letter grade!")
    
    theLoop = 1

    while(theLoop):
        
        theGrade = input("Enter the letter of your grade: ")
    
        if(theGrade == "A" or theGrade == "a"):
            print("Your grade is between 90 and 100!")
                        
        elif(theGrade == "B" or theGrade == "b"):
            print("Your grade is between 80 and 89!")

        elif(theGrade == "C" or theGrade == "c"):
            print("Your grade is between 70 and 79!")
            
        elif(theGrade == "D" or theGrade == "d"):
            print("Your grade is between 60 and 69!")

        elif(theGrade == "F" or theGrade == "f"):
            print("Your grade is between 0 and 59!")

        keepGoing = input("Do you want to keep going? (y/n): ")
        
        if(keepGoing == "n"):
            print("Thank you for trying this app. Have a good one!")
            theLoop = 0
                  


main()
