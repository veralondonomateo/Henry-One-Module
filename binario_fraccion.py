def binario(numero,limite):
    if numero > 1 or numero < 0:
        return None
    elif numero == 0:
        return 0
    
    numero_binario = '0.'
    while numero > 0 and limite > 0:
        numero_binario += str(int(numero * 2))
        numero = numero * 2 - int(numero*2)
        limite -= 1

   
    return numero_binario

for i in range(2,10):
    print(f'Fracción 1/{i} : {1/i}, en binario {binario(1/i,20)}')