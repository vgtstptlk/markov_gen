class Node:
    def __init__(self, dat):
        self.value = dat
        self.next = None


class List:
    def __init__(self):
        self.head = None

    def append(self, node):
        if not self.head:  # if seq is empty
            self.head = Node(node);
        else:  # if is not => next = new item
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(node)

    def append_first(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def length(self):
        cur = self.head
        count = 0
        while not cur:
            count += 1
            cur = cur.next
        return count

    def pop(self):  # deleting. for future in lab
        cur = self.head
        if List.length(self) == 1:
            cur = None
            return
        while ((cur.next).next != None):
            cur = cur.next
        cur.next = None

    def append_from(self, sequence):  # append from others sequences (list, ...)
        for item in sequence:
            List.append(self, item)

    def __str__(self):  # system func for printing list
        l = "["
        cur = self.head
        l += '"' + str(cur.value) + '", '
        cur = cur.next
        while cur != None:
            l += '"' + str(cur.value) + '", '
            cur = cur.next
        l = l[0:-2]  # deleting ", " in the end
        l += "]"
        return l

    def __len__(
            self):  # for item in sequence does not work without this func :(. updЖ does not work with this thing too
        return List.length(self)

    def __getitem__(self, key):  # system class for accessing to item. for ex. "a[1]"
        length = 0
        cur1 = None
        cur = self.head
        while key != length and cur.next != None:
            cur = cur.next
            length += 1
        if key == length:
            cur1 = cur.value
        return cur1
