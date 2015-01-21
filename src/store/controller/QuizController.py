from store.domain.Quiz import Quiz
from store.domain.validators import DuplicateIdError
from store.repository.QuizRepository import QuizRepository

__author__ = 'victor'


class QuizController(object):
    def __init__(self, repo: QuizRepository):
        self.__repo = repo

    def add_quiz(self, Id, question, answer, correct):
        q = Quiz(Id, question, answer, correct)
        if Id in [q.Id for q in self.__repo.get_all()]:
            raise DuplicateIdError("Code does not exist")
            return
        self.__repo.save(q)

    def find(self, Id):
        if len(self.__repo.get_all()) == 0:
            return False
        return Id in [q.Id for q in self.__repo.get_all()]

    def get_all(self):
        return self.__repo.get_all()