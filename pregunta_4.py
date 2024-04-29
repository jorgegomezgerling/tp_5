# 4. Modifique el programa IS2_taller_scanner.py para que además la secuencia de barrido de radios que tiene incluya la sintonía de una serie de frecuencias memorizadas tanto de AM como de FM. Las frecuencias estarán etiquetadas como M1, M2, M3 y M4. Cada memoria podrá corresponder a una radio de AM o de FM en sus respectivas frecuencias específicas. En cada ciclo de barrido se barrerán las cuatro memorias. 

import os

#*--------------------------------------------------------------------
#* Ejemplo de design pattern de tipo state
#*--------------------------------------------------------------------
"""State class: Base State class"""
class State:

    def __init__(self, radio):
        self.radio = radio

    def scan(self):
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print("Sintonizando... Estación {} {}".format(self.stations[self.pos], self.name))

    def toggle_amfm(self):
        pass

#*------- Implementa como barrer las estaciones de AM
class AmState(State):

    def __init__(self, radio):
        super().__init__(radio)
        self.stations = ["1250", "1380", "1510", "M1", "M2", "M3", "M4"]
        self.pos = 0
        self.name = "AM"

    def toggle_amfm(self):
        print("Cambiando a FM")
        self.radio.state = self.radio.fmstate

#*------- Implementa como barrer las estaciones de FM
"""Separate class for FM state"""
class FmState(State):

    def __init__(self, radio):
        super().__init__(radio)
        self.stations = ["81.3", "89.1", "103.9", "M1", "M2", "M3", "M4"]
        self.pos = 0
        self.name = "FM"

    def toggle_amfm(self):
        print("Cambiando a AM")
        self.radio.state = self.radio.amstate

#*--------- Construye la radio con todas sus formas de sintonía
class Radio:

    def __init__(self):
        self.fmstate = FmState(self)
        self.amstate = AmState(self)
        self.state = self.fmstate  # Inicialmente en FM

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()


#*---------------------

if __name__ == "__main__":
    os.system("clear")
    print("\nCrea un objeto radio y almacena las siguientes acciones")
    radio = Radio()
    actions = [radio.scan] * 7 + [radio.toggle_amfm] + [radio.scan] * 7  # Scan 7 stations, toggle AM/FM, then scan 7 more stations
    actions *= 2  # Repeat the sequence

    #*---- Recorre las acciones ejecutando la acción
    print("Recorre las acciones ejecutando la acción, el objeto cambia la interfaz según el estado")
    for action in actions:
        action()
