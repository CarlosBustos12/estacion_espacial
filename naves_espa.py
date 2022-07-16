class Naves:
    def __init__(self, nombre, tipo_de_nave, pais, combustible, actividad, peso):
        self.nombre=nombre
        self.tipo_de_nave=tipo_de_nave
        self.pais=pais
        self.combustible=combustible
        self.actividad=actividad
        self.peso=peso
    def datos(self):
        
        return{
            'nombre':self.nombre,
            'tipo_de_nave':self.tipo_de_nave,
            'pais':self.pais,
            'combustible':self.combustible,
            'actividad':self.actividad,
            'peso':self.peso

        }