import random
import string


def generate_random_string_lowercase(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def generate_random_string_uppercase(length):
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(length))


def generate_random_definite_char(length: int, char: str):
    """Generate_random_definite_char() Генерация строки с определенными символами.
    Принимает первым агрументом длину строки, вторым аргументом набор чаров строкой"""
    letters = char
    return ''.join(random.choice(letters) for i in range(length))


def generate_random_string_a_non_repeat_char(length):
    letters = string.ascii_lowercase
    return ''.join(random.sample(letters, length))


def generate_alphanum_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.sample(letters_and_digits, length))


def generator_phone_number():
    return '89' + str(random.randint(170000000, 999999999))


def get_list_num(a):
    return [i for i in range(a)]