import os
import shutil
import send2trash


#print(os.walk('C:\\Users\\Isma\\OneDrive\\Programación\\Python\\Día 09'))

ruta = 'C:\\Users\\Isma\\OneDrive\\Programación\\Python\\Día 09'

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'En la carpeta: {carpeta}')
    print('Las subcarpetas son:')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('Los archivos son:')
    for arch in archivo:
        print(f'\t{arch}')
    print('\n')



#send2trash.send2trash('curso.txt') Lo mueve a la papelera y se puede revertir con facilidad
#os.unlink()  Elimina un archivo de una carpeta indicada
#os.rmdir()  Elimina una carpeta vacía
#shutil.rmtree() Borra todo lo q seleccionas dentro y es irreversible, recomendable no utiliziar


#shutil.move('curso.txt','C:\\Users\\Isma\\OneDrive\\Programación\\Python')

#print(os.getcwd())

#archivo = open('curso.txt','w')
#archivo.write('Prueba')
#archivo.close()

#print(os.listdir())
