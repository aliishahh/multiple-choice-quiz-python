
# in this exercise we build a multiple choice quiz using the Class created in 'questions.py'
# (refer to 'classesAndObject.py' for all the information about Classes and Objects)

# in order to use the 'Question' Class from 'questions.py' we have to import it using 'from ____ import _____'
from questions import Question  # this is saying 'from the questions.py file, import the Class called Question'

# this is an Array of the question prompts that will be in the multiple choice quiz - it called 'question_prompts'
question_prompts = [
    "For each question, enter the letter of the answer you think it is\n"
    "What colour are Apples?\n(a) Red/ Green\n(b) Purple\n(c) Orange\n\n",
    "What colour are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What colour are Strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
]

# here we create an Array to start creating the Objects for each question (shown above)
# we create each question (from above). [] contains the index of the question. and "" contains the answer to it
questions = [
    Question(question_prompts[0], "a"),  # [0] is the first question, "a" is the answer to the question
    Question(question_prompts[1], "c"),  # [1] is the second question, "c" is the answer to the question
    Question(question_prompts[2], "b"),  # [2] is the third question, "b" is the answer to the question
]


# we have to create a Function that will run the test i.e. ask the questions and see if they got the answer right
# we pass one Parameter, it is 'questions' (as above), this will be the list of question Objects to ask the user
def run_test(questions):
    score = 0  # we create a variable, every time the user gets an answer correct, we increment the 'score' variable

    # now we want to loop through each question, ask it, get the answer, and then check if it's right using a For Loop
    for Question in questions:  # for each 'Question' Object inside the questions Array above, we want to do something

        # this 'answer' variable stores the user's answer. we ask for the user's input, by using .prompt in the (),
        # - the programme will automatically ask the user each question from the Array we created above, one by one
        answer = input(Question.prompt)

        # now we have to check if the answer the user gave is the correct answer, using an If statement
        if answer == Question.answer:  # this says 'if the user's answer = to the answer we defined above then...'
            score += 1  # ...if the answer is correct then we increment the score (add 1) using +=

    # now we want to print out how many questions they got right. In order to print a number alongside a String we
    # - have to use 'str' to convert the number into a String.
    # we use 'len' in order to figure out how many questions were in the 'questions' Array
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")


# then we call the 'run_test' Function and pass it the 'questions' Array created above that has the Objects inside
run_test(questions)
