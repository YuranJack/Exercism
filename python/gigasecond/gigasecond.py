from ast import Add
from datetime import datetime, timedelta
from sqlite3 import Time
from time import time
from xmlrpc.client import DateTime


def add(moment):
    giga_second = timedelta(seconds=1000000000)
    return moment + giga_second
