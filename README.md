# Proyecto 6: Computer Vision

# Sistema de Asistencia con Reconocimiento Facial

## Descripción

Este proyecto implementa un sistema simple de **asistencia automatizada utilizando reconocimiento facial** mediante la librería **DeepFace** en Python.

El programa compara el rostro capturado con imágenes previamente registradas para determinar si una persona está en la base de datos. Si el rostro coincide, el sistema registra la asistencia.

Este proyecto demuestra una aplicación básica de **visión por computadora y redes neuronales** utilizando modelos ya entrenados.

---

## Tecnologías utilizadas

* Python 3
* DeepFace
* OpenCV
* TensorFlow
* NumPy

---

## Instalación

### 1. Clonar el repositorio

git clone <URL_DEL_REPOSITORIO>
cd nombre-del-repositorio

### 2. Crear un entorno virtual

python -m venv venv

Activar el entorno virtual:

**Windows**

venv\Scripts\activate

**Mac / Linux**

source venv/bin/activate

### 3. Instalar dependencias

pip install -r requirements.txt


---

## Uso

1. Coloca las imágenes de las personas registradas dentro de la carpeta:

fotos/

2. Ejecuta el programa:

python main.py


3. El sistema comparará el rostro capturado con las imágenes registradas.

Si encuentra coincidencia, mostrará:
Asistencia registrada

Si no encuentra coincidencia:
Persona no reconocida
---

## Estructura del proyecto

proyecto-vision/
│
├── main.py
├── fotos/
│   ├── alumno1.jpg
│   └── alumno2.jpg
│
├── requirements.txt
└── README.md

---

## Funcionalidades

* Verificación facial usando DeepFace
* Comparación de rostros con imágenes registradas
* Registro simple de asistencia mediante reconocimiento facial

---

## Posibles mejoras

* Uso de cámara en tiempo real
* Interfaz gráfica para el sistema
* Base de datos de estudiantes
+ Videovigilancia
