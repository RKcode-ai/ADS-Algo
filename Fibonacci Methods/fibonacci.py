# This is a sample Python script.
import math
import time
import matplotlib.pyplot as plt
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

n_value = [0, 1, 2, 3, 4, 5, 6, 8, 10, 13, 16, 20, 25, 32, 40, 50,
           63, 80, 100, 125, 160, 200, 250, 315, 400, 500
           , 610, 730, 850, 1000]
Time_limit = 3.0

def naive_recursion(n):
    if n < 2:
        return n
    else:
        return naive_recursion(n - 1) + naive_recursion(n - 2)


def bottom_up(n):
    if n <= 1:
        return n
    prev1 = 1
    prev2 = 0
    sum = 0
    for i in range(2, n+1):
        sum = prev1 + prev2
        prev2 = prev1
        prev1 = sum
    return sum


def closed_form(n):
    if n <= 1:
        return n
    else:
        golden_ratio = ((1 + math.sqrt(5)) / 2)
        term = 3
        term_value = 2
        while term < n:
            term_value = round(term_value * golden_ratio)
            term += 1
        return term_value

def matrix_multiplication(n):
    if n == 0:
        return 0
    result00, result01 = 1, 0
    result10, result11 = 0, 1
    b00, b01 = 1, 1
    b10, b11 = 1, 0

    while n > 0:
        if n % 2 == 1:
            next_result00 = (result00 * b00) + (result01 * b10)
            next_result01 = (result00 * b01) + (result01 * b11)
            next_result10 = (result10 * b00) + (result11 * b10)
            next_result11 = (result10 * b01) + (result11 * b11)
            result00, result01, result10, result11 = next_result00, next_result01, next_result10, next_result11

        next_b00 = (b00 * b00) + (b01 * b10)
        next_b01 = (b00 * b01) + (b01 * b11)
        next_b10 = (b10 * b00) + (b11 * b10)
        next_b11 = (b10 * b01) + (b11 * b11)
        b00, b01, b10, b11 = next_b00, next_b01, next_b10, next_b11
        n = n // 2
    return result01

functions = {
    'naive_recursion': naive_recursion,
    'bottom_up': bottom_up,
    'closed_form': closed_form,
    'matrix_multiplication': matrix_multiplication
}
active_functions = {
    'naive_recursion': True,
    'bottom_up': True,
    'closed_form': True,
    'matrix_multiplication': True
}
def testing():
    graph_data = {
        'naive_recursion': [],
        'bottom_up': [],
        'closed_form': [],
        'matrix_multiplication': []
    }
    for n in n_value:
        times = {
            'naive_recursion': "n/a",
            'bottom_up': "n/a",
            'closed_form': "n/a",
            'matrix_multiplication': "n/a"
        }
        for name, function in functions.items():
            if active_functions[name]:
                start_time = time.perf_counter()
                function(n)
                end_time = time.perf_counter()
                time_taken = end_time - start_time

                if time_taken > Time_limit:
                    active_functions[name] = False
                    times[name] = f"{time_taken:.6f}"
                    graph_data[name].append(time_taken)
                else:
                    times[name] = f"{time_taken:.6f}"
                    graph_data[name].append(time_taken)
            else:
                graph_data[name].append(None)
        print(f"{n:<5} | {times['naive_recursion']:<12} | {times['bottom_up']:<12} | {times['closed_form']:<12} | {times['matrix_multiplication']:<12}")
    return graph_data

def plotting(n_val, graph_data):
    plt.figure(figsize=(10, 8))
    plt.plot(n_val, graph_data['naive_recursion'], label="naive_recursion", color='red')
    plt.plot(n_val, graph_data['bottom_up'], label="bottom_up", color='blue')
    plt.plot(n_val, graph_data['closed_form'], label="closed_form", color='green')
    plt.plot(n_val, graph_data['matrix_multiplication'], label="matrix_multiplication", color='orange')
    plt.yscale('log')
    plt.xscale('log')
    plt.xlabel("n (fibonacci)")
    plt.ylabel("time (s)")
    plt.title("Different Fibonacci methods")
    plt.grid(True)
    plt.legend()
    plt.savefig("graph.png")
    plt.show()


def main():
    n = int(input("Enter a number for recursion: \n"))
    print(f"Naive recursion: {naive_recursion(n)}")
    print(f"Bottom up: {bottom_up(n)}")
    print(f"Closed form: {closed_form(n)}")
    print(f"Matrix multiplication: {matrix_multiplication(n)}")
    print("\n\n")
    print(f"{'n':<5} | {'Naive':<12} | {'Bottom-Up':<12} | {'Closed-Form':<12} | {'Matrix':<12}")
    graph_data = testing()
    plotting(n_value, graph_data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
