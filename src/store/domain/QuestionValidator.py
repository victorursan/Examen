from store.domain.Question import Question
from store.domain.validators import Validator, ValidatorError

__author__ = 'victor'


class QuestionValidator(Validator):
    @staticmethod
    def validate(question: Question):
        errors = []
        if len(errors) > 0:
            raise ValidatorError(str(errors))