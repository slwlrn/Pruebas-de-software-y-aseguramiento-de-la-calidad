# Proyecto: Análisis y Conversión de Datos en Python

Este proyecto contiene tres programas en Python que realizan distintas operaciones sobre archivos de texto. A continuación, se describen los programas, sus funcionalidades y las instrucciones para ejecutarlos correctamente.

---

## 📌 **Estructura del Proyecto**

```
📂 pythonProject2
 ├── 📂 P1  # Programa 1 - Análisis de estadísticas
 │   ├── compute_statistics.py
 │   ├── TC1.txt
 │   ├── TC2.txt
 │   ├── ...
 │   └── StatisticsResults.txt  # Salida generada
 ├── 📂 P2  # Programa 2 - Conversión de números
 │   ├── convert_numbers.py
 │   ├── TC1.txt
 │   ├── TC2.txt
 │   ├── ...
 │   └── ConversionResults.txt  # Salida generada
 ├── 📂 P3  # Programa 3 - Conteo de palabras
 │   ├── word_count.py
 │   ├── TC1.txt
 │   ├── TC2.txt
 │   ├── ...
 │   ├── TC1.txt.Results.txt  # Salidas generadas
 │   └── ...
 ├── README.md  # Este documento
```

---

## 🔹 **Requerimientos Previos**
Para ejecutar los programas, necesitas:
- Python 3.8 o superior instalado.
- Instalar la herramienta **pylint** para verificar el código:
  ```sh
  pip install pylint
  ```

---

## 🚀 **Cómo Ejecutar Cada Programa**

### **📊 Programa 1 - Cálculo de Estadísticas**
#### 📍 Ubicación: `P1/compute_statistics.py`
#### 🔹 **Funcionalidad:**
Este programa analiza un archivo de texto que contiene números y calcula:
- Media
- Mediana
- Moda
- Varianza
- Desviación estándar

#### ✅ **Ejemplo de Ejecución:**
```sh
python P1/compute_statistics.py
```

#### 📤 **Salida esperada:**
El resultado se guardará en `P1/StatisticsResults.txt` con el siguiente formato:
```
==================================================
Results for TC1.txt:
Mean: 241.91
Median: 239.00
Mode: #N/A
Variance: 21086.31
Standard Deviation: 145.21
Execution Time: 0.000993 seconds
==================================================
```

---

### **🔢 Programa 2 - Conversión de Números**
#### 📍 Ubicación: `P2/convert_numbers.py`
#### 🔹 **Funcionalidad:**
Convierte números decimales de un archivo de texto a:
- Binario
- Hexadecimal

#### ✅ **Ejemplo de Ejecución:**
```sh
python P2/convert_numbers.py
```

Esto procesará **todos los archivos `.txt` en la carpeta P2**. Para ejecutar solo un archivo específico:
```sh
python P2/convert_numbers.py P2/TC1.txt
```

#### 📤 **Salida esperada:**
El resultado se guardará en `P2/ConversionResults.txt` con el siguiente formato:
```
==================================================
Results for TC1.txt:
Decimal: 25, Binary: 11001, Hexadecimal: 19
Decimal: -10, Binary: -1010, Hexadecimal: -A
...
Execution Time: 0.001234 seconds
==================================================
```

---

### **🔠 Programa 3 - Conteo de Palabras**
#### 📍 Ubicación: `P3/word_count.py`
#### 🔹 **Funcionalidad:**
Cuenta la frecuencia de palabras en un archivo de texto, ignorando signos de puntuación y convirtiendo todo a minúsculas.

#### ✅ **Ejemplo de Ejecución:**
```sh
python P3/word_count.py
```

#### 📤 **Salida esperada:**
El resultado se guardará en archivos como `P3/TC1.txt.Results.txt`, con el siguiente formato:
```
python  5
program 3
language 2
...
Execution Time: 0.002145 seconds
```

---

## ✅ **Validación de Estilo con Pylint**
Para verificar que el código cumple con los estándares PEP 8, ejecutar:
```sh
python -m pylint P1/compute_statistics.py
python -m pylint P2/convert_numbers.py
python -m pylint P3/word_count.py
```
Un puntaje de 10/10 indica que no hay errores de estilo.

---

## ⚠ **Notas Importantes**
- **El archivo `ConversionResults.txt` ahora guarda los resultados de todos los archivos procesados, en lugar de sobrescribirse en cada ejecución.**
- Si hay errores en los archivos de entrada, se mostrarán advertencias en la terminal.

---

## 🎯 **Conclusión**
Estos programas permiten analizar archivos de texto para obtener estadísticas, realizar conversiones numéricas y contar palabras, utilizando principios de programación estructurada y buenas prácticas de codificación con PEP 8.

---

