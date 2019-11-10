
import markov
import os
import random

intro = []
main_part = []


def gen(rule, g):
    if isinstance(rule, tuple):
        return gen(random.choice(rule), g)
    elif isinstance(rule, list):
        return "".join([gen(x, g) for x in rule])
    elif rule in g:
        return gen(g[rule], g)
    else:
        return str(rule + " ")


random_gen = {
    "S": [intro, "E"],
    "E": (main_part, "M"),
    "M": (main_part, "")

}


normal_gen = {
    "S": [intro, main_part, "E"],
    "E": (main_part, "")
}


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


def gen_markov(lst, size=100, file_name="sample1.txt"):
    mark = markov.train_model(normalize(os.getcwd() + "\\samples\\" + file_name))
    for i in range(30):
        lst.append(markov.generate_sentence(size, mark))
    return lst


def gen_markov_higher(lst, size=100, file_name="sample1.txt"):
    mark = markov.train_model_higher(normalize(os.getcwd() + "\\samples\\" + file_name))
    for i in range(10):
        lst.append(markov.generate_sentence(size, mark))
    return lst


gen_markov_higher(intro, 10, "intro.txt")
gen_markov_higher(main_part, 10, "sample5_LEARN.txt")

text = gen("S", normal_gen).replace('.,', ',').replace('.-', '-').replace('..', '.').replace(',.', '.')
save_long_file(text, "Грамматики")
save_text(text)
