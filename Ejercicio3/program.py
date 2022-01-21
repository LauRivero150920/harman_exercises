# lista
lines = []
# El método open abre el archivo de texto y lo guarda en file
with open('data.txt') as file:
    # El método readlines regresa una lista y cada línea del archivo de texto es un elemento de la lista
    lines = file.readlines()

for x in range(len(lines)):
    # Busca las líneas de texto que no sean saltos de línea
    if(lines[x] != '\n'):
        # Busca si en la cadena existen lso carácteres 'ABC'
        if(lines[x].find('ABC') != -1):
            print(f'X| {lines[x]}')
        else:
            print(f'0| {lines[x]}')
