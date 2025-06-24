# PFO 2: Sistema de Gestión de Tareas con API y Base de Datos 📝

<!-- ÍNDICE -->
  <a name="indice"></a>
  ## 📌 Índice
  <ol>
    <li><a href="#objetivo">Objetivo</a></li>
      <ul>
        <li><a href="#servidor">Servidor</a></li>
        <li><a href="#requisitos-tec">Requisitos técnicos</a></li>
       </ul>
    <li><a href="#tecnologias">Tecnologías utilizadas</a></li>
    <li><a href="#instrucciones">Instrucciones</a></li>
    <li><a href="#capturas">Capturas</a></li>
    <li><a href="#preguntas">Preguntas conceptuales</a>
  </ol>

<!-- OBJETIVO -->
<a name="objetivo"></a>
## ✏ Objetivo 
Al finalizar este trabajo práctico, serás capaz de: 
- Implementar una API REST con endpoints funcionales. 
- Utilizar autenticación básica con protección de contraseñas. 
- Gestionar datos persistentes con SQLite. 
- Construir un cliente en consola que interactúe con la API. 

<a name="servidor"></a>
### Servidor
Servidor (API Flask) 
Desarrolla un servidor que realiza lo siguiente: 
<ol>
    <li>Registro de Usuarios</li>
      <ul>
        <li>Endpoint: POST /registro</li>
        <li>Debe recibir {"usuario": "nombre", "contraseña": "1234"}.</li>
        <li>Almacenar usuarios en SQLite con contraseñas hasheadas (¡nunca en texto plano!). </li>
      </ul>
    <li>Inicio de Sesión</li>
      <ul>
        <li>Endpoint: POST /login</li>
        <li>Verifica credenciales y permite acceso a las tareas.</li>
      </ul>
    <li>Gestión de Tareas</li>
      <ul>
        <li>GET /tareas: Muestre un html de bienvenida</li>
      </ul>
  </ol> 

<a name="requisitos-tec"></a>
### Requisitos técnicos: 
- Usar alguna librería para hashear contraseñas. 
- La persistencia de los datos debe ser en sqlite. 

<a name="tecnologias"></a>
## ✅ Tecnologías utilizadas
- Python 3.13.2
- Flask, requests
- SQLite

<a name="instrucciones"></a>
## 🔧 Instrucciones
1. Ejecutar `servidor.py` para levantar la API
2. Usar `cliente.py` para registrar y loguearse
3. Visualizar `/tareas` en navegador o desde el cliente

<a name="capturas"></a>
## 📸 Capturas

<a name="preguntas"></a>
## ❓ Preguntas conceptuales

### ¿Por qué hashear contraseñas?
Porque almacenar contraseñas en texto plano es un riesgo de seguridad. Hashearlas asegura que incluso si la base es vulnerada, las claves no son legibles.

### Ventajas de usar SQLite
- Es simple y sin necesidad de servidor externo.
- Ideal para proyectos chicos y pruebas locales.
