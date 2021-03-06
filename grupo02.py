producciones = []
lista = []
first = []
follow = []
select = []

class Gramatica:

    def __init__(self, gramatica):
        """Constructor de la clase.
        Parameters
        ----------
        gramatica : string
            Representación de las producciones de una gramática determinada.
            Ejemplo:
            "A:b A\nA:a\nA:A B c\nA:lambda\nB:b"
        """
        producciones = gramatica.split('\n')  # Genera una lista con cada producción
        self.gramatica = producciones
        calculo_first = []
        calculo_first = Gramatica.calcular_first(producciones)
        self.first = calculo_first #le paso las producciones como parámetro
        if 'Recursividad' in calculo_first:
            self.follows = 'Recursividad'
            self.selects = 'Recursividad'
            self.LL1 = False
        else:
            self.follows = Gramatica.calcular_follows(self.gramatica)
            self.selects = Gramatica.calcular_select(self.gramatica, self.first, self.follows)
            self.antecedentes = Gramatica.calculo_antecedentes(producciones)
            self.no_terminales = Gramatica.calculo_no_terminales(producciones)
            self.terminales = Gramatica.calculo_terminales(producciones)
            self.LL1 = Gramatica.isLL1(self)

    def calculo_antecedentes(producciones):
        lista_antecedentes = []
        for p in producciones:
            antecedentes = p.split(':')
            lista_antecedentes.append(antecedentes[0])
        return lista_antecedentes

    def calculo_no_terminales(producciones):
        lista_antecedentes = []
        for p in producciones:
            antecedentes = p.split(':')
            if antecedentes[0] not in lista_antecedentes:
                lista_antecedentes.append(antecedentes[0])
        return lista_antecedentes

    def calculo_terminales(producciones):
        lista_terminales = []
        for p in producciones:
            divAnt = p.split(":")  # Divido ant de consec.
            conse = divAnt[1].split()  # Consecuentes
            for c in conse:
                if str.isupper(c):
                    continue
                else:
                    if c not in lista_terminales:
                        lista_terminales.append(c)
        return lista_terminales

    def calcular_first(reglas):  # calculo de first para una regla pasada como parámetro.
        primeros = []
        FirstPorRegla = []
        indice = 0
        union = []
        lista_terminales = Gramatica.calculo_terminales(reglas)
        for r in reglas:  # Por cada regla
            primeros.clear()
            reglaActual = r
            divisionAC = r.split(":")  # Divido antecedente del consecuente
            consecuentes = divisionAC[1].split()  # Armo una lista con cada elemento del consecuente para esa regla
            primer_consecuente = list(consecuentes[0])
            #Evaluar recursividad.
            if divisionAC[0] == consecuentes[0]: #Encontré como primer consecuente el mismo antecedente.
                FirstPorRegla.append("Recursividad")
                break
            if str.isupper(primer_consecuente[0]):  # Si la primera letra del primer consecuente empieza con mayúscula, es NT.
                no_terminal = consecuentes[0]  # Guardo el no terminal en una variable.
                aux_first = Gramatica.busqueda_first(no_terminal, r, reglas)
                union.clear()
                for a in aux_first:
                    union.append(a)
                cadena_final = " ".join(union)
                FirstPorRegla.insert(indice, cadena_final)
            else:  # Si no comienza con mayúsculas, es un terminal -> ya tenemos el first de la regla.
                if consecuentes[0] == 'lambda':
                    terminal = 'lambda'
                else:
                    terminal = consecuentes[0]
                FirstPorRegla.insert(indice, terminal)  # Agrego en la posición indicada el terminal que es el first.
            indice += 1
        for elemento in range(0, len(FirstPorRegla)):
            hacerSplit = FirstPorRegla[elemento].split()
            listaNueva = list(hacerSplit)
            listaNueva2 = []
            for x in listaNueva:
                if 'Recursividad' in listaNueva:
                    FirstPorRegla = 'Recursividad'
                if x not in listaNueva2 and x in lista_terminales:
                    listaNueva2.append(x)
                    FirstPorRegla[elemento] = listaNueva2
        return FirstPorRegla  # lista de first para cada antecedente

    def busqueda_first(noterminal, regla, producciones):
        concate = []
        concat = []
        primeros = []
        divisionRegla = regla.split(":")  # Divido la regla original en antecedente y consecuente
        divisionConsecuenteRegla = divisionRegla[1].split()  # Divido el consecuente en una lista. Cada pos un elemento.
        for p in producciones:  # por cada producción
            antecedenteconsecuente = p.split(":")  # Divido antecedente del consecuente
            consecuente = antecedenteconsecuente[1].split()  # Divido los consecuentes de esa regla.
            if antecedenteconsecuente[0] == noterminal:  # Si el antecedente es igual al no terminal que traigo del otro método
                if str.islower(consecuente[0]):  # Si el primer consecuente es minúscula
                    if consecuente[0] == 'lambda':  # Si es igual a lambda, veo si sigue en la regla original otra cosa.
                        ind = 0
                        for x in divisionConsecuenteRegla:  # por cada consecuente de la regla original, pregunto si es igual al NT, para id si es el ultimo
                            if x == noterminal:
                                if x == divisionConsecuenteRegla[-1]:  # Si es el último elemento de la lista, significa que no viene más nada
                                    terminal = 'lambda'
                                    if terminal not in primeros:  # Guardo lambda en la lista de first.
                                        primeros.append(terminal)
                                else:  # Si ese NT no es el último elemento, puede venir otro NT o un terminal.
                                    elemento_siguiente = list(divisionConsecuenteRegla[ind + 1])
                                    if str.isupper(elemento_siguiente[0]):  # Si es mayúscula, calcular firsts.
                                        auxiliar = Gramatica.busqueda_first(divisionConsecuenteRegla[ind + 1], regla, producciones)
                                        if 'lambda' in auxiliar:
                                            primeros.append('lambda')
                                        for u in auxiliar:
                                            for m in u:
                                                if m not in primeros:
                                                    concat.append(m)
                                        auxiliar2 = " ".join(concat)
                                        primeros.append(auxiliar2)
                                    else:  # Es minúsculas, se agrega directamente.
                                        terminal = elemento_siguiente
                                        if terminal not in primeros:  # Lo agrego a los first
                                            primeros.append(elemento_siguiente)
                            ind = ind + 1
                    else:  # Si es distinto de lambda
                        terminal = consecuente[0]
                        if terminal not in primeros:
                            primeros.append(terminal)
                else:
                    elemento = list(consecuente[0])
                    if str.isupper(elemento[0]):
                        auxiliar3 = Gramatica.busq_terminal(consecuente[0], p, producciones)  # ver que cambia si pongo p o r
                        for m in auxiliar3:
                            if m not in primeros:
                                concate.append(m)
                        auxiliar3 = " ".join(concate)
                        primeros.append(auxiliar3)
        return primeros

    def calcular_follows(reglas):
        aux_first = []
        lista_extra = []
        lista_follows = []
        lista_terminales = Gramatica.calculo_terminales(reglas)
        lista_antecedentes = Gramatica.calculo_no_terminales(reglas)
        for a in range(0, len(lista_antecedentes)): #Por cada antecedente que encuentro, le creo una lista vacía. Resultado va a ser lista de listas.
            lista_follows.insert(a, [])
        lista_First = Gramatica.calcular_first(reglas)
        for m in lista_First:
                if 'Recursividad' in lista_First:
                    lista_follows.append('Recursividad')
                    break
        for i in range(0, len(lista_antecedentes)):  # POR CADA ANTECEDENTE
            if i == 0:
                lista_follows[i].append('$')  # Si es el distinguido, agrego $ en sus follows.
            for x in range(0, len(reglas)):  # recorro cada regla a ver si lo encuentro como consecuente en alguna.
                division = reglas[x].split(":")  # Antecedente y consecuente
                consecuentes = division[1].split()  # Lista de consecuentes
                for c in range(0, len(consecuentes)):  # Por cada consecuente de la regla en la que estoy.
                    if consecuentes[c] == lista_antecedentes[i]:  # Si encuentro el antecedente como consecuente
                        if consecuentes[c] == consecuentes[-1]:  # Pregunto si es el último elemento consecuente.
                            ant = division[0]  # Antecedente de la regla donde encontre ese NT como ultimo elemento.
                            for n in range(0, len(lista_antecedentes)): #Agrego los follows de ese antecedente en el anterior.
                                if lista_antecedentes[n] == ant:
                                    for elemento in lista_follows[n]:
                                        if elemento not in lista_follows[i]:
                                            lista_follows[i].append(elemento)
                        else:  # Si no es el último elemento, tengo que ver que sigue: follow.
                            siguiente = consecuentes[c + 1]  # elemento siguiente
                            if str.islower(siguiente):  # si el siguiente elemento es minusculas, es un terminal.
                                lista_follows[i].append(siguiente)
                            else:  # buscar los first de ese elemento. Es un NT. primer follow.
                                lista_extra = Gramatica.busqueda_follow(reglas[x],siguiente,reglas,lista_follows)
                                for item in lista_extra:
                                    if item not in lista_follows[i]:
                                        lista_follows[i].extend(item)
        return lista_follows

    def busqueda_follow(regla, cons, producciones, follow_list):  # llega regla y el consecuente siguiente.
        first_retorno = []
        newlist = []
        aux_first = Gramatica.calcular_first(producciones) # first de todas las reglas.
        for n in range(0, len(producciones)):  # Por cada regla
            dividir = producciones[n].split(":")
            if dividir[0] == cons:  # Encontré la posición del first. (m).
                for elemento in aux_first[n]:
                    if elemento == 'lambda': #Si encuentro lambda en los first, tengo que ver si hay un prox elemento.
                        divRegla = regla.split(":")
                        cons_regla = divRegla[1].split() #Consecuentes
                        for h in range(0,len(cons_regla)):
                            if cons_regla[h] == cons:
                                if cons == cons_regla[-1]: #Si es el último elemento
                                    lista_antecedentes = Gramatica.calculo_no_terminales(producciones)
                                    for g in range(0,len(lista_antecedentes)):
                                        if lista_antecedentes[g] == divRegla[0]:
                                            for fol in follow_list[g]:
                                                if fol not in first_retorno:
                                                    first_retorno.append(fol)
                                else:
                                    prox_siguiente = cons_regla[h+1]
                                    if str.islower(prox_siguiente):
                                        if prox_siguiente not in first_retorno:
                                            first_retorno.append(prox_siguiente)
                                    else:
                                        nueva_lista = Gramatica.busqueda_follow(regla, prox_siguiente, producciones, follow_list)
                                        for k in nueva_lista:
                                            if k not in first_retorno:
                                                first_retorno.append(k)
                    else:
                        if elemento not in first_retorno:
                            first_retorno.append(aux_first[n])
        return first_retorno

    def calcular_select(reglas, listaFirst, listaFollow):
        SelectsPorRegla = []
        lista_antecedentes = []
        lista_no_terminales = []
        for item in range(0, len(listaFirst)):
            if 'lambda' not in listaFirst[item]:
                SelectsPorRegla.insert(item, listaFirst[item])
            else:  # en item hay un lambda
                lista_antecedentes = Gramatica.calculo_antecedentes(reglas)
                lista_no_terminales = Gramatica.calculo_no_terminales(reglas)
                antecedente = lista_antecedentes[item]
                for i in range(0, len(lista_no_terminales)):
                    if lista_no_terminales[i] == antecedente:
                        nuevaLista = listaFirst[item] + listaFollow[i]
                        nuevaLista.remove('lambda')
                        SelectsPorRegla.insert(item, nuevaLista)
        return SelectsPorRegla

    def isLL1(self):
        """
        Verifica si una gramática permite realizar derivaciones utilizando
           la técnica LL1.
        Returns
        -------
        resultado : bool
            Indica si la gramática es o no LL1.
        DEVOLVER BOOLEANO.
        No recibe parámetros. Devuelve booleano de acuerdo a si es o no LL(1)
        Calcular first, follows y selects de la gramática que ingresó.
        De ahí, mirar selects y y ver si son o no disyuntos: de ahí el booleano
        """
        antecedente = ''
        es_LL1 = True
        lista_selects = []
        for r in producciones:
            if r.regla[0] != antecedente:
                #print(r.regla[0])
                antecedente = r.regla[0]
                lista_selects.clear()
            for s in r.selects:
                print(r.selects)
                if s in lista_selects:
                    es_LL1 = False
                    break
                else:
                    lista_selects.append(s)
        return es_LL1

    def parse(self, cadena):
        """Retorna la derivación para una cadena dada utilizando las
           producciones de la gramática y los conjuntos de Fi, Fo y Se
           obtenidos previamente.
        Parameters
        ----------
        cadena : string
            Cadena de entrada.
            Ejemplo:
            babc
        Returns
        -------
        devivacion : string
            Representación de las reglas a aplicar para derivar la cadena
            utilizando la gramática.
        -Método Parse, recibe como parámetro una cadena de texto, string.
        A partir de ese string devuelve una representación de las derivaciones
        que se harian a partir de la gramática que se está utilizando.
        Partiendo del distinguido, todas las reglas que se aplicarían
        hasta llegar a esa cadena. X=>X Y=>b Y=>b d
        """
        if (self.isLL1()):
            if es_LL1:
                for NT in self.no_terminales:
                    self.tabla[NT, '$'] = ([])
                    for term in self.terminales:
                        if term != 'lambda':
                            self.tabla[NT, term] = ([])
                            for NT in self.no_terminales:
                                self.tabla[NT, '$'] = ([])
                                for term in self.terminales:
                                    if term != 'lambda':
                                        self.tabla[NT, term] = ([])
                                        contador = 0
                                        lista = self.selects
                                        for sublista in lista:
                                            for select in sublista:
                                                self.tabla[self.antecedentes[contador], select] = self.consecuentes[
                                                    contador]
                                            contador = contador + 1

        c_en = cadena.split(" ")
        derivaciones = self.distinguido
        pila = []
        pila.append('$')
        pila.append(self.distinguido)
        lookahead = c_en[0]
        es_r = 1
        es_a = 0
        aux = []

        while es_r:
            tope = pila[-1]
            if tope in self.no_terminales and (lookahead in self.terminales or lookahead == '$'):
                consecuente = self.tabla[tope, lookahead]
                if len(consecuente) != 0:
                    if 'lambda' in consecuente:
                        pila.pop()
                    else:
                        pila.pop()
                        for item in reversed(consecuente):
                            pila.append(item)
                else:
                    es_r = False
                if es_r:
                    derivaciones = derivaciones + "=>"
                    for x in aux:
                        if x != "$":
                            derivaciones = derivaciones + x
                    for item in reversed(pila):
                        if item != '$':
                            derivaciones = derivaciones + x
                    if derivaciones[-1] == " ":
                        derivaciones = derivaciones[:-1]
            else:  # si en tope pila hay terminal o $
                if tope == lookahead:
                    pila.pop()
                    aux.append(lookahead)
                    entrada.pop(0)  # consumir de la entrada
                    if tope == '$' and lookahead == '$':
                        es_a = 1
                    else:
                        lookahead = entrada[0]
                else:
                    es_r = 0
            if es_a:
                break
        return derivaciones