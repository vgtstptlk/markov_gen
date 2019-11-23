"""
Для генерации текста нужно запустить main.py. Для генераци текста без грамматик запустите test_struct.py.
Каждый новый текст будет сгенерирован в output.txt.
Посмотреть историю можно в examples.txt.
Лучшие тексты (по мнению автора) записаны в best.txt или в паблике марковской цепи, где она выкладывает мысли не только
о физике, но и по философии. Иногда даже пишет новые главы романа "Преступление и наказание".
https://vk.com/markov_thoughts
"""


from markov import Markov
import os
import random


intro = []
main_part = []


def normalize(file_name):
    f = open(file_name, 'r')
    result = f.read()
    result = result.replace('\n', '').replace(';', ',').replace('"', '')
    while result.find('  ') != -1:
        result = result.replace('  ', ' ')
    f.close()
    return result


def save_long_file(text, sample, file_name="examples.txt"):
    f = open(file_name, 'a')
    f.write('-----------'+sample+'-------------\n')
    f.write(text+'\n')
    f.write('------------end----------------\n')
    f.close()


def save_text(text, file_name="output_text.txt"):
    f = open(file_name, 'w')
    f.write(text)
    f.close()


# Для более веселых текстов создаем несколько примеров
def gen_markov(lst, size=100, file_name="sample1.txt"):
    markov = Markov()
    mark = markov.train_model(normalize(os.getcwd() + "\\samples\\" + file_name))
    for i in range(5):
        lst.append(markov.generate_sentence(size, mark))
    return lst


def gen_markov_higher(lst, size=100, file_name="sample1.txt"):
    markov = Markov()
    mark = markov.train_model_higher(normalize(os.getcwd() + "\\samples\\" + file_name))
    for i in range(30):
        lst.append(markov.generate_sentence(size, mark))
    return lst


gen_markov(intro, 10, "intro.txt")
gen_markov_higher(main_part, 100, "sample5_LEARN.txt")
random.choice(intro)+random.choice(main_part)
text = (random.choice(intro)+random.choice(main_part)).replace(':.', '.').replace('.,', ',').replace('.-', '-').replace('..', '.').replace(',.', '.')
save_long_file(text, "Грамматики")
save_text(text)
