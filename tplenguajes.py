producciones = []
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
        #print(producciones)

    def isLL1(self):
        """Verifica si una gramática permite realizar derivaciones utilizando
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

    def calc_first(indice_regla):  # calculo de first para una regla pasada como parámetro.
        global Agregar_First
        firsts = []
        Agregar_First = True
        terminal = ''
        Regla_Temporal = producciones[indice_regla]
        temporal = []
        temporal2 = []

        temporal = producciones[indice_regla].split(':') #divide antecedente de consecuente. Pos 0 ant, pos 1 cons
        temporal2 = temporal[1].split() #divide en una lista cada elemento del consecuente

        if str.isupper(temporal2[0]):  # Si el primer consecuente es un NT, busco los firsts de sus reglas.
            no_terminal = temporal2[0] #VER
            #buscar_terminal(no_terminal, Regla_Temporal) #VER

        else:  # Sino, significa que ya tenemos el first de la regla. Si el primer consecuente es terminal, pertenece al first.
            terminal = temporal2[0]
            Terminal_lambda = terminal_es_lambda(terminal)
            if Terminal_lambda == True:  # Si el terminal es lambda
                terminal = 'lambda'
            if terminal not in firsts:
                firsts.append(terminal)

        Agregar_First = False
        return firsts


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




