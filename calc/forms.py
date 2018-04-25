from django import forms
from . import models
class CalcForm(forms.Form):
	glubina = forms.IntegerField(
		required=True,
		min_value=1000,
		max_value=3000,
		widget=forms.NumberInput(attrs={
			'class':'form-control'
		}))
	dgidromotor = forms.FloatField(
		required = True,
		min_value=0,
		max_value=10000,
		widget = forms.NumberInput(attrs={
			'class':'form-control'
		}))
		
	turboburtype = forms.ChoiceField(
		required = True,
		choices = ((i.id,i.name) for i in models.Turbobur.objects.all()),		
		widget = forms.Select(
			attrs={
				'class':'form-control'
			})
		)
	dstoyak = forms.ChoiceField(
		required = True,
		choices = ((i.id,i.diametr) for i in models.Stoyak.objects.all()),		
		widget = forms.Select(
			attrs={
				'class':'form-control'
			})
		)
	dburshlang = forms.ChoiceField(
		required = True,
		choices = ((i.id,i.diametr) for i in models.Burshlang.objects.all()),		
		widget = forms.Select(
			attrs={
				'class':'form-control'
			})
		)
	dvedtruba = forms.ChoiceField(
		required = True,
		choices = ((i.id,i.diametr) for i in models.Vedtruba.objects.all()),		
		widget = forms.Select(
			attrs={
				'class':'form-control'
			})
		)
	dvertlug = forms.ChoiceField(
		required = True,
		choices = ((i.id,i.diametr) for i in models.Vertlug.objects.all()),		
		widget = forms.Select(
			attrs={
				'class':'form-control'
			})
		)
	nasos_count = forms.IntegerField(
		required=True,
		min_value=1,
		max_value=5,
		widget=forms.NumberInput(attrs={
			'class':'form-control'
		}))
	nasos_type = forms.ChoiceField(
		required = True,
		choices =  ((i.id,i.name) for i in models.Nasos.objects.all()),
		widget = forms.Select(
			attrs={
				'class':'form-control rounded-right'
			})
		)
	d_bt = forms.FloatField(
		required=True,
		min_value=0,
		max_value=100000,
		widget=forms.NumberInput(attrs={
			'class':'form-control'
		}))
	t_bt = forms.FloatField(
		required=True,
		min_value=0,
		max_value=100000,
		widget=forms.NumberInput(attrs={
			'class':'form-control'
		}))

	d_ubt = forms.FloatField(
		required=True,
		min_value=0,
		max_value=100000,
		widget=forms.NumberInput(attrs={
			'class':'form-control'
		}))
	vd_ubt = forms.FloatField(
		required=True,
		min_value=0,
		max_value=100000,
		widget=forms.NumberInput(attrs={
			'class':'form-control'
		}))
	dl_ubt = forms.FloatField(
		required=True,
		min_value=0,
		max_value=100000,
		widget=forms.NumberInput(attrs={
			'class':'form-control'
		}))

	dl_nt = forms.FloatField(
		required=True,
		min_value=0,
		max_value=100000,
		widget=forms.NumberInput(attrs={
			'class':'form-control'
		}))
	d_nt = forms.FloatField(
		required=True,
		min_value=0,
		max_value=100000,
		widget=forms.NumberInput(attrs={
			'class':'form-control'
		}))
	t_nt = forms.FloatField(
		required=True,
		min_value=0,
		max_value=100000,
		widget=forms.NumberInput(attrs={
			'class':'form-control'
		}))
