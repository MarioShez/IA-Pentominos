import problema_espacio_estados as probee
import copy

class poner_Figura_IH(probee.Acción):
    
    #Este método define los parámetros de entrada de la clase, que en este caso serán, filas y columnas.
    def __init__(self, f, c):
        nombre = 'Pongo la figura I horizontal en la posición: ({},{})'.format(f,c)
        super().__init__(nombre)#este será el init de la clase heredada
        self.fila=f
        self.columna=c
    
    #Este método comprueba que los huecos que va a ocupar la figura están vacíos
    #Inicializo la matriz con estado[0], que es la matriz a tratar.
    #Inicializo el resultado a True
    #Recorro las 5 primeras columnas desde el píxel que tomo como referencia
    #Voy metiendo en cont el valor de la fila f y las 5 primeras columnas
    #Si lo que contiene cont es distinto de vacío, el resultado es False
    #Devuelvo todos los res. Todos los res deben ser True para que la figura se pueda poner
    def esta_vacio_puntos(self, estado, f, c): 
        matriz = estado[0]                     
        res = [True]                           
        for i in range(c,c+5):                  
            cont = matriz[f][i]                
            if (cont != ''):                   
                res.append(False)              
                break

        return all(res)                        
    
    #Este método comprueba los límites de la figura
    #Inicializo la matriz con estado[0], que es la matriz a tratar.
    #Una fila y 5 columnas deben ser <= que el tamaño de filas/columnas.
    #Si se cumple, devuelvo True, si no, devuelvo False
    def limites(self, estado, f, c):                            
        matriz = estado[0]                                        
        if f <= matriz.shape[0]-1 and(c+4) <= matriz.shape[1]-1:
            return True                                         
        else:                                                   
            return False                                         
        
    #Este método comprueba que es aplicable la figura. Además se establece una restricción para poner un número máximo de esta figura.
    def es_aplicable(self, estado):           
        return self.limites(estado, self.fila, self.columna) and self.esta_vacio_puntos(estado, self.fila, self.columna and estado[2]>0)
    
    #Este método realiza la acción de poner la figura en el tablero.
    #Creo una nueva matriz.
    #Recorro las 5 primeras columnas desde el píxel que tomo como referencia.
    #En esas 5 posiciones introduzco la letra I.
    #Decremento 5 al número de huecos libres que quedan en el tablero.
    #Deremento 1 al número de letras I que puedo usar.
    #Devuelvo el tablero actualizado con la letra I.
    def poner_figura(self, estado, fil, col):
        nuevaMatriz = estado[0]        
        for i in range(col, col+5):     
            nuevaMatriz[fil][i] = 'I'  
        estado[1] -= 5                 
        estado[2] -= 1                 
        return estado                  
    
    #Este método aplica la acción de poner la figura I.
    #Hago una copia del tablero.
    #Pongo la figura.
    #Devuelvo el tablero actualizado.
    def aplicar(self,estado):
        nuevo_estado = copy.deepcopy(estado)                     
        self.poner_figura(nuevo_estado, self.fila, self.columna) 
        return nuevo_estado                                      
    
class poner_Figura_L(probee.Acción):
    
    #Este método define los parámetros de entrada de la clase, que en este caso serán, filas y columnas.
    def __init__(self, f, c):
        nombre = 'Pongo la figura L en la posición: ({},{})'.format(f,c)
        super().__init__(nombre)#este será el init de la clase heredada
        self.fila=f
        self.columna=c
    
    #Este método comprueba que los huecos que va a ocupar la figura están vacíos
    #Inicializo la matriz con estado[0], que es la matriz a tratar.
    #Inicializo el resultado a True
    #Si alguna posición que va a ocupar la figura es distinto de vacío, el resultado es False
    #Devuelvo todos los res. Todos los res deben ser True para que la figura se pueda poner
    def esta_vacio_puntos(self, estado, f, c):
        matriz = estado[0]
        res = [True]
        
        if (matriz[f][c] != ''):
            res.append(False)
        elif (matriz[f+1][c] != ''):
            res.append(False)
        elif (matriz[f+2][c] != ''):
            res.append(False)
        elif (matriz[f+3][c] != ''):
            res.append(False)
        elif (matriz[f+3][c+1] != ''):
            res.append(False)
           
        return all(res)
    
    #Este método comprueba los límites de la figura
    #Inicializo la matriz con estado[0], que es la matriz a tratar.
    #4 filas y 2 columnas deben ser <= que el tamaño de filas/columnas.
    #Si se cumple, devuelvo True, si no, devuelvo False
    def limites(self, estado, f, c):
        matriz = estado[0]
        if (f + 3) <= matriz.shape[0]-1 and c <= matriz.shape[1]-2:
            return True
        else:
            return False
    
    #Este método comprueba que es aplicable la figura.
    def es_aplicable(self, estado):
        return self.limites(estado, self.fila, self.columna) and self.esta_vacio_puntos(estado, self.fila, self.columna)
    
    #Este método realiza la acción de poner la figura en el tablero.
    #Creo una nueva matriz.
    #Recorro las 4 primeras filas desde el píxel que tomo como referencia.
    #En esas 4 posiciones introduzco la letra L.
    #En la fila 4 y la columna 2 introduzco la letra L.
    #Decremento 5 al número de huecos libres que quedan en el tablero.
    #Devuelvo el tablero actualizado con la letra L.
    def poner_figura(self, estado, fil, col):
        nuevaMatriz = estado[0]
        for i in range(fil, fil+4):
            nuevaMatriz[i][col] = 'L'
        nuevaMatriz[fil+3][col+1] = 'L'
        estado[1] -= 5
        return estado
    
    #Este método aplica la acción de poner la figura L.
    #Hago una copia del tablero.
    #Pongo la figura.
    #Devuelvo el tablero actualizado.
    def aplicar(self,estado):
        nuevo_estado = copy.deepcopy(estado)
        self.poner_figura(nuevo_estado, self.fila, self.columna)
        return nuevo_estado


class poner_Figura_N(probee.Acción):
    
    #Este método define los parámetros de entrada de la clase, que en este caso serán, filas y columnas.
    def __init__(self, f, c):
        nombre = 'Pongo la figura N en la posición: ({},{})'.format(f,c)
        super().__init__(nombre)#este será el init de la clase heredada
        self.fila=f
        self.columna=c
    
    
    #Este método comprueba que los huecos que va a ocupar la figura están vacíos
    #Inicializo la matriz con estado[0], que es la matriz a tratar.
    #Inicializo el resultado a True
    #Si alguna posición que va a ocupar la figura es distinto de vacío, el resultado es False
    #Devuelvo todos los res. Todos los res deben ser True para que la figura se pueda poner
    def esta_vacio_puntos(self, estado, f, c):
        matriz = estado[0]
        res = [True]

        if (matriz[f][c] != ''):
            res.append(False)
        elif (matriz[f+1][c] != ''):
            res.append(False)
        elif (matriz[f+1][c-1] != ''):
            res.append(False)
        elif (matriz[f+2][c-1] != ''):
            res.append(False)
        elif (matriz[f+3][c-1] != ''):
            res.append(False)
                
        return all(res)
    
    #Este método comprueba los límites de la figura
    #Inicializo la matriz con estado[0], que es la matriz a tratar.
    #4 filas deben ser <= que el tamaño de filas y la columna debe ser > 0.
    #Si se cumple, devuelvo True, si no, devuelvo False
    def limites(self, estado, f, c):
        matriz = estado[0]
        if (f + 3) <= matriz.shape[0]-1 and c > 0:
            return True
        else:
            return False
    
    #Este método comprueba que es aplicable la figura.
    def es_aplicable(self, estado):
        return self.limites(estado, self.fila, self.columna) and self.esta_vacio_puntos(estado, self.fila, self.columna)
    
    #Este método realiza la acción de poner la figura en el tablero.
    #Creo una nueva matriz.
    #Recorro las 2 primeras filas desde el píxel que tomo como referencia.
    #En esas 2 posiciones introduzco la letra N.
    #En la fila 2 y la columna -1 introduzco la letra N.
    #En la fila 3 y la columna -1 introduzco la letra N.
    #En la fila 4 y la columna -1 introduzco la letra N.
    #Decremento 5 al número de huecos libres que quedan en el tablero.
    #Devuelvo el tablero actualizado con la letra N.
    def poner_figura(self, estado, fil, col):
        nuevaMatriz = estado[0]
        for i in range(fil, fil+2):
            nuevaMatriz[i][col] = 'N'
        nuevaMatriz[fil+1][col-1] = 'N'
        nuevaMatriz[fil+2][col-1] = 'N'
        nuevaMatriz[fil+3][col-1] = 'N'
        estado[1] -= 5
        return estado
    
    #Este método aplica la acción de poner la figura N.
    #Hago una copia del tablero.
    #Pongo la figura.
    #Devuelvo el tablero actualizado.
    def aplicar(self,estado):
        nuevo_estado = copy.deepcopy(estado)
        self.poner_figura(nuevo_estado, self.fila, self.columna)
        return nuevo_estado
    
    
class poner_Figura_P(probee.Acción):
    
    #Este método define los parámetros de entrada de la clase, que en este caso serán, filas y columnas.
    def __init__(self, f, c):
        nombre = 'Pongo la figura P en la posición: ({},{})'.format(f,c)
        super().__init__(nombre)#este será el init de la clase heredada
        self.fila=f
        self.columna=c
    
    #Este método comprueba que los huecos que va a ocupar la figura están vacíos
    #Inicializo la matriz con estado[0], que es la matriz a tratar.
    #Inicializo el resultado a True
    #Si alguna posición que va a ocupar la figura es distinto de vacío, el resultado es False
    #Devuelvo todos los res. Todos los res deben ser True para que la figura se pueda poner
    def esta_vacio_puntos(self, estado, f, c):
        matriz = estado[0]
        res = [True]
        
        if (matriz[f][c] != ''):
                res.append(False)
        elif (matriz[f+1][c] != ''):
                res.append(False)
        elif (matriz[f+2][c] != ''):
                res.append(False)
        elif (matriz[f+1][c-1] != ''):
                res.append(False)
        elif (matriz[f+2][c-1] != ''):
                res.append(False)
        
        return all(res)
    
    #Este método comprueba los límites de la figura
    #Inicializo la matriz con estado[0], que es la matriz a tratar.
    #3 filas deben ser <= que el tamaño de filas y la columna debe ser > 0.
    #Si se cumple, devuelvo True, si no, devuelvo False
    def limites(self, estado, f, c):
        matriz = estado[0]
        if (f + 2) <= matriz.shape[0]-1 and c > 0:
            return True
        else:
            return False
    
    #Este método comprueba que es aplicable la figura.
    def es_aplicable(self, estado):
        return self.limites(estado, self.fila, self.columna) and self.esta_vacio_puntos(estado, self.fila, self.columna)
    
    #Este método realiza la acción de poner la figura en el tablero.
    #Creo una nueva matriz.
    #Recorro las 3 primeras filas desde el píxel que tomo como referencia.
    #En esas 3 posiciones introduzco la letra P.
    #En la fila 2 y la columna -1 introduzco la letra P.
    #En la fila 3 y la columna -1 introduzco la letra P.
    #Decremento 5 al número de huecos libres que quedan en el tablero.
    #Devuelvo el tablero actualizado con la letra P.
    def poner_figura(self, estado, fil, col):
        nuevaMatriz = estado[0]
        for i in range(fil, fil+3):
            nuevaMatriz[i][col] = 'P'
        nuevaMatriz[fil+1][col-1] = 'P'
        nuevaMatriz[fil+2][col-1] = 'P'
        estado[1] -= 5
        return estado
    
    #Este método aplica la acción de poner la figura P.
    #Hago una copia del tablero.
    #Pongo la figura.
    #Devuelvo el tablero actualizado.
    def aplicar(self,estado):
        nuevo_estado = copy.deepcopy(estado)
        self.poner_figura(nuevo_estado, self.fila, self.columna)
        return nuevo_estado
    
    
class poner_Figura_T(probee.Acción):
    
    #Este método define los parámetros de entrada de la clase, que en este caso serán, filas y columnas.
    def __init__(self, f, c):
        nombre = 'Pongo la figura T en la posición: ({},{})'.format(f,c)
        super().__init__(nombre)#este será el init de la clase heredada
        self.fila=f
        self.columna=c
    
    #Este método comprueba que los huecos que va a ocupar la figura están vacíos
    #Inicializo la matriz con estado[0], que es la matriz a tratar.
    #Inicializo el resultado a True
    #Si alguna posición que va a ocupar la figura es distinto de vacío, el resultado es False
    #Devuelvo todos los res. Todos los res deben ser True para que la figura se pueda poner
    def esta_vacio_puntos(self, estado, f, c):
        matriz = estado[0]
        res = [True]
        
        if (matriz[f][c] != ''):
                res.append(False)
        elif (matriz[f+1][c] != ''):
                res.append(False)
        elif (matriz[f+2][c] != ''):
                res.append(False)
        elif (matriz[f][c-1] != ''):
                res.append(False)
        elif (matriz[f][c+1] != ''):
                res.append(False)
        
        return all(res)
    
    #Este método comprueba los límites de la figura
    #Inicializo la matriz con estado[0], que es la matriz a tratar.
    #3 filas y 2 columnas deben ser <= que el tamaño de filas/columnas y la columna debe ser > 0.
    #Si se cumple, devuelvo True, si no, devuelvo False
    def limites(self, estado, f, c):
        matriz = estado[0]
        if (f + 2) <= matriz.shape[0]-1 and c <= matriz.shape[1]-2 and c > 0:
            return True
        else:
            return False
    
    #Este método comprueba que es aplicable la figura.
    def es_aplicable(self, estado):
        return self.limites(estado, self.fila, self.columna) and self.esta_vacio_puntos(estado, self.fila, self.columna)
    
    #Este método realiza la acción de poner la figura en el tablero.
    #Creo una nueva matriz.
    #Recorro las 3 primeras filas desde el píxel que tomo como referencia.
    #En esas 3 posiciones introduzco la letra T.
    #En la fila 1 y la columna -1 introduzco la letra T.
    #En la fila 1 y la columna 2 introduzco la letra T.
    #Decremento 5 al número de huecos libres que quedan en el tablero.
    #Devuelvo el tablero actualizado con la letra T.
    def poner_figura(self, estado, fil, col):
        nuevaMatriz = estado[0]
        for i in range(fil, fil+3):
            nuevaMatriz[i][col] = 'T'
        nuevaMatriz[fil][col-1] = 'T'
        nuevaMatriz[fil][col+1] = 'T'
        estado[1] -= 5
        return estado
    
    #Este método aplica la acción de poner la figura T.
    #Hago una copia del tablero.
    #Pongo la figura.
    #Devuelvo el tablero actualizado.
    def aplicar(self,estado):
        nuevo_estado = copy.deepcopy(estado)
        self.poner_figura(nuevo_estado, self.fila, self.columna)
        return nuevo_estado
    
    
class poner_Figura_U(probee.Acción):
    
    #Este método define los parámetros de entrada de la clase, que en este caso serán, filas y columnas.
    def __init__(self, f, c):
        nombre = 'Pongo la figura U en la posición: ({},{})'.format(f,c)
        super().__init__(nombre)#este será el init de la clase heredada
        self.fila=f
        self.columna=c
    
    #Este método comprueba que los huecos que va a ocupar la figura están vacíos
    #Inicializo la matriz con estado[0], que es la matriz a tratar.
    #Inicializo el resultado a True
    #Si alguna posición que va a ocupar la figura es distinto de vacío, el resultado es False
    #Devuelvo todos los res. Todos los res deben ser True para que la figura se pueda poner
    def esta_vacio_puntos(self, estado, f, c):
        matriz = estado[0]
        res = [True]
       
        if (matriz[f][c] != ''):
                res.append(False)
        elif (matriz[f+1][c] != ''):
                res.append(False)
        elif (matriz[f+1][c+1] != ''):
                res.append(False)
        elif (matriz[f][c+2] != ''):
                res.append(False)
        elif (matriz[f+1][c+2] != ''):
                res.append(False)
            
        return all(res)
    
    #Este método comprueba los límites de la figura
    #Inicializo la matriz con estado[0], que es la matriz a tratar.
    #2 filas y 3 columnas deben ser <= que el tamaño de filas/columnas.
    #Si se cumple, devuelvo True, si no, devuelvo False
    def limites(self, estado, f, c):
        matriz = estado[0]
        if (f + 1) <= matriz.shape[0]-1 and c <= matriz.shape[1]-3:
            return True
        else:
            return False
    
    #Este método comprueba que es aplicable la figura.
    def es_aplicable(self, estado):
        return self.limites(estado, self.fila, self.columna) and self.esta_vacio_puntos(estado, self.fila, self.columna)
    
    #Este método realiza la acción de poner la figura en el tablero.
    #Creo una nueva matriz.
    #Recorro las 2 primeras filas desde el píxel que tomo como referencia.
    #En esas 2 posiciones introduzco la letra U.
    #En la fila 1 y la columna 3 introduzco la letra U.
    #En la fila 2 y la columna 2 introduzco la letra U.
    #En la fila 2 y la columna 3 introduzco la letra U.
    #Decremento 5 al número de huecos libres que quedan en el tablero.
    #Devuelvo el tablero actualizado con la letra U.
    def poner_figura(self, estado, fil, col):
        nuevaMatriz = estado[0]
        for i in range(fil, fil+2):
            nuevaMatriz[i][col] = 'U'
        nuevaMatriz[fil][col+2] = 'U'
        nuevaMatriz[fil+1][col+1] = 'U'
        nuevaMatriz[fil+1][col+2] = 'U'
        estado[1] -= 5
        return estado
    
    #Este método aplica la acción de poner la figura U.
    #Hago una copia del tablero.
    #Pongo la figura.
    #Devuelvo el tablero actualizado.
    def aplicar(self,estado):
        nuevo_estado = copy.deepcopy(estado)
        self.poner_figura(nuevo_estado, self.fila, self.columna)
        return nuevo_estado
    
    
class poner_Figura_V(probee.Acción):
    
    #Este método define los parámetros de entrada de la clase, que en este caso serán, filas y columnas.
    def __init__(self, f, c):
        nombre = 'Pongo la figura V en la posición: ({},{})'.format(f,c)
        super().__init__(nombre)#este será el init de la clase heredada
        self.fila=f
        self.columna=c
    
    #Este método comprueba que los huecos que va a ocupar la figura están vacíos
    #Inicializo la matriz con estado[0], que es la matriz a tratar.
    #Inicializo el resultado a True
    #Si alguna posición que va a ocupar la figura es distinto de vacío, el resultado es False
    #Devuelvo todos los res. Todos los res deben ser True para que la figura se pueda poner
    def esta_vacio_puntos(self, estado, f, c):
        matriz = estado[0]
        res = [True]
        
        if (matriz[f][c] != ''):
                res.append(False)
        elif (matriz[f+1][c] != ''):
                res.append(False)
        elif (matriz[f+2][c] != ''):
                res.append(False)
        elif (matriz[f+2][c+1] != ''):
                res.append(False)
        elif (matriz[f+2][c+2] != ''):
                res.append(False)
        
        return all(res)
    
    #Este método comprueba los límites de la figura
    #Inicializo la matriz con estado[0], que es la matriz a tratar.
    #3 filas y 3 columnas deben ser <= que el tamaño de filas/columnas.
    #Si se cumple, devuelvo True, si no, devuelvo False
    def limites(self, estado, f, c):
        matriz = estado[0]
        if (f + 2) <= matriz.shape[0]-1 and (c + 2) <= matriz.shape[1]-1:
            return True
        else:
            return False
    
    #Este método comprueba que es aplicable la figura.
    def es_aplicable(self, estado):
        return self.limites(estado, self.fila, self.columna) and self.esta_vacio_puntos(estado, self.fila, self.columna)
    
    #Este método realiza la acción de poner la figura en el tablero.
    #Creo una nueva matriz.
    #Recorro las 3 primeras filas desde el píxel que tomo como referencia.
    #En esas 3 posiciones introduzco la letra V.
    #En la fila 3 y la columna 2 introduzco la letra V.
    #En la fila 3 y la columna 3 introduzco la letra V.
    #Decremento 5 al número de huecos libres que quedan en el tablero.
    #Devuelvo el tablero actualizado con la letra V.
    def poner_figura(self, estado, fil, col):
        nuevaMatriz = estado[0]
        for i in range(fil, fil+3):
            nuevaMatriz[i][col] = 'V'
        nuevaMatriz[fil+2][col+1] = 'V'
        nuevaMatriz[fil+2][col+2] = 'V'
        estado[1] -= 5
        return estado
    
    #Este método aplica la acción de poner la figura V.
    #Hago una copia del tablero.
    #Pongo la figura.
    #Devuelvo el tablero actualizado.
    def aplicar(self,estado):
        nuevo_estado = copy.deepcopy(estado)
        self.poner_figura(nuevo_estado, self.fila, self.columna)
        return nuevo_estado
    
    
class poner_Figura_W(probee.Acción):
    
    #Este método define los parámetros de entrada de la clase, que en este caso serán, filas y columnas.
    def __init__(self, f, c):
        nombre = 'Pongo la figura W en la posición: ({},{})'.format(f,c)
        super().__init__(nombre)#este será el init de la clase heredada
        self.fila=f
        self.columna=c
    
    #Este método comprueba que los huecos que va a ocupar la figura están vacíos
    #Inicializo la matriz con estado[0], que es la matriz a tratar.
    #Inicializo el resultado a True
    #Si alguna posición que va a ocupar la figura es distinto de vacío, el resultado es False
    #Devuelvo todos los res. Todos los res deben ser True para que la figura se pueda poner
    def esta_vacio_puntos(self, estado, f, c):
        matriz = estado[0]
        res = [True]
       
        if (matriz[f][c] != ''):
            res.append(False)
        elif (matriz[f+1][c] != ''):
            res.append(False)
        elif (matriz[f+1][c+1] != ''):
            res.append(False)
        elif (matriz[f+2][c+1] != ''):
            res.append(False)
        elif (matriz[f+2][c+2] != ''):
            res.append(False)
            
        return all(res)
    
    #Este método comprueba los límites de la figura
    #Inicializo la matriz con estado[0], que es la matriz a tratar.
    #3 filas y 3 columnas deben ser <= que el tamaño de filas/columnas.
    #Si se cumple, devuelvo True, si no, devuelvo False
    def limites(self, estado, f, c):
        matriz = estado[0]
        if (f + 2) <= matriz.shape[0]-1 and (c + 2) <= matriz.shape[1]-1:
            return True
        else:
            return False
    
    #Este método comprueba que es aplicable la figura.
    def es_aplicable(self, estado):
        return self.limites(estado, self.fila, self.columna) and self.esta_vacio_puntos(estado, self.fila, self.columna)
    
    #Este método realiza la acción de poner la figura en el tablero.
    #Creo una nueva matriz.
    #Recorro las 2 primeras filas desde el píxel que tomo como referencia.
    #En esas 2 posiciones introduzco la letra W.
    #En la fila 2 y la columna 2 introduzco la letra W.
    #En la fila 3 y la columna 2 introduzco la letra W.
    #En la fila 3 y la columna 3 introduzco la letra W.
    #Decremento 5 al número de huecos libres que quedan en el tablero.
    #Devuelvo el tablero actualizado con la letra W.
    def poner_figura(self, estado, fil, col):
        nuevaMatriz = estado[0]
        for i in range(fil, fil+2):
            nuevaMatriz[i][col] = 'W'
        nuevaMatriz[fil+1][col+1] = 'W'
        nuevaMatriz[fil+2][col+1] = 'W'
        nuevaMatriz[fil+2][col+2] = 'W'
        estado[1] -= 5
        return estado
    
    #Este método aplica la acción de poner la figura W.
    #Hago una copia del tablero.
    #Pongo la figura.
    #Devuelvo el tablero actualizado.
    def aplicar(self,estado):
        nuevo_estado = copy.deepcopy(estado)
        self.poner_figura(nuevo_estado, self.fila, self.columna)
        return nuevo_estado
    
    
class poner_Figura_X(probee.Acción):
    
    #Este método define los parámetros de entrada de la clase, que en este caso serán, filas y columnas.
    def __init__(self, f, c):
        nombre = 'Pongo la figura X en la posición: ({},{})'.format(f,c)
        super().__init__(nombre)#este será el init de la clase heredada
        self.fila=f
        self.columna=c
    
    #Este método comprueba que los huecos que va a ocupar la figura están vacíos
    #Inicializo la matriz con estado[0], que es la matriz a tratar.
    #Inicializo el resultado a True
    #Si alguna posición que va a ocupar la figura es distinto de vacío, el resultado es False
    #Devuelvo todos los res. Todos los res deben ser True para que la figura se pueda poner
    def esta_vacio_puntos(self, estado, f, c):
        matriz = estado[0]
        res = [True]
        
        if (matriz[f][c] != ''):
                res.append(False)
        elif (matriz[f+1][c] != ''):
                res.append(False)
        elif (matriz[f+2][c] != ''):
                res.append(False)
        elif (matriz[f+1][c-1] != ''):
                res.append(False)
        elif (matriz[f+1][c+1] != ''):
                res.append(False)
        
        return all(res)
    
    #Este método comprueba los límites de la figura
    #Inicializo la matriz con estado[0], que es la matriz a tratar.
    #3 filas y 2 columnas deben ser <= que el tamaño de filas/columnas y la columna debe ser > 0.
    #Si se cumple, devuelvo True, si no, devuelvo False
    def limites(self, estado, f, c):
        matriz = estado[0]
        if (f + 2) <= matriz.shape[0]-1 and c <= matriz.shape[1]-2 and c > 0:
            return True
        else:
            return False
    
    #Este método comprueba que es aplicable la figura.
    def es_aplicable(self, estado):
        return self.limites(estado, self.fila, self.columna) and self.esta_vacio_puntos(estado, self.fila, self.columna)
    
    #Este método realiza la acción de poner la figura en el tablero.
    #Creo una nueva matriz.
    #Recorro las 3 primeras filas desde el píxel que tomo como referencia.
    #En esas 3 posiciones introduzco la letra X.
    #En la fila 2 y la columna -1 introduzco la letra X.
    #En la fila 2 y la columna 2 introduzco la letra X.
    #Decremento 5 al número de huecos libres que quedan en el tablero.
    #Devuelvo el tablero actualizado con la letra X.
    def poner_figura(self, estado, fil, col):
        nuevaMatriz = estado[0]
        for i in range(fil, fil+3):
            nuevaMatriz[i][col] = 'X'
        nuevaMatriz[fil+1][col-1] = 'X'
        nuevaMatriz[fil+1][col+1] = 'X'
        estado[1] -= 5
        return estado
    
    #Este método aplica la acción de poner la figura X.
    #Hago una copia del tablero.
    #Pongo la figura.
    #Devuelvo el tablero actualizado.
    def aplicar(self,estado):
        nuevo_estado = copy.deepcopy(estado)
        self.poner_figura(nuevo_estado, self.fila, self.columna)
        return nuevo_estado
    
    
class poner_Figura_Y(probee.Acción):
    
    #Este método define los parámetros de entrada de la clase, que en este caso serán, filas y columnas.
    def __init__(self, f, c):
        nombre = 'Pongo la figura Y en la posición: ({},{})'.format(f,c)
        super().__init__(nombre)#este será el init de la clase heredada
        self.fila=f
        self.columna=c
    
    #Este método comprueba que los huecos que va a ocupar la figura están vacíos
    #Inicializo la matriz con estado[0], que es la matriz a tratar.
    #Inicializo el resultado a True
    #Si alguna posición que va a ocupar la figura es distinto de vacío, el resultado es False
    #Devuelvo todos los res. Todos los res deben ser True para que la figura se pueda poner
    def esta_vacio_puntos(self, estado, f, c):
        matriz = estado[0]
        res = [True]
       
        if (matriz[f][c] != ''):
                res.append(False)
        elif (matriz[f+1][c] != ''):
                res.append(False)
        elif (matriz[f+2][c] != ''):
                res.append(False)
        elif (matriz[f+3][c] != ''):
                res.append(False)
        elif (matriz[f+1][c-1] != ''):
                res.append(False)
            
        return all(res)
    
    #Este método comprueba los límites de la figura
    #Inicializo la matriz con estado[0], que es la matriz a tratar.
    #4 filas y 1 columna deben ser <= que el tamaño de filas/columnas y la columna debe ser > 0.
    #Si se cumple, devuelvo True, si no, devuelvo False
    def limites(self, estado, f, c):
        matriz = estado[0]
        if (f + 3) <= matriz.shape[0]-1 and c <= matriz.shape[1]-1 and c > 0:
            return True
        else:
            return False
    
    #Este método comprueba que es aplicable la figura.
    def es_aplicable(self, estado):
        return self.limites(estado, self.fila, self.columna) and self.esta_vacio_puntos(estado, self.fila, self.columna)
    
    #Este método realiza la acción de poner la figura en el tablero.
    #Creo una nueva matriz.
    #Recorro las 4 primeras filas desde el píxel que tomo como referencia.
    #En esas 4 posiciones introduzco la letra Y.
    #En la fila 2 y la columna -1 introduzco la letra X.
    #Decremento 5 al número de huecos libres que quedan en el tablero.
    #Devuelvo el tablero actualizado con la letra X.
    def poner_figura(self, estado, fil, col):
        nuevaMatriz = estado[0]
        for i in range(fil, fil+4):
            nuevaMatriz[i][col] = 'Y'
        nuevaMatriz[fil+1][col-1] = 'Y'
        estado[1] -= 5
        return estado
    
    #Este método aplica la acción de poner la figura Y.
    #Hago una copia del tablero.
    #Pongo la figura.
    #Devuelvo el tablero actualizado.
    def aplicar(self,estado):
        nuevo_estado = copy.deepcopy(estado)
        self.poner_figura(nuevo_estado, self.fila, self.columna)
        return nuevo_estado

    
class poner_Figura_Z(probee.Acción):
    
    #Este método define los parámetros de entrada de la clase, que en este caso serán, filas y columnas.
    def __init__(self, f, c):
        nombre = 'Pongo la figura Z en la posición: ({},{})'.format(f,c)
        super().__init__(nombre)#este será el init de la clase heredada
        self.fila=f
        self.columna=c
    
    #Este método comprueba que los huecos que va a ocupar la figura están vacíos
    #Inicializo la matriz con estado[0], que es la matriz a tratar.
    #Inicializo el resultado a True
    #Si alguna posición que va a ocupar la figura es distinto de vacío, el resultado es False
    #Devuelvo todos los res. Todos los res deben ser True para que la figura se pueda poner
    def esta_vacio_puntos(self, estado, f, c):
        matriz = estado[0]
        res = [True]
       
        if (matriz[f][c] != ''):
                res.append(False)
        elif (matriz[f+1][c] != ''):
                res.append(False)
        elif (matriz[f+2][c] != ''):
                res.append(False)
        elif (matriz[f][c-1] != ''):
                res.append(False)
        elif (matriz[f+2][c+1] != ''):
                res.append(False)
    
        return all(res)
    
    #Este método comprueba los límites de la figura
    #Inicializo la matriz con estado[0], que es la matriz a tratar.
    #3 filas y 2 columnas deben ser <= que el tamaño de filas/columnas y la columna debe ser > 0.
    #Si se cumple, devuelvo True, si no, devuelvo False
    def limites(self, estado, f, c):
        matriz = estado[0]
        if (f + 2) <= matriz.shape[0]-1 and (c + 1) <= matriz.shape[1]-1 and c > 0:
            return True
        else:
            return False
    
    #Este método comprueba que es aplicable la figura.
    def es_aplicable(self, estado):
        return self.limites(estado, self.fila, self.columna) and self.esta_vacio_puntos(estado, self.fila, self.columna)
    
    #Este método realiza la acción de poner la figura en el tablero.
    #Creo una nueva matriz.
    #Recorro las 3 primeras filas desde el píxel que tomo como referencia.
    #En esas 3 posiciones introduzco la letra Z.
    #En la fila 1 y la columna -1 introduzco la letra Z.
    #En la fila 3 y la columna 2 introduzco la letra Z.
    #Decremento 5 al número de huecos libres que quedan en el tablero.
    #Devuelvo el tablero actualizado con la letra Z.
    def poner_figura(self, estado, fil, col):
        nuevaMatriz = estado[0]
        for i in range(fil, fil+3):
            nuevaMatriz[i][col] = 'Z'
        nuevaMatriz[fil][col-1] = 'Z'
        nuevaMatriz[fil+2][col+1] = 'Z'
        estado[1] -= 5
        return estado
    
    #Este método aplica la acción de poner la figura Z.
    #Hago una copia del tablero.
    #Pongo la figura.
    #Devuelvo el tablero actualizado.
    def aplicar(self,estado):
        nuevo_estado = copy.deepcopy(estado)
        self.poner_figura(nuevo_estado, self.fila, self.columna)
        return nuevo_estado
    
    
class poner_Figura_F(probee.Acción):
    
    #Este método define los parámetros de entrada de la clase, que en este caso serán, filas y columnas.
    def __init__(self, f, c):
        nombre = 'Pongo la figura F en la posición: ({},{})'.format(f,c)
        super().__init__(nombre)#este será el init de la clase heredada
        self.fila=f
        self.columna=c
    
    #Este método comprueba que los huecos que va a ocupar la figura están vacíos
    #Inicializo la matriz con estado[0], que es la matriz a tratar.
    #Inicializo el resultado a True
    #Si alguna posición que va a ocupar la figura es distinto de vacío, el resultado es False
    #Devuelvo todos los res. Todos los res deben ser True para que la figura se pueda poner
    def esta_vacio_puntos(self, estado, f, c):
        matriz = estado[0]
        res = [True]
       
        if (matriz[f][c] != ''):
                res.append(False)
        elif (matriz[f+1][c] != ''):
                res.append(False)
        elif (matriz[f+2][c] != ''):
                res.append(False)
        elif (matriz[f][c+1] != ''):
                res.append(False)
        elif (matriz[f+1][c-1] != ''):
                res.append(False)
        
        return all(res)
    
    #Este método comprueba los límites de la figura
    #Inicializo la matriz con estado[0], que es la matriz a tratar.
    #3 filas y 2 columnas deben ser <= que el tamaño de filas/columnas y la columna debe ser > 0.
    #Si se cumple, devuelvo True, si no, devuelvo False
    def limites(self, estado, f, c):
        matriz = estado[0]
        if (f + 2) <= matriz.shape[0]-1 and c <= matriz.shape[1]-2 and c > 0:
            return True
        else:
            return False
    
    #Este método comprueba que es aplicable la figura.
    def es_aplicable(self, estado):
        return self.limites(estado, self.fila, self.columna) and self.esta_vacio_puntos(estado, self.fila, self.columna)
    
    #Este método realiza la acción de poner la figura en el tablero.
    #Creo una nueva matriz.
    #Recorro las 3 primeras filas desde el píxel que tomo como referencia.
    #En esas 3 posiciones introduzco la letra F.
    #En la fila 1 y la columna 2 introduzco la letra F.
    #En la fila 2 y la columna -1 introduzco la letra F.
    #Decremento 5 al número de huecos libres que quedan en el tablero.
    #Devuelvo el tablero actualizado con la letra F.    
    def poner_figura(self, estado, fil, col):
        nuevaMatriz = estado[0]
        for i in range(fil, fil+3):
            nuevaMatriz[i][col] = 'F'
        nuevaMatriz[fil][col+1] = 'F'
        nuevaMatriz[fil+1][col-1] = 'F'
        estado[1] -= 5
        return estado
    
    #Este método aplica la acción de poner la figura F.
    #Hago una copia del tablero.
    #Pongo la figura.
    #Devuelvo el tablero actualizado.
    def aplicar(self,estado):
        nuevo_estado = copy.deepcopy(estado)
        self.poner_figura(nuevo_estado, self.fila, self.columna)
        return nuevo_estado

    

class poner_Figura_I(probee.Acción):
    
    #Este método define los parámetros de entrada de la clase, que en este caso serán, filas y columnas.
    def __init__(self, f, c):
        nombre = 'Pongo la figura I en la posición: ({},{})'.format(f,c)
        super().__init__(nombre)#este será el init de la clase heredada
        self.fila=f
        self.columna=c
    
    #Este método comprueba que los huecos que va a ocupar la figura están vacíos
    #Inicializo la matriz con estado[0], que es la matriz a tratar.
    #Inicializo el resultado a True
    #Recorro las 5 primeras filas desde el píxel que tomo como referencia
    #Voy metiendo en cont el valor de la columna c y las 5 primeras filas
    #Si lo que contiene cont es distinto de vacío, el resultado es False
    #Devuelvo todos los res. Todos los res deben ser True para que la figura se pueda poner
    def esta_vacio_puntos(self, estado, f, c):
        matriz = estado[0]
        res = [True]
        for i in range(f, f+5):
            cont = matriz[i][c]
            if (cont != ''):
                res.append(False)
                break
        return all(res)
    
    #Este método comprueba los límites de la figura
    #Inicializo la matriz con estado[0], que es la matriz a tratar.
    #4 filas y 1 columna deben ser <= que el tamaño de filas/columnas.
    #Si se cumple, devuelvo True, si no, devuelvo False
    def limites(self, estado, f, c):
        matriz = estado[0]
        if (f + 4) <= matriz.shape[0]-1 and c <= matriz.shape[1]-1:
            return True
        else:
            return False
    #Este método comprueba que es aplicable la figura. Además se establece una restricción para poner un número máximo de esta figura.
    def es_aplicable(self, estado):
        return self.limites(estado, self.fila, self.columna) and self.esta_vacio_puntos(estado, self.fila, self.columna) and estado[2]>0
    
    #Este método realiza la acción de poner la figura en el tablero.
    #Creo una nueva matriz.
    #Recorro las 5 primeras filas desde el píxel que tomo como referencia.
    #En esas 5 posiciones introduzco la letra I.
    #Decremento 5 al número de huecos libres que quedan en el tablero.
    #Deremento 1 al número de letras I que puedo usar.
    #Devuelvo el tablero actualizado con la letra I.
    def poner_figura(self, estado, fil, col):
        nuevaMatriz = estado[0]
        for i in range(fil, fil+5):
            nuevaMatriz[i][col] = 'I'
        estado[1] -= 5
        estado[2] -= 1
        return estado
    
    #Este método aplica la acción de poner la figura I.
    #Hago una copia del tablero.
    #Pongo la figura.
    #Devuelvo el tablero actualizado.
    def aplicar(self,estado):
        nuevo_estado = copy.deepcopy(estado)
        self.poner_figura(nuevo_estado, self.fila, self.columna)
        return nuevo_estado