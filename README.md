## Proyecto 2 ADA II

### Integrantes:

- Juan Esteban López Aránzazu - 202313026

### Descripción:

Diseñar un modelo que permita ubicar los nuevos programas de ingeniería de sistemas, de tal forma se maximice el segmento de población y el entorno empresarial que se cubre, cumpliendo las restricciones

- Los nuevos programas no pueden ser contiguos a ninguno de los establecidos
- El segmento de población se toma sumando en el punto que va estar el nuevo programa y sumando los contiguos, este no puede ser menor que 25
- El entorno empresarial se toma sumando en el punto que va estar el nuevo programa y
sumando los contiguos de la zona y no puede ser menos a 20

### Entorno virtual e instalar dependencias

Para instalar las dependencias especificadas en `requirements.txt`, abre una terminal y navega hasta el directorio del proyecto. Luego, ejecuta el siguiente comando:

Para el entorno virtual en linux
```bash
python3 -m venv venv
source venv/bin/activate # Para activar el entorno virtual
deactivate # Para desactivar el entorno virtual
```

Para el entorno virtual en windows
```bash
python -m venv venv
.\venv\Scripts\activate # Para activar el entorno virtual
.\venv\Scripts\deactivate # Para desactivar el entorno virtual
```

Para instalar dependencias
```bash
pip install -r requirements.txt
```

### Ejecución del programa

Para correr el programa puedes ejecutar el siguiente comando:
```bash
python main.py
```
