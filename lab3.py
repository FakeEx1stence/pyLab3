import numpy as np
import random

def DigitCount(K):
    if 0 < K < 10000:
        if K >= 1000:
            return 4
        elif K >= 100:
            return 3
        elif K >= 10:
            return 2
        else:
            return 1
    else:
        return ("Out of range")

def task1():
    # Proc 27(28 не було)
    try:
        arr = [int(input(f"({i + 1}) element :")) for i in range(5)]
        result = list(map(DigitCount, arr))
        print(result)

    except ValueError:
        print("Invalid input")

def solution(filename):
    with open(filename) as f:
        temp = f.readline().split(" ")
        M = int(temp[0])
        N = int(temp[1])

    input = np.loadtxt(filename, skiprows=1, max_rows=M)
    print(input)

    a = np.zeros((M, N))

    for i in range (M):
        for j in range (N):
            a[i][j] = random.randint(0, 20)

    multiply = a * input

    min_values = []
    summary = 0
    summaries = []
    for i in range(0, M, 2):
        min_value = min(input[i])
        min_values.append(min_value.item())
        for j in range(N):
            summary += input[i][j]

        summary /= N
        summaries.append(summary.item())
        summary = 0

    return multiply, min_values, summaries


def task2():
    filename = ("input.txt")
    scalar, min_values, summaries = solution(filename)
    print("Умноженная матрица:", scalar)
    print("Минимальное число: ", min_values)
    print("Среднее арифметическое", summaries)
