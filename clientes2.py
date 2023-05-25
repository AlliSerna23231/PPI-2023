class Cliente2:

    def __init__(self, nombre,
                apellido,
                documento,
                fnacimiento,
                Genero,
                grado,
                ):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.fnacimiento = fnacimiento
        self.Genero = Genero
        self.grado = grado

    def __str__(self):
        return f"Nombre: {self.nombre} Documento: {self.documento}"