from copy import deepcopy

class Module:
    def __init__(self):
        self.data = []
        self.i = -1

    def __getitem__(self, index):
        '''
        Getter for the [] operator
        '''
        if index >= len(self.data):
            raise IndexError("Index out of range.")
        return self.data[index]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def extend(self, NR):
        self.data.extend([0] * NR)

    def append(self, object):
        self.data.append(object)

    def __len__(self):
        return len(self.data)

    def __iter__(self):
            return iter(self.data)

    def __next__(self):
        if self.i < len(self.data) - 1:
            self.i += 1
            return self.data[self.i]
        else:
            raise StopIteration

    def __len__(self):
        return len(self.data)


def gnomeSort(list):
    i, j, size = 1, 2, len(list)
    cpy = deepcopy(list)
    while i < size:
        if cpy[i - 1] <= cpy[i]:
            i, j = j, j + 1
        else:
            cpy[i - 1], cpy[i] = cpy[i], cpy[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    return cpy


def _filter(list, f):
    result = []
    for e in list:
        if f(e):
            result.append(e)
    return result

def lbm(x):
    if x % 3 == 0:
        return False
    else:
        return True

if __name__ == "__main__":
    a = Module()
    a.extend(4)
    print(a.data)
    a[0] = 15
    a[1] = 10
    a[2] = 5
    a[3] = 3
    a.extend(1)
    print(a.data)
    for i in a:
        print(i)
    print("The sort")
    for i in gnomeSort(a):
        print(i)
    print("The Filter")
    for i in _filter(a, lambda x: x % 3):
        print(i)