from store.domain.Quiz import Quiz
from store.domain.validators import Validator, ValidatorError

__author__ = 'victor'


class QuizValidator(Validator):
    @staticmethod
    def validate(quiz: Quiz):
        errors = []

        if len(errors) > 0:
            raise ValidatorError(str(errors))