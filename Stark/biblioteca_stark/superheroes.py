from biblioteca_stark.funciones import *
class SuperHeroes:
    def __init__(self, lista_personajes):
        self.lista_personajes = lista_personajes

    def ordenar_por_nombre(self):
        """
        Ordena la lista de superhéroes por el nombre de manera ascendente.
        """
        return ordenar_por_nombre(self.lista_personajes, 'nombre')

    def mostrar_superheroes_en_tabla(self):
        """
        Imprime los datos de los superhéroes en formato de tabla.
        """
        claves = ['nombre', 'identidad', 'empresa', 'altura', 'peso', 'genero', 'color_ojos', 'color_pelo', 'fuerza', 'inteligencia']
        mostrar_personajes_ordenados(self.lista_personajes, claves)
    def buscar_debil(self):
        """
        Busca al masculino mas debil y lo muestra
        """
        return buscar_debil(self.lista_personajes)
    def contar_por_color_ojos(self):
        """
        Muestra cuantos personajes hay de cada color de ojo
        """
        return contar_por_color_ojos(self.lista_personajes)
    def ordenar_por_color_pelo(self):
        """
        Muestra cuantos personajes hay de cada color de pelo
        """
        ordenar_por_color_pelo(self.lista_personajes)
    def ordenar_por_inteligencia(self):
        """
        Agrupa a los superheroes por nivel de inteligencia |Good|Average|High|
        """
        ordenar_por_inteligencia(self.lista_personajes)
    def promediar_fuerza_f(self):
        """
        Acumula la fuerza de los superheroes femeninos y hace el promedio
        """
        promediar_fuerza_f(self.lista_personajes)
    def superheroes_mas_fuertes(self):
        """
        Utiliza el promedio de fuerza de los superheroes femeninos y lo compara con la fuerza de todos los superheroes, para ver que heroes tienen mas fuerza que el promedio femenino
        """
        promedio_fuerza_f = promediar_fuerza_f(self.lista_personajes)
        superheroes_mas_fuertes(promedio_fuerza_f,self.lista_personajes)
    def calcular_y_agregar_imc(self):
        """
        Calcular el IMC de cada superhéroe y agregarlo a cada uno en el diccionario.
        Llama a las funciones externas que realizan los cálculos y la asignación.
        """
        calcular_y_agregar_imc(self.lista_personajes)
        