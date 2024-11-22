import numpy as np
matrix1 = np.array([[1+2j, 2-1j], [3+4j, 4+5j]])
matrix2 = np.array([[5-3j, 1+1j], [2-2j, 0+4j]])
addition = np.add(matrix1, matrix2)
subtraction=np.subtract(matrix1,matrix2)
mul=np.matmul(matrix1,matrix2)
print("Addition of two complex matrices:")
print(addition)
print("Subtraction of two complex matrices:")
print(subtraction)
print("Multiplication of two complex matrices:")
print(mul)
