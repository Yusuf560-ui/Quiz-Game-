#Python Quiz Game

#Display questions and answers
#Prompt users for answers
#Score users based on answer (correct or incorrect)

questions = {
                 1:  "Who discovered python ?",
                 2:  "When was facebook launched ?",
                 3:  "What is the full meaning of HTML ?",
                 4:  "Which of the following is mostly correct ?",
                5:  "What is my name ?"}
                    
options = (
                ("A. Guido van Rossum", 
                "B. Bill Gatep", 
                "C. Hugo Devries", 
                "None of the above"), 
                
                ("A. January 6, 2004",
                 "B. February 6, 2006", 
                 "C. ebruary 4, 2004", 
                 "D. April 8, 2008"), 
                 
                ("A. HyperText Markup Language", 
                "B. HyperType Markup Languages",
                "C. HyperTags Markup Language",
                "D. HyperTexts Markup Language"), 
                
                ("A. Tailwind is a libary while Bootstrap is a framework",
                "B. Tailwind is a framework while Boostrap is a libary",
                "C. Both are libaries, but Tailwind is more of a utility-based libary, while Bootstrap is a component-based libary.",
                "D. Both are frameworks, but Tailwind is more of a utility-based framework, while Bootstrap is a component-based framework."), 
                
                ("A. DevExplorer", 
                "B. Yusluv",
                "C. Boyman",
                "D. DevExplorer da boyman"
                ),
              )
answers = ("A", "C", "A", "D", "A")

def play():
    while True:
        score = 0
        question_num = 0
    
        for x, question in questions.items():
            print(f"----------Question {x}----------")
            print(question)
            for option in options[question_num]:
                print(option)
            guess = input("Answer: ")
            print("\n")
            if guess.upper() == answers[question_num]:
                score +=1
            question_num +=1
        print("\n")
        print("--------------------")
        print(f"You answered {score} question(s) correctly")
        print(f"Your aggregate is {(score / question_num) * 100}")
        print(f"Thanks for playing 🥲🤭😍🥳")
        print()
        play_again = input("Do you wanna play again (y-yes ) any character to quit? ")
        print("")
        if play_again.lower() == "y":
            continue
        else:
            break
        
    
    
print("Welcome to my EsayPy Game 🤗🥰🎉")
print()

playing = input("Do you want to play: y-yes / n-no? ").lower()

while playing != "y" and  playing != "n":
    print("Invalid choice (Enter y to continue playing or n-to quit)")
    playing = input("Do you want to play: y-yes / n-no? ").lower()
    
if playing == "y":
    play()
elif playing == "n":
    print("Go and sleep 😑😏")
