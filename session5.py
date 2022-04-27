import numpy as np 
import matplotlib.pyplot as plt

def main():
	x = np.arange(0, 2, 2/1000)
	y = np.sin(x)
	plt.plot(x, y)
	plt.show()

if __name__ == "__main__":
	main()