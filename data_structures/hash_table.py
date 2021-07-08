import random


class Hash_Table:
    def __init__(self):
        self.seed = random.randint(0, 1000)
        self.table = [[] for i in range(0, 2069)]

    def hash(self, string):
        random.seed(self.seed)

        hash_value = 0

        for char in str(string):
            hash_value += ord(char) * random.randint(0, 1000)

        return hash_value % 2069

    def set_val(self, key, value):
        hash_value = self.hash(key)
        for i in range(0, len(self.table[hash_value])):
            if self.table[hash_value][i][0] == key:
                self.table[hash_value][i][1] = value
                return

        self.table[hash_value].append([key, value])

    def get_val(self, key):
        hash_value = self.hash(key)
        for i in range(0, len(self.table[hash_value])):
            if self.table[hash_value][i][0] == key:
                return self.table[hash_value][i][1]
        return None

    def del_val(self, key):
        hash_value = self.hash(key)
        for i in range(0, len(self.table[hash_value])):
            if self.table[hash_value][i][0] == key:
                del self.table[hash_value][i]
                return
        return None


if __name__ == "__main__":
    h = Hash_Table()
    h.set_val("one", 1)
    h.set_val("two", 2)
    print(h.get_val("one"))
    print(h.get_val("two"))
    h.del_val("two")
    print(h.get_val("two"))
