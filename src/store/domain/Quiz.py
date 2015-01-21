__author__ = 'victor'


class Quiz(object):
    def __init__(self, Id, question, answer, correct):
        self.__Id = Id
        self.__question = question
        self.__answer = answer
        self.__correct = correct

    @property
    def Id(self):
        return self.__Id

    @property
    def question(self):
        return self.__question

    @property
    def answer(self):
        return self.__answer

    @property
    def correct(self):
        return self.__correct

    @Id.setter
    def Id(self, value):
        self.__Id = value

    @question.setter
    def question(self, value):
        self.__question = value

    @answer.setter
    def answer(self, value):
        self.__answer = value

    @correct.setter
    def correct(self, value):
        self.__correct = value