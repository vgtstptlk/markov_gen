# file for testing structs
# every struct will be checked here

from n_tree import Tree
import markov
import os
from own_markov import markov as mrk


def test_tree():
    tree = Tree(["hello"])
    tree.append_el(["my friend"], "A")
    tree.append_el("honey", "A")
    tree.append_el(["atmta", "vsyachena"], "B")
    tree.append_el("magicmag", "B")
    print(tree[None], tree["A"])
    print(tree)


def normalize(file_name):
    f = open(file_name, 'r')
    result = f.read()
    result = result.replace('\n', '')
    while result.find('  ') != -1:
        result.replace('  ', ' ')

    return result


def save_text(text, file_name="output_text.txt"):
    f = open(file_name, 'w')
    f.write(text)


def test_markov(size=100, file_name="sample1.txt"):
    mark = markov.train_model(normalize(os.getcwd() + "\\samples\\" + file_name))
    text = markov.generate_sentence(size, mark)
    save_text(text)
    print(text)


def own_markov():
    mark = mrk()
    mark.train_from_text("Раз есть две такие взаимоисключающие области, значит есть и граница между ними "
                             "(она называется горизонтом событий). Свет оказавшийся на этой границе и движущийся "
                             "в правильном направлении, может выйти на орбиту вокруг черной дыры. "
                             "То есть он не будет «засасываться» черной дырой, и тем не менее уже "
                             "не сможет удалиться от неё, а вместо этого"
                             " будет вечно вращаться по орбите вокруг черной дыры."
                             " Это и будет пограничным состоянием между пролететь мимо и быть поглощенным.")
    mark.generate_text()


test_tree()
test_markov()
