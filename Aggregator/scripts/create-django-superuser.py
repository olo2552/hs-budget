#!/usr/bin/env python
import sys

import pexpect


try:
    _, python, managepy, username, password = sys.argv
except ValueError:
    print("Usage: <python executable> <path to manage py> <username> <password>", file=sys.stderr)
    exit(1)

p = pexpect.spawn ("{} {} createsuperuser --username {}".format(python, managepy, username))

expect, send, interact = p.expect, p.sendline, p.interact

expect("Email address:")
send("")

expect("Password")
send(password)

expect("Password")
send(password)

expect("Bypass password validation and create user anyway?")
send("y")

interact()

