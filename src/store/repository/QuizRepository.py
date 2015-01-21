__author__ = 'victor'

from store.domain.Quiz import Quiz
from store.domain.validators import RepositoryError
from store.repository.Repository import Repository


class QuizRepository(Repository):
    def __init__(self, validator, file_name):
        Repository.__init__(self, validator)
        self.__file_name = file_name
        self.__load()

    def save(self, item):
        super().save(item)
        self.__save(item)

    def update(self, Id, item):
        super().update(Id, item)
        self.__update()

    def delete(self, Id):
        super().delete(Id)
        self.__update()

    def __update(self):
        try:
            with open(self.__file_name, "w") as f:
                for qui in self.get_all():
                    q = str(qui.Id) + ", " + qui.question + ", " + qui.answer + qui.correct + "\n"
                    f.write(q)
        except Exception as ex:
            print(RepositoryError("Error opening file in updatef " + self.__file_name, ex))

    def __load(self):
        try:
            with open(self.__file_name) as f:
                for line in f:
                    try:
                        arr = line.split(", ")
                        q = Quiz(int(arr[0]), arr[1], arr[2], arr[3])
                        super().save(q)
                    except Exception as ex:
                        raise RepositoryError("Corrupted file", ex)
        except Exception as ex:
            print(RepositoryError("Error opening file " + self.__file_name, ex))
            quit()

    def __save(self, quiz: Quiz):
        try:
            with open(self.__file_name, "a") as f:
                q = quiz.Id + ", " + quiz.question + ", " + quiz.answer + ", " + quiz.correct + "\n"
                f.write(q)
        except Exception as ex:
            print(RepositoryError("Error opening file " + self.__file_name, ex))