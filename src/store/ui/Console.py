from store.controller.QuestionController import QuestionController
from store.controller.QuizController import QuizController
from store.domain.validators import RepositoryError, ValidatorError, DuplicateIdError

__author__ = 'victor'


class Console(object):
    def __init__(self, quiz_ctrl: QuizController, question_ctrl: QuestionController):
        try:
            self.__quiz_ctrl = quiz_ctrl
            self.__question_ctrl = question_ctrl
        except RepositoryError as ex:
            print(ex)
            quit()

    def quit_ui(self):
        quit()

    def quiz_ui(self):
        print("Quiz\n")
        questions = self.__question_ctrl.get_random(3)
        i = 0
        cor = 0
        al = 0
        while i < len(questions) and al != len(questions) - 1:
            q = questions[i]
            print(q.question + "\n" + "a) " + q.a + " b) " + q.b + " c) " + q.c)
            options = {"a": q.a, "b": q.b, "c": q.c}
            if self.__quiz_ctrl.find(q.Id):
                print("prev/next")
                inp = input("> ")
                if inp == "prev":
                    i -= 1
                elif inp == "next":
                    i += 1
            else:
                print("prev/answer/next")
                inp = input("> ")

                if inp == "prev":
                    i -= 1
                elif inp == "next":
                    i += 1
                else:
                    al += 1
                    try:
                        inp = inp.split(" ")
                        print(inp[1])
                        answer = options[inp[1]]
                        self.__quiz_ctrl.add_quiz(q.Id, q.question, answer, q.correct)
                        if answer == q.correct.rstrip("\n"):
                            cor += 1
                            print("Congrats")
                            print("Correct: " + q.correct.rstrip("\n"))
                            print("your answer: " + answer)
                        else:
                            print("Failed")
                            print("Correct: " + q.correct.rstrip("\n"))
                            print("your answer: " + answer)
                        print(str(cor) + "/" + str(al))
                        i += 1
                    except KeyError:
                        print("option wasn't implemented")
                    except ValidatorError as ve:
                        print(ve)



    def review_ui(self):
        print("Review\n")
        quizes = self.__quiz_ctrl.get_all()
        i = 0
        while i < len(quizes):
            q = quizes[i]
            print(q.question + "\n" + "Answer: " + q.answer + " Correct: " + q.correct)
            print("prev/next")
            inp = input("> ")
            if inp == "prev":
                i -= 1
            elif inp == "next":
                i += 1
    def run(self):
        options = {"quiz": self.quiz_ui, "review": self.review_ui, "exit": self.quit_ui}
        while True:
            print("Idle\n")
            inp = input("> ")
            try:
                options[inp]()
            except KeyError:
                print("option wasn't implemented")
            except ValidatorError as ve:
                print(ve)