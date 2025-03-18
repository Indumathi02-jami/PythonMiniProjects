
def run_quiz(question):
    score=0
    for ques in question:
        print(ques["prompt"])
        for option in ques['options']:
            print(option)
        answer=input("Enter your answer").upper()
        if answer==ques["Answer"]:
            print("Correct..!HURRY \n")
            score+=1
        else:
            print("Wrong.. Loserr")
    print(f"You got {score} out of {len(question)} questions correct")


question=[
    {
        'prompt':"What is capital of AMERICA?",
        'options':["A. Paaris","B. Landon","C. Ireland","D. USA"],
        'Answer':'A'
    },
    {
        'prompt':"What is capital of AMERICA",
        'options':["A. Paaris","B. Landon","C. Ireland","D. USA"],
        'Answer':'B'
    },
    {
        'prompt':"What is capital of AMERICA",
        'options':["A. Paaris","B. Landon","C. Ireland","D. USA"],
        'Answer':'C'
    },
    {
        'prompt':"What is capital of AMERICA",
        'options':["A. Paaris","B. Landon","C. Ireland","D. USA"],
        'Answer':'D'
    }
]



run_quiz(question)