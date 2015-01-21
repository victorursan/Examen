from store.repository.QuestionRepository import QuestionRepository

__author__ = 'victor'


class QuestionController(object):
    def __init__(self, repo: QuestionRepository):
        self.__repo = repo