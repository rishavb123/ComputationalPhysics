from trapezoidal import integrate, accuracy

f = open('./res/velocities.txt')
data = f.readlines()
f.close()

vs = []

for line in data:
    vs.append(float(line.split("\t")[1][:-1]))

def f(x):
    return vs[int(x)]

print("The distance travelled is", integrate(f, 0, 100, 100))