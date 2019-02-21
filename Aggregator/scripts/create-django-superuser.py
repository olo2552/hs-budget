#!/usr/bin/env python
import sys
import os

import pexpect


def main():
    validate_args(sys.argv)
    _, python, managepy, username, password = sys.argv

    if exists(username, python, managepy):
        pass
    else:
        print("Creating superuser!")
        create_django_superuser(python, managepy, username, password)


def create_django_superuser(python, managepy, username, password):
    p = pexpect.spawn("{} {} createsuperuser --username {}".format(python, managepy, username))

    p.expect("Email address:")
    p.sendline("")

    p.expect("Password")
    p.sendline(password)

    p.expect("Password")
    p.sendline(password)

    if p.expect(["Bypass password validation and create user anyway?", "Superuser created successfully"]) == 0:
        p.sendline("y")
        p.interact()


def exists(username, python, managepy):

    raw_output = pexpect.run("""{} {} shell --command 'from django.contrib.auth.models import User;users = User.objects.all();usernames = map(lambda u: u.username, users);print("{}" in usernames)'""".format(python, managepy, username))

    output = raw_output.decode('utf-8').rstrip()

    string_to_bool = {
        "True": True,
        "False": False,
    }

    return string_to_bool[output]
    

def validate_args(args):
    if len(sys.argv) > 4 + 1:
        log_and_quit("Too many arguments", err_code=2)
    
    if len(sys.argv) < 4 + 1:
        log_and_quit("Too few arguments", err_code=3)


def log_and_quit(err, err_code=1):
    print("Err: {}. Usage: <python executable> <path to manage py> <username> <password>".format(err), file=sys.stderr)
    exit(err_code)


if __name__ == "__main__":
    main()
