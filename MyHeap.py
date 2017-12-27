

class MyHeap:
    def __init__(self):
        self.values = [-1]

    def __str__(self):
        return str(self.values)

    def add(self, element):
        self.values.append(element)
        self._shift_up(self.size())

    def remove(self):
        if self.empty():
            raise Exception("Cannot remove from empty heap.")

        self._swap_values(1, self.size())

        element = self.values.pop()

        if not self.empty():
            self._shift_down(1)

        return element

    def size(self):
        return len(self.values) - 1

    def empty(self):
        return self.size() == 0

    @staticmethod
    def _parent(index):
        return index // 2

    @staticmethod
    def _left_child(index):
        return 2*index

    @staticmethod
    def _right_child(index):
        return 2*index+1

    def _shift_up(self, index):
        if index == 1:
            return

        if self.values[self._parent(index)] >= self.values[index]:
            self._swap_values(index,self._parent(index))

        self._shift_up(self._parent(index))

    def _shift_down(self, index):
        if self._left_child(index) > len(self.values) - 1:
            return

        right_valid = self._right_child(index) < len(self.values)
        if self.values[index] > self.values[self._left_child(index)] and (
                not right_valid or self.values[self._left_child(index)] < self.values[self._right_child(index)]):
            self._swap_values(index, self._left_child(index))
            self._shift_down(self._left_child(index))
        elif right_valid and self.values[index] > self.values[self._right_child(index)]:
            self._swap_values(index, self._right_child(index))
            self._shift_down(self._right_child(index))

    def _swap_values(self, a, b):
        self.values[a], self.values[b] = self.values[b], self.values[a]

