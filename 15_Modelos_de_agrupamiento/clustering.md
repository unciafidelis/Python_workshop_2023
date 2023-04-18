# Modelos de machine learning de agrupamiento

## Introducción
En esta sección, exploraremos los conceptos de agrupamiento y clustering en el contexto del machine learning. Aprenderemos sobre los diferentes tipos de algoritmos de clustering y sus aplicaciones en una variedad de campos, desde la segmentación de clientes hasta el análisis de datos espaciales.

Los objetivos de aprendizaje de este módulo incluyen:

- Comprender las diferencias entre el agrupamiento y el clustering, y cuándo utilizar cada uno de estos enfoques.
- Familiarizarse con los diferentes tipos de algoritmos de clustering y sus fortalezas y debilidades.
- Saber cómo evaluar la calidad de los clusters y cómo preprocesar los datos antes del clustering.
- Aprender cómo implementar técnicas de clustering en Python utilizando bibliotecas populares como Scikit-learn y Scipy.
- Eer las aplicaciones del aprendizaje no supervisado, como la detección de anomalías y la reducción de dimensionalidad.

## Agrupamiento vs Clustering 

El agrupamiento y el clustering son dos términos que a menudo se utilizan indistintamente, pero que tienen diferencias sutiles. Ambos se refieren a la tarea de dividir un conjunto de datos en grupos o clusters, pero se utilizan en diferentes contextos.

El agrupamiento se refiere a la tarea de dividir un conjunto de datos en grupos predefinidos. Por ejemplo, podemos tener una base de datos de clientes y queremos dividirlos en diferentes categorías basadas en la edad, género o ingresos. En este caso, los grupos o categorías son predefinidos y conocidos de antemano.

Por otro lado, el clustering se refiere a la tarea de dividir un conjunto de datos en grupos que no se conocen de antemano. Es decir, no tenemos ninguna información previa sobre cómo deberían ser los grupos o categorías. El objetivo del clustering es encontrar patrones y estructuras ocultas en los datos y agruparlos en función de esas similitudes.

En resumen, el agrupamiento se utiliza cuando queremos dividir los datos en grupos predefinidos, mientras que el clustering se utiliza cuando queremos descubrir patrones y estructuras ocultas en los datos y dividirlos en grupos desconocidos.

### Definición y diferencias entre agrupamiento y clustering

El agrupamiento y el clustering son dos técnicas de análisis de datos que se utilizan para dividir un conjunto de datos en grupos o clusters. Aunque a menudo se utilizan indistintamente, tienen diferencias sutiles que vale la pena señalar.

El agrupamiento se refiere a la tarea de dividir un conjunto de datos en grupos predefinidos o categorías conocidas de antemano. En otras palabras, se parte de una estructura ya definida y se clasifican los datos según esta estructura. Por ejemplo, si tenemos una base de datos de clientes y queremos dividirlos en diferentes grupos según su edad, género o ubicación geográfica, estamos utilizando una técnica de agrupamiento.

Por otro lado, el clustering se refiere a la tarea de dividir un conjunto de datos en grupos o clusters desconocidos previamente, es decir, no se tiene información previa sobre cómo deberían ser los grupos o categorías. En este caso, el algoritmo de clustering buscará patrones y similitudes en los datos y creará los grupos en función de estas similitudes. Por ejemplo, si tenemos una base de datos de clientes y queremos descubrir grupos de clientes similares en función de sus patrones de compra, podríamos utilizar una técnica de clustering.

En resumen, la principal diferencia entre el agrupamiento y el clustering es que el agrupamiento se utiliza cuando se conocen de antemano las categorías o grupos en los que se deben clasificar los datos, mientras que el clustering se utiliza cuando se desea descubrir patrones y estructuras ocultas en los datos y agruparlos en función de estas similitudes.

### Aplicaciones de cada enfoque

Tanto el agrupamiento como el clustering tienen aplicaciones en una amplia variedad de campos. A continuación se describen algunas de las aplicaciones más comunes de cada enfoque:

Aplicaciones del agrupamiento:

- Segmentación de clientes en función de la edad, género, ingresos o comportamiento de compra
- Agrupación de productos o servicios similares para análisis de mercado o recomendaciones de productos
- Clasificación de noticias, artículos o documentos en diferentes categorías para la recuperación de información
- Agrupación de genes o proteínas similares en estudios de genómica o proteómica
- Agrupación de imágenes de satélite para la detección de patrones geográficos

Aplicaciones del clustering:

- Agrupación de clientes similares en función de sus patrones de compra o comportamiento en línea
- Análisis de sentimiento en redes sociales para identificar grupos de usuarios con actitudes similares
- Detección de anomalías o fraudes en transacciones financieras o de seguridad
- Agrupación de datos de sensores para la detección de patrones en la monitorización de procesos industriales
- Agrupación de imágenes para la segmentación de objetos en visión por computadora

En general, el agrupamiento se utiliza cuando se conocen de antemano las categorías o grupos en los que se deben clasificar los datos, mientras que el clustering se utiliza cuando se desea descubrir patrones y estructuras ocultas en los datos y agruparlos en función de estas similitudes.

## Tipos de Clustering 

Existen varios tipos de algoritmos de clustering utilizados en el análisis de datos. A continuación, se describen brevemente algunos de los tipos más comunes:

Clustering jerárquico: Es un método que agrupa los datos en función de su similitud y crea una estructura jerárquica de clusters, que se asemeja a un árbol invertido o dendrograma. Este método puede ser aglomerativo (bottom-up) o divisivo (top-down).

Clustering k-means: Es un método que divide los datos en k grupos o clusters, en los cuales cada punto de datos pertenece a un solo grupo. El número de clusters k debe ser especificado por el usuario. Este método es rápido y escalable, pero puede dar resultados subóptimos dependiendo de la inicialización aleatoria de los centroides.

DBSCAN: Es un método que encuentra clusters de alta densidad y detecta puntos de datos que no pertenecen a ningún cluster (outliers). Este método es eficiente y no requiere especificar el número de clusters, pero es sensible a los parámetros y puede ser menos adecuado para conjuntos de datos de baja densidad.

Gaussian Mixture Models (GMM): Es un método que modela cada cluster como una distribución gaussiana, lo que permite la estimación de la probabilidad de cada punto de datos de pertenecer a cada cluster. Este método es adecuado para conjuntos de datos con distribuciones de probabilidad desconocidas, pero puede ser computacionalmente costoso y puede dar lugar a clusters superpuestos.

Clustering espectral: Es un método que utiliza la matriz de similitud o de distancia entre los puntos de datos para agruparlos en clusters. Este método es adecuado para conjuntos de datos con estructuras no lineales y no es sensible a los valores atípicos, pero puede ser computacionalmente costoso y puede requerir la especificación del número de clusters.

En resumen, cada algoritmo de clustering tiene sus fortalezas y debilidades y es importante elegir el método adecuado para cada conjunto de datos y problema específico.

### Clustering jerárquico

El clustering jerárquico es un método que agrupa los datos en función de su similitud y crea una estructura jerárquica de clusters, que se asemeja a un árbol invertido o dendrograma. Este método puede ser aglomerativo (bottom-up) o divisivo (top-down).

En el clustering jerárquico aglomerativo, cada punto de datos se considera un cluster inicial y los clusters se fusionan iterativamente hasta que se alcanza un único cluster que contiene todos los datos. En cada paso, se fusionan los dos clusters más similares según una medida de distancia, como la distancia euclidiana o la correlación de Pearson. Esta medida de distancia se representa gráficamente en el dendrograma como la altura de la fusión.

En el clustering jerárquico divisivo, se comienza con un único cluster que contiene todos los datos y se divide iterativamente en sub-clusters más pequeños. En cada paso, se divide el cluster más disimilar en dos sub-clusters.

Un ejemplo de clustering jerárquico en Python se puede realizar utilizando el conjunto de datos Iris, que se encuentra disponible en la biblioteca de conjuntos de datos de scikit-learn.

En este ejemplo, utilizaremos la biblioteca de clustering de scikit-learn para realizar el clustering jerárquico aglomerativo. Primero, se importan las bibliotecas necesarias y se cargan los datos:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import AgglomerativeClustering

iris = load_iris()
X = iris.data
y = iris.target

#A continuación, se crea un objeto de clustering jerárquico aglomerativo y se ajusta a los datos:

clustering = AgglomerativeClustering(n_clusters=3)
clustering.fit(X)

#Finalmente, se visualiza el dendrograma y los clusters resultantes:

from scipy.cluster.hierarchy import dendrogram, linkage

Z = linkage(X, method='ward')
plt.figure(figsize=(10, 5))
dendrogram(Z)
plt.show()

plt.scatter(X[:, 0], X[:, 1], c=clustering.labels_, cmap='viridis')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.show()
```
En el dendrograma, se puede ver cómo los clusters se fusionan y se forman los grupos finales. En la gráfica de dispersión, se muestran los clusters coloreados según su etiqueta de cluster. En este caso, se han utilizado tres clusters, ya que el conjunto de datos Iris contiene tres clases de flores diferentes.

### Clustering K-means

El clustering K-means es un método que divide los datos en K clusters en los que cada punto de datos pertenece al cluster con el centroide más cercano. El centroide es el punto de datos medio del cluster, que se actualiza en cada iteración del algoritmo.

El proceso comienza asignando aleatoriamente K centroides en el espacio de datos. Luego, cada punto de datos se asigna al cluster con el centroide más cercano. Después de cada asignación de cluster, se actualizan los centroides para que estén en el centro de los puntos de datos asignados a cada cluster. El proceso de asignación y actualización se repite hasta que la asignación de cluster ya no cambia o se alcanza un número máximo de iteraciones.

El algoritmo de K-means tiene una complejidad de tiempo O(nkdi), donde n es el número de puntos de datos, k es el número de clusters, d es el número de características y i es el número de iteraciones.

Un ejemplo de clustering K-means en Python se puede realizar utilizando el conjunto de datos Wine, que se encuentra disponible en la biblioteca de conjuntos de datos de scikit-learn.

En este ejemplo, utilizaremos la biblioteca de clustering de scikit-learn para realizar el clustering K-means. Primero, se importan las bibliotecas necesarias y se cargan los datos:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.cluster import KMeans

wine = load_wine()
X = wine.data
y = wine.target

# A continuación, se crea un objeto de clustering K-means y se ajusta a los datos:

clustering = KMeans(n_clusters=3)
clustering.fit(X)

# Finalmente, se visualizan los clusters resultantes en una gráfica de dispersión:

plt.scatter(X[:, 0], X[:, 1], c=clustering.labels_, cmap='viridis')
plt.xlabel('Alcohol')
plt.ylabel('Malic acid')
plt.show()
```
En la gráfica de dispersión, se muestran los clusters coloreados según su etiqueta de cluster. En este caso, se han utilizado tres clusters, ya que el conjunto de datos Wine contiene tres clases de vino diferentes. La gráfica de dispersión muestra la relación entre las dos primeras características del conjunto de datos (alcohol y ácido málico).

### DBSCAN

El DBSCAN (Density-Based Spatial Clustering of Applications with Noise) es un algoritmo de clustering basado en la densidad que agrupa puntos de datos en función de su densidad local. Este algoritmo es capaz de encontrar clusters de cualquier forma y tamaño, y también puede identificar puntos de datos que no pertenecen a ningún cluster (ruido).

El proceso de clustering comienza seleccionando un punto de datos aleatorio y luego determinando todos los puntos de datos que se encuentran dentro de una distancia especificada (denominada "epsilon") de este punto. Si hay suficientes puntos de datos dentro de la distancia epsilon, se forma un nuevo cluster. Si no hay suficientes puntos de datos dentro de la distancia epsilon, el punto de datos se considera ruido.

Luego, se repite el proceso para todos los puntos de datos dentro de cada nuevo cluster, y así sucesivamente, hasta que se han identificado todos los clusters posibles.

Un ejemplo de clustering DBSCAN en Python se puede realizar utilizando el conjunto de datos Iris, que se encuentra disponible en la biblioteca de conjuntos de datos de scikit-learn.

En este ejemplo, utilizaremos la biblioteca de clustering de scikit-learn para realizar el clustering DBSCAN. Primero, se importan las bibliotecas necesarias y se cargan los datos:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import DBSCAN

iris = load_iris()
X = iris.data
y = iris.target

# A continuación, se crea un objeto de clustering DBSCAN y se ajusta a los datos:

clustering = DBSCAN(eps=0.5, min_samples=5)
clustering.fit(X)

# Finalmente, se visualizan los clusters resultantes en una gráfica de dispersión:

plt.scatter(X[:, 0], X[:, 1], c=clustering.labels_, cmap='viridis')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.show()
```
En la gráfica de dispersión, se muestran los clusters coloreados según su etiqueta de cluster. En este caso, se han utilizado los valores eps=0.5 y min_samples=5, lo que significa que un punto de datos se considera como parte de un cluster si hay al menos 5 puntos de datos dentro de una distancia de 0.5 unidades.

### Modelos de mezclas gaussianas (GMM)

Gaussian Mixture Models (GMM) es un algoritmo de clustering probabilístico que modela los datos como una mezcla de distribuciones gaussianas. En lugar de asignar los puntos de datos a un solo cluster, GMM asigna cada punto de datos a una distribución de probabilidad, lo que permite una mayor flexibilidad en la forma de los clusters.

El proceso de clustering comienza con la inicialización de un conjunto de distribuciones gaussianas con diferentes medias y covarianzas. A continuación, se ajustan los parámetros de las distribuciones gaussianas para maximizar la verosimilitud de los datos, es decir, se busca una combinación de distribuciones que explique mejor los datos.

GMM es un algoritmo iterativo que utiliza el algoritmo de Expectation-Maximization (EM) para encontrar la combinación óptima de distribuciones gaussianas que mejor se ajuste a los datos.

Ejemplo en Python usando un conjunto de datos público en línea

Un ejemplo de clustering GMM en Python se puede realizar utilizando el conjunto de datos Iris, que se encuentra disponible en la biblioteca de conjuntos de datos de scikit-learn.

En este ejemplo, utilizaremos la biblioteca de clustering de scikit-learn para realizar el clustering GMM. Primero, se importan las bibliotecas necesarias y se cargan los datos:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.mixture import GaussianMixture

iris = load_iris()
X = iris.data
y = iris.target

# A continuación, se crea un objeto de clustering GMM y se ajusta a los datos:

clustering = GaussianMixture(n_components=3)
clustering.fit(X)

# Finalmente, se visualizan los clusters resultantes en una gráfica de dispersión:

plt.scatter(X[:, 0], X[:, 1], c=clustering.predict(X), cmap='viridis')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.show()
```

En la gráfica de dispersión, se muestran los clusters coloreados según su etiqueta de cluster. En este caso, se han utilizado 3 componentes gaussianas para modelar los datos.

### Clustering espectral

Spectral clustering es un algoritmo de clustering que utiliza técnicas de álgebra lineal para agrupar datos. En lugar de agrupar directamente los datos, este algoritmo construye una matriz de similitud entre los puntos de datos y luego aplica técnicas de descomposición espectral para encontrar las estructuras de agrupación.

El proceso de clustering comienza con la construcción de una matriz de similitud entre los puntos de datos. Luego, se utiliza la descomposición espectral para transformar esta matriz en un espacio de características de menor dimensión. En este espacio de características, se aplican técnicas de clustering tradicionales, como K-means, para agrupar los datos.

Spectral clustering tiene varias ventajas sobre otros algoritmos de clustering, como la capacidad de detectar clusters no convexos y la robustez a los ruidos y las irregularidades en los datos.

Un ejemplo de clustering espectrales en Python se puede realizar utilizando el conjunto de datos de circulos, que se encuentra disponible en la biblioteca de conjuntos de datos de scikit-learn.

En este ejemplo, utilizaremos la biblioteca de clustering de scikit-learn para realizar el clustering espectrales. Primero, se importan las bibliotecas necesarias y se cargan los datos:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles
from sklearn.cluster import SpectralClustering

X, y = make_circles(n_samples=1000, noise=0.05, factor=0.5)

# A continuación, se crea un objeto de clustering espectrales y se ajusta a los datos:

clustering = SpectralClustering(n_clusters=2, affinity='nearest_neighbors')
clustering.fit(X)

# Finalmente, se visualizan los clusters resultantes en una gráfica de dispersión:

plt.scatter(X[:, 0], X[:, 1], c=clustering.labels_, cmap='viridis')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
```

En la gráfica de dispersión, se muestran los clusters coloreados según su etiqueta de cluster. En este caso, se han utilizado 2 clusters para agrupar los datos de los círculos.

## Evaluación de la calidad del cluster 

La evaluación de la calidad de los clusters es una tarea importante en el proceso de clustering. Hay varias métricas que se pueden utilizar para evaluar la calidad de los clusters, tanto internas como externas. Las métricas internas evalúan la calidad de los clusters en función de las características de los datos, mientras que las métricas externas evalúan la calidad de los clusters en función de la información de etiquetas conocidas.

Métricas de evaluación interna

- Coeficiente de Silhouette
- Índice de Calinski-Harabasz
- Índice de Davies-Bouldin

Métricas de evaluación externa

- Índice de Rand ajustado
- Información mutua normalizada

### Métricas de evaluación interna: Silhouette Score

El Silhouette Score es una medida de cuán similar es un objeto a su propio clúster en comparación con otros clústeres. Va desde -1 hasta 1, donde un puntaje de 1 indica que el objeto coincide bien con su propio clúster y mal con los clústeres vecinos, mientras que un puntaje de -1 indica lo contrario. Un puntaje de 0 indica que el objeto está en el límite entre dos clústeres. El puntaje promedio de silueta para todos los objetos en un conjunto de datos se puede utilizar para evaluar la calidad general de clustering.

El Silhouette Score se puede calcular utilizando los siguientes pasos:

1. Para cada objeto i, calcule la distancia promedio a todos los demás objetos en su clúster, denotada como ai.
2. Para cada objeto i, calcule la distancia promedio a todos los objetos en el clúster vecino más cercano, denotada como bi.
3. El Silhouette Score para el objeto i se da por (bi - ai) / max(ai, bi).
4. El Silhouette Score promedio para todos los objetos es la media de los puntajes de silueta para cada objeto.

En Python, se puede calcular el Silhouette Score utilizando la función silhouette_score del módulo sklearn.metrics. Aquí hay un ejemplo utilizando el conjunto de datos iris:

```python
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Load the iris dataset
iris = load_iris()

# Fit K-means clustering with k=3
kmeans = KMeans(n_clusters=3, random_state=0).fit(iris.data)

# Calculate the silhouette score
silhouette_avg = silhouette_score(iris.data, kmeans.labels_)

print("The average silhouette score is:", silhouette_avg)
```

### Métricas de evaluación interna: Índice de Calinski-Harabasz

El índice de Calinski-Harabasz es otra medida para evaluar la calidad de clustering en un conjunto de datos. Se basa en la relación entre la dispersión dentro de los clústeres y la dispersión entre los clústeres.

El índice de Calinski-Harabasz se puede calcular utilizando los siguientes pasos:

Calcular la media de cada variable en todo el conjunto de datos y denotarla como el centroide global.
Para cada clúster, calcular la media de cada variable dentro del clúster y denotarla como el centroide del clúster.
Calcular la suma total de la distancia euclidiana al cuadrado entre cada objeto y su centroide de clúster correspondiente, y denotarla como la dispersión dentro de los clústeres (WSS).
Calcular la suma total de la distancia euclidiana al cuadrado entre cada centroide de clúster y el centroide global, ponderada por el tamaño del clúster correspondiente, y denotarla como la dispersión entre los clústeres (BSS).
Calcular el índice de Calinski-Harabasz como BSS / WSS x (n - k) / (k - 1), donde n es el número total de objetos y k es el número de clústeres.
El índice de Calinski-Harabasz mide la relación entre la varianza entre los clústeres y la varianza dentro de los clústeres. Un índice más alto indica una mejor separación entre los clústeres.

En Python, se puede calcular el índice de Calinski-Harabasz utilizando la función calinski_harabasz_score del módulo sklearn.metrics. Aquí hay un ejemplo usando el conjunto de datos iris:

```python
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import calinski_harabasz_score

# Load the iris dataset
iris = load_iris()
X = iris.data

# Fit KMeans clustering with k=3
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

# Calculate the Calinski-Harabasz index
ch_score = calinski_harabasz_score(X, kmeans.labels_)

print("Calinski-Harabasz index:", ch_score)
```

En este ejemplo, primero cargamos el conjunto de datos de iris y extraemos la matriz de características X. Luego, ajustamos el clustering KMeans con k=3 clusters y calculamos el índice de Calinski-Harabasz usando la función calinski_harabasz_score del módulo metrics de scikit-learn. Finalmente, imprimimos el valor del índice de Calinski-Harabasz.

Tenga en cuenta que el índice de Calinski-Harabasz es una medida relativa de la calidad del clustering y debe usarse en comparación con otras soluciones de clustering. Un valor más alto indica una mejor calidad de clustering.

### Métricas de evaluación interna: Índice de Davies-Bouldin

El índice de Davies-Bouldin es otra métrica de evaluación interna para algoritmos de clustering. Evalúa la similitud entre los clusters y se basa en la similitud promedio entre cada cluster y su cluster más similar, donde la similitud se mide como la razón de la suma de distancias dentro del cluster a la distancia entre clusters. El índice varía de 0 a infinito, con un puntaje más bajo indicando una mejor calidad de clustering.

En Python, el índice de Davies-Bouldin se puede calcular usando la función davies_bouldin_score del módulo sklearn.metrics. Aquí hay un ejemplo utilizando el conjunto de datos iris:

```python
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import davies_bouldin_score

# Load the iris dataset
iris = load_iris()
X = iris.data

# Fit KMeans clustering with k=3 clusters
kmeans = KMeans(n_clusters=3, random_state=42).fit(X)

# Calculate the Davies-Bouldin index
db_index = davies_bouldin_score(X, kmeans.labels_)

# Print the Davies-Bouldin index value
print("Davies-Bouldin index:", db_index)
```

En este ejemplo, primero cargamos el conjunto de datos de iris y extraemos la matriz de características X. Luego, ajustamos el agrupamiento KMeans con k = 3 grupos y calculamos el índice de Davies-Bouldin utilizando la función davies_bouldin_score del módulo de métricas de scikit-learn. Finalmente, imprimimos el valor del índice de Davies-Bouldin.

Tenga en cuenta que el índice de Davies-Bouldin es una medida relativa de la calidad del agrupamiento y debe usarse en comparación con otras soluciones de agrupamiento. Un valor más bajo indica una mejor calidad de agrupamiento.

### Métricas de evaluación externa: Adjusted Rand Index

El índice de Rand ajustado (ARI) es una métrica de evaluación externa popular para algoritmos de clustering. Mide la similitud entre las etiquetas de clase verdaderas y las etiquetas de clase predichas. El ARI varía de -1 a 1, donde una puntuación de 1 indica que las etiquetas predichas son idénticas a las etiquetas verdaderas, una puntuación de 0 indica que las etiquetas predichas son aleatorias y una puntuación de -1 indica un desacuerdo completo entre las etiquetas predichas y verdaderas.

En Python, el ARI se puede calcular utilizando la función adjusted_rand_score del módulo sklearn.metrics. Aquí hay un ejemplo utilizando el conjunto de datos iris:

```python
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

iris = load_iris()
X = iris.data

kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
pred_labels = kmeans.labels_
true_labels = iris.target

ari = adjusted_rand_score(true_labels, pred_labels)
print("Adjusted Rand index:", ari)
```

En este ejemplo, primero cargamos el conjunto de datos iris y extraemos la matriz de características X. Luego, ajustamos el clustering KMeans con k=3 clústeres y predecimos las etiquetas de clúster para cada punto de datos. También cargamos las verdaderas etiquetas de clase del conjunto de datos iris. Finalmente, calculamos el ARI usando la función adjusted_rand_score y mostramos el valor de ARI.

Tenga en cuenta que el ARI requiere que las verdaderas etiquetas de clase sean conocidas y, por lo tanto, solo es aplicable para conjuntos de datos con etiquetas de referencia conocidas. Un puntaje de ARI más alto indica una mejor calidad de agrupamiento.

### Métricas de evaluación externa: Normalized Mutual Information

La información mutua normalizada (NMI) es una métrica de evaluación externa comúnmente utilizada en algoritmos de clustering. Mide la similitud entre las etiquetas de clase verdaderas y las etiquetas de clase predichas. La NMI varía de 0 a 1, donde un puntaje de 1 indica que las etiquetas predichas son idénticas a las etiquetas verdaderas, un puntaje de 0 indica que las etiquetas predichas son aleatorias y un puntaje cercano a 0 indica que las etiquetas predichas no se corresponden con las verdaderas.

En Python, la NMI se puede calcular utilizando la función normalized_mutual_info_score del módulo sklearn.metrics. Aquí hay un ejemplo utilizando el conjunto de datos iris:

```python
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import normalized_mutual_info_score

# Load the iris dataset
iris = load_iris()
X = iris.data

# Fit KMeans clustering with k=3 clusters
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)

# Get the true class labels
y_true = iris.target

# Predict the cluster labels
y_pred = kmeans.labels_

# Calculate the NMI
nmi = normalized_mutual_info_score(y_true, y_pred)

# Print the NMI value
print("Normalized Mutual Information: {:.2f}".format(nmi))
```
Tenga en cuenta que la NMI requiere que las etiquetas de clase verdaderas sean conocidas y, por lo tanto, solo es aplicable para conjuntos de datos con etiquetas de verdad terreno. Un puntaje NMI más alto indica una mejor calidad de clustering.

## Aplicaciones de aprendizaje no supervisado 

Las técnicas de aprendizaje no supervisado, como el agrupamiento y la clusterización, tienen una amplia gama de aplicaciones en diversos campos. Aquí hay algunos ejemplos:

Segmentación de clientes: El aprendizaje no supervisado se puede utilizar para agrupar a los clientes según su comportamiento, preferencias y demografía. Esta información se puede utilizar para adaptar las campañas de marketing y mejorar la satisfacción del cliente.

Segmentación de imágenes: Los algoritmos de aprendizaje no supervisado se pueden utilizar para agrupar los píxeles de una imagen que pertenecen al mismo objeto o región. Esto es útil en aplicaciones de procesamiento de imágenes como el reconocimiento, seguimiento y segmentación de objetos.

Detección de anomalías: El aprendizaje no supervisado se puede utilizar para detectar valores atípicos o anomalías en un conjunto de datos. Esto es útil en la detección de fraudes, intrusiones y en la identificación de defectos de fabricación.

Procesamiento de lenguaje natural: El aprendizaje no supervisado se puede utilizar para clusterizar documentos similares o agrupar palabras con significados similares. Esto se puede utilizar en aplicaciones como la modelización de temas, el análisis de sentimientos y la clasificación de documentos.

Bioinformática: El aprendizaje no supervisado se puede utilizar para clusterizar perfiles de expresión génica, identificar funciones de proteínas y clasificar imágenes médicas.

Sistemas de recomendación: El aprendizaje no supervisado se puede utilizar para agrupar a los usuarios según sus preferencias y recomendar productos o servicios en función de su comportamiento pasado.

Estos son solo algunos ejemplos de cómo se pueden aplicar las técnicas de aprendizaje no supervisado en aplicaciones de agrupamiento y clusterización.

### Reducción de dimensionalidad con PCA y t-SNE

La reducción de la dimensionalidad es una técnica utilizada para reducir el número de características o variables en un conjunto de datos mientras se retiene la información más importante. Dos métodos populares para la reducción de la dimensionalidad son el Análisis de Componentes Principales (PCA) y el Ensamble de Vecinos Estocásticos Distribuidos en t (t-SNE).

PCA es una técnica de reducción de la dimensionalidad lineal que proyecta datos de alta dimensión en un espacio de menor dimensión encontrando los componentes principales de los datos. Los componentes principales son las direcciones en las que los datos varían más y los primeros componentes principales capturan típicamente la información más importante en los datos.

t-SNE es una técnica de reducción de la dimensionalidad no lineal que es particularmente útil para visualizar datos de alta dimensión. Mapea los datos de alta dimensión a un espacio de baja dimensión mientras preserva las similitudes entre los puntos de datos.

En Python, tanto PCA como t-SNE pueden implementarse utilizando la biblioteca scikit-learn. Aquí hay un ejemplo utilizando el conjunto de datos iris:

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Perform PCA with 2 components
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Perform t-SNE with 2 components
tsne = TSNE(n_components=2)
X_tsne = tsne.fit_transform(X)

# Plot the results
plt.subplot(121)
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y)
plt.title('PCA')
plt.subplot(122)
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y)
plt.title('t-SNE')
plt.show()
```

En este ejemplo, primero cargamos el conjunto de datos iris y extraemos la matriz de características X y el vector de destino y. Luego, realizamos PCA con 2 componentes y t-SNE con 2 componentes utilizando las clases PCA y TSNE de scikit-learn. Finalmente, graficamos los resultados usando matplotlib, donde cada clase se representa con un color diferente.

Tenga en cuenta que la elección del número de componentes es un hiperparámetro que se puede ajustar para lograr el nivel deseado de reducción de dimensionalidad.

### Detección de anomalías con clustering

La detección de anomalías es el proceso de identificar puntos de datos que son significativamente diferentes a la mayoría de los datos. El clustering es una técnica común de aprendizaje no supervisado utilizada en la detección de anomalías, donde los puntos de datos se agrupan en clústeres según su similitud. Las anomalías se identifican como puntos de datos que no pertenecen a ningún clúster o pertenecen a un clúster pequeño o distante.

En Python, la detección de anomalías basada en clustering se puede implementar utilizando el algoritmo Local Outlier Factor (LOF) de la biblioteca scikit-learn. LOF calcula un puntaje para cada punto de datos basado en la densidad de su vecindario local en comparación con las densidades de sus puntos vecinos. Los puntos de datos con un puntaje LOF bajo se consideran anomalías.

Aquí hay un ejemplo utilizando el conjunto de datos iris para demostrar la detección de anomalías basada en clustering con LOF:

```python
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.neighbors import LocalOutlierFactor

# Load the iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Cluster the data using KMeans
kmeans = KMeans(n_clusters=3, random_state=42).fit(X)

# Identify anomalies using LOF
lof = LocalOutlierFactor(n_neighbors=20)
anomalies = lof.fit_predict(X)

# Plot the results
import matplotlib.pyplot as plt

plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_)
plt.scatter(X[anomalies == -1, 0], X[anomalies == -1, 1], marker='x', s=100, linewidth=2, c='red')
plt.show()
```

En este ejemplo, primero cargamos el conjunto de datos de iris y extraemos la matriz de características X. Luego, realizamos la agrupación KMeans con k=3 grupos e identificamos anomalías utilizando LOF con 20 vecinos. Finalmente, graficamos los resultados con las anomalías representadas por cruces rojos. Tenga en cuenta que la elección del número de grupos y el número de vecinos son hiperparámetros que se pueden ajustar para lograr el nivel deseado de agrupación y detección de anomalías.