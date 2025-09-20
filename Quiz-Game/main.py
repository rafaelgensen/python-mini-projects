""" Quiz Game! """

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from art import art

question_bank = []
for i, value in enumerate(question_data):
    question_bank.append(Question(question_data[i]['text'], question_data[i]['answer']))

quiz = QuizBrain(question_bank)

print(art)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}\n")
