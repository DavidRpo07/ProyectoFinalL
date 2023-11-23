import random

class Concursante:
    def __init__(self, nombre, ID, numero, duracion, se_retiro, comodines_elegidos):
        self.nombre = nombre
        self.ID = ID
        self.numero = numero
        self.duracion = duracion
        self.se_retiro = se_retiro
        self.comodines_elegidos = comodines_elegidos

    def calcular_premio(self):
        if self.se_retiro:
            return premios[self.numero]
        else:
            if 0 <= self.numero <= 4:
                return 0
            elif 5 <= self.numero <= 9:
                return 1000000
            elif 10 <= self.numero <= 14:
                return 10000000
            elif self.numero == 15:
                return 300000000
            else:
                return 0

    def __str__(self):
        return f"Nombre: {self.nombre}, ID: {self.ID}, Última pregunta correcta: {self.numero}, Premio: {self.calcular_premio()}, Se demoró {self.duracion} en minutos en resolver la pregunta clasificatoria, Se Retiró: {self.se_retiro}, Comodines Elegidos: {', '.join(self.comodines_elegidos)}"

class DiaSemana:
    def __init__(self, numero_dia, *participantes):
        self.numero_dia = numero_dia
        self.participantes = participantes
        self.total_premios = self.calcular_total_premios()

    def calcular_total_premios(self):
        return sum(participante.calcular_premio() for participante in self.participantes)

    def __str__(self):
        titulo = f"Día {self.numero_dia}"
        participantes_info = '\n'.join(str(participante) for participante in self.participantes)
        return f"{titulo}\n{participantes_info}\nTotal de premios: {self.total_premios}\n------------"

class Nodo:
    def __init__(self, dia_semana):
        self.dia_semana = dia_semana
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_nodo(self, nodo):
        if not self.cabeza:
            self.cabeza = nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nodo

    def imprimir_lista(self):
        actual = self.cabeza
        while actual:
            print(str(actual.dia_semana))
            actual = actual.siguiente

    def sumar_premios_totales(self):
        total = 0
        actual = self.cabeza
        while actual:
            total += actual.dia_semana.total_premios
            actual = actual.siguiente
        return total

def generar_datos_aleatorios(num_dias=5, participantes_por_dia=2):
    comodines_ayuda = ["llamada a un amigo", "pregunta al público", "50/50"]
    nombres = ['Alejandro', 'Berenice', 'Carlos', 'David', 'Juan', 'Fernando', 'María', 'Juana', 'Isabel', 'Jerónimo',
               'Kelly', 'Luis', 'Mario', 'Natalia', 'Olivia', 'Pablo', 'Daniel', 'Ricardo', 'Samuel', 'Camila']

    datos_aleatorios = []
    for _ in range(num_dias):
        participantes_dia = []
        for _ in range(participantes_por_dia):
            nombre = random.choice(nombres)
            numero = random.randint(1, 15)
            id = random.randint(1, 100)
            duracion = random.randint(1, 5)
            se_retiro = random.choice([True, False])

            comodines_elegidos = random.sample(comodines_ayuda, k=random.randint(0, 3))

            concursante = Concursante(nombre, id, numero, duracion, se_retiro, comodines_elegidos)
            participantes_dia.append(concursante)

        datos_aleatorios.append(participantes_dia)

    return datos_aleatorios

premios = {
    15: 300000000,
    14: 100000000,
    13: 50000000,
    12: 20000000,
    11: 12000000,
    10: 10000000,
    9: 7000000,
    8: 5000000,
    7: 3000000,
    6: 2000000,
    5: 1000000,
    4: 500000,
    3: 300000,
    2: 200000,
    1: 100000
}

datos_aleatorios = generar_datos_aleatorios(num_dias=5, participantes_por_dia=2)
lista_enlazada = ListaEnlazada()

dia = 1
for participantes_dia in datos_aleatorios:
    dia_semana = DiaSemana(dia, *participantes_dia)
    nodo = Nodo(dia_semana)
    lista_enlazada.agregar_nodo(nodo)
    dia += 1



lista_enlazada.imprimir_lista()


suma_premios = lista_enlazada.sumar_premios_totales()
print(f"\nSuma total de premios de los 5 días de concurso: {suma_premios}")