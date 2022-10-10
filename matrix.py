class Matrix:
    def __init__(self, rows, columns, fill=0):
        self.rows = rows
        self.columns = columns
        self.fill = fill
        self.matrix = self.makeMatrix()

    def __getitem__(self, tup):
        row, column = tup
        return self.matrix[row][column]

    def makeMatrix(self):
        m = []
        for i in range(self.rows):
            m.append([self.fill] * self.columns)

        return m

    def to_string(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if j < self.columns - 1:
                    print(f' {self[i, j]} ', end='')
                else:
                    print(f' {self[i, j]} ')


def test():
    m = Matrix(3, 3)
    m.to_string()


if __name__ == '__main__':
    test()
