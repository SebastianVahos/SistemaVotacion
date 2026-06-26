# Sistema de Votación API

API RESTful desarrollada con **Python**, **FastAPI**, **SQLAlchemy** y **PostgreSQL** para gestionar un sistema de votaciones.

## Descripción

Esta API permite:

* Registrar votantes.
* Registrar candidatos.
* Emitir votos.
* Consultar estadísticas de la votación.
* Garantizar que cada votante solo pueda votar una vez.
* Impedir que un votante sea candidato y viceversa.

---

## Tecnologías utilizadas

| Tecnología              | Función                                                                                                           |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Python 3.12**         | Lenguaje de programación utilizado para el desarrollo de la API.                                                  |
| **FastAPI**             | Framework para el desarrollo de APIs RESTful de alto rendimiento.                                                 |
| **SQLAlchemy**          | ORM utilizado para interactuar con la base de datos PostgreSQL mediante modelos de Python.                        |
| **PostgreSQL**          | Sistema de gestión de bases de datos relacional donde se almacena la información de votantes, candidatos y votos. |
| **pgAdmin 4**           | Herramienta gráfica utilizada para la administración y consulta de la base de datos PostgreSQL.                   |
| **Pydantic**            | Biblioteca utilizada para la validación de datos de entrada y salida mediante Schemas.                            |
| **EmailStr (Pydantic)** | Validación del formato de los correos electrónicos recibidos por la API.                                          |
| **Uvicorn**             | Servidor ASGI encargado de ejecutar la aplicación FastAPI.                                                        |
| **python-dotenv**       | Carga las variables de entorno definidas en el archivo `.env`.                                                    |
| **psycopg2-binary**     | Driver que permite la conexión entre Python y PostgreSQL.                                                         |
| **Swagger UI**          | Documentación interactiva generada automáticamente por FastAPI para probar los endpoints.                         |
| **Git**                 | Sistema de control de versiones utilizado durante el desarrollo del proyecto.                                     |
| **GitHub**              | Plataforma utilizada para alojar el repositorio público del proyecto.                                             |

### Arquitectura implementada

El proyecto sigue una arquitectura por capas para separar responsabilidades y facilitar el mantenimiento del código:

* **Controllers:** Definen los endpoints de la API y reciben las peticiones HTTP.
* **Services:** Contienen la lógica de negocio y las validaciones del sistema.
* **Repositories:** Se encargan del acceso y manipulación de los datos en la base de datos.
* **Models:** Representan las tablas de la base de datos mediante SQLAlchemy.
* **Schemas:** Definen y validan la estructura de los datos enviados y recibidos por la API utilizando Pydantic.

### Validaciones implementadas

* Validación de formato de correo electrónico mediante **EmailStr**.
* Validación de unicidad del correo para votantes y candidatos.
* Validación para impedir que un votante sea registrado como candidato y viceversa.
* Validación para garantizar que un votante solo pueda emitir un voto.
* Validación de existencia del votante antes de registrar un voto.
* Validación de existencia del candidato antes de registrar un voto.
* Manejo de excepciones mediante **HTTPException** con códigos de estado HTTP apropiados (`404`, `409`, `201` y `200`).

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/SebastianVahos/SistemaVotacion.git
```

Entrar al proyecto

```bash
cd SistemaVotacionAPI
```

---

### 2. Crear el entorno virtual

Windows

```bash
python -m venv venv
```

Activar

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Configuración

Crear un archivo **.env** con la siguiente información:

```env
DATABASE_URL=postgresql://USUARIO:CONTRASEÑA@localhost:5432/PruebaTecnicaNewInntech
```

Reemplazar:

* USUARIO
* CONTRASEÑA
* Nombre de la base de datos

por los valores correspondientes de PostgreSQL.

---

## Base de datos

Crear la base de datos en PostgreSQL y ejecutar el script SQL suministrado para crear:

* Tablas
* Restricciones
* Triggers

El proyecto utiliza los siguientes triggers:

* Evitar que un votante sea candidato.
* Evitar que un candidato sea votante.
* Incrementar automáticamente los votos de un candidato al registrar un voto.

---

## Ejecutar el proyecto

Desde la raíz del proyecto ejecutar:

```bash
uvicorn app.main:app --reload
```

La API estará disponible en:

```
http://127.0.0.1:8000
```

---

## Documentación Swagger

```
http://127.0.0.1:8000/docs
```

---

## Endpoints

### Votantes

| Método | Endpoint     | Descripción                |
| ------ | ------------ | -------------------------- |
| POST   | /voters      | Registrar un votante       |
| GET    | /voters      | Obtener todos los votantes |
| GET    | /voters/{id} | Obtener un votante por ID  |
| DELETE | /voters/{id} | Eliminar un votante        |

---

### Candidatos

| Método | Endpoint         | Descripción                  |
| ------ | ---------------- | ---------------------------- |
| POST   | /candidates      | Registrar un candidato       |
| GET    | /candidates      | Obtener todos los candidatos |
| GET    | /candidates/{id} | Obtener un candidato por ID  |
| DELETE | /candidates/{id} | Eliminar un candidato        |

---

### Votos

| Método | Endpoint          | Descripción                         |
| ------ | ----------------- | ----------------------------------- |
| POST   | /votes            | Registrar un voto                   |
| GET    | /votes            | Obtener todos los votos             |
| GET    | /votes/statistics | Obtener estadísticas de la votación |

---

## Validaciones implementadas

* No se permiten correos duplicados entre votantes.
* No se permiten correos duplicados entre candidatos.
* Un votante no puede registrarse como candidato.
* Un candidato no puede registrarse como votante.
* Un votante solo puede votar una vez.
* Se valida que el candidato exista antes de votar.
* Se valida que el votante exista antes de votar.
* Se actualiza automáticamente el campo `has_voted`.
* El número de votos del candidato se incrementa automáticamente mediante un trigger de PostgreSQL.

---

## Ejemplo de creación de un votante

**POST /voters**

```json
{
    "name": "Juan Pérez",
    "email": "juan@gmail.com"
}
```

---

## Ejemplo de creación de un candidato

**POST /candidates**

```json
{
    "name": "María Gómez",
    "party": "Partido Verde",
    "email": "maria@gmail.com"
}
```

---

## Ejemplo de emisión de un voto

**POST /votes**

```json
{
    "voter_id": 1,
    "candidate_id": 1
}
```

---

## Ejemplo de estadísticas

```json
{
    "total_votes": 5,
    "total_voters_voted": 5,
    "statistics": [
        {
            "candidate_id": 1,
            "candidate_name": "María Gómez",
            "votes": 3,
            "percentage": 60.0
        },
        {
            "candidate_id": 2,
            "candidate_name": "Carlos Pérez",
            "votes": 2,
            "percentage": 40.0
        }
    ]
}
```

---

## Autor

Desarrollado como solución a una prueba técnica para Desarrollador de Software utilizando Python, FastAPI y PostgreSQL.
