import unittest
from sys import path
import json
path.append("../")

from ezdict import EZDict

with open("data/20.json") as small_file:
    small_data = json.loads(small_file.read())


class TestEZDict(unittest.TestCase):
    def test_empty(self):
        self.assertEqual({}, EZDict())

    def test_from_dict(self):
        data = {str(i): i for i in range(10)}
        self.assertEqual(dict(data), EZDict(data))

    def test_from_seq(self):
        seq = [(str(i), i) for i in range(10)]
        self.assertEqual(dict(seq), EZDict(seq))

    def test_from_nested(self):
        self.assertEqual(dict(small_data[0]), EZDict(small_data[0]))

    def test_single_nested(self):
        self.assertEqual(
            small_data[0]["friends"],
            EZDict(small_data[0]).friends
        )

    def test_double_nested(self):
        self.assertEqual(
            small_data[0]["favoriteFruit"]["apple"],
            EZDict(small_data[0]).favoriteFruit.apple
        )

    def test_increment(self):
        genders = EZDict()
        manual = {}
        for item in small_data:
            genders.incrementer(EZDict(item).gender)

            if item["gender"] in manual:
                manual[item["gender"]] += 1
            else:
                manual[item["gender"]] = 1

        self.assertEqual(manual, genders)

    def test_append(self):
        genders = EZDict()
        manual = {}
        for item in small_data:
            genders.appender(EZDict(item).gender, item)

            if item["gender"] in manual:
                manual[item["gender"]].append(item)
            else:
                manual[item["gender"]] = [item]

        self.assertEqual(manual, genders)


if __name__ == "__main__":
    unittest.main()
