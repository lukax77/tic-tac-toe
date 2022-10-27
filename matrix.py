class Matrix:
    def __init__(self, rows, columns, fill=0):
        self.rows = rows
        self.columns = columns
        self.fill = fill
        self.matrix = self.makeMatrix()

    def __getitem__(self, tup):
        row, column = tup
        return self.matrix[row][column]

    def __setitem__(self, tup, value):
        row, column = tup
        self.matrix[row][column] = value

    def setValues(self, array):
        if self.rows == len(array) and self.columns == len(array[0]):
            for i in range(self.rows):
                for j in range(self.columns):
                    self[i, j] = array[i][j]

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

    def product(self, b):
        rows_a = self.rows          
        columns_a = self.columns    
        rows_b = b.rows             
        columns_b = b.columns  

        if columns_a != rows_b:
            print('Error')
            return Matrix(0, 0)

        result = Matrix(rows_a, columns_b) 
        
        for i in range(rows_a): 
            for j in range(columns_b):
                accumulator = 0
                
                for k in range(columns_a):
                    accumulator += self[i, k] * b[k, j]

                result[i, j] = accumulator
        
        return result

    def addition(self, b):
        for i in range(self.rows):
            for j in range(self.columns):
                self[i, j] = self[i, j] + b[i, j]


    def apply_function(self, f):
        for i in range(self.rows):
            for j in range(self.columns):
                self[i, j] = f(self[i, j])
                
    def find_max_value(self):
        max = self[0, 0]
        row, col = 0, 0
        for i in range(self.rows):
            for j in range(self.columns):
                if self[i, j] > max:
                    max = self[i, j]
                    row = i
                    col = j

        return (row, col, max)


def test():
    a = [[3, 2, 1], [1, 1, 3], [0, 2, 1]]
    m = Matrix(3, 3)
    m.setValues(a)
    m.to_string()

    
    b = [[2, 1], [1, 0], [3, 2]]
    m2 = Matrix(3, 2)
    m2.setValues(b)
    m2.to_string()

    r = m.product(m2)
    r.to_string()


if __name__ == '__main__':
    test()
