* How to do model regularization?
	* In the constructor of the layer there is an option to specify the regularizer. 

L2 Regularization

```python
model = Sequential([
		Dense(64, activation='relu',
		kernel_regularizer=tf.keras.regularizers.l2(0.001)),
		Dense(1, activation='sigmoid')
	])
```

L1 Regularization

```python
model = Sequential([
		Dense(64, activation='relu',
		kernel_regularizer=tf.keras.regularizers.l1(0.001)),
		Dense(1, activation='sigmoid')
	])
```

Combination of L1 and L2 Regularization

```python
model = Sequential([
		Dense(64, activation='relu',
		kernel_regularizer=tf.keras.regularizers.l1_l2(l1=0.001,l2=0.05)),
		Dense(1, activation='sigmoid')
	])
```

One case also specify the bias regularization. 

```python
model = Sequential([
		Dense(64, activation='relu',
		kernel_regularizer=tf.keras.regularizers.l2(0.001)),
		bias_regularizer=tf.keras.regularizers.l2(0.001),
		Dense(1, activation='sigmoid')
	])
```

Dropout

```python
model = Sequential([
		Dense(64, activation='relu'),
		Dropout(0.5),
		Dense(1, activation='sigmoid')
	])
```

* Call back functions help you monitor the progress made by the model during, training, testing and prediction. Call back functions are implemented by deriving the Callback class. There are some builtin callback functions available in keras. The history value returned by the model fit method is also a callback. 

```python
# Write a custom callback

from tensorflow.keras.callbacks import Callback

class TrainingCallback(Callback):
    def on_predict_begin(self, logs=None):
        print("Started prdedict")
                
    def on_predict_end(self, logs=None):
        print(f"Finished ")
        
```

* Batch normalization can be added like just another layer. 

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import BatchNormalization, Dropout

model = Sequential([
    Dense(64, input_shape=[train_data.shape[1],], activation="relu"),
    BatchNormalization(),  # <- Batch normalisation layer
    Dropout(0.5),
    BatchNormalization(),  # <- Batch normalisation layer
    Dropout(0.5),
    Dense(256, activation='relu'),
])

```

* Early stopping