from store.domain.Question import Question
from store.domain.validators import Validator, ValidatorError

__author__ = 'victor'


class QuestionValidator(Validator):
    @staticmethod
    def validate(question: Question):
        errors = []
        if question.question == "":
            errors.append("Question can't be empty")
        if question.correct == "":
            errors.append("Correct answer can't be empty")
        if question.a == "":
            errors.append("value answer can't be empty")
        if question.b == "":
            errors.append("value answer can't be empty")
        if question.c == "":
            errors.append("value answer can't be empty")
        if len(errors) > 0:
            raise ValidatorError(str(errors))