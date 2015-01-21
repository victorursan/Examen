from store.repository.QuizRepository import QuizRepository

__author__ = 'victor'


class QuizController(object):
    def __init__(self, repo: QuizRepository):
        self.__repo = repo