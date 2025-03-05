from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView,CreateView,DeleteView,UpdateView ,View
from django.urls import reverse_lazy


from .models import Smartphone
from .forms import SmartphoneForm


# Create your views here.
def smartphone(request):
    smartphones = Smartphone.objects.all()
    return render(request,'smartphone.html',context={'smartphones':smartphones})

class Smartphoneslist(ListView):
    model = Smartphone
    template_name = 'smartphone.html'
    context_object_name = 'smartphones'


def smartphone_det(request,pk):
    smartphone =Smartphone.objects.get(id=pk)
    return render(request,'smartphone_det.html',context={'smartphone':smartphone})



def create_smartphone(request):
    form = SmartphoneForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        return redirect('smartphone_list')
    return render(request,'smartphone_create.html',{'form':form})

def update_smartphone(request, pk):
    smartphone = get_object_or_404(Smartphone, pk=pk)
    form = SmartphoneForm(request.POST or None, request.FILES or None, instance=smartphone)
    
    if form.is_valid():
        form.save()
        return redirect('smartphone_list')
    
    return render(request, 'smartphone_update.html', {'form': form, 'smartphone': smartphone})



# def create_smartphone(request):
#     if request.method == 'POST':
#         smartphone = Smartphone()
#         smartphone.make = request.POST.get('make','')
#         smartphone.model = request.POST.get('model','')
#         smartphone.memory = request.POST.get('memory','')
#         smartphone.color = request.POST.get('color','')
#         smartphone.price = request.POST.get('price','')
#         smartphone.description = request.POST.get('description','')
#         smartphone.image = request.FILES.get('image','')
        
#         smartphone.save()
        
#         return redirect('smartphone_list')
    
#     return render(request,'smartphone_create.html',{'smartphone':'smartphone'})



# def update_smartphone(request,pk):
#     smartphone = Smartphone.objects.get(id=pk)
#     if request.method == 'POST':
#         smartphone.make = request.POST.get('make',smartphone.make)
#         smartphone.model = request.POST.get('model',smartphone.model)
#         smartphone.memory = request.POST.get('memory',smartphone.memory)
#         smartphone.color = request.POST.get('color',smartphone.color)
#         smartphone.price = request.POST.get('price',smartphone.price)
#         smartphone.description = request.POST.get('description',smartphone.description)
#         smartphone.image = request.FILES.get('image',smartphone.image)
#         smartphone.save()
        
#         return redirect('smartphone_det', pk=pk)
    
#     return render(request, 'smartphone_update.html', {'smartphone': smartphone})
        
    
def delete_smartphone(request,pk):
    smartphone = get_object_or_404(Smartphone,id=pk)
    if request.method =='POST':
        smartphone.delete()
        return redirect('smartphone_list')
    return render(request,'smartphone_delete.html',{'smartphone':smartphone})
    
    
    
    
# class SmartphoneCreate(CreateView):
#     model = Smartphone
#     form_class = SmartphoneForm
#     success_url = reverse_lazy('smartphone_list')
#     template_name = 'smartphone_create.html'
    
    
# class SmartphoneDelete(DeleteView):
#     model = Smartphone
#     success_url = reverse_lazy('smartphone_list')
#     template_name = 'smartphone_delete.html'
    
# class SmartphoneUpdate(UpdateView):
#     model = Smartphone
#     form_class = SmartphoneForm
#     template_name = 'smartphone_update.html'
#     context_object_name = 'smartphone'
    
#     # def get_success_url(self):
#     #     return reverse_lazy('smartphone_det', kwargs={'pk': self.object.pk})
    
#     def get_success_url(self):
#         return reverse_lazy('smartphone_list')
    
    

# class SmartphoneCreate(View):
#     def get(self,request):
#         form = SmartphoneForm()
#         return render(request,'smartphone_create.html',{'form':form})
    
#     def post(self,request):
#         form = SmartphoneForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('smartphone_list')
#         return render(request,'smartphone_create.html',{'form':form})
    
    
    
# class SmartphoneDelete(View):
#     def get(self,request):
#         form = SmartphoneForm()
#         return render(request,'smartphone_delete.html',{'form':form})
    
#     def post(self,request):
#         pass
    





















    






        

        
        
