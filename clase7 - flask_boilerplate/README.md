# BOILERPLATE FLASK

## MODULOS

1.- USUARIOS
2.- ROLES
3.- AUTENTICACION

## MODELOS

```sql
-- Usuarios
- id
- name
- last_name
- username
- password
- email
- rol_id
- status

-- Roles
- id
- name
- status

```

## Caracteristicas

1. Login

- Creacion de Token (JWT - JSON WEB TOKEN | access_token, refresh_token).
- Validacion de contrasenas encriptadas (bcrypt)

2. Registro

- Encriptacion de contrasena (bcrypt)

3. Recuperar contrasena

- Generar una contrasena nueva
- Envio de un correo con un template, mencionando la contrasena generada

4. CRUD para el Modelo

- Listado con paginacion (Obtener datos relacionados)
- Obtener Registros por id (Obtener datos relacionados)
- Creacion de registro
- Eliminacion registro (SOFTDELETE)

5. Decoradores

- Proteger rutas con autenticacion
- Proteger rutas por rol

6. Documentacion y validaciones

- Swagger
- Schemas

7. Despliegue

- Render o algun otro sitio

# Recursos

- ### Conexion URI a PGSQL

```py
postgresql://usuario:password@ip_servidor:puerto/nombre_db
```

## Migraciones

#### 1. Iniciar las migraciones

```sh
flask db init
```

- ###### Solo se ejecuta/inicializa una sola vez,
- ###### si ya hay la carpeta "migrations", quiere decir que ya hay la info "models" de la db respectiva para el ORM

  ###### Nota: En caso, ya existe la carpeta migraciones, porsi las dudas ejecutamos

  ```sh
  flask db stamp head
  ```

- ###### Este comando actualiza la marca de versión de la base de datos a la última versión disponible en el directorio "migrations". En otras palabras, le dice a Alembic (el sistema de migraciones de Flask) que la base de datos ya está actualizada a la última versión.
- ###### Cuando ejecutas este comando, Alembic verifica la versión actual de la base de datos y la compara con la última versión disponible en el directorio "migrations". Si la base de datos ya está actualizada, no hace nada. Si no, actualiza la marca de versión de la base de datos para que coincida con la última versión disponible.

### 2. Crear una migracion

- ###### si ya esta la carpeta de migraciones, ejecutar el comando de flask db migrate para que esas mmigraciones vayan a la base de datos

```sh
flask db migrate -m "comentario"
```

- ###### usos:

  - ###### cuando se crea un "model" nuevo o se modifica alguno
  - ###### es el equivalente a hacer "commit"
### 3. Aplicar el commit que habia en migrations a nuestra DB
```sh
flask db upgrade
```
  - ###### Sube/aplica los cambios que hayamos registrado en "migrations" a nuestra base de datos
