from store.domain.Quiz import Quiz
from store.domain.validators import Validator, ValidatorError

__author__ = 'victor'


class QuizValidator(Validator):
    @staticmethod
    def validate(quiz: Quiz):
        errors = []
        if quiz.question == "":
            errors.append("Question can't be empty string")
        if quiz.answer == "":
            errors.append("Answer can't be empty string")
        if quiz.correct == "":
            errors.append("Correct can't be empty string")
        if len(errors) > 0:
            raise ValidatorError(str(errors))