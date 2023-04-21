# Tensorflow y Keras

Keras y TensorFlow son dos de las bibliotecas más utilizadas en el campo del aprendizaje profundo. Keras es una API de redes neuronales de alto nivel, escrita en Python y capaz de funcionar sobre TensorFlow, CNTK o Theano. TensorFlow es una biblioteca de software de código abierto para el flujo de datos y la programación diferenciable en una amplia gama de tareas. Es una biblioteca de matemáticas simbólicas y también se utiliza para aplicaciones de aprendizaje automático como redes neuronales. TensorFlow fue desarrollado por el equipo de Google Brain y lanzado como una biblioteca de software de código abierto en noviembre de 2015.

Keras proporciona una API fácil de usar que facilita la creación de modelos de aprendizaje profundo, mientras que TensorFlow proporciona una plataforma flexible y escalable para implementar y entrenar estos modelos. Al utilizar Keras y TensorFlow juntos, podemos aprovechar las fortalezas de ambas bibliotecas y construir modelos de aprendizaje profundo potentes.

En este curso, cubriremos los conceptos básicos tanto de Keras como de TensorFlow, y luego pasaremos a temas más avanzados, como la construcción de redes neuronales convolucionales y redes neuronales recurrentes. También cubriremos los últimos avances en el campo, como el aprendizaje de transferencia y el uso de modelos pre-entrenados.

A lo largo del curso, proporcionaremos numerosos ejemplos en Python para demostrar los conceptos cubiertos. Al final del curso, deberías tener un sólido entendimiento tanto de Keras como de TensorFlow, y ser capaz de construir tus propios modelos de aprendizaje profundo para una variedad de aplicaciones.

## Resumen de Keras y TensorFlow

Keras y TensorFlow son dos de las bibliotecas más utilizadas en el campo del aprendizaje profundo. Keras es una API de redes neuronales de alto nivel, escrita en Python y capaz de funcionar en TensorFlow, CNTK o Theano. TensorFlow es una biblioteca de software de código abierto para la programación diferenciable y de flujo de datos en una amplia gama de tareas. Es una biblioteca de matemáticas simbólicas y también se utiliza para aplicaciones de aprendizaje automático como las redes neuronales. TensorFlow fue desarrollado por el equipo de Google Brain y lanzado como una biblioteca de software de código abierto en noviembre de 2015.

Keras proporciona una API fácil de usar que hace que sea fácil construir modelos de aprendizaje profundo, mientras que TensorFlow proporciona una plataforma flexible y escalable para implementar y entrenar estos modelos. Al usar Keras y TensorFlow juntos, podemos aprovechar las fortalezas de ambas bibliotecas y construir modelos de aprendizaje profundo potentes.

En este curso, cubriremos los conceptos básicos tanto de Keras como de TensorFlow, y luego avanzaremos a temas más avanzados como la construcción de redes neuronales convolucionales y redes neuronales recurrentes. También cubriremos los últimos avances en el campo, como el aprendizaje por transferencia y el uso de modelos pre-entrenados.

## Ventajas del uso de Tensorflow y keras

1. API fácil de usar: Keras proporciona una API de alto nivel y fácil de usar para construir modelos de aprendizaje profundo, lo que puede ahorrar mucho tiempo y esfuerzo a los desarrolladores.

2. Flexibilidad y escalabilidad: TensorFlow es una plataforma flexible y escalable que permite a los usuarios construir y entrenar modelos de aprendizaje profundo en una variedad de dispositivos, desde computadoras de escritorio hasta teléfonos móviles e incluso en la nube.

3. Código abierto: Tanto Keras como TensorFlow son bibliotecas de código abierto, lo que significa que los desarrolladores pueden acceder al código fuente y contribuir al desarrollo de las bibliotecas.

4. Soporte de la comunidad: Existe una gran comunidad de desarrolladores que utilizan Keras y TensorFlow, lo que significa que hay muchos recursos disponibles, incluyendo tutoriales, documentación y foros, para ayudar a los desarrolladores a resolver problemas y aprender nuevas técnicas.

5. Integración con otras herramientas: Keras y TensorFlow se pueden integrar con otras herramientas populares como scikit-learn y Apache Spark, lo que facilita la construcción de tuberías complejas de aprendizaje automático.

## Requerimientos para utilizar keras y tensorflow

1. Python: Tanto Keras como TensorFlow están escritos en Python, por lo que deberá tener Python instalado en su computadora.

2. Librerías: También necesitará tener instaladas algunas bibliotecas de Python, incluyendo NumPy, SciPy y Matplotlib.

3. GPU: Si bien es posible ejecutar Keras y TensorFlow en una CPU, usar una GPU puede acelerar significativamente el entrenamiento de modelos de aprendizaje profundo. Si planea entrenar modelos grandes, se recomienda una GPU con soporte de CUDA.

4. IDE: Necesitará un entorno de desarrollo integrado (IDE) para escribir y ejecutar su código. Las opciones populares incluyen Jupyter Notebook, PyCharm y Spyder.

5. Conocimientos: Por último, es importante tener una buena comprensión de los conceptos y técnicas de aprendizaje profundo antes de sumergirse en Keras y TensorFlow. También es útil tener un sólido conocimiento en matemáticas y estadísticas.

# Keras

Keras es una biblioteca de redes neuronales de alto nivel escrita en Python que permite construir y entrenar modelos de aprendizaje profundo de manera rápida y fácil. Algunos de los conceptos clave en Keras son:

## Introducción a Keras

Keras proporciona una API fácil de usar que permite a los desarrolladores crear rápidamente modelos de aprendizaje profundo. Es compatible con TensorFlow, CNTK y Theano, y puede ejecutarse en CPU y GPU.

## Modelos secuenciales y funcionales

En Keras, puede construir modelos secuenciales y funcionales. Los modelos secuenciales se utilizan para construir modelos de capas apiladas donde la salida de una capa es la entrada de la siguiente. Los modelos funcionales son más flexibles y se pueden utilizar para construir modelos con capas compartidas, múltiples entradas y salidas, y bucles.

## Capas en Keras

Keras proporciona una amplia variedad de capas para construir modelos, desde capas de entrada y salida básicas hasta capas convolucionales y recurrentes.

## Compilando un modelo Keras

Antes de entrenar un modelo Keras, es necesario compilarlo. Durante la compilación, se especifica la función de pérdida, el optimizador y las métricas que se utilizarán para evaluar el modelo.

## Entrenando un modelo Keras

Después de compilar un modelo Keras, puede entrenarlo con un conjunto de datos de entrenamiento. Durante el entrenamiento, el modelo ajusta sus pesos para minimizar la función de pérdida.

## Evaluando un modelo Keras

Una vez que se entrena un modelo Keras, se puede evaluar su rendimiento utilizando un conjunto de datos de prueba. Keras proporciona una variedad de métricas para evaluar la precisión de un modelo, como la precisión y la pérdida.

## Guardando y cargando un modelo Keras

Después de entrenar un modelo Keras, es posible guardarlo en disco para su uso posterior. Keras proporciona una API fácil de usar para guardar y cargar modelos.

## Afinamiento de un modelo pre-entrenado

El afinamiento de modelos pre-entrenados es una técnica común en el aprendizaje profundo que implica el ajuste de un modelo pre-entrenado en un conjunto de datos diferente. Esto se hace típicamente mediante el congelamiento de algunas de las capas del modelo pre-entrenado y el entrenamiento de las capas restantes en el nuevo conjunto de datos.

## Transferencia de aprendizaje con Keras

La transferencia de aprendizaje es una técnica en el aprendizaje profundo que implica la reutilización de un modelo pre-entrenado para una tarea similar a la tarea original para la que fue entrenado. Keras hace que la transferencia de aprendizaje sea fácil con su API de modelos pre-entrenados y la capacidad de congelar capas y entrenar otras.

## Ejemplos en python utilizando keras

## MNIST classification

La Clasificación de MNIST es un ejemplo popular de aprendizaje supervisado. El conjunto de datos MNIST consiste en 70,000 imágenes en escala de grises de 28x28 píxeles de dígitos escritos a mano, con 60,000 imágenes para entrenamiento y 10,000 para pruebas. En este ejemplo, usaremos Keras y TensorFlow para construir un modelo de clasificación de dígitos utilizando la base de datos MNIST.

Primero, importaremos las bibliotecas necesarias y cargaremos los datos de MNIST.

```python
import tensorflow as tf
from tensorflow import keras

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
```

A continuación, normalizamos los datos y los convertimos a formato de tipo flotante.

```python
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0
```

Luego, construimos el modelo utilizando una red neuronal con dos capas ocultas de 128 y 64 unidades, respectivamente, y una capa de salida softmax.

```python
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])
```

Compilamos el modelo, especificando la función de pérdida, el optimizador y las métricas de evaluación.

```python
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
```

Entrenamos el modelo en los datos de entrenamiento y especificamos el número de épocas y el tamaño del lote.

```python
model.fit(x_train, y_train, epochs=5, batch_size=32, verbose=1)
```

Por último, evaluamos el modelo en los datos de prueba.

```python
test_loss, test_acc = model.evaluate(x_test, y_test)
print('Test accuracy:', test_acc)
```

Este modelo simple de red neuronal puede lograr una precisión de alrededor del 98% en la clasificación de dígitos escritos a mano en la base de datos MNIST.

## CIFAR-10 classification

A continuación se muestra un ejemplo de clasificación de imágenes usando el conjunto de datos CIFAR-10 en Keras:

```python
import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.utils import to_categorical

# Cargamos los datos CIFAR-10
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# Preprocesamiento de datos
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

# One-hot encoding para las etiquetas
num_classes = 10
y_train = to_categorical(y_train, num_classes)
y_test = to_categorical(y_test, num_classes)

# Definición del modelo
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=x_train.shape[1:]))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))

# Compilación del modelo
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenamiento del modelo
batch_size = 128
epochs = 20
model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_data=(x_test, y_test))

# Evaluación del modelo
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
```

Este código carga el conjunto de datos CIFAR-10, preprocesa los datos y define un modelo de red neuronal convolucional (CNN) en Keras. El modelo se compila con la función de pérdida "categorical_crossentropy" y el optimizador "adam". Luego, se entrena el modelo durante 20 épocas y se evalúa en el conjunto de prueba.

En este ejemplo, el modelo alcanza una precisión de prueba de alrededor del 77%. Sin embargo, la precisión puede mejorarse mediante técnicas de ajuste de hiperparámetros o utilizando arquitecturas de red neuronal más avanzadas.

## Fashion-MNIST classification

En este ejemplo, aprenderás a clasificar imágenes de prendas de vestir utilizando la base de datos Fashion-MNIST. Usaremos Keras y TensorFlow para construir una red neuronal convolucional que pueda clasificar las imágenes con una alta precisión.

```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Cargar el conjunto de datos Fashion-MNIST
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# Escalar los datos entre 0 y 1
train_images = train_images / 255.0
test_images = test_images / 255.0

# Definir el modelo
model = keras.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dense(10)
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Entrenar el modelo
model.fit(train_images, train_labels, epochs=10)

# Evaluar el modelo en el conjunto de prueba
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print('\nTest accuracy:', test_acc)
```

Este código primero carga el conjunto de datos Fashion-MNIST y lo divide en conjuntos de entrenamiento y prueba. Luego, los datos se escalan para que estén entre 0 y 1. Se define un modelo de red neuronal secuencial simple con dos capas densas, la última de las cuales tiene 10 neuronas para clasificar las 10 categorías de prendas de vestir en el conjunto de datos. El modelo se compila con una función de pérdida y un optimizador, y se entrena en el conjunto de entrenamiento durante 10 épocas. Finalmente, el modelo se evalúa en el conjunto de prueba para ver qué tan bien se generaliza a datos nuevos.

## Sentiment analysis with IMDB dataset

En este ejemplo, aprenderás a realizar un análisis de sentimientos utilizando la base de datos IMDB. Utilizaremos Keras y TensorFlow para construir una red neuronal que pueda clasificar las críticas de películas como positivas o negativas.

```python
from keras.datasets import imdb
from keras.models import Sequential
from keras.layers import Dense, Embedding, GlobalAveragePooling1D
from keras.utils import pad_sequences

# Load the IMDB dataset
max_features = 20000
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)

# Preprocess the data
maxlen = 80
x_train = pad_sequences(x_train, maxlen=maxlen)
x_test = pad_sequences(x_test, maxlen=maxlen)

# Define the model architecture
model = Sequential()
model.add(Embedding(max_features, 128))
model.add(GlobalAveragePooling1D())
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
batch_size = 32
epochs = 10
model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_data=(x_test, y_test))

# Evaluate the model
loss, accuracy = model.evaluate(x_test, y_test, batch_size=batch_size)
print('Test loss:', loss)
print('Test accuracy:', accuracy)
```
Este código carga primero el conjunto de datos IMDB utilizando la función imdb.load_data() de Keras. Luego, procesa los datos rellenando las secuencias hasta una longitud fija usando la función sequence.pad_sequences().

La arquitectura del modelo consta de una capa de embedding, una capa de pooling global y una capa de salida densa con una función de activación sigmoidal. La capa Embedding() aprende una representación vectorial densa para cada palabra en la secuencia de entrada. La capa GlobalAveragePooling1D() promedia sobre la dimensión de secuencia para producir una salida de longitud fija. La capa Dense() de salida utiliza una función de activación sigmoidal para producir una salida de clasificación binaria.

El modelo se compila con la función de pérdida de entropía cruzada binaria y el optimizador Adam. Luego se entrena durante 10 épocas en los datos de entrenamiento, con un tamaño de lote de 32. Los datos de validación se utilizan para evaluar el modelo después de cada época.

Finalmente, se evalúa el modelo en los datos de prueba utilizando la función evaluate(), que devuelve la pérdida y la precisión de la prueba.

## Ejemplos de tensorflow

## Autoencoder:
Un autoencoder es un tipo de red neuronal que se utiliza para comprimir datos de entrada en una representación más pequeña y luego descomprimirlos para producir datos de salida similares a los de entrada. El objetivo es minimizar la pérdida entre los datos de entrada y de salida, lo que permite a la red aprender patrones en los datos de entrada. Los autoencoders se utilizan a menudo para la reducción de la dimensionalidad, la eliminación de ruido y la generación de datos.

```python
import tensorflow as tf
from tensorflow.keras.datasets import mnist
import numpy as np

(x_train, _), (x_test, _) = mnist.load_data()

# Normalización de los datos
x_train = x_train.astype('float32') / 255.
x_test = x_test.astype('float32') / 255.

# Aplanamiento de los datos
x_train = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))
x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))
encoding_dim = 32

input_img = tf.keras.Input(shape=(784,))
encoded = tf.keras.layers.Dense(encoding_dim, activation='relu')(input_img)
decoded = tf.keras.layers.Dense(784, activation='sigmoid')(encoded)

autoencoder = tf.keras.Model(input_img, decoded)
autoencoder.compile(optimizer='adam', loss='binary_crossentropy')
autoencoder.fit(x_train, x_train,
                epochs=10,
                batch_size=256,
                shuffle=True,
                validation_data=(x_test, x_test))
decoded_imgs = autoencoder.predict(x_test)

# Visualización de las imágenes originales y las reconstruidas
import matplotlib.pyplot as plt

n = 10
plt.figure(figsize=(20, 4))
for i in range(n):
    # Original
    ax = plt.subplot(2, n, i+1)
    plt.imshow(x_test[i].reshape(28,28))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # Reconstruido
    ax = plt.subplot(2, n, i+n+1)
    plt.imshow(decoded_imgs[i].reshape(28, 28))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

plt.show()
```

Este código entrenará un autoencoder en el conjunto de datos MNIST y luego utilizará el modelo entrenado para generar imágenes de entrada reconstruidas.

