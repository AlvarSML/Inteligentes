def AStar(inicial, sucesoresF, metaF, heuristicoF):
    abiertos=Abiertos()
    nInicial=inicial
    abiertos.put(nInicial)
    cerrados=[]
    
    #Mientras abiertos no esté vacio:
    while not abiertos.empty():
        nodoActual=abiertos.getNodes()[0]
        ValorF=nodoActual.getF()
        
        #Cogemos el nodo con la menor F.
        for i in abiertos.getNodes():
            print(abiertos) 
            if i.getF()<ValorF:
                nodoActual=i
                ValorF=i.getF()
        print(abiertos) 

        #Añadimos dicho nodo a cerrados.
        cerrados.append(nodoActual)
        estado=nodoActual.getEstado()

        print(cerrados)
        #Si el nodo esta en la meta retorna el camino.
        #if metaF(estado):
        #MIOOOOOO1 linea
        if metaF(nodoActual):
            return nodoActual.camino()
         
        #Sacamos el primer nodo de abiernos.
        abiertos.pop()

        #Recorremos los sucesores:
        #        for suc in sucesoresF(nodoActual):
        #       MIOOOOOO1 linea
        for suc in sucesoresF(nodoActual,heuristicoF): #ponía heuristicaGrafo
            #Si el sucesor no esta en abiertos ni en cerrados, lo ponemos en abiertos.
            if suc not in abiertos.getNodes() and suc not in cerrados:
                abiertos.put(suc)
            #Si el sucesor esta en abiertos y el sucesor tiene menor G, lo actualizo en abiertos.
            if suc in abiertos.getNodes():
                nodoViejo=abiertos.getNodo(suc.getEstado())
                if suc.getG() < nodoViejo.getG():
                    abiertos.update(nodoViejo,suc)
           #Si el sucesor esta en cerrados y el sucesor tiene menor G,lo elimino de cerrrados y lo meto en abiertos.     
            if suc in cerrados:
                for k in cerrados:
                    if k.getEstado() == suc.getEstado():
                        if suc.getG() < k.getG():
                            cerrados.remove(k)
                            abiertos.put(suc)
               
    return []