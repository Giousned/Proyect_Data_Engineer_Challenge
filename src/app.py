# Importamos random para crear nuestros propios arrays
import random

# Elegimos el alto y el ancho que queremos que en este caso nos lo dan en el enunciado los valores máximos y mínimos
alto = random.randint(3, 1000)              # Limites fijados por el enunciado, se pueden cambiar para ir probando combinaciones diferentes o más pequeñas
ancho = random.randint(3, 1000)

array = []
labyrinth = []


# Creamos nuestro array aleatorio cada vez para jugar nosotros
def two_dimensional_array(alto, ancho):

    for i in range(alto):

        array = []

        for j in range(ancho):
            
            numero_aleatorio = random.randint(0, 15)
            
            if (numero_aleatorio == 7):
                array.append("#")
            else:
                array.append(".")
        
        labyrinth.append(array)
        
    return labyrinth


# Creamos la funcion para buscar los movimientos minimos para llegar al extremo inferior derecho del array
def go_corner_right(labyrinth):
    
    ancho = len(labyrinth[0])
    alto = len(labyrinth)

    counter = 0
    horizontal = True
    vertical = False

    # Aqui usamos "guardas/cortafuegos" para que si ocurre alguno de estos 2 casos salga directamente de la funcion e indique que no hay solucion posible
    if (labyrinth[-1][-1] == "#"):
        counter = -1
        return "solution(labyrinth) = " + str(counter)
    
    if (labyrinth[0][0] == "#" or labyrinth[0][1] == "#"  or labyrinth[0][2] == "#"):
        counter = -1
        return "solution(labyrinth) = " + str(counter)
    
    
    # Si llegamos hasta aquí ya buscamos los movimientos minimos que hacen falta para llegar, dividimos la busqueda en 2 casos, cuando la longitud del array es 3 o cuando es superior. 
    # Este primer caso es cuando es superior a 3. Que hay que moverse horizontalmente y verticalmente y con cambios de horientacion.    
    if (ancho>3):
        
        j = 3
        
        for i in range(0, alto - 1):
            
            while (j < ancho):

                if (labyrinth[i][j] != "#"):                            # Buscamos y vamos moviendo horizontalmente primero, y cuando no podemos bajamos 1 vertical si es posible
                    counter += 1
                    j += 1
                elif (labyrinth[i+1][j-2] != "#" and labyrinth[i+1][j-1] != "#" and labyrinth[i+1][j] != "#"):          # Aqui se baja 1 vertical si se puede
                    counter += 1
                    i += 1
                else:
                    counter = -1
                    return "solution(labyrinth) = " + str(counter)
            
            if (labyrinth[i+1][j-3] != "#" and labyrinth[i+1][j-2] != "#" and labyrinth[i+1][j-1] != "#" and horizontal):               # Cuando ya estamos en el borde derecho ya solo queda bajar verticalmente
                counter += 1
            
            elif (i >= 2):
                if (horizontal):                            # Aqui hacemos una orientacion de horizontal a vertical de la piedra, al comprobar que hemos bajado 2 lineas verticalmente y con lo cual hay una superficie de 3x3 libre alrededor de la piedra
                    counter += 1                            # Sumamos un movimiento por el cambio de horientacion solo cuando lo hacemos
                horizontal = False
                vertical = True
                
                if(labyrinth[i+1][j-1] != "#" and vertical):            # Seguimos buscando verticalmente pero con la horientacion vertical tambien
                    counter += 1
                else:
                    counter = -1
                    return "solution(labyrinth) = " + str(counter)              # Devolvemos la solucion del menor numero de movimientos
            else:
                counter = -1
                return "solution(labyrinth) = " + str(counter)



    else:
        for i in range(0, alto - 1):                                        # Y aquí es exactamente igual pero solo con busqueda vertical desde el principio ya que el array solo tiene una longitud de 3 y la piedra no puede moverse horizontalmente en horizontal
            
            if (labyrinth[i+1][0] != "#" and labyrinth[i+1][1] != "#" and labyrinth[i+1][2] != "#" and horizontal):
                counter += 1
            
            elif (i >= 2):
                if (horizontal):
                    counter += 1
                horizontal = False
                vertical = True
                
                if(labyrinth[i+1][j-1] != "#" and vertical):
                    counter += 1
                else:
                    counter = -1
                    return "solution(labyrinth) = " + str(counter)
            
            else:
                counter = -1
                return "solution(labyrinth) = " + str(counter)

    
    return "solution(labyrinth) = " + str(counter)
                
        

print("labyrinth = ", two_dimensional_array(alto, ancho))               # Aqui imprimimos en pantalla nuestro array aleatorio creado para jugar

print(go_corner_right(labyrinth))                                       # Aqui se imprime los movimientos minimos que hacen falta


###########                                                         # Aqui comprobamos con una serie de test que nos dan de ejemplo/prueba y se pueden añadir más para comprobar nuestra solucion
## TESTS ##
###########

labyrinth_test1 = [[".",".",".",".",".",".",".",".","."],["#",".",".",".","#",".",".",".","."],[".",".",".",".","#",".",".",".","."],[".","#",".",".",".",".",".","#","."],[".","#",".",".",".",".",".","#","."]]

print("Solution Test 1", go_corner_right(labyrinth_test1))


labyrinth_test2 = [[".",".",".",".",".",".",".",".","."],["#",".",".",".","#",".",".","#","."],[".",".",".",".","#",".",".",".","."],[".","#",".",".",".",".",".","#","."],[".","#",".",".",".",".",".","#","."]]

print("Solution Test 2", go_corner_right(labyrinth_test2))


labyrinth_test3 = [[".",".","."],[".",".","."],[".",".","."]]

print("Solution Test 3", go_corner_right(labyrinth_test3))


labyrinth_test4 = [[".",".",".",".",".",".",".",".",".","."],[".","#",".",".",".",".","#",".",".","."],[".","#",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".","."],[".","#",".",".",".",".",".",".",".","."],[".","#",".",".",".","#",".",".",".","."],[".",".",".",".",".",".","#",".",".","."],[".",".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".","."]]

print("Solution Test 4", go_corner_right(labyrinth_test4))
