<a name="ir-arriba"></a>
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
    <li><a href="#desarrollado">Desarrollado por...</a>
    <li><a href="#contacto">Contacto</a>
  </ol>

<!-- OBJETIVO -->
<a name="objetivo"></a>
## ✏ Objetivo 
Al finalizar este trabajo práctico, serás capaz de: 
- Implementar una API REST con endpoints funcionales. 
- Utilizar autenticación básica con protección de contraseñas. 
- Gestionar datos persistentes con SQLite. 
- Construir un cliente en consola que interactúe con la API. 
<p align="right">(<a href="#ir-arriba">Ir arriba</a>)</p>

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
<p align="right">(<a href="#ir-arriba">Ir arriba</a>)</p>

<a name="requisitos-tec"></a>
### Requisitos técnicos: 
- Usar alguna librería para hashear contraseñas. 
- La persistencia de los datos debe ser en sqlite. 
<p align="right">(<a href="#ir-arriba">Ir arriba</a>)</p>

<!-- TECNOLOGÍAS UTILIZADAS -->
<a name="tecnologias"></a>
## ✅ Tecnologías utilizadas
- Python 3.13.2
- Flask, requests
- SQLite
<p align="right">(<a href="#ir-arriba">Ir arriba</a>)</p>

<!-- INSTRUCCIONES -->
<a name="instrucciones"></a>
## 🔧 Instrucciones
1. Ejecutar `servidor.py` para levantar la API
2. Usar `cliente.py` para registrar y loguearse
3. Visualizar `/tareas` en navegador o desde el cliente
<p align="right">(<a href="#ir-arriba">Ir arriba</a>)</p>

<!-- CAPTURAS -->
<a name="capturas"></a>
## 📸 Capturas

<img src="https://raw.githubusercontent.com/JoanaColl/TSDS-Redes-PFO2/refs/heads/main/capturas/01_servidor.png" width="700px" align="center">
<img src="https://raw.githubusercontent.com/JoanaColl/TSDS-Redes-PFO2/refs/heads/main/capturas/02_menu.png" width="400px" align="center">
<img src="https://raw.githubusercontent.com/JoanaColl/TSDS-Redes-PFO2/refs/heads/main/capturas/03_registro.png" width="400px" align="center">
<img src="https://raw.githubusercontent.com/JoanaColl/TSDS-Redes-PFO2/refs/heads/main/capturas/04_logOK.png" width="300px" align="center">
<img src="https://raw.githubusercontent.com/JoanaColl/TSDS-Redes-PFO2/refs/heads/main/capturas/05_logKO.png" width="300px" align="center">
<img src="https://raw.githubusercontent.com/JoanaColl/TSDS-Redes-PFO2/refs/heads/main/capturas/06_tareas.png" width="500px" align="center">
<img src="https://raw.githubusercontent.com/JoanaColl/TSDS-Redes-PFO2/refs/heads/main/capturas/07_salir.png" width="260px" align="center">
<img src="https://raw.githubusercontent.com/JoanaColl/TSDS-Redes-PFO2/refs/heads/main/capturas/08_web.png" width="600px" align="center">
<p align="right">(<a href="#ir-arriba">Ir arriba</a>)</p>

<!-- PREGUNTAS CONCEPTUALES -->
<a name="preguntas"></a>
## ❓ Preguntas conceptuales

### ¿Por qué hashear contraseñas?
Porque almacenar contraseñas en texto plano es un riesgo de seguridad. Hashearlas asegura que incluso si la base es vulnerada, las claves no son legibles.

### Ventajas de usar SQLite
- Es simple y sin necesidad de servidor externo.
- Ideal para proyectos chicos y pruebas locales.
<p align="right">(<a href="#ir-arriba">Ir arriba</a>)</p>

<!-- DESARROLLADO POR -->
  <a name="desarrollado"></a>
  ## 💁 Desarrollado por...
  * **Joana Coll** - [joana-coll](https://github.com/joana-coll)
  
  <p align="right">(<a href="#ir-arriba">Ir arriba</a>)</p>

<!-- CONTACTO -->
  <a name="contacto"></a>
  ## 📩 Contacto
  Si deseas contactarte conmigo:
  <a href="https://ar.linkedin.com/in/joana-coll" target="_blank">
  <img src="https://raw.githubusercontent.com/joana-coll/joana-coll/1ce466f12c925e1e39ab93b44ff985f102c9aed8/icons/linkedin.svg" alt="Github" height="30" />
  </a>
  <a href="mailto:colljoana@gmail.com" target="_blank">
  <img src="https://raw.githubusercontent.com/joana-coll/joana-coll/1ce466f12c925e1e39ab93b44ff985f102c9aed8/icons/envelope-solid.svg" alt="Github" height="30" />
  </a>
  <p align="right">(<a href="#ir-arriba">Ir arriba</a>)</p>
