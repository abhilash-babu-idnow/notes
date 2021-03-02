#dithering #errordiffusion 

This algorithm is also based on the concept of error diffusion, but uses a bigger diffusion matrix compared to [[Floyd_Steinberg]]. The diffusion matrix used in this alogirithm is shown below. 

| *   | *   | *   | *   | *   |
|:---:|:---:|:---:|:---:|:---:|
| *   | *   |P    |7/48 | 5/48|
|3/48 |5/48 |7/48 |5/48 | 3/48|
|1/48 |3/48 |5/48 |3/48 | 1/48|