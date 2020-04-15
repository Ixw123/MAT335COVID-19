import numpy as numpy
import matplotlib.pyplot as plt

def main():

    usPop = 300000000

    y0 = [0.0] * 3

    h = .01
    gamma = .1
    beta = .2

    # data for 2/29/20
    dead = 1
    recovered = 7
    infected = 68

    y0[1] = infected
    y0[2] = dead + recovered
    y0[0] = usPop - y[1] - y[2]
    
    y = eulerExplict(y0, h, beta=beta, gamma=gamma)

    plt.plot(t, y[0])
    plt.plot(t, y[1])
    plt.plot(t, y[2])
    plt.show()

def eulerExplict(h, y0, beta=.1, gamma=.1, tol=1e-10):
    outputs = [y0]

    while outputs[-1][0] > tol:

        outputs.append(y[-1] + h*f(y[-1], beta=beta, gamma=gamma))

    t = np.arange(0, len(outputs), 1)
    print("number of time steps", t)

    return outputs

def f(y, beta=.1, gamma=.1):
    beta = .1
    gamma = .2

    n = sum(y)

    return np.array([(-beta*y[0]*y[1])/n, (beta*y[0]*y[1])/n - (gamma*y[1]), gamma*y[1]])

if __name__ == "__main__":
    main()

