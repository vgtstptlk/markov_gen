class Node:
    def __init__(self, value, pointer=None, tag=None):
        self.value = value
        self.pointer = pointer
        self.tag = tag


class Tree:
    def __init__(self, value):  # node - > [0] - value, [1] - pointer for other nodes
        self.nodes = Node(value)

    def append_el(self, el, tag=None):
        cur = self.nodes
        while cur.pointer:
            if cur.tag and (cur.tag == tag):
                cur.value.append(el)
                return
            cur = cur.pointer
        if cur.tag and (cur.tag == tag):
            cur.value.append(el)
            return
        cur.pointer = Node(el, None, tag)

    def __getitem__(self, tag):
        cur = self.nodes
        while cur.tag != tag:
            cur = cur.pointer
        return cur.value

    def __str__(self):
        cur = self.nodes
        result = ""
        while cur.pointer:
            result += str(cur.tag) + ": " + str(cur.value) + "\n"
            cur = cur.pointer
        return result + str(cur.tag) + ": " + str(cur.value)



