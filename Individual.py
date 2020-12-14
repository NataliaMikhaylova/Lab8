#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Использовать словарь, содержащий следующие ключи: фамилия и инициалы; номер
# группы; успеваемость (список из пяти элементов). Написать программу, выполняющую
# следующие действия: ввод с клавиатуры данных в список, состоящий из словарей заданной
# структуры; записи должны быть упорядочены по возрастанию среднего балла; вывод на
# дисплей фамилий и номеров групп для всех студентов, имеющих оценки 4 и 5; если таких
# студентов нет, вывести соответствующее сообщение.

import json
import sys

def _add(students, name, group, marks):

    student = {
        'name': name,
        'group': group,
        'marks': marks,
    }

    students.append(student)

    if len(students) > 1:
        students.sort(key=lambda item: item.get('marks', 0))

def _list(students):
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 15
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
            "No",
            "Ф.И.О.",
            "Группа",
            "Успеваемость"
        )
    )
    print(line)

    for idx, student in enumerate(students, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                idx,
                student.get('name', ''),
                student.get('group', ''),
                student.get('marks[0]', '')
            )
        )

    print(line)

def _select(marks):

    result = []
    for student in students:
        if sum(student.get('marks', '')) / len(marks) >= 4:
            result.append(student)

    return result

def _load(filename):
    with open(filename, 'r') as f:
        return json.load(f)


def _save(students, filename):
    with open(filename, 'w') as f:
        json.dump(students, f)

def _help():
    print("Список команд:\n")
    print("add - добавить студента;")
    print("list - вывести список студентов;")
    print("select <успеваемость> - запросить студентов с успеваемостью выше четверки;")
    print("load <имя файла> - загрузить данные из файла;")
    print("save <имя файла> - сохранить данные в файл;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")

def _err():
    print(f"Неизвестная команда {command}", file=sys.stderr)

if __name__ == '__main__':
    students = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            name = input("Фамилия и инициалы? ")
            group = input("Номер группы? ")
            marks = list(map(int, input('Введите оценки').split()))

            _add(students, name, group, marks)

        elif command == 'list':
            print(_list(students))


        elif command.startswith('select'):
            selected = _select(students)

            if selected:
                for idx, students in enumerate(selected, 1):
                    print(students.get('name', ''))
            else:
                print("Студентов с такими оценками нет")

        elif command.startswith('load '):
            parts = command.split(' ', maxsplit=1)
            students = _load(parts[1])

        elif command.startswith('save '):
            parts = command.split(' ', maxsplit=1)
            _save(students, parts[1])

        elif command == 'help':
            _help()

        else:
            _err()