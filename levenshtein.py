import numpy as np

def levenshtein(str1: str, str2: str) -> int:
    str1_len = len(str1)
    str2_len = len(str2)

    matrix = np.zeros((str1_len + 1, str2_len + 1), dtype=int)

    for i in range(0, str1_len + 1):
        matrix[i, 0] = i

    for j in range(0, str2_len + 1):
        matrix[0, j] = j

    for i in range(0, len(str1)):
        for j in range(0, len(str2)):
            if str1[i] == str2[j]:
                substitution = 0
            else:
                substitution = 1

            matrix[i + 1, j + 1] = min(
                matrix[i, j + 1] + 1,
                matrix[i + 1, j] + 1,
                matrix[i, j] + substitution
            )

    return matrix[len(str1), len(str2)]

str1 = "james"
str2 = "jame"

print(levenshtein(str1, str2))
