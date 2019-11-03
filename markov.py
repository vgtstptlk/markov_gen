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

    def return_random_word(self):
        random_key = random.sample(self, 1)
        return random_key[0]

    def return_weighted_random_word(self):
        random_int = random.randint(0, self.tokens-1)
        index = 0
        list_keys = list(self.keys())
        for i in range(0, self.types):
            index += self[list_keys[i]]
            if index > random_int:
                return list_keys[i]


def train_model(data):
    markov_model = dict()
    data = data.split()
    for i in range(0, len(data)-1):
        if data[i] in markov_model:
            # print(data)
            markov_model[data[i]].update([data[i+1]])
        else:
            markov_model[data[i]] = MarkDict([data[i + 1]])
    return markov_model


def generate_start(model):
    return random.choice(list(model.keys()))


def generate_sentence(length, markov_model):
    current_word = generate_start(markov_model)
    sentence = [current_word]
    for i in range(0, length):
        # print(markov_model[current_word])
        current_dictogram = markov_model[current_word]
        random_weighted_word = current_dictogram.return_weighted_random_word()
        current_word = random_weighted_word
        sentence.append(current_word)
    sentence[0] = sentence[0].capitalize()
    return ' '.join(sentence) + '.'


# def train_model_higher(level, data):
#     data = data.split()
#     markov_model = dict()
#     for i in range(0, len(data)-level):
#         wind = tuple(data[i: i+level])
#         if wind in markov_model:
#             markov_model[wind].update([data[i+level]])
#         else:
#             markov_model[wind] = MarkDict([data[i+level]])
#     print(markov_model)
#     return markov_model
