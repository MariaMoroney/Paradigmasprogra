import sys
from lexer import tokenize
from parser import parse

def main():
    if len(sys.argv) != 3:
        print('Formato: python main.py <archivo_entrada> <archivo_salida>')
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    try:
        with open(input_file, 'r') as infile:
            lines = infile.readlines()
        
        with open(output_file, 'w') as outfile:
            outfile.write('Analizador Little English\n')
            outfile.write('Archivo de entrada: ' + input_file + '\n')
            outfile.write('Archivo de salida: ' + output_file + '\n')
            outfile.write('========================\n\n')
            
            for i, line in enumerate(lines):
                line = line.strip()
                if not line:
                    continue
                
                outfile.write(f'Linea {i+1}: {line}\n')
                
                try:
                    tokens = tokenize(line)
                    outfile.write('Analisis lexico: EXITOSO\n')
                    
                    try:
                        parse(tokens)
                        outfile.write('Analisis sintactico: EXITOSO\n')
                    except RuntimeError as e:
                        outfile.write(f'Analisis sintactico: FALLO - {str(e)}\n')
                        
                except RuntimeError as e:
                    outfile.write(f'Analisis lexico: FALLO - {str(e)}\n')
                    outfile.write('Analisis sintactico: NO EJECUTADO\n')
                
                outfile.write('\n')
        
        print(f'Procesamiento completo. Ver {output_file}')
        
    except IOError:
        print(f'No se puede leer {input_file}')
        sys.exit(1)

if __name__ == '__main__':
    main()