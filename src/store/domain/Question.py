__author__ = 'victor'


class Question(object):
    def __init__(self, Id, question, a, b, c, correct):
        self.__Id = Id
        self.__question = question
        self.__a = a
        self.__b = b
        self.__c = c
        self.__correct = correct

    @property
    def Id(self):
        return self.__Id

    @property
    def question(self):
        return self.__question

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    @property
    def c(self):
        return self.__c

    @property
    def correct(self):
        return self.__correct

    @Id.setter
    def Id(self, value):
        self.__Id = value

    @question.setter
    def question(self, value):
        self.__question = value

    @a.setter
    def a(self, value):
        self.__a = value

    @b.setter
    def b(self, value):
        self.__b = value

    @c.setter
    def c(self, value):
        self.__c = value

    @correct.setter
    def correct(self, value):
        self.__correct = value