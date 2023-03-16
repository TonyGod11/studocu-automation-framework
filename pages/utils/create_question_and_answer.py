import logging
from random import randrange

from random_word import RandomWords


def generate_random_question():
    logging.info("Random question generation")
    question = "This is a random question " + str(randrange(10))
    return question


def generate_random_answer():
    logging.info("Random answer generation")
    r = RandomWords()
    return r.get_random_word()
