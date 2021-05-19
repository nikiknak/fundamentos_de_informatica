class Enterprise :

	def __init__ ( self ) :

		self.potencia_maxima = 100
		self.coraza_maxima = 20
		self._coraza = 5
		self._potencia = 50

	def potencia(self):
		return self._potencia

	def coraza(self):
		return self._coraza

	def encontrarPilaAtomica(self):
		self._potencia = self._potencia + 25

		if self._potencia > self.potencia_maxima :
			self._potencia = self.potencia_maxima


	def encontrarEscudo(self):
		self._coraza = self._coraza + 10

		if self._coraza > self.coraza_maxima :
			self._coraza = self.coraza_maxima


	def recibirAtaque(self, puntos):

		if puntos > self._coraza :

			no_alcanzo = puntos - self._coraza
			self._coraza = 0

			self._potencia = self._potencia - no_alcanzo

			if self._potencia < 0 :
				self._potencia = 0

		else :

			self._coraza = self._coraza - puntos

			if self._coraza < 0 :
				self._coraza = 0

	def fortalezaDefensiva(self) :
		return self._coraza + self._potencia

	def necesitaFortalecerse(self):
		if self._coraza == 0 and self._potencia < 20 :
			return true
		else:
			return false

	def fortalezaOfensiva(self) :
		if self._potencia < 20 :
			return 0
		else :
			return ( self._potencia - 20 ) / 2 

enterprise = Enterprise ()
enterprise.encontrarPilaAtomica()
enterprise.recibirAtaque(14)
enterprise.encontrarEscudo()

print (enterprise.potencia())
print (enterprise.coraza())



