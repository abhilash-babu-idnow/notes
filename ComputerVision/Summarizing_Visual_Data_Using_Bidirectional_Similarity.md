# Summarizing Visual Data Using Bidirectional Similarity.

[URL of the research paper](https://www.comp.nus.edu.sg/~cs6240/papers/bidirectional_similarity_CVPR2008.pdf)

Problem Statement:
- Re targeting or summarization of image/video data into smaller sizes. 
- Should contain as much visual information as possible.
- Should introduce only as few visual artefacts as possible.

**Dissimilarity Measure**

$$
d(S,T) = \frac{1}{N_S}\sum_{P{\subset}S}{\min_{Q{\subset}T}{D(P,Q)}} + \frac{1}{N_T}\sum_{Q{\subset}T}{\min_{P{\subset}S}{D(P,Q)}}
$$

- In the above equation *S* is the source signal *T* is the target signal 
- *D(,)* is some distance like SSD, sum of squared distances.
- *N<sub>S</sub>* and *N<sub>T</sub>* denote the number of patches in *S* and *T* respectively. 