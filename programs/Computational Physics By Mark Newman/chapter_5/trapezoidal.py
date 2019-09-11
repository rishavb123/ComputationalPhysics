def f(x):
    return x**4 -  2*x + 1

def integrate(f, a, b, N=10):
    h = (b - a) / N
    return h * (0.5 * f(a) + 0.5 * f(b) + sum([f(a + k*h) for k in range(1, N)]))

def accuracy(my_ans, correct_ans):
    return (my_ans - correct_ans) / correct_ans

if __name__ == "__main__":
    q = integrate(f, 0, 2, 10)
    print("The integral is", q, "with", accuracy(q, 4.4) * 100, "percent accuracy")