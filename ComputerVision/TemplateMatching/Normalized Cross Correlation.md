#TemplateMatching #NCC


Equation of **normalized cross correlation coefficient** is as follows. *source* : [Template Matching using Fast NCC](https://isas.iar.kit.edu/pdf/SPIE01_BriechleHanebeck_CrossCorr.pdf)

$$
\gamma = \frac{\sum_{x,y} {(f(x,y) - \bar{f}_{u,v})(t(x-u, y-v) - \bar{t})}}{\sqrt{\sum_{x,y} {(f(x,y) - \bar{f}_{u,v})}^2 \sum_{x,y}(t(x-u, y-v) - \bar{t})^2}}
$$