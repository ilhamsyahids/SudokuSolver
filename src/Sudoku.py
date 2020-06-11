class Sudoku:
    def __init__(self, matrix):
        """
        The contructors
        """
        super().__init__()
        if (isinstance(matrix, str)):
            matrix = self.preProcessing(matrix)
        self.matrix = matrix
        self.solved = False
        self.number = 5

    def preProcessing(self, matrix):
        """
        Convert string matrix to array of array of int
        """
        replaceZero = matrix.replace("#", '0')
        splittingMatrix = replaceZero.split('\n')
        intMatrix = map(
            lambda x: [int(i) for i in x.split(' ')],
            splittingMatrix
          )
        return list(intMatrix)

    def __str__(self):
        """
        Print matrix
        """
        printed = ""
        for i in range(9):
            for j in range(9):
                printed += str(self.matrix[i][j]) + " "
                if (j == 2 or j == 5):
                    printed += "|"
            printed += '\n'
            if (i == 2 or i == 5):
                printed += '--------------------\n'
        if (self.solved):
            printed += '\n' + self.coorNumber(self.number)
        return printed

    def coorNumber(self, numb):
        """
        Coordinate of number
        """
        printed = "Coordinate of number {0}:\n".format(numb)
        for i in range(9):
            for j in range(9):
                if (self.matrix[i][j] == numb):
                    printed += "({0},{1})\n".format(i + 1, j + 1)
        return printed

    def validate(self, horizontal, vertical, idx):
        """
        Validate number on horizontal and vertical line

        True if no idx on horizontal and vertical line
        Otherwise False
        """
        for i in range(9):
            hor = 3 * int(horizontal / 3) + int(i / 3)
            ver = 3 * int(vertical / 3) + i % 3
            if (idx == self.matrix[horizontal][i]
                or idx == self.matrix[i][vertical]
                    or idx == self.matrix[hor][ver]):
                return False

        return True

    def solve(self):
        """
        Solve the matrix

        True if solvable
        Otherwise False
        """
        for i in range(9):
            for j in range(9):
                if (self.matrix[i][j] == 0):
                    for k in range(1, 10):
                        if (self.validate(i, j, k)):
                            self.matrix[i][j] = k
                            if (self.solve()):
                                return True
                            self.matrix[i][j] = 0
                    return False
        self.solved = True
        return True
