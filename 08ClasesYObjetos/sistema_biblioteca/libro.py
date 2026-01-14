class Libro:
    def __init__(self, titulo, autor, genero):
        self._titulo = titulo
        self._autor = autor
        self._genero = genero

    #Getters
    @property #Solo lectura, no se modifica
    def titulo(self):
        return self._titulo
    @property
    def autor(self):
        return self._autor
    @property
    def genero(self):
        return self._genero