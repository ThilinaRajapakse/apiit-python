import sys
import os

with os.scandir('test_cases/') as tests:
    for test in tests:
        with open(test, 'r') as t:
            problem = t.readlines()

            ### YOUR SOLUTION HERE ###
