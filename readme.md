# Chapter 1 Summary
## Perceptrons
A simple weighted variable sum equation that is compared with a threshold to give a binary output (0 or 1).

output = ( 0 if weighted sum < threshold, 1 if weighted_sum >= threshold)

by decreasing the threshold, we are becoming more likely to take the decision.

## Logic gates
NN made with perceptrons can be used to mimick NAND gates, which can mimick any logic gate, so in its essence this means we can perform
computations with them but have the limitation of classical computation i.e it cannot learn.
solution: Sigmoid neurons
## Sigmoid Neurons
They accept decimal values and not just 0 and 1, which means we are not just taking a decision but measuring how likely are we to take this decision.
The usage of decimals allows small changes in weights to lead to small changes in the output instead of the output jumping from 0 to 1
this allows us the algorithm to learn and make better decisoins

## The architecture of neural networks
First layer is the input layer where we pass our parameters.
Last layer is the output layer which is the predicted output.
all the layers in between are called hidden layers which just means they are not input or output layers they are just computational layers
the output of each neuron in the hidden layer is denoted as sigmoid( sum(W*X+b) )
more hidden layer means more complex decision making abilities

## Learning with gradient descent
Gradient descent is an alogrithm that tries finding the lowest point on a multi variable graph by mimicking how a ball falls from a cliff to the lowest point.

## Cost function
Decreasing the value of this function means we are closer to the predicted output, we try minimizing this function using gradient descent.
A good cost function is the mean squared error.
