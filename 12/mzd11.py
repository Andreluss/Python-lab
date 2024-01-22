import numpy as np

x = np.array([[1.0, 2.2, 2.0, 1.5, 3.2],  # A
              [1.3, 1.1, 2.4, 3.2, 1.2]])  # B
y = np.array([0, 1, 1, 0, 1])  # Y


def logistic(w0, w1, xA, xB):
    return 1 / (1 + np.exp(-(w0 * xA + w1 * xB)))


def logistic_general(w, x):
    return 1 / (1 + np.exp(-np.dot(w, x)))


def mse(y, y_pred):
    return np.mean((y - y_pred) ** 2)


w0 = np.linspace(0, 1, 11)
w1 = np.linspace(2, 3, 11)

mse_array = np.zeros((len(w0), len(w1)))
# calculate predictions for each pair of w0 and w1
for i in range(len(w0)):
    for j in range(len(w1)):
        weights = np.array([w0[i], w1[j]])
        pred = logistic_general(weights, x)
        mse_array[i, j] = mse(y, pred)

print(mse_array)
