# 5. Modifique el programa IS2_taller_memory.py para que la clase tenga la capacidad de almacenar hasta 4 estados en el pasado y pueda recuperar los mismos en cualquier orden de ser necesario. El método undo deberá tener un argumento adicional indicando si se desea recuperar el inmediato anterior (0) y los anteriores a el (1,2,3). 

import os

#*--------------------------------------------------------------------
#* Design pattern memento, ejemplo
#*-------------------------------------------------------------------
class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content


class FileWriterUtility:
    def __init__(self, file):
        self.file = file
        self.content = ""
        self.history = []  # Historial de estados

    def write(self, string):
        self.content += string

    def save(self):
        if len(self.history) < 4:  # Guardar hasta 4 estados en el historial
            self.history.append(Memento(self.file, self.content))
        else:
            del self.history[0]  # Si hay más de 4 estados, eliminar el más antiguo
            self.history.append(Memento(self.file, self.content))

    def undo(self, steps=1):
        if steps == 0:
            if self.history:
                memento = self.history[-1]  # Recuperar el estado más reciente
                self.file = memento.file
                self.content = memento.content
                del self.history[-1]
        elif steps <= len(self.history):
            memento = self.history[-steps]  # Recuperar estado anterior según el número de pasos
            self.file = memento.file
            self.content = memento.content
            del self.history[-steps:]

class FileWriterCaretaker:
    def save(self, writer):
        writer.save()

    def undo(self, writer, steps=1):
        writer.undo(steps)


if __name__ == '__main__':
    os.system("clear")
    print("Crea un objeto que gestionará la versión anterior")
    caretaker = FileWriterCaretaker()

    print("Crea el objeto cuyo estado se quiere preservar")
    writer = FileWriterUtility("GFG.txt")

    print("Se graba algo en el objeto y se salva")
    writer.write("Clase de IS2 en UADER\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional")
    writer.write("Material adicional de la clase de patrones\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional II")
    writer.write("Material adicional de la clase de patrones II\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional III")
    writer.write("Material adicional de la clase de patrones III\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se invoca al <undo> para recuperar el estado inmediato anterior")
    caretaker.undo(writer, 0)
    print("Se muestra el estado actual")
    print(writer.content + "\n\n")

    print("Se invoca al <undo> para recuperar los estados anteriores")
    caretaker.undo(writer, 3)  # Recuperar los últimos 3 estados
    print("Se muestra el estado actual")
    print(writer.content + "\n\n")
