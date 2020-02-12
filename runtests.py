# coding: utf-8
import os
import sys


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "comments.tests.settings")

    from comments.tests import *

    from django.core.management import execute_from_command_line
    execute_from_command_line(['manage.py', 'test'])