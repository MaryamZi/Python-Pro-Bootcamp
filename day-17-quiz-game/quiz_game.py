# Data from https://replit.com/@appbrewery/quiz-game-start#data.py
question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {
        "text": "In West Virginia, USA, if you accidentally hit an animal with your car, "
                "you are free to take it home to eat.",
        "answer": "True"},
    {
        "text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.",
        "answer": "False"
    },
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


question_bank = []

for data in question_data:
    question_bank.append(Question(data["text"], data["answer"]))


class QuizBrain:
    def __init__(self, questions_list):
        self.questions_number = 0
        self.questions_list = questions_list
        self.score = 0

    def next_question(self):
        current = self.questions_number
        self.questions_number += 1
        question = self.questions_list[current]
        user_response = input(f"Q{self.questions_number}: {question.text} (true/false)? ")
        answer = question.answer
        if self.check_answer(user_response, answer):
            print("That was correct!")
            self.score += 1
        else:
            print("That's wrong!")

        print(f"The correct answer was {answer}")
        print(f"You're current score is {self.score}/{self.questions_number}\n")

    def still_has_questions(self):
        return self.questions_number < len(self.questions_list)

    def check_answer(self, user_response, answer):
        return user_response.lower() == answer.lower()


qb = QuizBrain(question_bank)

while qb.still_has_questions():
    qb.next_question()

print(f"You've completed the game! Final score: {qb.score}/{qb.questions_number}")
