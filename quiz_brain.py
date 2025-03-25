class Quizbrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number].text
        current_answer = self.question_list[self.question_number].answer
        player_answer = input(f"Q.{self.question_number+1}: {current_question} (True/False)?")
        if player_answer == current_answer:
            self.score += 1
            self.question_number += 1
            print(self.score)
        else:
            self.question_number += 1
