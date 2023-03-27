import random
class Pancakes:

	def __init__(self, pancakes):
		self.pancakes = pancakes
		self.orden = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n", "o", "p", "q", "r", "s", "t", "u", "v","w", "x", "y", "z"]

	def voltear(self, posicion, pancakes):
		return pancakes[0:len(pancakes)-posicion] + pancakes[len(pancakes)-posicion:len(pancakes)][::-1]

	def busqAmplitud(self, nodo):
		cola = [(nodo, [0])]		
		meta = self.orden[0:len(nodo)]
		nodos = 0
		while cola:
			pancakes, camino = cola.pop(0)
			if pancakes == meta:
				return " ".join(camino[1:])
			for i in range(2,len(pancakes)+1):
				if i == camino[-1]:
					continue
				pancake_volt = self.voltear(i, pancakes)
				cola.append((pancake_volt, camino + [str(i)]))

pancakes = ["a", "b", "c", "d", "e", "f"]
random.shuffle(pancakes)
print(f"Pancakes inicio: {pancakes}")
prueba = Pancakes(pancakes)
print(f"Solución: {prueba.busqAmplitud(pancakes)}")