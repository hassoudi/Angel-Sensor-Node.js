import numpy as np
import matplotlib.pyplot as plt

plt.ion()
i = 0
maxY = 65536 # 2 ^ 16;

while True:
    with open('data.txt', 'r') as f:
    	value = f.readline()
    	if (len(value) > 0):
	    	
	    	xMin = 0 if i < 100 else i - 100
	    	plt.axis([xMin, 10+i, 0, maxY])
	    	plt.scatter(i, value);
	    	plt.pause(0.0001)
	    	i += 1

