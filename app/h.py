
'''Videojuego de personaje y combate
- Herencia: Clase Pare - Base
- Encapsulamiento: Modificar la salud
'''
class Personaje():
    def __init__(self, nombre, salud, poder_ataque):
        self.nombre = nombre
        self.__salud = salud #Atributo Privado doble guio bajo al principio
        self.poder_ataque = poder_ataque

    def atacar(self, otro_personaje):

        otro_personaje.__salud -= self.poder_ataque
        print(f"{self.nombre} ataca a {otro_personaje.nombre} causando {self.poder_ataque} puntos de daño. ")

    

    def esta_vivo(self):
        return self.__salud > 0
    
    def __modificar_salud(self, cantidad):
        self.__salud += cantidad


    def obtener_salud(self):
        return self.__salud
    
    def __str__(self):
        return f'{self.nombre}: {self.__salud} HP.'
    
#------------------------------------------
#Herencia: clases hijas, dereivadas, subclases --- Polimorfismo

class Guerrero(Personaje):
    def __init__(self, nombre, salud, poder_ataque,tipo_arma):
        super().__init__(nombre, salud, poder_ataque)
        self.tipo_arma = tipo_arma

    def ataque_especial(self, otro_personaje):
        danio = self.poder_ataque * 2
        otro_personaje._Personaje_modificado_salud(-danio)
        print(f'{self.nombre} usa Espada Mortal contra {otro_personaje.nombre} causando {danio} de daño. ') 
    
class Mago(Personaje):
    def ataque_especial(self, otro_personaje): #Polimorfismo
        dano = self.poder_ataque * 3
        otro_personaje.salud -= dano
        print(f'{self.nombre} lanza un Hechizp de fuego {otro_personaje.nombre} causando {dano} de daño. ') 


class Arquero(Personaje):
    def ataque_especial(self, otro_personaje): #Polimorfismo
        dano = self.poder_ataque * 1.5
        otro_personaje.salud -= dano
        print(f'{self.nombre} dispara una flecha contra {otro_personaje.nombre} causando {dano} de daño.')


#----------------------------------------

def combate (personaje1, personaje2):
    print(f'\nComineca el combare entre {personaje1.nombre} y {personaje2.nombre}')

    while personaje1.esta_vivo() and personaje2.esta_vivo:
        personaje1.atacar(personaje2)
        if personaje2.esta_vivo():
            
            personaje2.ataque_especial(personaje1)
            print(personaje1)
            print(personaje2)
            print("\n")
        if personaje1.esta_vivo():
            print(f"¡{personaje1.nombre} gana el combate")
        else:
            print(f"¡{personaje2.nombre} gana el combate")

guerrero = Guerrero('Krull', 100, 15)

mago = Mago('Voldermor', 80, 20)

combate(guerrero, mago)             
'''

@property #Lo que hace es convertir el metodo privado para qeu la otra  persona pueda editar
def salud(self):
    return self.__salud

@salud.setter # esto perimite la modificacion
def salud(self, valor):
    if valor < 0:
        self.__salud = 0
    else:
        self.__salud = valor

'''
'''
print(f"Salud inicial de {guerrero.nombre}: {guerrero.salud} HP.")
print(f"Salud incial {mago.nombre}: {mago.salud} HP.")

guerreri.salud = -50
print(f"Salud final de {guerrero.nombre}: {guerrero.salud} HP.")
'''
print(guerrero._Personaje__salud)

#Herencias multiples 
#----------------------
class Volador():
    def volar(self):
        return 'Estoy volando'
    
    def desplazar(self):
        return 'Estoy volando'

class Nadador():
    def nadar(self):
        return 'Estoy Nadadando'
    
    def desplazar(self):
        return 'Estoy volando'

class Pato(Volador, Nadador):
    def sonido(self):
        return 'Cuac Cuac'
    
    def desplazar(self):
        return 'Estoy volando'
    

pato = Pato()
print(pato.volar())
print(pato.nadar())
print(pato.sonido())

print(pato.desplazar())

print(Pato.mro())
print(Pato.__mro__())


