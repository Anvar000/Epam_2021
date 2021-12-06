import datetime

from homework5.oop_1 import Student, Teacher

teacher = Teacher('Daniil', 'Shadrin')
student = Student('Roman', 'Petrov')
expired_homework = teacher.create_homework('Learn functions', 0)
create_homework_too = teacher.create_homework
oop_homework = create_homework_too('create 2 simple classes', 5)


def test_create_student():
    assert student.first_name, student.last_name == ('Roman', 'Petrov')


def test_create_teacher():
    assert teacher.first_name, teacher.last_name == ('Daniil', 'Shadrin')


def test_create_and_check_daedline_expired_homework():
    assert expired_homework.deadline == datetime.timedelta(0)


def test_create_and_check_name_expired_homework():
    assert expired_homework.text == "Learn functions"


def test_create_homework_too():
    assert oop_homework.deadline == datetime.timedelta(5)


def test_expired_homework():
    assert not student.do_homework(expired_homework)


def test_homework_too():
    assert student.do_homework(oop_homework) == oop_homework


def test_check_print(capsys):
    student.do_homework(expired_homework)
    captured = capsys.readouterr()
    assert captured.out == "You are late\n"
