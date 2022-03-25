import random


def rand_email(limit):
    email = "".join(random.choice("abcdefghijklmnopqrstuvwxyz1234567890") for _ in range(limit))
    return email


def rand_user(limit):
    username = "".join(random.choice("abcdefghijklmnopqrstuvwxyz1234567890") for _ in range(limit))
    return username


def rand_pass(limit):
    password = "".join(random.choice("abcdefghijklmnopqrstuvwxyz1234567890") for _ in range(limit))
    return password


def rand_birth(starty, endy, startm, endm, startd, endd, concat_type):
    year = random.randint(starty, endy)
    month = random.randint(startm, endm)
    day = random.randint(startd, endd)
    if concat_type == "hyphen":
        concat = year, "-", month, "-", day
    elif concat_type == "underscore":
        concat = year, "_", month, "_", day
    return concat
