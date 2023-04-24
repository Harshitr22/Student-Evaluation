# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1915214

# Date: 24/11/2022 




#PART - 1

#(A)
    
##while True:                                                               #loop starts
##    print('Welcome user, Enter the scores below to check results.')
##    pass_credits = int(input('ENTER YOUR PASS CREDITS:'))                 #asks for pass credits
##    defer_credits = int(input('ENTER YOUR DEFER CREDITS:'))               #asks for defer credits
##    fail_credits = int(input('ENTER YOUR FAIL CREDITS:'))                 #asks for fail credits
##
##    if pass_credits == 120 and defer_credits == 0 and fail_credits == 0:
##        print('Progressiomn outcome : PROGRESS')
##        
##    elif pass_credits == 100 and defer_credits <= 20 and fail_credits <= 20:
##        print('Progression outcome : PROGRESS(MODULE TRAILER)')
##        
##    elif  pass_credits <= 80 and defer_credits <=120 and fail_credits <=60:
##        print('Progression outcome: DO NOT PROGRESS - MODULE RETRIEVER')
##        
##    elif pass_credits <= 40 and defer_credits <= 40 and  fail_credits >= 80 and  fail_credits <=120:
##        print('Progression outcome : EXCLUDE')
##        
##    else:
##        print('Invalid input')


#(B)+ (C) + (D)

##numbers = [0,20,40,60,80,100,120]                   #defining numbers for the range .
##total = 0
##progress = 0
##total_inputs = 0                                    #initialising all of these to 0
##trailer = 0
##retriever = 0
##exclude = 0
##
##
##def Validation():                                               #creating function 
##    global pass_credits, defer_credits, fail_credits
##    global progress, trailer, retriever, exclude
##    print('Welcome user, Enter the scores below to check results.')
##    while True:
##        pass_credits= input('\n ENTER YOUR PASS CREDITS:')   
##        try:  
##            pass_credits = int(pass_credits)                            # to check if its an integer
##        except ValueError :
##            print('Requires a valid integer! Please try again')
##            continue
##        else:
##            if pass_credits not in numbers:                             #to check if its in defined range
##                print('Out of range.')
##            elif pass_credits in numbers:                                       
##                break
##    print("You successfully entered an integer.")
##
##    
##
##    while True: 
##        defer_credits = input('\n ENTER YOUR DEFER CREDITS:')
##        try:  
##            defer_credits = int(defer_credits)
##        except ValueError :
##            print('Requires a valid integer! Please try again')
##            continue
##        else:
##            if defer_credits not in numbers:
##                print('Out of range.')
##            elif defer_credits in numbers:
##                break    
##    print("You successfully entered an integer.")
##
##
##    while True:    
##        fail_credits = input('\n ENTER YOU FAIL CREDITS:')
##        try:  
##            fail_credits = int(fail_credits)
##        except ValueError :
##            print('Requires a valid integer! Please try again')
##            continue
##        else:
##            if fail_credits not in numbers:
##                print('Out of range.')
##            elif fail_credits in numbers:
##                break
##    print("You successfully entered an integer.")
##    
##
##    Total = pass_credits + defer_credits + fail_credits                 #to check the total of all three inputs
##    if Total == 120:
##        print('Total correct.')
##        
##    else:
##        print('Total Incorrect.')
##    
##
##    if pass_credits == 120 and defer_credits == 0 and fail_credits == 0:
##        print('Progressiomn outcome : PROGRESS')
##        progress = progress+1
##        run_again()
##
##
##    elif pass_credits == 100 and defer_credits <= 20 and fail_credits <= 20:
##        print('Progression outcome : PROGRESS(MODULE TRAILER)')
##        trailer = trailer +1
##        run_again()
##
##
##    elif  pass_credits <= 80 and defer_credits >= 0 and defer_credits <=120 and fail_credits >=0 and fail_credits <=60:
##        print('Progression outcome: DO NOT PROGRESS - MODULE RETRIEVER')
##        retriever = retriever +1
##        run_again()
##    
##    elif pass_credits <= 40 and defer_credits <= 40 and  80 <= fail_credits <=120:
##        print('Progression outcome : EXCLUDE')
##        exclude = exclude+1
##        run_again()
##        
##    else:
##        print('Invalid input')
##
##
##
##def run_again():
##    global close
##
##    global progress
##    global trailer                                          #globalising to use anywhere in function
##    global retriever
##    global exclude
##    while True:
##        print("\n")
##        try:
##            close = input("Would you like to enter another set of data?\n"                  #input to make a loop until q is entered. 
##                          "Enter 'y' for yes or 'q' to quit and view results: ")
##        except ValueError:
##            print("\n Please Enter 'y' or 'q' ")
##        else:
##            if close == "q":
##                print("\n")
##                print("-" * 60)
##                print("Horizontal Histogram\n")
##                print("Progress", progress, " :", "*" * progress)
##                print("Trailer", trailer, "  :", "*" * trailer)
##                print("Retriever", retriever, ":", "*" * retriever)
##                print("Excluded", exclude, " :", "*" * exclude)
##                total_outcomes = progress + trailer + retriever + exclude
##                print("\n")
##                print(total_outcomes, "outcomes in total.")
##                print("-" * 60)
##           
##            elif close == "y":
##                Validation()                                    #function call if another set of data is entered
##            else:
##                print("Please Enter 'y' or 'q'")
##
##
##    
##Validation()
##    
    





#PART - 2

##record = open('record.txt','w')  # opens blank/saved text documents for writing
##record.truncate(0)  #wipes text document
##results = open('record.txt','r')  #opens saved text documents for reading
##numbers = [0,20,40,60,80,100,120]
##total = 0
##progress = 0
##total_inputs = 0
##trailer = 0
##retriever = 0
##exclude = 0
##myList = []
##result = []
##student_scores = []
##
##
##
##def Validation():
##    global pass_credits, defer_credits, fail_credits
##    global progress, trailer, retriever, exclude
##    print('Welcome user, Enter the scores below to check results.')
##    while True:
##        pass_credits= input('\n ENTER YOUR PASS CREDITS:')
##        myList.append(pass_credits)
##        print(pass_credits , file = record)
##        try:  
##            pass_credits = int(pass_credits)
##        except ValueError :
##            print('Requires a valid integer! Please try again')
##            continue
##        else:
##            if pass_credits not in numbers:
##                print('Out of range.')
##            elif pass_credits in numbers:
##                break
##    print("You successfully entered an integer.")
##
##    
##
##    while True: 
##        defer_credits = input('\n ENTER YOUR DEFER CREDITS:')
##        myList.append(defer_credits)
##        print(defer_credits, file = record)
##        try:  
##            defer_credits = int(defer_credits)
##        except ValueError :
##            print('Requires a valid integer! Please try again')
##            continue
##        else:
##            if defer_credits not in numbers:
##                print('Out of range.')
##            elif defer_credits in numbers:
##                break    
##    print("You successfully entered an integer.")
##
##
##    while True:    
##        fail_credits = input('\n ENTER YOU FAIL CREDITS:')
##        myList.append(fail_credits)
##        print(fail_credits, file = record)
##        try:  
##            fail_credits = int(fail_credits)
##        except ValueError :
##            print('Requires a valid integer! Please try again')
##            continue
##        else:
##            if fail_credits not in numbers:
##                print('Out of range.')
##            elif fail_credits in numbers:
##                break
##    print("You successfully entered an integer.")
##    
##
##    Total = pass_credits + defer_credits + fail_credits
##    if Total == 120:
##        print('Total correct.')
##        
##    else:
##        print('Total Incorrect.')
##    
##
##    if pass_credits == 120 and defer_credits == 0 and fail_credits == 0:
##        print('Progressiomn outcome : PROGRESS', file = record)
##        print('Progressiomn outcome : PROGRESS')
##        progress = progress+1
##        run_again()
##
##
##    elif pass_credits == 100 and defer_credits <= 20 and fail_credits <= 20:
##        print('Progression outcome : PROGRESS(MODULE TRAILER)', file  = record)
##        print('Progression outcome : PROGRESS(MODULE TRAILER)')
##        trailer = trailer +1
##        run_again()
##
##
##    elif  pass_credits <= 80 and defer_credits >= 0 and defer_credits <=120 and fail_credits >=0 and fail_credits <=60:
##        print('Progression outcome: DO NOT PROGRESS - MODULE RETRIEVER', file = record)
##        print('Progression outcome: DO NOT PROGRESS - MODULE RETRIEVER')
##        retriever = retriever +1
##        run_again()
##    
##    elif pass_credits <= 40 and defer_credits <= 40 and  80 <= fail_credits <=120:
##        print('Progression outcome : EXCLUDE', file = record)
##        print('Progression outcome : EXCLUDE')
##        exclude = exclude+1
##        run_again()
##        
##    else:
##        print('Invalid input')
##
##    student_scores = [result_name  + str(pass_credits) + ',' + str(defer_credits) + + ',' + str(fail_credits)]
##    results.append(student_scores)
##
##
##
##def run_again():
##    global close
##
##    global progress
##    global trailer
##    global retriever
##    global exclude
##    while True:
##        print("\n")
##        try:
##            close = input("Would you like to enter another set of data?\n"
##                          "Enter 'y' for yes or 'q' to quit and view results: ")
##        except ValueError:
##            print("\n Please Enter 'y' or 'q' ")
##        else:
##            if close == "q":
##                print("\n")
##                print("-" * 60)
##                print("Horizontal Histogram\n")
##                print("Progress", progress, " :", "*" * progress)
##                print("Trailer", trailer, "  :", "*" * trailer)
##                print("Retriever", retriever, ":", "*" * retriever)
##                print("Excluded", exclude, " :", "*" * exclude)
##                total_outcomes = progress + trailer + retriever + exclude
##                print("\n")
##                print(total_outcomes, "outcomes in total.")
##                print("-" * 60)
##                print('PART-2')
##                record.close()  #closes text doc
##                file_content = results.read()  #variable with text doc contents
##                print(file_content)
##                results.close()  #closes text doc
##               
##                
##                
##               
##            elif close == "y":
##                Validation()
##                break
##            else:
##                print("Please Enter 'y' or 'q'")
##
##    
##Validation()
##    







# PART- 3

##record = open('record.txt','w')  # opens blank/saved text documents for writing
##record.truncate(0)  #wipes text document
##results = open('record.txt','r')  #opens saved text documents for reading
##
##numbers = [0,20,40,60,80,100,120]
##total = 0
##progress = 0
##total_inputs = 0
##trailer = 0
##retriever = 0
##exclude = 0
##
##
##def Validation():
##    global pass_credits, defer_credits, fail_credits
##    global progress, trailer, retriever, exclude
##    print('Welcome user, Enter the scores below to check results.')
##    while True:
##        pass_credits= input('\n ENTER YOUR PASS CREDITS:')
##        print(pass_credits, file = record)
##        try:  
##            pass_credits = int(pass_credits)
##        except ValueError :
##            print('Requires a valid integer! Please try again')
##            continue
##        else:
##            if pass_credits not in numbers:
##                print('Out of range.')
##            elif pass_credits in numbers:
##                break
##    print("You successfully entered an integer.")
##
##    
##
##    while True: 
##        defer_credits = input('\n ENTER YOUR DEFER CREDITS:')
##        print(defer_credits, file = record)
##        try:  
##            defer_credits = int(defer_credits)
##        except ValueError :
##            print('Requires a valid integer! Please try again')
##            continue
##        else:
##            if defer_credits not in numbers:
##                print('Out of range.')
##            elif defer_credits in numbers:
##                break    
##    print("You successfully entered an integer.")
##
##
##    while True:    
##        fail_credits = input('\n ENTER YOU FAIL CREDITS:')
##        print(fail_credits, file = record )
##        try:  
##            fail_credits = int(fail_credits)
##        except ValueError :
##            print('Requires a valid integer! Please try again')
##            continue
##        else:
##            if fail_credits not in numbers:
##                print('Out of range.')
##            elif fail_credits in numbers:
##                break
##    print("You successfully entered an integer.")
##    
##
##    Total = pass_credits + defer_credits + fail_credits
##    if Total == 120:
##        print('Total correct.')
##        
##    else:
##        print('Total Incorrect.')
##    
##
##    if pass_credits == 120 and defer_credits == 0 and fail_credits == 0:
##        print('Progressiomn outcome : PROGRESS' , file = record)
##        print('Progressiomn outcome : PROGRESS')
##        progress = progress+1
##        run_again()
##
##
##    elif pass_credits == 100 and defer_credits <= 20 and fail_credits <= 20:
##        print('Progression outcome : PROGRESS(MODULE TRAILER)' , file = record)
##        print('Progression outcome : PROGRESS(MODULE TRAILER)')
##        trailer = trailer +1
##        run_again()
##
##
##    elif  pass_credits <= 80 and defer_credits >= 0 and defer_credits <=120 and fail_credits >=0 and fail_credits <=60:
##        print('Progression outcome: DO NOT PROGRESS - MODULE RETRIEVER' , file = record)
##        print('Progression outcome: DO NOT PROGRESS - MODULE RETRIEVER')
##        retriever = retriever +1
##        run_again()
##    
##    elif pass_credits <= 40 and defer_credits <= 40 and  80 <= fail_credits <=120:
##        print('Progression outcome : EXCLUDE' , file = record)
##        print('Progression outcome : EXCLUDE')
##        exclude = exclude+1
##        run_again()
##        
##    else:
##        print('Invalid input')
##
##
##
##def run_again():
##    global close
##
##    global progress
##    global trailer
##    global retriever
##    global exclude
##    while True:
##        print("\n")
##        try:
##            close = input("Would you like to enter another set of data?\n"
##                          "Enter 'y' for yes or 'q' to quit and view results: ")
##        except ValueError:
##            print("\n Please Enter 'y' or 'q' ")
##        else:
##            if close == "q":
##                print("\n")
##                print("-" * 60)
##                print("Horizontal Histogram\n")
##                print("Progress", progress, " :", "*" * progress)
##                print("Trailer", trailer, "  :", "*" * trailer)
##                print("Retriever", retriever, ":", "*" * retriever)
##                print("Excluded", exclude, " :", "*" * exclude)
##                total_outcomes = progress + trailer + retriever + exclude
##                print("\n")
##                print(total_outcomes, "outcomes in total.")
##                print("-" * 60)
####                print('PART-3')
##                record.close()  #closes text doc
##                file_content = results.read()  #variable with text doc contents
##                print(file_content)   #prints contents of the text doc
##                results.close()  #closes text doc
##               
##            elif close == "y":
##                Validation()
##                break
##            else:
##                print("Please Enter 'y' or 'q'")
##
##    
##Validation()
    





















































