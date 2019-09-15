from trapezoidal import f, accuracy

def integrate(f, a, b, N=10):
    h = (b - a) / N
    return 1/3 * h * (f(a) + f(b) + 4 * sum([f(a + (2*k - 1) * h) for k in range(1, int(N/2) + 1)]) + 2 * sum([f(a + 2 * k * h) for k in range(1, int(N/2))]))

if __name__ == "__main__":
    q = integrate(f, 0, 2, 10)
    print("The integral is", q, "with", accuracy(q, 4.4) * 100, "percent error")