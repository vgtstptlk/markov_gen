import random
from new_dict import MarkDict


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


def train_model_higher(data):
    data = data.split(' ')
    markov_model = dict()
    k = 1
    for i in range(0, len(data)//2 -1):
        data[i] = data[k] + ' ' + data[k+1]
        k += 2

    for i in range(0, len(data)-1):
        if data[i] in markov_model:

            markov_model[data[i]].update([data[i+1]])
        else:
            markov_model[data[i]] = MarkDict([data[i+1]])
    return markov_model
