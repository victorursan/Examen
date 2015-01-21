from store.repository.QuestionRepository import QuestionRepository
import random

__author__ = 'victor'


class QuestionController(object):
    def __init__(self, repo: QuestionRepository):
        self.__repo = repo

    def get_random(self, nr):
        lst = []
        elements = self.__repo.get_all()
        for i in range(nr):
            el = random.choice(elements)
            lst.append(el)
            elements.pop(elements.index(el))
        return lst