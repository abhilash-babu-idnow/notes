What are hyperparameters? 
They are fine tuning knobs that can be tweaked to help a network successfully train. 

Required Hyperparameters: 
* Total number of input nodes.
* Total number of hidden layers.
* Total number of hidden nodes in each hidden layer. 
* Total number of output nodes. 
* Weight values. 
* Bias values. 
* Learning rate. 

Optional Hyperparameters
* Learning rate schedule ( learning rate decay )
* Momentum
* Mini batch size. 
* Weight decay
* Dropout. 

> Input Node
> Input to the network
> Numerical
> Each node => A feature 
> Each node => One dimension


> Hidden Layer
> Layer b/w Input and Output layer
> Can be single or multiple. 
> How  many? (out of scope) refer [[Practical_way_to_train_rbm]]

> Hidden Node
> Node in a hidden layer
> General rules of thumb and trial error to choose the number of hidden nodes.
> More info refer [[Practical_recom_gradient_based_training|Practical Recommendations for Gradient based training of deep architectures]]

> Output Node
> Node in output layer. 
> Single or multiple depending upon the objective of the network. 

> Weight Value
....
....
....

--- 
---

### Calculating the total error.
Total error is the difference between the networks actual output and target output. 
#### Forward
#### Mathematical Functions
> What is a cost function?
> Measure of how wrong a network is. 

> Types of cost functions?
> MSE, SE, RMS, SSE, Cross Entropy, Exponential, KL Divergence etc.

### Updating the weights. 

#### What is gradient descent?

> Optimization method; Find combination of weights that will minimize the error in the output of the network; Metaphor -> "It is how we turn the dials to fine tune the network"
> Learning rate -> Speeds up or slows down how quickly an algorithm learns. ~ 0.0001 to 1. ; Determines the size of the step an algorithm takes when moving towards the global minimum. 
> Analogy -> Gradient descent is like a person hiking down a mountain.

Reference: 
>    ![[An overview of gradient descent optimization algorithms.pdf]]

##### Gradient Descent Methods

###### Batch Gradient Descent (Full Batch)
* Summing the gradients for *every* training set element and then updating the weights. 
* eg. if there are 10000 images, then update of the weights will not occur until after the gradients of all 10000 images have been calculated and combined. 

###### Stochastic Gradient Descent (SGD / Online)
* Weights in the network are modified after every training set element. 
* Shuffle the inputs to avoid the network getting biased either after the every epoch or once before the training. 
* Can bounce around the global minimum 

###### Mini Batch Gradient Descent
* Summing the gradients for multiple training set inputs and then updating the weights. 
* Size of the mini batch is a hyperparameter. 
* Most popular

##### Updating Weight
###### General Weight Update Equation 
![[general_weight_update.png]]

###### Batch Training Weight Update Equation

For batch training, the weights are updated after passing an entire training set through the network (one epoch). 

> Purpose of a weight update is to minimize the error of a weight and help move the network towards minimizing the total error. 

![[batch_training_weight_update_1.png]]

![[batch_training_weight_update_2.png]]

![[batch_training_weight_update_3.png]]

###### SGD Training Weight update equation

![[sgd_weight_update.png]]

> Weights are updated after each single training example is passed through the network. 

> Multiplying the error of a weight by the learning rate and subtracting that from the current weight. 

###### Mini Batch Training Weight update equation

![[mini_batch_training_weight_update.png]]

> Weights are updated after a certain number of training elements have passed through the network. In the above equation mini batch size is 10. This is a hyperparameter. So if there are 1000 samples and the mini batch size is 10 then there will be 100 weight updates. 

