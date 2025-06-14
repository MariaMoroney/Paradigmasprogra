import re

with open('quijote.txt', 'r', encoding='utf-8') as archivo:
    lineas = archivo.readlines()
    texto = ''.join(lineas)

resultados = []

busqueda1 = []
for i, linea in enumerate(lineas, 1):
    matches = re.findall(r'CAP[ÍI]TULO\s+[IVXLCDM]+.*', linea, re.IGNORECASE)
    for match in matches:
        busqueda1.append((match.strip(), i))

busqueda2 = []
for i, linea in enumerate(lineas, 1):
    matches = re.findall(r'\b\w+\s+y\s+\w+\b', linea, re.IGNORECASE)
    for match in matches:
        busqueda2.append((match, i))

busqueda3 = []
for i, linea in enumerate(lineas, 1):
    matches = re.findall(r'\b\w*pr[aeiou]d\w*\b', linea, re.IGNORECASE)
    for match in matches:
        busqueda3.append((match, i))

busqueda4_todas = re.findall(r'\bcr[aeiou]\w*\b', texto, re.IGNORECASE)
busqueda4_distintas = list(set([palabra.lower() for palabra in busqueda4_todas]))

busqueda5 = []
for i, linea in enumerate(lineas, 1):
    matches = re.findall(r'\b\w*ch[aeiou]\b', linea, re.IGNORECASE)
    for match in matches:
        busqueda5.append((match, i))

with open('busqueda-quijote.txt', 'w', encoding='utf-8') as salida:
    salida.write('RESULTADOS DE BUSQUEDA EN EL QUIJOTE\n')
    salida.write('='*45 + '\n\n')
    
    salida.write('Requerimiento 1:\n')
    salida.write('cabeceras de capitulo\n')
    salida.write('Expresion regular: CAP[ÍI]TULO\\s+[IVXLCDM]+.*\n')
    salida.write(f'Cantidad: {len(busqueda1)}\n')
    for capitulo, linea in busqueda1[:10]:
        salida.write(f'Linea {linea}: {capitulo}\n')
    salida.write('-'*30 + '\n\n')
    
    salida.write('Requerimiento 2:\n')
    salida.write('uso de "y" para enumerar\n')
    salida.write('Expresion regular: \\b\\w+\\s+y\\s+\\w+\\b\n')
    salida.write(f'Cantidad: {len(busqueda2)}\n')
    for frase, linea in busqueda2[:10]:
        salida.write(f'Linea {linea}: {frase}\n')
    salida.write('-'*30 + '\n\n')
    
    salida.write('Requerimiento 3:\n')
    salida.write('silabas pra-pre-pri-pro-pru seguidas de d\n')
    salida.write('Expresion regular: \\b\\w*pr[aeiou]d\\w*\\b\n')
    salida.write(f'Cantidad: {len(busqueda3)}\n')
    for palabra, linea in busqueda3[:10]:
        salida.write(f'Linea {linea}: {palabra}\n')
    salida.write('-'*30 + '\n\n')
    
    salida.write('Requerimiento 4:\n')
    salida.write('palabras distintas que empiezan con cra-cre-cri-cro-cru\n')
    salida.write('Expresion regular: \\bcr[aeiou]\\w*\\b\n')
    salida.write(f'Palabras distintas: {len(busqueda4_distintas)}\n')
    salida.write(f'Total ocurrencias: {len(busqueda4_todas)}\n')
    for palabra in sorted(busqueda4_distintas)[:15]:
        salida.write(f'{palabra}, ')
    salida.write('\n')
    salida.write('-'*30 + '\n\n')
    
    salida.write('Requerimiento 5:\n')
    salida.write('palabras que terminan en cho-cha-che-chi-chu\n')
    salida.write('Expresion regular: \\b\\w*ch[aeiou]\\b\n')
    salida.write(f'Cantidad: {len(busqueda5)}\n')
    for palabra, linea in busqueda5[:10]:
        salida.write(f'Linea {linea}: {palabra}\n')

print('Archivo busqueda-quijote.txt creado')