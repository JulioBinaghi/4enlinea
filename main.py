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
        


secuencia= [1,2,3,4]

DibujarTablero(
    CompletarTableroenOrden(
        secuencia,
        TableroVacio()
        )
    )   
