from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import movie
from .form import mform
def fun1(request):

    movi=movie.objects.all()
    context={ 'movie_list':movi}
    return render(request, 'index.html', context)
def detail(request,movie_id):
    mov=movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'movie':mov})
def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('name',)
        desc= request.POST.get('desc', )
        year = request.POST.get('year', )
        img = request.FILES['img']
        m = movie(name=name,desc=desc,year=year,img=img)
        m.save()
    return render(request,'add.html')
def update(request,id):
    movi=movie.objects.get(id=id)
    form=mform(request.POST or None, request.FILES,instance=movi)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movi})
def delete(request,id):
    if request.method=='POST':
        moovi=movie.objects.get(id=id)
        moovi.delete()
        return redirect('/')
    return render(request,'delete.html')