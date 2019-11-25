import random
from new_dict import MarkDict


# Класс нужен для создания независимых объектов в main
class Markov:
    # Создаем простую модель с окном в 1 слово. Используется для вводной части
    def train_model(self, data):
        markov_model = MarkDict()
        data = data.split()
        for i in range(0, len(data)-1):
            if data[i] in markov_model:

                markov_model[data[i]].update([data[i+1]])
            else:
                markov_model[data[i]] = MarkDict([data[i + 1]])
        return markov_model

    def generate_start(self, model):

        if '.' in model.keys():
            print(0)
            return model['.'].return_weighted_random_word()
        print(1)
        return random.choice(list(model.keys()))

    # Здесь мы находим первое слово, а дальше по принципу марковской цепи находим последующие
    def generate_sentence(self, length, markov_model):
        current_word = Markov.generate_start(self, markov_model)
        sentence = [current_word]
        for i in range(0, length):
            # print(markov_model[current_word])
            current_dictogram = markov_model[current_word]
            random_weighted_word = current_dictogram.return_weighted_random_word()
            current_word = random_weighted_word
            sentence.append(current_word)
        sentence[0] = sentence[0].capitalize()
        return ' '.join(sentence) + '.'

    # Создание окна в 2 слова. Использую только для главной части (т.к. нужен большой объем словаря)
    # Мы просто привязываем к слову 2 последующих слова, а дальше тот же алгоритм
    def train_model_higher(self, data):
        data = data.split(' ')
        markov_model = dict()
        k = 1

        for i in range(0, len(data)//2-1):
            data[i] = data[k] + ' ' + data[k+1]
            k += 2

        for i in range(0, len(data)-1):
            if data[i] in markov_model:

                markov_model[data[i]].update([data[i+1]])
            else:
                markov_model[data[i]] = MarkDict([data[i+1]])
        return markov_model
