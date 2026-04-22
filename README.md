# Asistente Virtual de Soporte Técnico

Proyecto desarrollado en Python como prototipo de asistente virtual de soporte técnico basado en procesamiento del lenguaje natural (PLN).

El sistema permite analizar consultas escritas por el usuario, clasificarlas en una categoría de incidencia y devolver una respuesta automática con una serie de recomendaciones básicas.

## Funcionalidades

- Clasificación de consultas en lenguaje natural
- Diagnóstico básico de incidencias técnicas
- Respuesta automática con pasos recomendados
- API REST desarrollada con FastAPI
- Interfaz web sencilla tipo chatbot

## Categorías que reconoce

- Problemas de internet
- Problemas de contraseña
- Problemas de impresora
- Problemas de rendimiento del equipo

## Tecnologías utilizadas

- Python
- FastAPI
- Jinja2
- scikit-learn
- HTML
- CSS
- JavaScript

## Estructura del proyecto

```text
asistente_soporte_ia/
├── app/
│   ├── data.py
│   ├── main.py
│   ├── model.py
│   └── schemas.py
├── templates/
│   └── chat.html
└── venv/
```

## Instalación
Clonar el repositorio:
```text
git clone https://github.com/tu-usuario/asistente_soporte_ia.git
cd asistente_soporte_ia
```
Crear y activar el entorno virtual:
Windows
```text
python -m venv venv
venv\Scripts\activate
Linux / macOS
```text
python3 -m venv venv
source venv/bin/activate
```
Instalar dependencias:
```text
pip install fastapi uvicorn scikit-learn jinja2 pandas
```

## Ejecución

Iniciar el servidor con:
```text
uvicorn app.main:app --reload
```
Acceso a la aplicación
Documentación automática de la API:
```text
http://127.0.0.1:8000/docs
```
Interfaz web del chatbot:
```text
http://127.0.0.1:8000/chat
```

## Ejemplos de consultas
No puedo conectarme al wifi
He olvidado mi contraseña
La impresora no imprime
El ordenador va muy lento

## Mejoras futuras
Ampliar el dataset de entrenamiento
Añadir nuevas categorías de incidencias
Mejorar la interfaz web
Incorporar base de datos
Añadir autenticación y medidas de seguridad

## Autor
Gema Sánchez Navarro
