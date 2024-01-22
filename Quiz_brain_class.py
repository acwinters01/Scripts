class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        total_questions = len(self.question_list)
        if self.question_number < total_questions:
            return True
        else:
            return False
        # A simplified version would be
        # return self.question_number < total_questions

    def next_question(self):
        new_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"{self.question_number}: {new_question.text} (True/False)?:  ")
        self.check_answer(user_answer, new_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("\nYou got it right!")
            self.score += 1
        else:
            print("\nThat's wrong")
        print(f"The correct answer is: {correct_answer}.")
        print(f"\nYour current score is: {self.score}/{self.question_number}")
