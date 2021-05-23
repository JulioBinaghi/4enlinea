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
       
def DibujarTablero(tablero):
    for element in tablero: 
        print(element)

def RevisarSecuencia(secuencia):
    for element in secuencia:
        if element > 7 or element < 1:
            return False
    return True

    

secuencia= [1,2,3,4,16]

if RevisarSecuencia(secuencia):
    DibujarTablero(
        CompletarTableroenOrden(secuencia,TableroVacio()
         )
    )   
else: print ("El tablero no existe")    
