producciones = []
lista = []
first = []
follow = []
select = []
reservadas = ["lambda"]


class Gramatica:

    def __init__(self, gramatica,first):
        """Constructor de la clase.
        Parameters
        ----------
        gramatica : string
            Representación de las producciones de una gramática determinada.
            Ejemplo:
            "A:b A\nA:a\nA:A B c\nA:lambda\nB:b"
        """
        # gramatica = 'X:X Y\nX:e\nX:b\nX:lambda\nY:a\nY:d'
        producciones = gramatica.split('\n')  # Genera una lista con cada producción
        self.gramatica = producciones
        #self.first = first  # lista de first.
        #self.first = Gramatica.calc_first(producciones)  # lista de first.

        """
        lista = gramatica.split('\n')  # Genera una lista con cada producción
        for p in lista:
            producciones[p] = Gramatica(lista[p], [], [], [])
            first[p] = []
            follow[p] = []
            select[p] = []
        self.gramatica = lista #tengo guardado una lista con cada producción, y paralelamente una lista de f,f y s.
        #print(producciones)
        """


def calc_first(reglas):  # calculo de first para una regla pasada como parámetro.
    primeros = []
    FirstPorRegla = []
    indice=0
    concatenacion = []
    print('REGLAS')
    print(reglas)
    for r in reglas:  # Por cada regla
        primeros.clear()
        divisionAC = r.split(":")  # Divido antecedente del consecuente
        #print (divisionAC)
        divisionConsecuente = divisionAC[1].split()  # Armo una lista con cada elemento del consecuente para esa regla
        reglaActual = r
        if str.isupper(divisionConsecuente[0]):  # Si el primer elemento del consecuente es un NT, busco los first de ese NT.
            no_terminal = divisionConsecuente[0]
            aux_first = buscar_terminal(no_terminal, r, reglas)  # devuelve lista con firsts. Le paso como parámetro ese NT, la regla que estoy evaluando y la gramática completa.
            for a in aux_first:
                if a not in FirstPorRegla:
                    concatenacion.append(a)
            StrC = " ".join(concatenacion)
            FirstPorRegla.insert(indice, StrC)
            #FirstPorRegla.insert(indice, primeros)  # En la posición r, inserto los first. Por cada pos voy a tener los first de cada regla.
        else:  # Sino, significa que ya tenemos el first de la regla.
            if divisionConsecuente[0] == reservadas[0]:  # Si el terminal es lambda, lo guardo
                terminal = reservadas[0]
            else:
                terminal = divisionConsecuente[0]  # Si no es lambda, lo guardo tmb
            FirstPorRegla.insert(indice, terminal)
        indice = indice + 1
    return FirstPorRegla  # lista de first para cada antecedente
    # REVISAR METODO


def buscar_terminal(noterminal, regla, producciones):
    concat = []
    primeros = []
    divisionRegla = regla.split(":") #Divido la regla original en antecedente y consecuente
    divisionConsecuenteRegla = divisionRegla[1].split() #Divido el consecuente en una lista. Cada pos un elemento.
    for p in producciones: #por cada producción
        antecedenteconsecuente = p.split(":")  # Divido antecedente del consecuente
        consecuente = antecedenteconsecuente[1].split()  # Divido los consecuentes de esa regla.
        if antecedenteconsecuente[0] == noterminal:  #Si el antecedente es igual al no terminal que traigo del otro método
            if str.islower(consecuente[0]):
                if consecuente[0] == 'lambda':
                    #ver si despues de esa regla sigue un NT.
                    ind = 0
                    for x in divisionConsecuenteRegla: #por cada consecuente, pregunto si es igual al NT
                        if x == noterminal:
                            if x == divisionConsecuenteRegla[-1]: #Si es el último elemento
                                terminal = 'lambda'
                                if terminal not in primeros:
                                    primeros.append(terminal)
                            else: #Si ese NT no es el último elemento, puede venir otro NT o un terminal.
                                if str.islower(divisionConsecuenteRegla[ind+1]): #Si es minuscula, es terminal
                                    terminal = divisionConsecuenteRegla[ind+1]
                                    if terminal not in primeros:
                                        primeros.append(terminal)
                                else: #Es mayuscula.
                                    auxiliar = buscar_terminal(divisionConsecuenteRegla[ind+1], regla, producciones)
                                    for u in auxiliar:
                                        if u not in primeros:
                                            concat.append(u)
                                    auxiliar2 = " ".join(concat)
                                    primeros.append(auxiliar2)
                        ind = ind + 1
                else:
                    terminal = consecuente[0]
                    if terminal not in primeros:
                        primeros.append(terminal)
            if str.isupper(consecuente[0]): #Si el primer consecuente es un NO TERMINAL.
                buscar_terminal(consecuente[0], p, producciones)
    return primeros


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
        De ahí, mirar selects y y ver si son o no disyuntos: de ahí el booleano.

        """

    def terminal_es_lambda(regla):
        temp = producciones[regla]
        temp2 = producciones[regla].split(':')
        temp3 = temp2[1].split()  # En elemento 0 tengo el primer consecuente
        if temp3[0] == 'lambda':
            return True
        else:
            return False

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
        pass

#reglas = "S:A B\nA:a A\nA:c\nA:lambda\nB:b B\nB:d"
#reglas = "S:X Y Z\nX:a\nX:b\nX:lambda\nY:a\nY:d\nY:lambda\nZ:e\nZ:f\nZ:lambda"
reglas = 'S:A b\nS:B a\nA:a A\nA:a\nB:a'

producciones = reglas.split("\n")  # La lista reglas tiene 4 posiciones (regla, firsts, follows y select) por cada posicion
#print(producciones)
print(' ')
print('-------------- F I R S T S ---------------')
print(' ')
print(calc_first(producciones))

