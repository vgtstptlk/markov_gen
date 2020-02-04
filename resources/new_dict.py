import random


class MarkDict(dict):
    def __init__(self, old_dict=None):
        super(MarkDict, self).__init__()
        self.types = 0
        self.tokens = 0
        if old_dict:
            self.update(old_dict)

    def update(self, old_dict):
        for item in old_dict:
            if item in self:
                self[item] += 1
                self.tokens += 1
            else:
                self[item] = 1
                self.types += 1
                self.tokens += 1

    def count(self, item):
        if item in self:
            return self[item]
        return 0

    def return_weighted_random_word(self):
        random_int = random.randint(0, self.tokens-1)
        index = 0
        list_keys = list(self.keys())
        for i in range(0, self.types):
            index += self[list_keys[i]]
            if index > random_int:
                return list_keys[i]
