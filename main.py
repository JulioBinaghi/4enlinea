def TableroVacio():
    return[
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            ]

def CompletarTableroenOrden(secuencia, tablero):
    x = 1
    for element in secuencia:
        SoltarFichaenColumna(x, element, tablero)
        if x == 1:
            x = 2                               
        elif x == 2:
            x = 1
    return tablero

def SoltarFichaenColumna(ficha,columna,tablero):
    for fila in range(6, 0, -1):
        if tablero[fila - 1][columna - 1] == 0: 
           tablero[fila - 1][columna - 1] = ficha 
           return

def RevisarSecuencia(secuencia):
    for element in secuencia:
        if element > 7 or element < 1:
            return False
    return True

def contenidoColumna(nro_columna,tablero):
    columna = []
    for element in tablero:
        celda = element[nro_columna - 1]
        columna.append(celda)     
    return columna 

def todasColumnas(tablero):
    for x in range (0, 7):
        columna = []
        columna = contenidoColumna(x, tablero)
        print(columna)
    return

def todasFilas(tablero):
    for element in tablero:
        print(element)

def dibujarTablero(tablero):
    print(f' +-- -- -- -- -- -- -- --+', end='')
    print('')
    for fila in tablero:
        print(f' | ', end='')
        for celda in fila:
            if celda == 0:
                print(f' 0 ', end='')
            else:
                if celda == 1:
                    print(f' %s ' %celda, end='')
                else:
                    print(f' %s ' %celda, end='')
        print(f' | ', end='')
        print('')
    print(f' +-----------------------+ ', end='')
    print('')        

secuencia= [ 1, 2, 3, 4, 5]

tablero = [] 
if RevisarSecuencia(secuencia):
    tablero = CompletarTableroenOrden(secuencia,TableroVacio())
    dibujarTablero(tablero)
  
else: print("El tablero no existe")    

"""print(contenidoColumna( 2, tablero))"""   
"""print(todasColumnas(tablero))"""
"""print(todasFilas(tablero))"""
