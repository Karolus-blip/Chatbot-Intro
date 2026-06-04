# Chatbot-Intro

# Asistente Virtual para Librería: Gestión de Devoluciones y Atención al Cliente

Este es un proyecto inicial de **Diseño Conversacional (CxD)** enfocado en la creación y simulación de un asistente virtual automatizado para el ecosistema de una librería. El proyecto aborda el diseño desde la arquitectura lingüística inicial hasta un prototipo lógico funcional.

## 🎯 Objetivo del Proyecto
Explorar y optimizar las estructuras de interacción entre usuarios y asistentes virtuales en contextos de atención al cliente, analizando cómo la pragmática del lenguaje y los flujos lógicos impactan la experiencia de usuario (UX) en entornos culturales y comerciales.

---

## 🛠️ Contenidos del Proyecto y Arquitectura

El repositorio está estructurado para mostrar el ciclo completo de diseño de una interfaz conversacional:

### 1. ✍️ Guión y Diálogo de Devolución de Libros
* **Ubicación:** `/dialogos/`
* **Descripción:** Diseño de los scripts de conversación que modelan la interacción. Incluye el camino ideal (*Happy Path*) para la devolución de un ejemplar, así como la redacción y estrategia de textos conversacionales (Copywriting) adaptados al tono de una librería.
* **Enfoque CxD:** Manejo de la cortesía lingüística y técnicas de reparación de errores (*Turn-taking* y gestión de *No-Match*).

### 2. 🗺️ Diagrama de Flujo Conversacional
* **Ubicación:** `/diagramas/` 
* **Descripción:** El árbol de decisión completo y la arquitectura de la información del bot. Muestra visualmente las bifurcaciones de la conversación basadas en las intenciones del usuario, las condicionales del sistema (ej. si el libro está dañado o fuera de tiempo) y los puntos de salida hacia un agente humano.

### 3. 🐍 Prototipo Lógico en Python
* **Ubicación:** `/src/`
* **Descripción:** La traducción de la estructura lingüística a código funcional. Un script en Python que simula la lógica del backend conversacional, manejando variables, control de estados de la conversación y el procesamiento de entradas simuladas del usuario para determinar la respuesta correcta.

### 4. 🌐 Interfaz de Usuario Básica en HTML
* **Ubicación:** `/frontend/`
* **Descripción:** Un entorno visual e interactivo mínimo (maqueta) que simula la ventana de chat (*webchat*), permitiendo experimentar el flujo conversacional en una interfaz cercana a un producto real.

---

## 🚀 Tecnologías y Herramientas Utilizadas
* **Diseño y Flujo:** 
* **Lógica del Backend:** Python 3.x (Estructuras de control, condicionales y manejo de strings)
* **Maquetación Frontend:** HTML5 y CSS básico

---

## 📈 Aprendizajes y Próximos Pasos
Este proyecto me permitió experimentar de primera mano el puente entre la **lingüística teórica** y la **lógica de programación**, entendiendo que un buen bot no solo responde, sino que guía al usuario de forma clara a través de la ambigüedad del lenguaje natural.

* **Próximo hito:** Integrar este flujo en una plataforma de NLP (como Dialogflow o Rasa) para añadir entrenamiento de intenciones (*Intents*) y extracción de entidades (*Entities*).
