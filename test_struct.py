# file for testing structs
# every struct will be checked here

from n_tree import Tree


def test_tree():
    tree = Tree("hello")
    tree.append_el(["my friend"], "A")
    tree.append_el("honey", "A")
    print(tree[None], tree["A"])
    print(tree)


test_tree()