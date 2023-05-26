class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.questions_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)             

    def next_question(self):
        question = self.questions_list[self.question_number]
        self.question_number += 1
        user_guess = input(f"Q.{self.question_number}: {question.text} (True/False): ").lower()
        self.check_answer(user_guess, question.answer.lower())
        

    def check_answer(self, user_guess, correct_answer):
        if user_guess == correct_answer:
            print("You are correct!")
            self.score += 1            
        else:
            print("You are wrong!")
            
        print(f"Score is {self.score}/{self.question_number}\n")

