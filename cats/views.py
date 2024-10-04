from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import CreateView , UpdateView, DeleteView
from django.urls import reverse_lazy

from cats.models import Breed,Cat
from cats.forms import BreedForm

# Create your views here.

class MainView(LoginRequiredMixin , View):
    def get(self,request):
        bc=Breed.objects.count()
        ca=Cat.objects.all()

        ctx={'breed_count':bc , 'cats_list':ca}
        return render(request, 'cats/cat_list.html',ctx)

class BreedView(LoginRequiredMixin, View):
    #why do we put View in here
    def get(self,request):
        br= Breed.objects.all()
        ctx={'breed_list':br}
        return render(request,'cats/breed_list.html',ctx)


class BreedCreate(LoginRequiredMixin, View):
    template ='cats/breed_form.html'
    success_url = reverse_lazy('cats:all')

    def get(self,request):
        form=BreedForm() #what does this thing do
        ctx= {'form':form}
        return render(request , self.template ,ctx)

    def post(self,request):
        form=BreedForm(request.POST)#why an argument in this
        if not form.is_valid():
            ctx={'form': form}
            return render(request,self.template,ctx)#what does that self do also that form thingy when its wrong
            #obivously the form is wrong if i'm here isn't it?

        breed= form.save()
        return redirect(self.success_url)


class BreedUpdate(LoginRequiredMixin, View):
    model=Breed
    success_url = reverse_lazy('cats:all')
    template ='cats/breed_form.html'

    def get(self,request,pk):
        breed=get_object_or_404(self.model,pk=pk)
        form=BreedForm(instance=breed)
        ctx={'form':form}
        return render(request, self. template, ctx)

    def post(self,request,pk):
        breed=get_object_or_404(self.model,pk=pk)
        form=BreedForm(request.POST,instance=breed)
        if not form.is_valid():
            ctx={'form':form}
            return render(request, self. template, ctx)

        form.save()
        return redirect(self.success_url)

class BreedDelete(LoginRequiredMixin,View):
    model=Breed
    success_url= reverse_lazy('cats:all')
    template='cats/breed_confirm_delete.html'

    def get(self,request,pk):
        breed=get_object_or_404(self.model , pk=pk)
        ctx={'breed':breed}
        return render(request,self.template,ctx)

    def post(self,request,pk):
        breed=get_object_or_404(self.model,pk=pk)
        breed.delete()
        return redirect(self.success_url)

class CatCreate(LoginRequiredMixin,CreateView):
    model=Cat
    fields='__all__'
    success_url=reverse_lazy('cats:all')

class CatUpdate(LoginRequiredMixin,UpdateView):
    model=Cat
    fields='__all__'
    success_url=reverse_lazy('cats:all')

class CatDelete(LoginRequiredMixin,DeleteView):
    model=Cat
    fields='__all__'
    success_url=reverse_lazy('cats:all')



