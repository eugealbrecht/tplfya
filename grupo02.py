producciones = []
lista=[]
first=[]
follow=[]
select=[]
reservadas = ["lambda"]
class Gramatica():

    def __init__(self, gramatica):
        """Constructor de la clase.

        Parameters
        ----------
        gramatica : string
            Representación de las producciones de una gramática determinada.

            Ejemplo:
            "A:b A\nA:a\nA:A B c\nA:lambda\nB:b"
        """
        #gramatica = 'X:X Y\nX:e\nX:b\nX:lambda\nY:a\nY:d'
        producciones = gramatica.split('\n')  # Genera una lista con cada producción
        self.gramatica = producciones
        self.first = Gramatica.calc_first(producciones) #lista de first.


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
    divisionAC = []
    divisionConsecuente = []
    FirstPorRegla = []
    aux_first = []
    for r in reglas: #Por cada regla
        divisionAC = reglas[r].split(":") #Divido antecedente del consecuente
        divisionConsecuente = divisionAC[1].split() #Armo una lista con cada elemento del consecuente para esa regla
        reglaActual = r
        if str.isupper(divisionConsecuente[0]): #Si el primer elemento del consecuente es un NT, busco los first de ese NT.
            no_terminal = divisionConsecuente[0]
            aux_first = buscar_terminal(no_terminal, r, reglas) #devuelve lista con firsts. Le paso como parámetro ese NT, la regla que estoy evaluando y la gramática completa.
            for a in aux_first:
                primeros.append(a)
        else: #Sino, significa que ya tenemos el first de la regla.
            if divisionConsecuente[0] == reservadas[0]: #Si el terminal es lambda, lo guardo
                terminal = reservadas[0]
            else:
                terminal = divisionConsecuente[0] #Si no es lambda, lo guardo tmb
            if terminal not in primeros:
                primeros.append(terminal) #Si el terminal que encontré no está en la lista, lo agrego.
        FirstPorRegla.append(r, primeros) #En la posición r, inserto los first. Por cada pos voy a tener los first de cada regla.
    return FirstPorRegla #lista de first para cada antecedente
    #REVISAR METODO


def buscar_terminal(noterminal, regla, producciones):
    primeros = []
    antecedenteconsecuente = []
    consecuente = []
    for p in producciones:
        antecedenteconsecuente = p.split(":") #Divido antecedente del consecuente
        consecuente = antecedenteconsecuente[1].split() #Divido los consecuentes.
        if antecedenteconsecuente[0] == noterminal: #Si el antecedente es igual al no terminal que traigo del otro método
            if str.isupper(consecuente[0]): #Pregunto si es mayúscula -> No terminal. Repito proceso hasta encontrar un terminal.
                buscar_terminal(consecuente[0], producciones)
            else:
                if consecuente[0] == reservadas[0]: #Si es lambda, tengo que buscar de la regla original el que sigue.
                    terminal = reservadas[0]
                    #volver a la regla original y ver si desp del NT sigue otra cosa pq serían parte de los first tmb.
                    for x in range(0, len(regla)): #Por cada elemento de la regla original
                        if x == noterminal:
                            if x == regla[-1]: #Si ese NT era el último elemento de la lista.
                                break #VER QUE HACER
                            else:
                                if str.islower(regla[x+1]):
                                    primeros.append(regla[x+1])
                else:
                    terminal = consecuente[0] #Si no es lambda, lo agrego.
            primeros.append(terminal)
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
        temp3 = temp2[1].split() #En elemento 0 tengo el primer consecuente
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




