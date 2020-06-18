producciones = []
lista=[]
first=[]
flag_first= False
follow=[]
flag_follow= False
select=[]
reservadas = ["lambda"]
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
            #producciones= gramatica.split(':')
            self.gramatica = gramatica
            # self.producciones=gramatica.split ("\n")
            # print (self.producciones)

            for x in self.gramatica:
                reglaindividual = x.split(':')  # Divido Antecedente de Consecuente
                antecedente = reglaindividual[0]
                print(reglaindividual)
                consecuente = reglaindividual[1].split()
                # producciones=x.split(':')#Así formamos la lista de todas las producciones que contienen a la regla
                diccionarioantecedente = dict.fromkeys(antecedente)

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
    indice = 0
    union = []
    print('REGLAS')
    print(reglas)
    for r in reglas:  # Por cada regla
        primeros.clear()
        reglaActual = r
        divisionAC = r.split(":")  # Divido antecedente del consecuente
        consecuentes = divisionAC[1].split()  # Armo una lista con cada elemento del consecuente para esa regla
        primer_consecuente = list(consecuentes[0])
        if str.isupper(primer_consecuente[0]):  # Si la primera letra del primer consecuente empieza con mayúscula, es NT.
            no_terminal = consecuentes[0] #Guardo el no terminal en una variable.
            aux_first = buscar_terminal(no_terminal, r, reglas)  # Busco los first del no terminal que tengo como first.
            for a in aux_first:
                if a not in FirstPorRegla:
                    union.append(a)
            cadena_final = " ".join(union)
            FirstPorRegla.insert(indice, cadena_final)
        else:  # Si no comienza con mayúsculas, es un terminal -> ya tenemos el first de la regla.
            if consecuentes[0] == 'lambda':
                terminal = 'lambda'
            else:
                terminal = consecuentes[0]
            FirstPorRegla.insert(indice, terminal) #Agrego en la posición indicada el terminal que es el first.
        indice += 1
    return FirstPorRegla  # lista de first para cada antecedente

def calc_follow(reglas):
    siguientes=[]
    indice=0
    #siguientes.append('$')
    for r in reglas:  # Se usa para recorrer todas las reglas
        antecedenteconsecuente=r.split(":")
        consecuente=antecedenteconsecuente[1].split()
        #print(antecedenteconsecuente[0])
        #print(consecuente[0])
        primer_antecedente= list(antecedenteconsecuente[0])
        primer_consecuente = list(consecuente[0])
        antecedente=primer_antecedente[0]
        #print (primer_consecuente)
        if primer_antecedente[0]==antecedente:
            siguientes.append('$')
        if str.isupper(primer_antecedente[0]): # Si la primera letra del primer antecendente empieza con mayúscula, es NT.
            no_terminal = antecedenteconsecuente[0]
            #ind=0
            for x in consecuente:
                if x==no_terminal:
                    if x == consecuente[-1]:  # Si es el último elemento
                        calc_follow(reglas)
                    else:
                        ind=0
                        elemento_siguiente = list(consecuente[ind + 1])
                        if str.isupper(elemento_siguiente[0]): #Si es Mayuscula -> Buscar first
                            #siguientes.append(first(no_terminal[r]))
                        else:
                            if str.islower(consecuente[ind + 1]):  # Si es minuscula, es terminal
                                terminal = consecuente[ind + 1]
                                if terminal not in siguientes:
                                    siguientes.append(terminal)
                    ind = ind + 1
                    indice= indice +1
    return siguientes

    def buscar_terminal(noterminal, regla, producciones):
        concate = []
        concat = []
        primeros = []
        divisionRegla = regla.split(":")  # Divido la regla original en antecedente y consecuente
        divisionConsecuenteRegla = divisionRegla[1].split()  # Divido el consecuente en una lista. Cada pos un elemento.
        for p in producciones:  # por cada producción
            antecedenteconsecuente = p.split(":")  # Divido antecedente del consecuente
            consecuente = antecedenteconsecuente[1].split()  # Divido los consecuentes de esa regla.
            if antecedenteconsecuente[
                0] == noterminal:  # Si el antecedente es igual al no terminal que traigo del otro método
                if str.islower(consecuente[0]):  # Si el primer consecuente es minúsculas
                    if consecuente[0] == 'lambda':  # Si es igual a lambda, veo si sigue en la regla original otra cosa.
                        ind = 0
                        for x in divisionConsecuenteRegla:  # por cada consecuente de la regla original, pregunto si es igual al NT, para id si es el ultimo
                            if x == noterminal:
                                if x == divisionConsecuenteRegla[
                                    -1]:  # Si es el último elemento de la lista, significa que no viene más nada
                                    terminal = 'lambda'
                                    if terminal not in primeros:  # Guardo lambda en la lista de first.
                                        primeros.append(terminal)
                                else:  # Si ese NT no es el último elemento, puede venir otro NT o un terminal.
                                    elemento_siguiente = list(divisionConsecuenteRegla[ind + 1])
                                    if str.isupper(elemento_siguiente[0]):  # Si es mayúscula, calcular firsts.
                                        auxiliar = buscar_terminal(divisionConsecuenteRegla[ind + 1], regla,
                                                                   producciones)
                                        for u in auxiliar:
                                            if u not in primeros:
                                                concat.append(u)
                                        auxiliar2 = " ".join(concat)
                                        primeros.append(auxiliar2)
                                    else:  # Es minúsculas, se agrega directamente.
                                        terminal = divisionConsecuenteRegla[x + 1]
                                        if terminal not in primeros:  # Lo agrego a los first
                                            primeros.append(terminal)
                            ind = ind + 1
                    else:  # Si es distinto de lambda
                        terminal = consecuente[0]
                        if terminal not in primeros:
                            primeros.append(terminal)
                else:
                    elemento = list(consecuente[0])
                    if str.isupper(elemento[0]):
                        auxiliar3 = buscar_terminal(consecuente[0], p, producciones)  # ver que cambia si pongo p o r
                        for m in auxiliar3:
                            if m not in primeros:
                                concate.append(m)
                        auxiliar3 = " ".join(concate)
                        primeros.append(auxiliar3)
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

reglas = "S:A B\nA:a A\nA:c\nA:lambda\nB:b B\nB:d"
producciones = reglas.split("\n")  # La lista reglas tiene 4 posiciones (regla, firsts, follows y select) por cada posicion
Gramatica(producciones)

