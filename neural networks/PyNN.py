import numpy as np
inputs = [1, 2,3,2.5]

weights = [	[0.2,0.8,-0.5,1.0],
			[0.5,-0.91,0.26,0.5],
			[-0.26,-0.27,0.17,0.87]]

bias1 = [2, 3, 0.5]

# layer_outputs = []

# for w , b in zip(weights,bias1):
# 	neuron_op = 0
# 	for i , w1 in zip(inputs,w): 
# 		neuron_op += i * w1
# 	neuron_op += b
# 	layer_outputs.append(neuron_op)

print(np.dot(weights, inputs) + bias1)
