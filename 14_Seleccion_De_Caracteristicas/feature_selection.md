# Selección de características

## Introducción

En esta sección, exploraremos el concepto de selección de características, que es un paso importante en el desarrollo de modelos de machine learning. Cubriremos los diferentes tipos de técnicas de selección de características, sus ventajas y desventajas, y cómo implementarlas usando Python.

### ¿Qué es la selección de características?

- Definición e importancia de la selección de características
- Tipos de técnicas de selección de características
- Selección de características supervisadas vs no supervisadas
- Filtro vs Envoltorio vs Selección de características embedidas (Embedded Feature Selection Techniques)

### Definición e importancia de la selección de características

La selección de características es el proceso de seleccionar un subconjunto de características relevantes (variables, predictores) de un conjunto más grande de características para usar en un modelo de machine learning. El objetivo de la selección de características es reducir la complejidad del modelo, mejorar su rendimiento predictivo y evitar el sobreajuste.

La selección de características es importante en el machine learning porque el uso de demasiadas características irrelevantes o redundantes puede provocar un rendimiento deficiente del modelo, tiempos de entrenamiento lentos y una capacidad de interpretación reducida. La selección de características ayuda a identificar las características más importantes, lo que puede mejorar la precisión del modelo y reducir el tiempo de capacitación.

Además, la selección de características también puede ayudar a reducir el costo y el tiempo necesarios para la recopilación de datos, ya que nos permite concentrarnos en recopilar solo las características más relevantes. Esto es especialmente importante en situaciones en las que la recopilación de datos es costosa o lleva mucho tiempo, como en la investigación médica o el monitoreo ambiental.

### Tipos de técnicas de selección de características

Hay tres tipos principales de técnicas de selección de características:

1. Selección de características de filtro (Filter Feature Selection Techniques)

2. Selección de características de la envoltura

3. Selección de características embedidas (Embedded Feature Selection Techniques)

La elección de la técnica de selección de características adecuada depende de las características del conjunto de datos, el algoritmo de machine learning que se utiliza y los objetivos específicos del análisis.

### Selección de características supervisadas vs no supervisadas

La selección de características supervisada y no supervisada son dos enfoques diferentes para seleccionar características en función de la presencia o ausencia de una variable objetivo.

Los métodos de selección de características supervisadas utilizan la variable objetivo (es decir, la variable dependiente) para identificar las características más relevantes para la predicción. Estos métodos se utilizan cuando tenemos datos etiquetados y el objetivo es seleccionar las características que son más predictivas de la variable objetivo. Los ejemplos de métodos de selección de características supervisadas incluyen la selección de características basada en la correlación, la selección de características de información mutua y los métodos de envoltorio como la selección hacia adelante y la eliminación hacia atrás.

Los métodos de selección de características no supervisados, por otro lado, no utilizan la variable de destino para seleccionar características. En cambio, se enfocan en identificar las características que capturan la información o estructura más importante en los datos. Estos métodos se utilizan cuando tenemos datos sin etiquetar o cuando queremos explorar la estructura de los datos. Los ejemplos de métodos de selección de características no supervisados ​​incluyen el análisis de componentes principales (PCA), el análisis de componentes independientes (ICA) y la selección de características basada en agrupaciones.

Tanto los métodos de selección de características supervisados ​​como los no supervisados ​​tienen sus ventajas y desventajas, y la elección del método depende de la naturaleza de los datos y los objetivos específicos del análisis.

### Técnicas Filter vs Wrapper vs Embedded en la selección de características

La selección de características incrustadas, el contenedor y el filtro son tres tipos diferentes de técnicas de selección de características basadas en cómo incorporan la selección de características en el flujo de trabajo de machine learning.

## Ejemplos en python de técnicas de selección de características de filtro (Filter Feature Selection Techniques)

Los métodos de selección de características de filtro son independientes del algoritmo de machine learning y seleccionan características en función de medidas estadísticas como correlación, información mutua o pruebas de chi-cuadrado. Estos métodos son computacionalmente eficientes y se pueden aplicar como un paso de preprocesamiento. Sin embargo, es posible que no seleccionen necesariamente las características más relevantes para el problema de machine learning dado. Los ejemplos de métodos de selección de características de filtro incluyen la selección de características basada en la correlación, la selección de características de chi-cuadrado y la selección de características de información mutua.

A continuación se proporcionan diversos ejemplos en la selección de características de filtro:

### Selección de características basada en la correlación (Correlation-based feature selection)

Correlación basada en selección de características es un método de filtro para la selección de características que evalúa la correlación entre cada característica y la variable objetivo, así como la correlación entre pares de características. Este método es útil cuando queremos identificar las características que están más fuertemente correlacionadas con la variable objetivo y aquellas que son redundantes entre sí.

Los pasos básicos involucrados en la selección de características basada en correlación son los siguientes:

1. Calcular el coeficiente de correlación entre cada característica y la variable objetivo. Esto se puede hacer utilizando el coeficiente de correlación de Pearson para variables continuas o el coeficiente de correlación punto-biserial para variables binarias.

2. Ordenar las características en función de su coeficiente de correlación con la variable objetivo y seleccionar las primeras n características.

3. Calcular la matriz de correlación entre las características seleccionadas y eliminar las características que tienen una alta correlación entre sí. Esto se hace para evitar la redundancia en las características seleccionadas.

El número de características a seleccionar (es decir, n en el paso 2) se puede determinar utilizando conocimientos de dominio o mediante el uso de un algoritmo de optimización que maximiza el rendimiento del algoritmo de machine learning en un conjunto de validación.

Una limitación de la selección de características basada en correlación es que solo captura relaciones lineales entre características y la variable objetivo. Las relaciones no lineales pueden pasarse por alto si existen. Además, la selección de características basada en correlación puede ser sensible a valores atípicos y ruido en los datos.

En general, la selección de características basada en correlación es una técnica útil para seleccionar un subconjunto de características relevantes en función de su correlación con la variable objetivo y su redundancia entre sí.

Este es un ejemplo de cómo realizar una selección de características basada en la correlación usando Python y un conjunto de datos en línea:

```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = pd.read_csv(url, header=None)
iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

# Compute the correlation matrix
corr = iris.corr()

# Plot the correlation matrix
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')

# Perform feature selection based on correlation
threshold = 0.5
corr_features = set()
for i in range(len(corr.columns)):
    for j in range(i):
        if abs(corr.iloc[i, j]) > threshold:
            corr_features.add(corr.columns[i])

print('Selected features:', list(corr_features))

# Create a new dataframe with the selected features
selected_features_df = iris[list(corr_features)]

# Display the new dataframe
print('\nNew dataframe with selected features:')
print(selected_features_df.head())
```
En este ejemplo, estamos usando el conjunto de datos Iris, que es un conjunto de datos de uso común en el machine learning. Cargamos el conjunto de datos usando su URL y establecemos los nombres de las columnas. Luego calculamos la matriz de correlación utilizando el método corr() de Pandas DataFrame. Trazamos la matriz de correlación utilizando la biblioteca Seaborn para visualizar las correlaciones entre las características.

Luego realizamos una selección de características basada en la correlación estableciendo un umbral de 0,5 y seleccionando las características cuyo valor de correlación absoluta con otra característica es mayor que el umbral. Creamos un nuevo DataFrame con las características seleccionadas y lo mostramos.

Este es solo un ejemplo simple, y el umbral y el método de selección de características pueden variar según el conjunto de datos y el problema en cuestión.

### Selección de características de chi-cuadrado (Chi-Squared Feature Selection)

La selección de características basada en chi-cuadrado es una técnica de selección de características que se utiliza para seleccionar las características más relevantes en un conjunto de características categóricas. La idea detrás de esta técnica es encontrar la relación entre cada característica y la variable objetivo mediante el cálculo de la chi-cuadrado entre ellas. Las características con los valores de chi-cuadrado más altos se consideran las más relevantes.

La técnica de selección de características basada en chi-cuadrado se puede utilizar tanto para problemas de clasificación como de regresión. En el caso de la clasificación, se puede utilizar para seleccionar las características más discriminativas para cada clase. En el caso de la regresión, se puede utilizar para seleccionar las características más relacionadas con la variable objetivo.

Para utilizar la técnica de selección de características basada en chi-cuadrado en Python, se puede utilizar la función chi2 de la biblioteca scikit-learn. Aquí hay un ejemplo de cómo se puede utilizar esta técnica en Python:

```python
import pandas as pd
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

# Load the dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = pd.read_csv(url, header=None)
iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

# Separate features and target variable
X = iris.iloc[:, :-1]  # features
y = iris.iloc[:, -1]   # target variable

# Apply chi-squared feature selection
k = 2  # number of top features to select
selector = SelectKBest(chi2, k=k)
selector.fit(X, y)

# Get the selected features
selected_features = X.columns[selector.get_support()]

print('Selected features:', list(selected_features))
```

En este ejemplo, estamos utilizando el conjunto de datos Iris nuevamente. Primero cargamos el conjunto de datos y separamos las características y la variable objetivo. Luego, aplicamos la selección de características basada en chi-cuadrado utilizando la función SelectKBest de scikit-learn. Especificamos el número de características principales que queremos seleccionar (en este caso, 2) y ajustamos el selector a nuestros datos. Finalmente, imprimimos las características seleccionadas.

Es importante tener en cuenta que la selección de características basada en chi-cuadrado solo funciona con características categóricas. Si el conjunto de datos contiene características numéricas, es necesario discretizarlas antes de aplicar esta técnica.

### Selección de características de información mutua (Mutual Information Feature Selection)

La selección de características basada en información mutua es una técnica de selección de características que se utiliza para seleccionar las características más relevantes en un conjunto de características. La idea detrás de esta técnica es encontrar la relación entre cada característica y la variable objetivo mediante el cálculo de la información mutua entre ellas. Las características con los valores de información mutua más altos se consideran las más relevantes.

La información mutua mide la dependencia entre dos variables aleatorias y puede ser utilizada para medir la relación entre las características y la variable objetivo en un problema de aprendizaje automático. En la selección de características basada en información mutua, se calcula la información mutua entre cada característica y la variable objetivo y se seleccionan las características con los valores más altos.

Para utilizar la técnica de selección de características basada en información mutua en Python, se puede utilizar la función mutual_info_classif de la biblioteca scikit-learn. Aquí hay un ejemplo de cómo se puede utilizar esta técnica en Python:

```python
import pandas as pd
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import mutual_info_classif

# Load the dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = pd.read_csv(url, header=None)
iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

# Separate features and target variable
X = iris.iloc[:, :-1]  # features
y = iris.iloc[:, -1]   # target variable

# Apply mutual information feature selection
k = 2  # number of top features to select
selector = SelectKBest(mutual_info_classif, k=k)
selector.fit(X, y)

# Get the selected features
selected_features = X.columns[selector.get_support()]

print('Selected features:', list(selected_features))
```
En este ejemplo, estamos utilizando el conjunto de datos Iris nuevamente. Primero cargamos el conjunto de datos y separamos las características y la variable objetivo. Luego, aplicamos la selección de características basada en información mutua utilizando la función SelectKBest de scikit-learn. Especificamos el número de características principales que queremos seleccionar (en este caso, 2) y ajustamos el selector a nuestros datos. Finalmente, imprimimos las características seleccionadas.

Es importante tener en cuenta que la selección de características basada en información mutua solo funciona con características numéricas. Si el conjunto de datos contiene características categóricas, es necesario convertirlas a numéricas antes de aplicar esta técnica.

### Selección de características de ANOVA (ANOVA Feature Selection)

La selección de características ANOVA es una técnica de selección de características que se utiliza para seleccionar las características más relevantes en un conjunto de características. La idea detrás de esta técnica es encontrar las características que están más relacionadas con la variable objetivo mediante el análisis de la varianza (ANOVA).

En la selección de características ANOVA, se calcula la F-score (puntuación F) de cada característica, que mide la variabilidad entre las muestras con diferentes etiquetas de clase en relación con la variabilidad dentro de cada clase. Cuanto mayor sea la puntuación F de una característica, mayor será la diferencia entre las muestras con diferentes etiquetas de clase y mayor será la relevancia de la característica para la clasificación.

Para utilizar la técnica de selección de características ANOVA en Python, se puede utilizar la función f_classif de la biblioteca scikit-learn. Aquí hay un ejemplo de cómo se puede utilizar esta técnica en Python:

```python
import pandas as pd
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif

# Load the dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = pd.read_csv(url, header=None)
iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

# Separate features and target variable
X = iris.iloc[:, :-1]  # features
y = iris.iloc[:, -1]   # target variable

# Apply ANOVA feature selection
k = 2  # number of top features to select
selector = SelectKBest(f_classif, k=k)
selector.fit(X, y)

# Get the selected features
selected_features = X.columns[selector.get_support()]

print('Selected features:', list(selected_features))
```

En este ejemplo, estamos utilizando el conjunto de datos Iris nuevamente. Primero cargamos el conjunto de datos y separamos las características y la variable objetivo. Luego, aplicamos la selección de características ANOVA utilizando la función SelectKBest de scikit-learn. Especificamos el número de características principales que queremos seleccionar (en este caso, 2) y ajustamos el selector a nuestros datos. Finalmente, imprimimos las características seleccionadas.

Es importante tener en cuenta que la selección de características ANOVA solo funciona con características numéricas y asume que las muestras siguen una distribución normal. Si el conjunto de datos contiene características categóricas o no sigue una distribución normal, es necesario utilizar otra técnica de selección de características.

### Selección de características de ganancia de información (Information Gain Feature Selection)

La selección de características de ganancia de información es una técnica de selección de características que se utiliza para seleccionar las características más informativas en un conjunto de características. La idea detrás de esta técnica es encontrar las características que tienen la mayor cantidad de información sobre la variable objetivo.

En la selección de características de ganancia de información, se calcula la ganancia de información de cada característica, que mide la reducción de la entropía de la variable objetivo cuando se conoce el valor de la característica. Cuanto mayor sea la ganancia de información de una característica, mayor será la información que proporciona sobre la variable objetivo y mayor será la relevancia de la característica para la clasificación.

Para utilizar la técnica de selección de características de ganancia de información en Python, se puede utilizar la función mutual_info_classif de la biblioteca scikit-learn. Aquí hay un ejemplo de cómo se puede utilizar esta técnica en Python:

```python
import pandas as pd
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import mutual_info_classif

# Load the dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = pd.read_csv(url, header=None)
iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

# Separate features and target variable
X = iris.iloc[:, :-1]  # features
y = iris.iloc[:, -1]   # target variable

# Apply information gain feature selection
k = 2  # number of top features to select
selector = SelectKBest(mutual_info_classif, k=k)
selector.fit(X, y)

# Get the selected features
selected_features = X.columns[selector.get_support()]

print('Selected features:', list(selected_features))
```

En este ejemplo, estamos utilizando el conjunto de datos Iris nuevamente. Primero cargamos el conjunto de datos y separamos las características y la variable objetivo. Luego, aplicamos la selección de características de ganancia de información utilizando la función SelectKBest de scikit-learn. Especificamos el número de características principales que queremos seleccionar (en este caso, 2) y ajustamos el selector a nuestros datos. Finalmente, imprimimos las características seleccionadas.

Es importante tener en cuenta que la selección de características de ganancia de información solo funciona con características numéricas y puede ser sensible a la escala de las características. Si el conjunto de datos contiene características categóricas o no numéricas, es necesario utilizar otra técnica de selección de características.

## Técnicas de selección de características de contenedor (Wrapper Feature Selection Techniques)

Los métodos de selección de características de contenedor seleccionan características en función del rendimiento del algoritmo de machine learning en diferentes subconjuntos de características. Estos métodos son costosos desde el punto de vista computacional y pueden dar lugar a un sobreajuste, pero tienden a ser más precisos que los métodos de filtrado. Los métodos de envoltorio pueden ser iterativos, seleccionando características una por una o en grupos, o recursivos, donde las características se eliminan paso a paso. Los ejemplos de métodos de selección de características de envoltorio incluyen la eliminación recursiva de características, la selección hacia adelante y la eliminación hacia atrás.

### Eliminación de características recursivas (Recursive Feature Elimination)

La eliminación recursiva de características (RFE) es una técnica de selección de características que se utiliza para seleccionar las características más importantes en un conjunto de características. La idea detrás de esta técnica es eliminar iterativamente las características menos importantes de un conjunto de características hasta que se alcanza el número deseado de características.

En la eliminación recursiva de características, se entrena un modelo con todas las características y se eliminan iterativamente las características menos importantes. Después de cada iteración, se evalúa el modelo y se mide la precisión. Las características que contribuyen menos a la precisión del modelo se eliminan y se vuelve a entrenar el modelo con las características restantes. Este proceso se repite hasta que se alcanza el número deseado de características.

Para utilizar la técnica de eliminación recursiva de características en Python, se puede utilizar la clase RFE de la biblioteca scikit-learn. Aquí hay un ejemplo de cómo se puede utilizar esta técnica en Python:

```python
import pandas as pd
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

# Load the dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = pd.read_csv(url, header=None)
iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

# Separate features and target variable
X = iris.iloc[:, :-1]  # features
y = iris.iloc[:, -1]   # target variable

# Apply recursive feature elimination
n_features = 2  # number of features to select
estimator = LogisticRegression()
selector = RFE(estimator, n_features_to_select=n_features)
selector = selector.fit(X, y)

# Get the selected features
selected_features = X.columns[selector.support_]

print('Selected features:', list(selected_features))
```

En este ejemplo, estamos utilizando el conjunto de datos Iris nuevamente. Primero cargamos el conjunto de datos y separamos las características y la variable objetivo. Luego, aplicamos la eliminación recursiva de características utilizando la clase RFE de scikit-learn. Especificamos el número de características principales que queremos seleccionar (en este caso, 2) y el estimador que se utilizará para evaluar las características. Finalmente, imprimimos las características seleccionadas.

Es importante tener en cuenta que la eliminación recursiva de características puede ser computacionalmente costosa para conjuntos de datos grandes y complejos. Además, el número de características a seleccionar debe ser determinado empíricamente y puede afectar la precisión del modelo resultante.

### Selección hacia adelante (Forward Selection)

La selección hacia adelante (forward selection) es una técnica de selección de características que se utiliza para construir un modelo añadiendo iterativamente características a partir de un conjunto inicial de características. En cada iteración, se selecciona la característica que proporciona la mayor mejora en la precisión del modelo y se agrega al conjunto de características seleccionadas. Este proceso se repite hasta que se alcanza el número deseado de características o se detiene la mejora en la precisión del modelo.

Para aplicar la técnica de selección hacia adelante en Python, se puede utilizar la biblioteca scikit-learn. Aquí hay un ejemplo de cómo se puede utilizar esta técnica en Python:

```python
import pandas as pd
from sklearn.feature_selection import f_regression
from sklearn.linear_model import LinearRegression

# Load the dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'
housing = pd.read_csv(url, sep='\s+', header=None)
housing.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS',
                   'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

# Separate features and target variable
X = housing.iloc[:, :-1]  # features
y = housing.iloc[:, -1]   # target variable

# Perform forward feature selection
n_features = 5  # number of features to select
estimator = LinearRegression()
selected_features = set()

for i in range(n_features):
    best_score = 0
    best_feature = None
    
    for feature in X.columns:
        if feature not in selected_features:
            selected_features.add(feature)
            X_selected = X[list(selected_features)]
            scores, _ = f_regression(X_selected, y)
            score = scores.mean()
            
            if score > best_score:
                best_score = score
                best_feature = feature
                
            selected_features.remove(feature)
            
    selected_features.add(best_feature)

print('Selected features:', list(selected_features))
```

En este ejemplo, estamos utilizando el conjunto de datos de precios de vivienda de Boston. Primero cargamos el conjunto de datos y separamos las características y la variable objetivo. Luego, realizamos la selección hacia adelante de características utilizando un modelo de regresión lineal. Especificamos el número de características principales que queremos seleccionar (en este caso, 5) y evaluamos cada característica individualmente utilizando la función de puntuación f_regression de scikit-learn. Seleccionamos la característica que proporciona la mayor mejora en la precisión del modelo y la agregamos al conjunto de características seleccionadas. Este proceso se repite hasta que se alcanza el número deseado de características.

Es importante tener en cuenta que la selección hacia adelante puede ser computacionalmente costosa para conjuntos de datos grandes y complejos. Además, la selección hacia adelante puede no ser la mejor opción si hay interacciones entre características o si las características seleccionadas son altamente correlacionadas.

### Eliminación hacia atrás (Backward Elimination)

La eliminación hacia atrás (backward elimination) es una técnica de selección de características que se utiliza para construir un modelo eliminando iterativamente características a partir de un conjunto inicial de características. En cada iteración, se elimina la característica que proporciona la menor mejora en la precisión del modelo y se elimina del conjunto de características seleccionadas. Este proceso se repite hasta que se alcanza el número deseado de características o se detiene la mejora en la precisión del modelo.

Para aplicar la técnica de eliminación hacia atrás en Python, se puede utilizar la biblioteca scikit-learn. Aquí hay un ejemplo de cómo se puede utilizar esta técnica en Python:

```python
import pandas as pd
from sklearn.feature_selection import f_regression
from sklearn.linear_model import LinearRegression

# Load the dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'
housing = pd.read_csv(url, sep='\s+', header=None)
housing.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS',
                   'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

# Separate features and target variable
X = housing.iloc[:, :-1]  # features
y = housing.iloc[:, -1]   # target variable

# Perform backward feature elimination
n_features = 5  # number of features to select
estimator = LinearRegression()
selected_features = set(X.columns)

while len(selected_features) > n_features:
    worst_score = float('inf')
    worst_feature = None
    
    for feature in selected_features:
        selected_features.remove(feature)
        X_selected = X[list(selected_features)]
        scores, _ = f_regression(X_selected, y)
        score = scores.mean()
        
        if score < worst_score:
            worst_score = score
            worst_feature = feature
                
        selected_features.add(feature)
            
    selected_features.remove(worst_feature)

print('Selected features:', list(selected_features))
```

En este ejemplo, estamos utilizando el conjunto de datos de precios de vivienda de Boston. Primero cargamos el conjunto de datos y separamos las características y la variable objetivo. Luego, realizamos la eliminación hacia atrás de características utilizando un modelo de regresión lineal. Especificamos el número de características principales que queremos seleccionar (en este caso, 5) y evaluamos cada característica individualmente utilizando la función de puntuación f_regression de scikit-learn. Se elimina la característica que proporciona la menor mejora en la precisión del modelo y se elimina del conjunto de características seleccionadas. Este proceso se repite hasta que se alcanza el número deseado de características.

Es importante tener en cuenta que la eliminación hacia atrás puede ser computacionalmente costosa para conjuntos de datos grandes y complejos. Además, la eliminación hacia atrás puede no ser la mejor opción si hay interacciones entre características o si las características seleccionadas son altamente correlacionadas.

## Técnicas de selección de características embedidas (Embedded Feature Selection Techniques)

Los métodos de selección de características embedidos incorporan la selección de características como parte del proceso de entrenamiento del modelo. Estos métodos son computacionalmente eficientes y tienden a producir modelos más precisos que los métodos de filtro, pero pueden ser sensibles al sobreajuste. Los ejemplos de técnicas de selección de características embedidas (Embedded Feature Selection Techniques) incluyen la regresión LASSO, la regresión de crestas y métodos basados ​​en árboles de decisión, como bosque aleatorio y aumento de gradiente.

La elección de la técnica de selección de características depende del conjunto de datos, el algoritmo de machine learning que se utiliza y los objetivos específicos del análisis. Los métodos de filtro son una buena opción cuando queremos una forma rápida y eficiente de reducir la dimensionalidad del conjunto de datos. Se prefieren los métodos de contenedor cuando queremos seleccionar un conjunto de características que optimizan el rendimiento de un algoritmo de machine learning específico. Los métodos embedidos son útiles cuando queremos identificar las características más importantes para un problema de machine learning dado, mientras entrenamos el modelo.

### Regresión LASSO (LASSO Regression)

La regresión LASSO (Least Absolute Shrinkage and Selection Operator) es una técnica de selección de características que utiliza regularización para reducir el número de características en un modelo y mejorar su capacidad de generalización. La regresión LASSO agrega una penalización a la función de pérdida que minimiza el error cuadrático medio, lo que reduce la magnitud de los coeficientes de las características menos importantes a cero. Esto significa que la regresión LASSO puede identificar y eliminar características irrelevantes del modelo.

Para aplicar la regresión LASSO en Python, se puede utilizar la biblioteca scikit-learn. Aquí hay un ejemplo de cómo se puede utilizar esta técnica en Python:

```python
import pandas as pd
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split

# Load the dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'
housing = pd.read_csv(url, sep='\s+', header=None)
housing.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS',
                   'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

# Separate features and target variable
X = housing.iloc[:, :-1]  # features
y = housing.iloc[:, -1]   # target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Fit the LASSO regression model
lasso = Lasso(alpha=0.1)
lasso.fit(X_train, y_train)

# Print the coefficients of the features
coef = pd.Series(lasso.coef_, index=X.columns)
print('Selected features:\n', coef[coef != 0])
```

En este ejemplo, estamos utilizando el conjunto de datos de precios de vivienda de Boston. Primero cargamos el conjunto de datos y separamos las características y la variable objetivo. Luego, dividimos el conjunto de datos en conjuntos de entrenamiento y prueba. A continuación, ajustamos un modelo de regresión LASSO en los datos de entrenamiento utilizando la clase Lasso de scikit-learn. Especificamos un valor para el hiperparámetro de regularización alpha que controla la fuerza de la regularización y, por lo tanto, la cantidad de características que se eliminan. Finalmente, imprimimos los coeficientes de las características seleccionadas por el modelo.

Es importante tener en cuenta que el hiperparámetro alpha debe ajustarse cuidadosamente para obtener un buen equilibrio entre la precisión del modelo y la cantidad de características seleccionadas. Además, la regresión LASSO puede no ser la mejor opción si hay interacciones entre características o si las características seleccionadas son altamente correlacionadas.

### Regresión de Ridge (Ridge Regression)

La regresión de Ridge es otra técnica de selección de características que utiliza regularización para reducir la complejidad del modelo y mejorar su capacidad de generalización. Al igual que la regresión LASSO, la regresión de Ridge agrega una penalización a la función de pérdida que minimiza el error cuadrático medio. Sin embargo, en lugar de reducir los coeficientes de las características menos importantes a cero, la regresión de Ridge reduce la magnitud de los coeficientes, lo que significa que todas las características contribuyen al modelo.

Para aplicar la regresión de Ridge en Python, también se puede utilizar la biblioteca scikit-learn. Aquí hay un ejemplo de cómo se puede utilizar esta técnica en Python:

```python
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split

# Load the dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'
housing = pd.read_csv(url, sep='\s+', header=None)
housing.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS',
                   'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

# Separate features and target variable
X = housing.iloc[:, :-1]  # features
y = housing.iloc[:, -1]   # target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Fit the Ridge regression model
ridge = Ridge(alpha=0.1)
ridge.fit(X_train, y_train)

# Print the coefficients of the features
coef = pd.Series(ridge.coef_, index=X.columns)
print('Selected features:\n', coef)
```

En este ejemplo, estamos utilizando el mismo conjunto de datos de precios de vivienda de Boston que en el ejemplo anterior. Primero cargamos el conjunto de datos y separamos las características y la variable objetivo. Luego, dividimos el conjunto de datos en conjuntos de entrenamiento y prueba. A continuación, ajustamos un modelo de regresión de Ridge en los datos de entrenamiento utilizando la clase Ridge de scikit-learn. Especificamos un valor para el hiperparámetro de regularización alpha. Finalmente, imprimimos los coeficientes de las características seleccionadas por el modelo.

Al igual que con la regresión LASSO, el hiperparámetro alpha debe ajustarse cuidadosamente para obtener un buen equilibrio entre la precisión del modelo y la cantidad de características seleccionadas. La regresión de Ridge también puede no ser la mejor opción si hay interacciones entre características o si las características seleccionadas son altamente correlacionadas.

## Conclusión

En este curso, hemos cubierto el concepto de selección de características, su importancia y varias técnicas que se pueden usar para seleccionar características para modelos de machine learning. Al final de este curso, comprenderá bien cómo implementar técnicas de selección de características en Python y qué técnica usar para diferentes tipos de conjuntos de datos.