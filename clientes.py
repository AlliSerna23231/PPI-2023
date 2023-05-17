class Cliente:

    def __init__(self, nombreCompleto,
                usuario,
                password1,
                documento,
                correo,
                contacto,
                direccion,
                genero,
                cargo,
                ):
        self.nombreCompleto = nombreCompleto
        self.usuario = usuario
        self.password1 = password1
        self.documento = documento
        self.correo = correo
        self.contacto = contacto
        self.direccion = direccion
        self.genero = genero
        self.cargo = cargo

    def __str__(self):
        return f"Nombre: {self.nombreCompleto} Documento: {self.documento}"