# O(n^2) time | O(n^2) space
def nthRowOfPascalTriangle(self, n):
    if n == 0:
        return 0
    else:
        triangle = [[0 for i in range(n)] for row in range(n)]
        for i in range(len(triangle)):
            for j in range(n):
                if j == i or j == 0:
                    triangle[i][j] = 1
                else:
                    triangle[i][j] = triangle[i-1][j] + triangle[i-1][j-1]
        return triangle[-1]


# O(n^2) time | O(1) space


def nthRowOfPascalTriangle(n):
    coefs = []
    for line in range(1, n + 1):
        c = 1
        for i in range(1, line + 1):
            if line == n:
                coefs.append(c)
            c = int(c * (line - i) / i)
    return coefs
