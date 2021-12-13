"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную


1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)

HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'

    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания

2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.

3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования

4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.

    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from collections import defaultdict


class DeadLineError(Exception):
    """A class exception for outdated homeworks.

    Args:
        msg (str): Message describing the exception
    """
    def __init__(self, msg: str):
        """Initialize exception message with msg."""
        self.msg = msg


class Homework:
    """A class to represent a homework.

    Attributes:
        text (str): text of the homework.
        deadline (datetime.timedelta): number of days for
            the doing the homework.
        created (datetime.datetime): a datetime of creating
            the homework.
    """
    def __init__(self, text: str, deadline: int) -> None:
        """Initialize a homework, and a deadline

        Args:
            text (str): text of the homework
            deadline (int): number of days for the doing the homework.
        """
        self.text = text
        self.deadline = datetime.timedelta(days=deadline)
        self.created = datetime.datetime.now()

    def is_activated(self) -> bool:
        """Check if the homework deadline is not outdated

        Returns:
            bool: True if if homework's deadline is not expired
                  False otherwise.
        """
        time = datetime.datetime.today()
        if time - self.created > self.deadline:
            return False
        return True


class Person():
    """A class to represent a person

    Attributes:
        last_name (str): a last name of the person
        first_name (str): a first name of the person
    """
    def __init__(self, first_name: str, last_name: str) -> None:
        """Initialise a person with last_name and first_name.

        Args:
            first_name: a first name of a person.
            last_name: a last name of a person.
        """
        self.first_name = first_name
        self.last_name = last_name


class Student(Person):
    """A class to rerepsent a student

    The class inherits properties from the Person.
    """
    def do_homework(self, homework: Homework, solution: str):
        """Check if a homework is active or not.

        Args:
            homework (Homework): a homework that should be done
            solution (str): a text solution of the homework.

        Returns:
            Receive a homework and a solution and returns object of
            HomeworkResult, if homework is active,
            else if the task is outdated, then raises exception
            DeadLineError 'You are late' and returns None.
        """
        if homework.is_activated():
            return HomeworkResult(self, homework, solution)
        raise DeadLineError("You are late")
        return None


class HomeworkResult():
    """A class saves info about a homework, its author, its solution.

    Attributes:
        author (Student): an author of a homework.
        homework (Homework): a homework.
        solution (str): a solution of the homework.
        created (datetime.datetime): date and time of the
            creating homework solution.
    """
    def __init__(self, author: Student, homework: Homework, solution: str):
        """Initilaze information about homework

        Args:
            author (Student): author of the homework
            homework (Homework): homework with the task
            solution (str): autohor's solution of the homework

        Raises:
            TypeError: if the given homework is not Homework.
        """
        if not isinstance(homework, Homework):
            raise TypeError("You gave a not Homework object")
        self.author = author
        self.homework = homework
        self.solution = solution
        self.created = datetime.datetime.now()


class Teacher(Person):
    """A class to represent a teacher.

    The class inherits properties from the Person.

    Args:
        homework_done (defaultsect): journal, saves results
            of homeworks, groups results by a key homework.
    """
    homework_done = defaultdict(set)
    CRITERIA_FOR_DONE_HW = 5

    @classmethod
    def create_homework(cls, text: str, deadline: int) -> Homework:
        """Create a homework

        Args:
            text (str): a task of the homework
            deadline (int): number of the days before the deadline

        Returns:
            Homework: generated homework
        """
        return Homework(text, deadline)

    @classmethod
    def check_homework(cls, homework_result: HomeworkResult):
        """"Check a homework with a criteria.

            Length of string with the solution should be bigger than 5.

        Args:
            homework_result (HomeworkResult): homework with its solution

        Returns:
            bool: True if homework is done, False otherwise
        """
        if not isinstance(homework_result, HomeworkResult):
            return False
        if len(homework_result.solution) >= cls.CRITERIA_FOR_DONE_HW:
            cls.homework_done[homework_result.homework].add(homework_result)
            return True
        return False

    @classmethod
    def reset_results(cls, homework: Homework = None):
        """Remove given homework from the journal homework_done

        Args:
            homework (Homework): homework, that should be removed, or
                None if all journal should be cleared.
        """
        if isinstance(homework, Homework):
            del Teacher.homework_done[homework]
            return None
        cls.homework_done = defaultdict(set)
        return None


if __name__ == '__main__':
    opp_teacher = Teacher('Daniil', 'Shadrin')
    advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')

    lazy_student = Student('Roman', 'Petrov')
    good_student = Student('Lev', 'Sokolov')

    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read docs', 5)

    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    result_3 = lazy_student.do_homework(docs_hw, 'done')
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print('There was an exception here')
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print(Teacher.homework_done[oop_hw])
    Teacher.reset_results()
