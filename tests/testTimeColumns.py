import unittest
import json
import pandas as pd

with open("Lesson.ipynb", "r") as file:
    f_str = file.read()

doc = json.loads(f_str)

code = [i for i in doc['cells'] if i['cell_type']=='code']
si = {}
for i in code:
    for j in i['source']:
        if "#si-exercise" in j:
            exec("".join(i['source']))


class testCases(unittest.TestCase):

    def testTimeColumns(self):
      answer = pd.read_csv("tests/answerPandas.csv")

      day = answer['day_of_week'].equals(occupancy['day_of_week'])
      hour = answer['hour'].equals(occupancy['hour'])
      minute = answer['minute'].equals(occupancy['minute'])
      print(day, minute, hour)

      self.assertTrue(day & hour & minute, "Your 'day', 'minute', and/or 'hour' column is incorrectly built.")
