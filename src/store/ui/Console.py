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

    def add_ui(self, *args):
        try:
            code = args[1]
            date = args[2]
            value = int(args[3])
            self.__grade_ctrl.add_grade(code, date, value)
        except ValidatorError as ve:
            print(ve)
        except DuplicateIdError as de:
            print(de)
        except ValueError as vee:
            print(vee)

    def delete_ui(self, *args):
        pass
        # try:
        #     code = args[1]
        #     date = args[2]
        #     self.__grade_ctrl.remove_grade(code, date)
        # except ValidatorError as ve:
        #     print(ve)
        # except RepositoryError as re:
        #     print(re)

    def list_ui(self, *args):
        li = self.__grade_ctrl.converted_data()
        self.pagination(li)

    def print_grade(self, grade):
        print(grade.code, grade.name, grade.date, grade.value)

    def pagination(self, li):
        for i in range(1, len(li) + 1):
            self.print_grade(li[i - 1])
            if i % 3 == 0:
                print("________________________________________", end="\n\n")
                inp = input("Next Page:")
                if inp.lower() != "yes":
                    break

    def quit_ui(self, *args):
        quit()

    def run(self):
        options = {"add": self.add_ui, "delete": self.delete_ui, "list": self.list_ui, "quit": self.quit_ui}
        while True:
            inp = input("> ")
            inp = inp.strip().split(" ")
            try:
                options[inp[0]](*inp)
            except KeyError:
                print("option wasn't implemented")
            except ValidatorError as ve:
                print(ve)