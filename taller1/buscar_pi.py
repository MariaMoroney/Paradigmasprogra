import re

with open('Pi125MDP.txt', 'r') as archivo:
    pi_texto = archivo.read().strip()

resultados = []

busqueda1 = re.findall(r'1415', pi_texto)
resultados.append(('1', 'todas las ocurrencias de la secuencia 1415', '1415', len(busqueda1)))

busqueda2 = re.findall(r'1415[13579]', pi_texto)
resultados.append(('2', 'secuencia 1415 seguida de un dígito impar', '1415[13579]', len(busqueda2)))

busqueda3 = re.findall(r'[02468]{3}', pi_texto)
resultados.append(('3', '3 dígitos pares seguidos', '[02468]{3}', len(busqueda3)))

busqueda4 = re.findall(r'[02468]{3}9', pi_texto)
resultados.append(('4', '3 dígitos pares seguidos de un 9', '[02468]{3}9', len(busqueda4)))

busqueda5 = re.findall(r'[02468]{3}[13579]', pi_texto)
resultados.append(('5', '3 dígitos pares seguidos de un dígito impar', '[02468]{3}[13579]', len(busqueda5)))

busqueda6 = re.findall(r'[02468]{3}[09]', pi_texto)
resultados.append(('6', '3 dígitos pares seguidos de 0 o 9', '[02468]{3}[09]', len(busqueda6)))

busqueda7 = re.findall(r'[02468]{2}([13579]{1}|[13579]{3})?', pi_texto)
resultados.append(('7', '2 dígitos pares seguidos que pueden venir seguidos de 1 o 3 dígitos impares', '[02468]{2}([13579]{1}|[13579]{3})?', len(busqueda7)))

busqueda8 = re.findall(r'[13579]{2}0', pi_texto)
resultados.append(('8', '2 dígitos impares seguidos de un 0', '[13579]{2}0', len(busqueda8)))

busqueda9 = re.findall(r'[13579][02468]{2,}', pi_texto)
resultados.append(('9', '1 dígito impar seguido de al menos 2 dígitos pares', '[13579][02468]{2,}', len(busqueda9)))

busqueda10 = re.findall(r'11[13579]', pi_texto)
resultados.append(('10', 'ocurrencias de 111,113,115,117 o 119', '11[13579]', len(busqueda10)))

busqueda11 = re.findall(r'11[13579][02468]', pi_texto)
resultados.append(('11', '111,113,115,117 o 119 seguidos de un dígito par', '11[13579][02468]', len(busqueda11)))

with open('busqueda-pi.txt', 'w') as salida:
    salida.write('RESULTADOS DE BUSQUEDA EN PI\n')
    salida.write('='*40 + '\n\n')
    
    for num, descripcion, regex, cantidad in resultados:
        salida.write(f'Requerimiento {num}:\n')
        salida.write(f'{descripcion}\n')
        salida.write(f'Expresion regular: {regex}\n')
        salida.write(f'Cantidad de resultados: {cantidad}\n')
        salida.write('-'*30 + '\n\n')

print('Archivo busqueda-pi.txt creado')