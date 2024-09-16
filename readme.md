#Chapter 1 Summary
##Perceptrons
A simple weighted variable sum equation that is compared with a threshold to give a binary output (0 or 1).

output = ( 0 if weighted sum < threshold, 1 if weighted_sum >= threshold)

by decreasing the threshold, we are becoming more likely to take the decision.

#Logic gates
NN made with perceptrons can be used to mimick NAND gates, which can mimick any logic gate, so in its essence this means we can perform
computations with them but have the limitation of classical computation i.e it cannot learn.
solution: Sigmoid neurons
##Sigmoid Neurons
They accept decimal values and not just 0 and 1, which means we are not just taking a decision but measuring how likely are we to take this decision.
The usage of decimals allows small changes in weights to lead to small changes in the output instead of the output jumping from 0 to 1
this allows us the algorithm to learn and make better decisoins
