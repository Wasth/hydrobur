from django.db import models


class Stoyak(models.Model):
	diametr = models.FloatField()
	coef = models.FloatField()

	def __str__(self):
		return str(self.diametr)+' - '+str(self.coef)


class Burshlang(models.Model):
	diametr = models.FloatField()
	coef = models.FloatField()

	def __str__(self):
		return str(self.diametr)+' - '+str(self.coef)


class Vertlug(models.Model):
	diametr = models.FloatField()
	coef = models.FloatField()

	def __str__(self):
		return str(self.diametr)+' - '+str(self.coef)


class Vedtruba(models.Model):
	diametr = models.FloatField()
	coef = models.FloatField()

	def __str__(self):
		return str(self.diametr)+' - '+str(self.coef)


class Nasos(models.Model):
	name = models.CharField(max_length=100)
	davl = models.FloatField()
	coef = models.FloatField()
	qd = models.FloatField()

	def __str__(self):
		return self.name


class Turbobur(models.Model):
	name = models.CharField(max_length=100)
	davl = models.FloatField()
	d = models.FloatField()
	pgr = models.FloatField()

	def __str__(self):
		return self.name


class Result(models.Model):
	author = models.CharField(max_length=100)
	result_datetime = models.DateTimeField()
	q = models.FloatField()
	p0 = models.FloatField()
	het = models.FloatField()
	ret = models.FloatField()
	hekp = models.FloatField()
	rekp = models.FloatField()
	psum = models.FloatField()
	razriv = models.FloatField()
	dn = models.FloatField()
	pdf = models.FloatField()

	def __str__(self):
		return self.author+' - '+str(self.result_datetime)