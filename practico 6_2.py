# Práctica Path 1
# Almacena en la variable ruta_base, un objeto Path que señale el directorio base del usuario.

# Recuerda importar Path del módulo pathlib, y utilizar el método home()
from pathlib import Path

ruta_base = Path.home()

#Práctica Path 2
# Implementa y crea una ruta relativa que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:

# "Curso Python"
# "Día 6"
# "practicas_path.py"
# Almacena el directorio obtenido en la variable ruta. No olvides importar Path
#from pathlib import Path

ruta_base = Path.home() / "Curso Python" / "Dia 6"

ruta = ruta_base / "practicas_path.py"

# Práctica Path 3
# Implementa y crea una ruta absoluta que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:


# Almacena el directorio obtenido en la variable ruta. No olvides importar Path, y de concatenar el objeto Path que refiere a la carpeta base del usuario

from pathlib import Path

ruta_base = Path.home()

ruta = ruta_base / "Curso Python" / "Dia 6" / "practicas_path.py"