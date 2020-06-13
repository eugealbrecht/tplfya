producciones = []
lista=[]
first=[]
follow=[]
select=[]
reservadas = ["lambda"]
class Gramatica():

    def calc_first(reglas):  # calculo de first para una regla pasada como parámetro.
        global Agregar_First
        first = []
        Agregar_First = True
        divisionAC = []
        divisionConsecuente = []
        FirstPorRegla = []

        for r in reglas: #Por cada regla
            divisionAC = reglas[r].split(":") #Divido antecedente del consecuente
            divisionConsecuente = divisionAC[1].split() #Armo una lista con cada elemento del consecuente para esa regla
            if str.isupper(divisionConsecuente[0]): #Si el primer elemento del consecuente es un NT, busco los first de sus reglas
                no_terminal = divisionConsecuente[0]
                #buscar_terminal(no_terminal, regla_temporal) #VER
            else: #Sino, significa que ya tenemos el first de la regla.
                if divisionConsecuente[0] == reservadas[0]:
                    terminal = reservadas[0]
                else:
                    terminal = divisionConsecuente[0]
                if terminal not in first:
                    first.append(terminal)
            FirstPorRegla.append(first)
         return FirstPorRegla


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
        self.first = Gramatica.calc_first(producciones #lista de first.

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


    def calc_follow(self):

    def calc_select(self):


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




