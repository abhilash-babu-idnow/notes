# ROC Analysis

**What is ROC?**

It stands for *Receiver operating characteristics* and is a graph for visualizing, organizing and selecting classifiers based on their performance. It is especially useful in domains with skewed class distribution and have unequal classification error costs. 

![[confusion_matrix.jpg]]

*True Positive* - If instance is positive and the classifier classifies it as positive
*False Positive* - If instance is negative and the classifier classifies it as positive
*False Negative* - If the instance is positve and the classifier classifies it as negative
*True Negative* - If the instance is negative and the classifier classifies it as positive

> True Positive Rate (TPR) / Hit Rate / Recall of a classifier is defined as 
>  tpr = TP / P , where TP is True Positive and P is the number of positives.

> False Positive Rate (FPR) / False alarm rate is defined as 
> fpr = FP / N , where FP is False Positives and N is the number of negatives.

> ROC Graphs are 2D graphs with TPR plotted on Y axis and FPR plotted on the X axis. In other words it shows the tradeoff between the benefits (TP) and costs (FP).