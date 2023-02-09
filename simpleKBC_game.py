print()
print("***************--Welcome to KBC--****************")
print()
name=input("Enter your name:- ") 
email=input("Enter your Email Address:- ") 
mo_no=int(input("Enter your Mobile Number:- ")) 
play=input("You want to play KBC game?..yes or no:-  ")
print()
print("_____________ Instruction's _____________")
print()
print("""---Before playing the game KBC, please read all the instrcution's carefully!---
            * There are 5 question's on every level you choose to play.
            * Each question will carry 5 marks.
            * No negative marking.
            * To WIN you have to give all the answer's are correct. 
            * You have to select only one of this four (a,b,c,d)..option's.
            * If you enter different option from those of four options then you lose your 5 marks.""")
print()
instruct=input("Are you read all the instruction's carefully?..please select yes or no ---> ")
print()
if instruct=='yes':
    print("Okay! now you can play!!!")
elif instruct=='no':
    print("Please read the instruction's carefully then you can play!")
print()
if play=='yes':
    level=input("""Choose the level you want to play?..
                1.easy 
                2.meduim 
                3.hard 
                --->  """)
    print()
    score=0
    if level=='1' or level=='easy':
        ready=input("Are you ready to start KBC...yes or no :- ")
        if ready=='yes':
            print("ok..Let's start!")
            print()
            q1=input("""1]. Who developed python programming language?
            a. Wick Van Rossum
            b. Rasmus Lerdorf
            c. Guido van Rossum
            d. Nilene Stom 
                          
            Answer:-->  """)
        
            if q1=='c':
                score+=5  
            print("______________________________________________________________________")
            print()
            q2=input("""2]. Which type of Programming does Python support?
            a. object-oriented programming
            b. structured programming
            c. functional programming
            d. all of the mentioned
                           
            Answer:-->  """)
            if q2=='d':
                score+=5  
            print("______________________________________________________________________")
            print()
            q3=input("""3]. Is Python case sensitive when dealing with identifiers?
            a. no
            b. yes
            c. machine dependent
            d. none of the mentioned
                           
            Answer:-->  """)
            if q3=='b':
                score+=5 
            print("______________________________________________________________________") 
            print()
            q4=input("""4]. Which of the following is the correct extension of the Python file?
            a. python
            b. pl
            c. py
            d. p
          
            Answer:-->  """)
            if q4=='c':
                score+=5  
            print("______________________________________________________________________")
            print()
            q5=input("""5]. Is Python code compiled or interpreted?
            a. Python code is both compiled and interpreted
            b. Python code is neither compiled nor interpreted
            c. Python code is only compiled
            d. Python code is only interpreted
          
            Answer:-->  """)
            if q5=='a':
                score+=5 
            print("______________________________________________________________________") 
            print()
            
        elif ready=='no':
            print("okay we will start after some time!")
        else:
            print("Invalid choice")     
        
        print(f"Your score is: {score} out of 25")
        print()
        if score==25:
            print("Congratulations!!..Your all answer's are right & You Win!")
        elif score==20 or score==15 or score==10:
            print("""You played better!..
                  but for winning you have to give all the question's have right answers..
                  So, better luck next time!""")
        elif score==5:
            print("""Oop's!!..You gave only one right answer!
                  Better Luck next time!""")
        else:
            print("""OOOPS!!!..Your score is zero..
                  You have to improve your python concepts!""")
        print()
    
    elif level=='2' or level=='medium':
        ready=input("Are you ready to start KBC...yes or no :- ")
        if ready=='yes':
            print("ok..Let's start!")
            print()
            q1=input("""1]. Which of the following is the truncation division operator in Python?
            a. |
            b. //
            c. /
            d. %
                          
            Answer:-->  """)
            if q1=='b':
                score+=5  
            print("______________________________________________________________________")
            print()
            q2=input("""2]. Which of the following functions is a built-in function in python?
            a. factorial()
            b. print()
            c. seed()
            d. sqrt()
                           
            Answer:-->  """)
            if q2=='b':
                score+=5  
            print("______________________________________________________________________")
            print()
            q3=input("""3].Which of the following is not a core data type in Python programming?
            a. Tuples
            b. Lists
            c. Class
            d. Dictionary
                           
            Answer:-->  """)
            if q3=='c':
                score+=5  
            print("______________________________________________________________________")
            print()
            q4=input("""4].Which one of the following is not a keyword in Python language?
            a. pass
            b. eval
            c. assert
            d. nonlocal

            Answer:-->  """)
            if q4=='b':
                score+=5  
            print("______________________________________________________________________")
            print()
            q5=input("""5].  What arithmetic operators cannot be used with strings in Python?
            a. *
            b. -
            c. +
            d. All of the mentioned
          
            Answer:-->  """)
            if q5=='b':
                score+=5  
            print("______________________________________________________________________")
            print()
            
        elif ready=='no':
            print("okay we will start after some time!")
        else:
            print("Invalid choice")     
        
        print(f"Your score is: {score} out of 25")
        print()
        if score==25:
            print("Congratulations!!..Your all answer's are right & You Win!")
        elif score==20 or score==15 or score==10:
            print("""You played better!..
                  but for winning you have to give all the question's have right answers..
                  So, better luck next time!""")
        elif score==5:
            print("""Oop's!!..You gave only one right answer!
                  Better Luck next time!""")
        else:
            print("""OOOPS!!!..Your score is zero..
                  You have to improve your python concepts!""")
        print()
        
    elif level=='3' or level=='hard':
        ready=input("Are you ready to start KBC...yes or no :- ")
        if ready=='yes':
            print("ok..Let's start!")
            print()
            q1=input("""1]. What will be the output of the following Python code?

            >>>list1 = [1, 3]
            >>>list2 = list1
            >>>list1[0] = 4
            >>>print(list2)
            
            a. [1, 4]
            b. [1, 3, 4]
            c. [4, 3]
            d. [1, 3] 
                          
            Answer:-->  """)
            if q1=='d': 
                score+=5  
            print("______________________________________________________________________")
            print()
            q2=input("""2]. What is the maximum possible length of an identifier in Python?
            a. 79 characters
            b. 31 characters
            c. 63 characters
            d. none of the mentioned
                           
            Answer:-->  """)
            if q2=='d':
                score+=5 
            print("______________________________________________________________________") 
            print()
            q3=input("""3]. What will be the output of the following Python code snippet?

            z=set('abc$de')
            'a' in z
            
            a. Error
            b. True
            c. False
            d. No output
                           
            Answer:-->  """)
            if q3=='b':
                score+=5 
            print("______________________________________________________________________") 
            print()
            q4=input("""4]. What is output of print(math.pow(3, 2))?
            a. 9.0
            b. None
            c. 9
            d. None of the mentioned

            Answer:-->  """)
            if q4=='a':
                score+=5  
            print("______________________________________________________________________")
            print()
            q5=input("""5]. What will be the output of the following Python expression?

            round(4.576)
            
            a. 4
            b. 4.6
            c. 5
            d. 4.5
          
            Answer:-->  """)
            if q5=='c':
                score+=5  
            print("______________________________________________________________________")
            print()
            
        elif ready=='no':
            print("okay we will start after some time!")
        else:
            print("Invalid choice")     
        
        print(f"Your score is: {score} out of 25")
        print()
        if score==25:
            print("Congratulations!!..Your all answer's are right & You Win!")
        elif score==20 or score==15 or score==10:
            print("""You played better!..
                  but for winning you have to give all the question's have right answers..
                  So, better luck next time!""")
        elif score==5:
            print("""Oop's!!..You gave only one right answer!
                  Better Luck next time!""")
        else:
            print("""OOOPS!!!..Your score is zero..
                  You have to improve your python concepts!""")
        print()
    else:
        print("Invalid choice!") 
elif play=='no':
    print("okay No problem..thank you!")
else:
    print("Invalid choice!")
print(f"------------------- Thanks for playing {name}!----------------------")
print()

# Writing in a file starts here!!! 
f = open("data.txt", "a")
f.write("\n")
f.write("\n")
f.write("\n")
f.write(f"*** Data of {name}\n")
f.write(f"The name of player is : {name} \n") 
f.write(f"The email of player is : {email} \n") 
f.write(f"The mobile no of player is : {mo_no} \n") 

if score >= 25:
    f.write("***** Winner Player *****\n")
f.write(f"The final score of player is : {score}\n")
f.write("*******************************************\n")

f.close()
