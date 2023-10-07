#Automate fini déterminant
class Etat:
    def __init__(self): 
        self.transitions = []
    
    def add_transitions(self, transitions): # Cette fonction évite un bug de définition du variable
        for i in transitions:#(état d'estination, lettre)
            assert isinstance(i, tuple) # Check the elements
            self.transitions.append(i)

    def move(self, lettre):
        for i in self.transitions:
            if i[1] == lettre:
                return i[0]
        return None

class AFD:
    def __init__(self, initial:Etat, terminal:list, sigma:list):
        self.inital = initial
        self.terminal = terminal
        self.sigma = sigma
    
    @staticmethod
    def delta(etat, lettre):
        return etat.move(lettre)
    
    def __isinsigma(self, lettre):
        return lettre in self.sigma

    def __isterminal(self, etat):
        return etat in self.terminal
    
    def reconnaitre(self, mot):
        current = self.inital
        for i in mot:
            if not self.__isinsigma(i):
                print("Ce mot ne peut pas reconnu par cet AFD : lettre inconnu.")
                return
            current = AFD.delta(current, i)
            if not current:
                print("Ce mot ne peut pas reconnu par cet AFD : lecture incomplet.")
                return
        if self.__isterminal(current):
            print("Félicitations ! Ce mot est reconnu par cet AFD !")
            return
        else:
            print("Ce mot ne peut pas reconnu par cet AFD : terminal incorrect.")
            return
        

        
#Figure 5.2
zero = Etat() 
un = Etat()
deux = Etat()
zero.add_transitions([(zero, 'b'), (un, 'a')])
un.add_transitions([(zero, 'b'), (deux, 'a')])
deux.add_transitions([(deux, 'a'), (deux, 'b')])         

example = AFD(zero, [deux], ['a', 'b'])
example.reconnaitre('abbv')


        
