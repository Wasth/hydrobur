import math, datetime

from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.contrib import auth
from django.contrib.auth.models import User
from django.db import IntegrityError

from .forms import CalcForm
from .models import *


# Create your views here.
def index(request):
	return render(request, 'calc/index.html')


def calc(request):
	if request.user.is_authenticated:
		form = CalcForm()
		return render(request, 'calc/calc.html', {
			'calcform': form
		})
	else:
		raise Http404


def result(request, res_id=None):
	if request.user.is_authenticated:
		data = {}
		if request.method == "POST":

			form = CalcForm(request.POST)

			if form.is_valid():
				calc_data = form.cleaned_data
				print(calc_data)

				# вытаскиваем данные
				nasos = Nasos.objects.get(id=calc_data['nasos_type'])
				turbobur = Turbobur.objects.get(id=calc_data['turboburtype'])
				d_bt = calc_data['d_bt'] * 0.001
				t_bt = calc_data['t_bt'] * 0.001
				vd_bt = (d_bt - 2 * t_bt)
				dgidromotor = float(calc_data['dgidromotor']) * 0.001
				dl_nt = calc_data['dl_nt']
				d_nt = calc_data['d_nt'] * 0.001
				t_nt = calc_data['t_nt'] * 0.001
				stoyak = Stoyak.objects.get(id=calc_data['dstoyak'])
				vedtruba = Vedtruba.objects.get(id=calc_data['dvedtruba'])
				burshlang = Burshlang.objects.get(id=calc_data['dburshlang'])
				vertlug = Vertlug.objects.get(id=calc_data['dvertlug'])
				glubina = calc_data['glubina']
				dl_ubt = calc_data['dl_ubt']
				vd_ubt = calc_data['vd_ubt']
				d_ubt = calc_data['d_ubt'] * 0.001

				# рассчитываем

				# первый набор расчетов
				q = float(nasos.coef) * 0.047
				q = float("%.2f" % q)
				p0 = 0.85 * float(nasos.davl)
				p0 = float("%.2f" % p0)

				# второй набор расчетов
				het = abs((2.5 * 1100 * (vd_bt ** 2)) / (0.014 ** 2))
				ret = abs((4 * q * 1100) / (3.14 * vd_bt * 0.014))
				hekp = abs((2.5 * 1100.0 * (dgidromotor - d_bt) ** 2) / (0.014 ** 2))
				rekp = abs((4 * q * 1100) / (3.14 * (dgidromotor + d_bt) * 0.014))

				if het > 100000:
					het = '%.2f' % (het * 0.00001)
				else:
					het = '%.3f' % het
				if ret > 10000:
					ret = '%.1f' % (ret * 0.001)
				else:
					ret = '%.3f' % ret
				if hekp > 100000:
					hekp = '%.2f' % (hekp * 0.00001)
				else:
					hekp = '%.3f' % hekp
				if rekp > 10000:
					rekp = '%.1f' % (rekp * 0.001)
				else:
					rekp = '%.3f' % rekp

				# третий набор расчетов
				am = (stoyak.coef + vedtruba.coef + burshlang.coef + vertlug.coef) * (10 ** 4)
				dl_bt = glubina - 26 - dl_ubt
				pm1 = ((8 * 0.02 * dl_nt * 1100 * (q ** 2)) / (d_nt - 2 * t_nt) ** 5) * 0.0000001
				pm2 = am * 1100 * (q ** 2) * 0.000001
				pt = (8 * 0.027 * dl_bt * 1100 * q ** 2) / ((3.14 ** 2) * (vd_bt ** 5)) * 0.000001
				pubt = (8 * 0.0255 * dl_ubt * 1100 * q ** 2) / (3.14 ** 2 * vd_ubt ** 5) * 1000000000
				pkpt = 0.000001 * ((8 * 0.038 * 1074 * 1100 * (q ** 2)) / abs(
						(3.14 ** 2) * ((dgidromotor - d_bt) ** 3) * (dgidromotor + d_bt) ** 2))
				pkpdv = 0.000001 * ((8 * 0.0395 * 26 * 1100 * q ** 2) / (
							3.14 ** 2 * (dgidromotor - turbobur.d) ** 3 * (dgidromotor + turbobur.d) ** 2))
				pkpubt = 0.000001 * ((8 * 0.039 * dl_ubt * 1100 * q ** 2) / (
							3.14 ** 2 * (dgidromotor - d_ubt) ** 3 * (dgidromotor + d_ubt) ** 2))
				pdv = turbobur.davl * 1100
				print('P values')

				pm1 = float('%.2f' % pm1)
				pm2 = float('%.1f' % pm2)
				pt = float('%.1f' % pt)
				pubt = float('%.1f' % pubt)
				pkpt = float('%.1f' % pkpt)
				pkpdv = float('%.2f' % pkpdv)
				pkpubt = float('%.2f' % pkpubt)

				print(pm1, pm2, pt, pubt, pkpt, pkpdv, pkpubt, pdv)
				psum = (pm1 + pm2 + pt + pubt + pkpt + pkpdv + pkpubt + pdv)
				psum = abs(float('%.1f' % psum))
				# четвертый набор расчетов
				pgd = 1100 * 9.8 * glubina + (pkpt + pkpdv + pkpubt) * 1000000
				pgd = float('%.1f' % (pgd * 0.000001))
				print('Pgd - ' + str(pgd))
				if turbobur.pgr >= pgd:
					razriv = False
				else:
					razriv = True

				dn = ((8 * 1100 * (nasos.qd ** 2)) / (
							(math.pi ** 2) * (3 ** 2) * (0.92 ** 2) * 6.8 * (10 ** 6))) ** 0.25
				dn = float('%.4f' % dn)
				dn_tmp = float('%.3f' % dn)
				if dn_tmp == 0.012:
					dn_tmp = 0.013

				pdf = (8 * 1100 * (nasos.qd ** 2)) / (3.14 ** 2 * 3 ** 2 * 0.92 ** 2 * dn_tmp ** 4)*0.000001
				pdf = float('%.2f'%pdf)
				data = {
					'author': request.user.username,
					'result_datetime': datetime.datetime.now(),
					'q': q,
					'p0': p0,
					'het': het,
					'ret': ret,
					'hekp': hekp,
					'rekp': rekp,
					'psum': psum,
					'razriv': razriv,
					'dn': dn,
					'pdf': pdf,
				}
				result_model = Result(**data)
				result_model.save()
		elif res_id:
			data = Result.objects.get(id=res_id)
		if data:
			return render(request, 'calc/results.html', {
				'result': data,
			})
		else:
			raise Http404
	else:
		raise Http404


def history(request):
	if request.user.is_authenticated:
		result_set = Result.objects.filter(author=request.user.username)
		return render(request, 'calc/history.html', {
			'result_set': result_set
		})
	else:
		raise Http404


def signin(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect('/')

	errors = []
	if request.method == 'POST':
		user = auth.authenticate(username=request.POST['login'], password=request.POST['password'])
		if user is not None:
			auth.login(request, user)
			return HttpResponseRedirect('/')
		else:
			errors.append('Неправильное имя пользователя или пароль')
	return render(request, 'calc/signin.html', {
		'errors': errors
	})


def signup(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect('/')
	errors = []
	if request.method == 'POST':
		if request.POST['password'] == request.POST['password2']:
			try:
				User.objects.create_user(request.POST['login'], password=request.POST['password'])
			except IntegrityError:
				errors.append('Такой пользователь уже существует')
			else:
				return HttpResponseRedirect('/signin')
		else:
			errors.append('Пароли не совпадают')
	return render(request, 'calc/signup.html', {
		'errors': errors,
	})


def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')


def help(request):
	return render(request, 'calc/help.html')
