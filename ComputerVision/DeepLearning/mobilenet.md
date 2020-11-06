# MOBILENET architecture

### Tags: #DeepLearning #Model #ComputerVision #DepthwiseSeperableConvolution

Link to the [original paper](https://arxiv.org/pdf/1704.04861.pdf)

#### Main Ideas from the paper:

Use of depth wise seperable convolution to create light weight deep neural networks. 
Two new hyperparamters - width multiplier and resolution multiplier. 

The main ideas is to use depthwise seperable convolution which split the standard convolution into two parts. 
a. Depthwise convolution
b. Pointwise convolution

![[depthwise_seperable_convolution.png]]

#### Depthwise seperable convolution
Computational cost of a standard convolution is 

$D_K$ . $D_K$ . $M$ . $N$ . $D_F$ . $D_F$

where 
* $D_K$ is the dimension of the kernel 
* $M$ is the number of input channels
* $N$ is the number of filters
* $D_F$ is the input dimension
* Here we are assuming square shape. 

Computational cost of depthwise seperable convolution is 

Cost of Deptwise convolution + Cost of pointwise convolution

$D_K$ . $D_K$ . $M$ . $D_F$ . $D_F$ + $M$ . $N$ . $D_F$ . $D_F$

So the reduction in computational cost is 
 
 $$ \frac{D_K.D_K.M.D_F.D_F + M.N.D_F.D_F}{D_K.D_K.M.N.D_F.D_F} $$
 
 $$ \frac{1}{N} + \frac{1}{{D_K}^2} $$
 
 #### Network Strucuture and Training
 
 * It has 28 layers
 
 ![[Pasted image 20201017053519.png]]
 
 ![[Pasted image 20201017053535.png]]
 
 * Trained using Tensorflow
 * [[RMSProp]] was used in the original paper #todo
 * [[Asynchronous Gradient Descent]] similar to [[Inception]] #todo
 * [[side labels]] and [[label smoothing]] was not used. #todo

##### Width multiplier
$$ \alpha \in (0,1] $$

Reduces the computational cost and number of parameters by roughly $\alpha^2$
For a given layer and width multiplier $\alpha$ the number of input channels become $\alpha.M$ and number of output channels become $\alpha.N$

##### Resolution multiplier
$$\rho \in (0,1] $$
* In practice, $\rho$ is set implicitly by setting the input resolution. Baseline value of $\rho$ is $1$. So the input resolution of network is 224, 192, 160 or 128.
* Reduces the computational cost by $\rho^2$

#### Further questions
* What is difference between mobilenet v1, v2, v3 etc? #todo
* 