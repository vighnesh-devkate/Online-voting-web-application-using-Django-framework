#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onlineVotingSystem.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        raise ImportError(
            "Django is not installed or not accessible."
            "Make sure it's installed and available on your PYTHONPATH environment variable, "
            "or activate your virtual environment if you're using one."
        )
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
