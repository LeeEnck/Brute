from sys import exit
from random import randint
from textwrap import dedent


#Start
class area(object):

    def play(self):
        pass


class Death(area):

    def enter(self):
        print(dedent("""
            You have died
            """))

        exit(1)
