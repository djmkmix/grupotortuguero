from django import forms


class addProductForm(forms.Form):

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

	imagen			= forms.ImageField(widget=forms.FileInput())
	nombre			= forms.CharField(widget=forms.TextInput())
	especie			= forms.ChoiceField(choices=ESPECIE, widget=forms.Select())
	sexo			= forms.ChoiceField(choices=SEXO, widget=forms.Select())
	sitioMonitoreo	= forms.CharField(widget=forms.TextInput())
	localizacion	= forms.CharField(widget=forms.TextInput())
	longitud		= forms.CharField(widget=forms.TextInput())
	latitud			= forms.CharField(widget=forms.TextInput())
	marea			= forms.ChoiceField(choices=MAREA, widget=forms.Select())
	metodo			= forms.ChoiceField(choices=METODO, widget=forms.Select())
	placas			= forms.ChoiceField(choices=PLACAS, widget=forms.Select())
	dernueva		= forms.CharField(widget=forms.TextInput())
	izqnueva		= forms.CharField(widget=forms.TextInput())
	dervieja		= forms.CharField(widget=forms.TextInput())
	izqvieja		= forms.CharField(widget=forms.TextInput())
	region			= forms.CharField(widget=forms.TextInput())
	LRC 			= forms.CharField(widget=forms.TextInput())
	LCC 			= forms.CharField(widget=forms.TextInput())
	ARC 			= forms.CharField(widget=forms.TextInput())
	ACC 			= forms.CharField(widget=forms.TextInput())
	LP 				= forms.CharField(widget=forms.TextInput())
	LTC 			= forms.CharField(widget=forms.TextInput())
	PC 				= forms.CharField(widget=forms.TextInput())
	peso	 		= forms.CharField(widget=forms.TextInput())

	def clean(self):
		return self.cleaned_data
