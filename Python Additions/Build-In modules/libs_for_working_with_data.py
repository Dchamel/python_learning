# decimal
# for round decimal numbers
import decimal

# ---------

# math
# for popular math functions and constants
import math

# ---------

# random
# for random generators
import random

random.random()
random.uniform(2.5, 10.0)
random.expovariate(1 / 5)
random.randrange(0, 101, 2)
random.choice([1, 2, 3])
random.shuffle(range(0, 10, 2))
random.sample(range(0, 10, 2), 2)

# ---------

# secrets
# for cryptography random numbers
import string
import secrets

alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(8))
password

# ---------

# uuid
# for implementing universal ids
import uuid

print(uuid.uuid1())
# print(uuid.uuid2())
print(uuid.uuid3(uuid.NAMESPACE_DNS, 'python.ord'))
print(uuid.uuid4())
print(uuid.uuid5(uuid.NAMESPACE_DNS, 'python.ord'))

# ---------

# base43
# for coding binary data into ASCII symbols
import base64

encoded = base64.b64encode(bytes(password, 'utf-8'))
print(encoded)

decoded = base64.b64decode()
print(decoded)

# ---------

# pprint
# for output data in useful format
import pprint

# ---------

# logging
# for log events
import logging

# ---------

# statistics
# for calculate math stat data
import statistics

# ---------

# datetime
# for work with date and timestamp
import datetime

# ---------

# time
# for time
import time

# ---------

# calendar
# for dates, week days, date ranges etc...
import calendar

# ---------

# re
# for regular expressions
import re

# ---------
