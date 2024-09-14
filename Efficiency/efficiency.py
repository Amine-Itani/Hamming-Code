# hamming code for error code connection and detection
from matplotlib import pyplot as plt

def parity_bit_counter(n):
    k = 1
    while not 2**k >= k + n + 1:
        k += 1
    return k

x = [] # 1 to 1000
y = [] # n/n+k

for n in range(1,1000):
    x.append(n)
    y.append(n/(n+parity_bit_counter(n)))
    if n > 1000-100:
        print(n/(n+parity_bit_counter(n)))
plt.figure(figsize=(10, 4))
plt.title("Hamming Code Efficiency as Msg Length Increases")
plt.plot(x, y)
plt.show()
