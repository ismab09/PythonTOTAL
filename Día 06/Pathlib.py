from pathlib import Path, PureWindowsPath

# no se usa ni el open ni el close

carpeta = Path('/Día 06/prueba.txt')

print(carpeta.read_text()) #seria como un read

print(carpeta.name) # te da el nombre del archivo y va sin()

#al ser funciones no van con ()

print(carpeta.suffix) # te da la terminación

print(carpeta.stem) # nombre sin la terminación

windows = PureWindowsPath(carpeta)
print(windows)

if not carpeta.exists():
    print('Este archivo no existe')
else:
    print('Existe')