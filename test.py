class Computer:
	tastatur = False
	strom = 750
	eingeschalten = False
	desktopBereit = False

	def checkTastatur(self):
		return self.tastatur

	def einschalten(self):
		if 500 < self.strom < 900:
			self.einschalten = True
			self.bootVorgang()

	def bootVorgang(self):
		if self.tastatur:
			self.desktopBereit = True
		else:
			self.ausschalten()

	def ausschalten(self):
		self.eingeschalten = False
		self.desktopBereit = False



x = 100

while x >= 49:
	if x % 2 == 0:
		x = x-3
	else:
		x = x-5

print x
