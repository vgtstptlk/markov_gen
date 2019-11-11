# file for testing structs
# every struct will be checked here

#from n_tree import Tree
from markov import Markov
import os
#from own_markov import markov as mrk


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


def test_markov(size=100, file_name="sample1.txt"):
    markov = Markov()
    mark = markov.train_model(normalize(os.getcwd() + "\\samples\\" + file_name))
    text = markov.generate_sentence(size, mark)
    save_text(text)
    save_long_file(text, file_name)
    print(text)


def test_markov_with_higher_level(size=100, file_name="sample1.txt"):
    markov = Markov()
    mark = markov.train_model_higher(normalize(os.getcwd() + "\\samples\\" + file_name))
    text = markov.generate_sentence(size, mark)
    save_text(text)
    save_long_file(text, file_name)
    print(text)

#test_tree()
#test_markov(50, "intro.txt")


test_markov_with_higher_level(100, "sample5_LEARN.txt")
