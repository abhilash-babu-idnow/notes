Three types of #lensdistortion

* Radial Distortion
* Decentering Distortion
* Thin prism Distortion

#### Radial Distortion
-> Barrel Distortion
-> Pincussion Distortion
							 
Radial Distortion Modelling

* [[#Brown Model | Brown Model]] 
	* Works well with small distortions
* [[#Fitzgibbon Model | Fitzgibbon Model]]
	* Works with both small and large distortions
	* Better results with lower order polynomials

### Brown Model



### Fitzgibbon Model

$$
\begin {equation}
x_u = \frac{x_d}{1 + \lambda_1 r_d^2 + \lambda_2 r_d^4 + ...}
\end {equation}
$$

$$
\begin {equation}
y_u = \frac{y_d}{1 + \lambda_1 r_d^2 + \lambda_2 r_d^4 + ...}
\end {equation}
$$


References
* 2010 [[algebraic_lens_distortion_model]]
* 2017 [[correction_of_lens_distortion_division_model]]