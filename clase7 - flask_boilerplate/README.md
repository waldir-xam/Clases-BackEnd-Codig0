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
