from pathlib import Path


base = Path.home()
guia = Path(base,'Europa','Real Madrid',Path('Campeon','Safa.txt'))#puede ir sin base
guia2 = guia.with_name('Bernabeu.txt')
print(base)
print(guia.parent.parent.parent)
print(guia2)


guia3 = Path(Path.home(),'Europa')

for txt in Path(guia3).glob('**/*.txt'):#con un solo * se fija en la primera carpeta, de esta manera tmb se fija en las subcarpetas
    print(txt)
    #no funciona porque no tengo los archivos




# si ponemos .relative_to(Path'nombre de carpeta' elegimos a partir de donde nos tiene q mostrar