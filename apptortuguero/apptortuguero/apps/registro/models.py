#encoding:utf-8
from django.db import models



class Responsable(models.Model):
	nombre = models.CharField(max_length=200)
	identificacion = models.CharField(max_length=200)

	def __unicode__(self):
		return self.nombre

class Tortugas(models.Model):
	CM		='Verde/Negra'
	EI		='Carey'
	LO		='Golfina'
	DE		='Laud'
	DC		='Amarilla'

	M		='Masculino'
	F		='Femenino'
	I		='Indefinido'

	SUBIENDO ='Subiendo'
	BAJANDO	='Bajando'

	RED 	='Red'
	AMANO	='A Mano'

	PLASTICO='Plastico'
	METAL	='Metal'

	ESPECIE = (
		(CM, 'Verde/Negra'),
		(EI, 'Carey'),
		(LO, 'Golfina'),
		(DE, 'Laud'),
		(DC, 'Amarilla'),
	)

	SEXO = (
		(M, 'Masculino'),
		(F, 'Femenino'),
		(I, 'Indefinido'),
	)

	MAREA = (
		(SUBIENDO, 'Subiendo'),
		(BAJANDO, 'Bajando'),
	)

	METODO = (
		(RED, 'Red'),
		(AMANO, 'A Mano'),
	)

	PLACAS = (
		(PLASTICO, 'Plastico'),
		(METAL, 'Metal'),
	)

	imagen 			= models.ImageField(upload_to='images/perfil', verbose_name='imagentortuga', null = True, blank = True)
	nombre			= models.CharField(max_length=200)
	especie 		= models.CharField(max_length=100, choices=ESPECIE,blank = True)
	sexo 			= models.CharField(max_length=100,choices=SEXO, blank = True)
	responsable		= models.ForeignKey(Responsable)
	tiempo_reg		= models.DateTimeField(auto_now=True)
	sitioMonitoreo 	= models.CharField(max_length=200)
	localizacion 	= models.CharField(max_length=200)
	longitud		= models.CharField(max_length=200)
	latitud			= models.CharField(max_length=200)
	marea 			= models.CharField(max_length=100,choices=MAREA, blank = True)
	metodo 			= models.CharField(max_length=100,choices=METODO, blank = True)
	placas 			= models.CharField(max_length=100,choices=PLACAS, blank = True)
	dernueva		= models.CharField(max_length=200)
	izqnueva		= models.CharField(max_length=200)
	dervieja		= models.CharField(max_length=200)
	izqvieja		= models.CharField(max_length=200)
	region 			= models.CharField(max_length=200)
	status			= models.BooleanField(default=True)
	LRC 			= models.CharField(max_length=200)
	LCC 			= models.CharField(max_length=200)
	ARC 			= models.CharField(max_length=200)
	ACC 			= models.CharField(max_length=200)
	LP 				= models.CharField(max_length=200)
	LTC 			= models.CharField(max_length=200)
	PC 				= models.CharField(max_length=200)
	peso 			= models.CharField(max_length=200)

	def __unicode__(self):
			tortugainfo = " Nombre: %s  Sexo: %s  Especie: %s  Hora de Registro: %s  Region: %s"%(self.nombre,self.sexo,self.especie,self.tiempo_reg,self.region)
			return tortugainfo
