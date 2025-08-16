import openai
import random
import string
from gamekey import key #my api key


#Quiz parameters
num_of_questions = 5
num_of_choices = 4
random_letters = string.ascii_uppercase[:num_of_choices]


client = openai.OpenAI(api_key=key)

#Goal: Making an interactive program that simulates a multiple choice quiz.

class Quiz:
    def __init__(self,topic,questions,score):
        self.topic = topic
        self.questions = questions
        self.score = score
    
    def start(self):
        print(f"Welcome to the {self.topic} quiz!")
        for i in range(num_of_questions):
            question, correct_answer = generate_questions(mode,difficulty) #save the question and answer generated
            print(question)
            input_answer = input("What is the answer? (A/B/C/D): ").strip().upper() #Handles user input, watches out for formatting
            if(input_answer == correct_answer):
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect!")
        
        print("Your score was", self.score,"/",num_of_questions,"!")
                

def generate_questions(subject,difficulty):
    #answer_key = random.choices(random_letters)
    correct_answer = random.choices(random_letters) #This is a list, which is why we return [0] later.
    prompt = (
        f"Generate EXACTLY one {difficulty} {subject} question with {num_of_choices} multiple choice answers."
        "Make sure each multiple choice are DIFFERENT from each other, with ONLY ONE choice being the correct option. NEVER have duplicate answer choices"
        "If the difficulty is EASY, then generate a simple/elementary question"
        "If the diffculty is MEDIUM, generate a moderately difficult question (middle school/early high school level)"
        "If the difficulty is HARD, generate a difficult question (late high school/early college level)"
        f"The correct answer to this question should be placed at letter choice {correct_answer}"
        "For example, if the correct answer is \"A\", then the question's correct answer will be placed at A"
        "Do NOT reveal the answer key"
        "Here is an example question. Make the format of the question exactly like this: Do you like apples? A. Yes B. No C. Unsure D. Maybe"
         )
    response = client.chat.completions.create(
            model = "gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
    return response.choices[0].message.content.strip(), correct_answer[0]

#In a loop so that if they put in a wrong input, they can do it again. Breaks from the loop if it is valid
while(True):
    while(True):

        #Select your difficulty/which quiz you want to do
        mode = input("Welcome! To start, pick which quiz you would like to do! (Math/Science/History)\n").capitalize().strip()   
        while(True):
            difficulty =  input("Choose the difficulty: Easy | Medium | Hard\n").lower().strip()
            if (difficulty == "easy" or difficulty == "medium" or difficulty == "hard"):
                break
            else:
                print("Please select a valid difficulty!")


        #Put them into their respective quiz
        if (mode == "Math"):
            math = Quiz("Math",generate_questions(mode,difficulty),0)
            math.start()
            break
        elif(mode == "Science"):
            science = Quiz("Science",generate_questions(mode,difficulty),0)
            science.start()
            break
        elif(mode=="History"):
            history = Quiz("History",generate_questions(mode,difficulty),0)
            history.start()
            break
        else:
            print("Please select a valid option!\n")
    
    #Ask if they want to go again
    go_again = input("Would you like to go again? (yes/no)\n").lower().strip()
    if(go_again =="yes"):
        continue 
    else:
        break 


