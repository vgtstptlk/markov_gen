import unittest
import os
from markov import Markov
from new_dict import MarkDict
standard_first_level = MarkDict({'wrote': {'this': 1}, 'it': {'.': 1, 'will': 1}, 'good': {'today': 1},
                                 'Hello': {'my': 1}, 'work': {'.': 1}, 'now': {'I': 1}, 'used': {'to': 1},
                                 'knows': {'how': 1}, 'friend': {'.': 1}, 'So': {'I': 1}, "Let's": {'go.': 1},
                                 '.': {"Let's": 1, 'So': 1, 'I': 2}, 'will': {'work': 1},
                                 'to': {'write': 1, 'test': 1}, 'nobody': {'knows': 1}, 'write': {'this': 1},
                                 'feeling': {'good': 1}, 'I': {'wrote': 1, 'need': 1, 'used': 1, 'would': 1, 'am': 1},
                                 'and': {'nobody': 1, 'now': 1}, 'need': {'to': 1}, 'my': {'friend': 1},
                                 'generator': {'and': 1}, 'today': {'.': 1}, 'would': {'check': 1},
                                 'check': {'this': 1}, 'how': {'it': 1}, 'this': {'and': 1, 'text': 1, 'generator': 1},
                                 'test': {'it': 1}, 'text': {'cause': 1}, 'cause': {'I': 1}, 'am': {'feeling': 1}})

standard_second_level = MarkDict({'wrote': {'this': 1}, 'test it': {". Let's": 1}, 'need to': {'test it': 1},
                                  'good today': {'. I': 1}, 'cause': {'I': 1}, 'work': {'.': 1},
                                  'this and': {'nobody knows': 1}, 'would check': {'this and': 1},
                                  'knows': {'how': 1}, 'go.': {'': 1}, 'I wrote': {'this text': 1},
                                  'So': {'I': 1}, 'am feeling': {'good today': 1}, '.': {"Let's": 1, 'So': 1},
                                  'will': {'work': 1}, 'my friend': {'. I': 1}, 'nobody': {'knows': 1},
                                  'cause I': {'need to': 1}, "Let's": {'go.': 1}, 'used to': {'write this': 1},
                                  'and': {'nobody': 1}, 'test': {'it': 1}, 'I': {'wrote': 1, 'need': 1},
                                  'now I': {'would check': 1}, 'nobody knows': {'how it': 1}, ". Let's": {'this': 1},
                                  'it': {'.': 1, 'will': 1}, 'to': {'test': 1}, 'how it': {'will work': 1},
                                  'this text': {'cause I': 1}, 'generator and': {'now I': 1},
                                  'need': {'to': 1}, '. I': {'am feeling': 1, 'used to': 1}, 'how': {'it': 1},
                                  'this': {'and': 1, 'text': 1}, 'write this': {'generator and': 1},
                                  'text': {'cause': 1}, 'will work': {'. So': 1}, '. So': {'I wrote': 1}})


class TestTrain(unittest.TestCase):
    def setUp(self):
        self.mark = Markov()
        self.model = self.mark.train_model(open(os.getcwd() + "\\samples\\" + "TEST.txt", "r").read())
        self.model_higher = self.mark.train_model_higher(open(os.getcwd() + "\\samples\\" + "TEST.txt", "r").read())

    def test_len(self):
        self.assertTrue(len(self.model) != 0, "Len must be >=0 ")

    def test_model(self):
        self.assertEquals(len(self.model), len(standard_first_level))

    def test_model_higher(self):
        self.assertEquals(len(self.model_higher), len(standard_second_level))

    def test_random_begin(self):
        self.assertTrue(self.mark.generate_start(self.model) in self.model['.'], "Error in generate_start")


if __name__ == '__main__':
    unittest.main()
