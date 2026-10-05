print("*********** WELCOME TO MY QUIZ AND GOODLUCK ***********")
print()

questions = ("What is the Largest Ocean in the world : ",
             "What is the hottest planet in the solar system : ",
             "What is the Largest continent : ")

options = (("A. Atlantic  B. Pacific  C. Indian  D. None of the Above"),
           ("A. Earth  B. Mercury  C. Venus  D. Jupiter"),
           ("A. Asia  B. Africa  C. Europe  D. Antartica "))

answers = ("A","C","A")
guesses = []
question_num =0

score = 0

for question in questions:
    print(question)
    for option in options[question_num]:
        print(option, end="")
    
    print() #makes each question appear on  its own line
    guess = (input("Choose your answer (A,B,C,D): ")).upper()
    guesses.append(guess)
    if guesses[question_num] == answers[question_num]:
        print("YOUR ANSWER IS CORRECT !!!")
        score +=1
    else:
        print("YOUR IS INCORRECT !!!")
        print(f"The correct answer is {answers[question_num]}")
    
    print() #adds a space between the questions 
    
    question_num +=1


print("Your answers are : ",guesses)
print("The correct answers are : ",answers)
print()
total_score = ((score / 3)*100)
print(f"Your % score is : {total_score:.2f}%")

     

    
    

