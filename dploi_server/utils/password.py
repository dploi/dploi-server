#-*- coding: utf-8 -*-
import random
import string

srandom = random.SystemRandom()
CHARACTER_CHOICES = string.ascii_lowercase + string.ascii_uppercase + string.digits


def generate_password(length=12, characters=CHARACTER_CHOICES):
    return ''.join(srandom.choice(characters) for x in range(length))