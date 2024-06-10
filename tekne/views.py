from django.shortcuts import render
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required,permission_required
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import Q
from .models import tur
from .models import tekne
from .models import ucret
from .models import rezerve
from datetime import date 
from django.shortcuts import get_object_or_404  
from .models import rezerve  
from django.contrib import messages
import matplotlib.pyplot as plt
from django.shortcuts import render  
from django.db.models import Sum  
from django.db.models.functions import ExtractMonth,ExtractYear
import threading      

# Create your views here.

def login(request): 
    
    if request.method == 'POST' or None:
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user is None:
            messages.info(request,'Kullanıcı Adı veya Parola Hatalı')
            return render(request,'login.html')
        auth_login(request,user)
        return redirect('rezerve')
    return render(request,'login.html')

def logoutUser(request): 
    logout(request)
    return redirect('login')



@login_required(login_url='login')
@permission_required('tekne.tekne_user', login_url='/tekne/permission_not_granted/')
def rzv(request): 

    if request.method == 'POST':

        q = rezerve(
            tarih= request.POST.get('tarih'),
            teknename= request.POST.get('teknename'),
            turname= request.POST.get('turname'),
            adet= request.POST.get('adet'),
            telno= request.POST.get('telno'),
            ucret= request.POST.get('ucret'),
            toplamucret= request.POST.get('toplamucret'),
            kapora= request.POST.get('kapora'),
            aciklama= request.POST.get('aciklama'),
            tamucret= request.POST.get('tamucret'),  
        )
        q.save()
        messages.success(request, 'Kayıt tamamlandı')
        context = {'tur_list':tur.objects.all(),'tekne_list':tekne.objects.all(),'ucret_list':ucret.objects.all()}
        return render(request,'rezerve.html',context)
    
    context = {'tur_list':tur.objects.all(),'tekne_list':tekne.objects.all(),'ucret_list':ucret.objects.all()}
    return render(request,'rezerve.html',context)

login_required(login_url='login')
@permission_required('tekne.tekne_user', login_url='/tekne/permission_not_granted/')
def rezerveedit(request,id): 
    b = rezerve.objects.get(pk=id)
    if  request.method == 'POST':

        b.tarih= request.POST.get('tarih')
        b.teknename= request.POST.get('teknename')
        b.turname= request.POST.get('turname')
        b.adet= request.POST.get('adet')
        b.telno= request.POST.get('telno')
        b.ucret= request.POST.get('ucret')
        b.toplamucret= request.POST.get('toplamucret')
        b.kapora= request.POST.get('kapora')
        b.aciklama= request.POST.get('aciklama')
        b.tamucret= request.POST.get('tamucret') 
        b.save()
        if 'confirm' in request.POST:
            b.delete()
            messages.success(request, 'Kayıt silindi')
            return redirect(irmak)

        messages.success(request, 'Kayıt tamamlandı')
        return redirect(irmak)
    
    context = {'rzv_table':rezerve.objects.get(pk=id),'tur_list':tur.objects.all(),'tekne_list':tekne.objects.all(),'ucret_list':ucret.objects.all()}
    return render(request,'rezerveedit.html',context)

@login_required(login_url='login')
@permission_required('tekne.tekne_user', login_url='/tekne/permission_not_granted/')
def irmak(request):  
    selected_date = date.today() 
    context = {  
        'tur1_table': rezerve.objects.filter(Q(teknename="Irmak") & Q(turname="07:00/12:00") & Q(tarih=selected_date)).order_by('-id'),  
        'tur2_table': rezerve.objects.filter(Q(teknename="Irmak") & Q(turname="12:30/17:30") & Q(tarih=selected_date)).order_by('-id'),  
        'tur3_table': rezerve.objects.filter(Q(teknename="Irmak") & Q(turname="18:00/23:00") & Q(tarih=selected_date)).order_by('-id'),  
        'tur4_table': rezerve.objects.filter(Q(teknename="Irmak") & Q(turname="24:00/07:00") & Q(tarih=selected_date)).order_by('-id')  
    }  
  
    return render(request, 'irmak.html', context) 

@login_required(login_url='login')
@permission_required('tekne.tekne_user', login_url='/tekne/permission_not_granted/')
def filter(request):  
    selected_date = request.GET.get('date')  
  
    context = {  
        'tur1_table': rezerve.objects.filter(Q(teknename="Irmak") & Q(turname="07:00/12:00") & Q(tarih=selected_date)).order_by('-id'),  
        'tur2_table': rezerve.objects.filter(Q(teknename="Irmak") & Q(turname="12:30/17:30") & Q(tarih=selected_date)).order_by('-id'),  
        'tur3_table': rezerve.objects.filter(Q(teknename="Irmak") & Q(turname="18:00/23:00") & Q(tarih=selected_date)).order_by('-id'),  
        'tur4_table': rezerve.objects.filter(Q(teknename="Irmak") & Q(turname="24:00/07:00") & Q(tarih=selected_date)).order_by('-id')  
    }  
  
    return render(request, 'filter.html', context) 


login_required(login_url='login')
@permission_required('tekne.tekne_user', login_url='/tekne/permission_not_granted/')
def rezerveedit1(request,id): 
    b = rezerve.objects.get(pk=id)
    if  request.method == 'POST':

        b.tarih= request.POST.get('tarih')
        b.teknename= request.POST.get('teknename')
        b.turname= request.POST.get('turname')
        b.adet= request.POST.get('adet')
        b.telno= request.POST.get('telno')
        b.ucret= request.POST.get('ucret')
        b.toplamucret= request.POST.get('toplamucret')
        b.kapora= request.POST.get('kapora')
        b.aciklama= request.POST.get('aciklama')
        b.tamucret= request.POST.get('tamucret') 
        b.save()
        if 'confirm' in request.POST:
            b.delete()
            messages.success(request, 'Kayıt silindi')
            return redirect(kaan)

        messages.success(request, 'Kayıt tamamlandı')
        return redirect(kaan)
    
    context = {'rzv_table':rezerve.objects.get(pk=id),'tur_list':tur.objects.all(),'tekne_list':tekne.objects.all(),'ucret_list':ucret.objects.all()}
    return render(request,'rezerveedit1.html',context)

@login_required(login_url='login')
@permission_required('tekne.tekne_user', login_url='/tekne/permission_not_granted/')
def kaan(request): 
    selected_date = date.today() 
    context = {  
        'tur1_table': rezerve.objects.filter(Q(teknename="Kaan") & Q(turname="07:00/12:00") & Q(tarih=selected_date)).order_by('-id'),  
        'tur2_table': rezerve.objects.filter(Q(teknename="Kaan") & Q(turname="12:30/17:30") & Q(tarih=selected_date)).order_by('-id'),  
        'tur3_table': rezerve.objects.filter(Q(teknename="Kaan") & Q(turname="18:00/23:00") & Q(tarih=selected_date)).order_by('-id'),  
        'tur4_table': rezerve.objects.filter(Q(teknename="Kaan") & Q(turname="24:00/07:00") & Q(tarih=selected_date)).order_by('-id')

    }  
  
    return render(request, 'kaan.html', context) 

@login_required(login_url='login')
@permission_required('tekne.tekne_user', login_url='/tekne/permission_not_granted/')
def filter1(request):  
    selected_date = request.GET.get('date')  
  
    context = {  
        'tur1_table': rezerve.objects.filter(Q(teknename="Kaan") & Q(turname="07:00/12:00") & Q(tarih=selected_date)).order_by('-id'),  
        'tur2_table': rezerve.objects.filter(Q(teknename="Kaan") & Q(turname="12:30/17:30") & Q(tarih=selected_date)).order_by('-id'),  
        'tur3_table': rezerve.objects.filter(Q(teknename="Kaan") & Q(turname="18:00/23:00") & Q(tarih=selected_date)).order_by('-id'),  
        'tur4_table': rezerve.objects.filter(Q(teknename="Kaan") & Q(turname="24:00/07:00") & Q(tarih=selected_date)).order_by('-id')  
    }  
  
    return render(request, 'filter1.html', context) 




@login_required(login_url='login')
@permission_required('lab.lab_user', login_url='/lab/permission_not_granted/')
def mkpills24(request):
    labels = []
    data = []
    labels2 = []
    data2 = []
        
    kazanc_listesi = rezerve.objects.filter(tamucret='Kapalı', tarih__year=2024).exclude(toplamucret__isnull=True).annotate(month=ExtractMonth('tarih')).values('month').annotate(total=Sum('toplamucret')).order_by('month')   
    yillik_kazanc = rezerve.objects.filter(tamucret='Kapalı').exclude(toplamucret__isnull=True).annotate(year=ExtractYear('tarih')).values('year').annotate(total=Sum('toplamucret')).order_by('year')     


    for brs in kazanc_listesi:  
        labels.append((brs['month']))
        data.append(brs['total'])
    for brs2 in yillik_kazanc:  
        labels2.append((brs2['year']))
        data2.append(brs2['total'])
  
    return render(request, 'mkpills24.html', {
        'labels': labels,
        'data': data,
        'labels2': labels2,
        'data2': data2,
        'month_table': rezerve.objects.filter(tamucret='Kapalı', tarih__year=2024).exclude(toplamucret__isnull=True).annotate(month=ExtractMonth('tarih')).values('month').annotate(total=Sum('toplamucret')).order_by('month'),
    })

@login_required(login_url='login')
@permission_required('lab.lab_user', login_url='/lab/permission_not_granted/')
def mkpills25(request):
    labels = []
    data = []
    labels2 = []
    data2 = []
        
    kazanc_listesi = rezerve.objects.filter(tamucret='Kapalı', tarih__year=2025).exclude(toplamucret__isnull=True).annotate(month=ExtractMonth('tarih')).values('month').annotate(total=Sum('toplamucret')).order_by('month')   
    yillik_kazanc = rezerve.objects.filter(tamucret='Kapalı').exclude(toplamucret__isnull=True).annotate(year=ExtractYear('tarih')).values('year').annotate(total=Sum('toplamucret')).order_by('year')     


    for brs in kazanc_listesi:  
        labels.append((brs['month']))
        data.append(brs['total'])
    for brs2 in yillik_kazanc:  
        labels2.append((brs2['year']))
        data2.append(brs2['total'])


    
    return render(request, 'mkpills25.html', {
        'labels': labels,
        'data': data,
        'labels2': labels2,
        'data2': data2,
        'month_table': rezerve.objects.filter(tamucret='Kapalı', tarih__year=2025).exclude(toplamucret__isnull=True).annotate(month=ExtractMonth('tarih')).values('month').annotate(total=Sum('toplamucret')).order_by('month'),
        
    })

@login_required(login_url='login')
@permission_required('lab.lab_user', login_url='/lab/permission_not_granted/')
def mkpills26(request):
    labels = []
    data = []
    labels2 = []
    data2 = []
        
    kazanc_listesi = rezerve.objects.filter(tamucret='Kapalı', tarih__year=2026).exclude(toplamucret__isnull=True).annotate(month=ExtractMonth('tarih')).values('month').annotate(total=Sum('toplamucret')).order_by('month')   
    yillik_kazanc = rezerve.objects.filter(tamucret='Kapalı').exclude(toplamucret__isnull=True).annotate(year=ExtractYear('tarih')).values('year').annotate(total=Sum('toplamucret')).order_by('year')     


    for brs in kazanc_listesi:  
        labels.append((brs['month']))
        data.append(brs['total'])
    for brs2 in yillik_kazanc:  
        labels2.append((brs2['year']))
        data2.append(brs2['total'])


    
    return render(request, 'mkpills26.html', {
        'labels': labels,
        'data': data,
        'labels2': labels2,
        'data2': data2,
        'month_table': rezerve.objects.filter(tamucret='Kapalı', tarih__year=2026).exclude(toplamucret__isnull=True).annotate(month=ExtractMonth('tarih')).values('month').annotate(total=Sum('toplamucret')).order_by('month'),
    })

