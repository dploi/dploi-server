#-*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
import re
import string

VARIABLE_ALLOWED_CHARS = string.ascii_lowercase + string.digits + '_'
VARIABLE_REGEX = '^[%s]*$' % (VARIABLE_ALLOWED_CHARS,)
VARIABLE_REGEX_COMPILED = re.compile(VARIABLE_REGEX)

VARIABLE_AND_DASH_ALLOWED_CHARS = VARIABLE_ALLOWED_CHARS + '-'
VARIABLE_AND_DASH_REGEX = '^[%s]*$' % (VARIABLE_AND_DASH_ALLOWED_CHARS,)
VARIABLE_AND_DASH_REGEX_COMPILED = re.compile(VARIABLE_AND_DASH_REGEX)


def variable_name_validator(value):
    """
    validates that the value is a valid variable name

    * lower case, a-z, 0-9, _
    * no spaces, no dashes or any other special characters
    """
    if not VARIABLE_REGEX_COMPILED.search(value):
        raise ValidationError('allowed characters: %s' % VARIABLE_ALLOWED_CHARS)


def variable_name_and_dash_validator(value):
    """
    validates the same as variable_name_validator, but may also include "-"
    """
    if not VARIABLE_AND_DASH_REGEX_COMPILED.search(value):
        raise ValidationError('allowed characters: %s' % VARIABLE_AND_DASH_ALLOWED_CHARS)