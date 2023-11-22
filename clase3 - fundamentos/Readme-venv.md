# Entornos virtuales

1. Crear el entorno

```py
python -m venv nombre_entorno
```

2. Activar el entorno

```py
source venv/Scripts/activate
```

3.  Desactivar el entorno

```py
deactivate
```

# Gestionar librearias instaladas

- Listar librerias instalas

```py
pip install nombre_libreria

-- Version
pip install nombre_libreria=1.00
```
- Guardar librerias instalatas (requeriments.txt)
```py
pip freeze>requeriments.exe
```
- Instalar todo lo del requirements.txt

```py
pip install -m requeriments.txt
```

- Desinstalar librerias

```py
pip uninstall nombre_libreria
```