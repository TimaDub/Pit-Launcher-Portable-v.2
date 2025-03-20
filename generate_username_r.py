import os
import random
from PyQt6.QtCore import QFile, QIODevice


def generate_username(num_results=1):
    # Чтение из adjectives.txt
    file_a = QFile("assets/data/adjectives.txt")
    if not file_a.open(QIODevice.OpenModeFlag.ReadOnly):
        return None

    data_a = file_a.readAll().data().decode("utf-8")
    file_a.close()

    # Чтение из nouns.txt
    file_n = QFile("assets/data/nouns.txt")
    if not file_n.open(QIODevice.OpenModeFlag.ReadOnly):
        return None

    data_n = file_n.readAll().data().decode("utf-8")
    file_n.close()

    # Разделение данных на строки
    adjectives = [line.strip() for line in data_a.splitlines()]
    nouns = [line.strip() for line in data_n.splitlines()]

    # Генерация имен пользователей
    usernames = []
    for _ in range(num_results):
        adjective = random.choice(adjectives)
        noun = random.choice(nouns).capitalize()
        num = str(random.randrange(10))
        usernames.append(adjective + noun + num)

    return usernames
