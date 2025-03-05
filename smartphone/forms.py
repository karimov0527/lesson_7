from django import forms
from .models import Smartphone


# class SmartphoneForm(forms.ModelForm):
#     class Meta:
#         model = Smartphone
#         fields = '__all__'
    

class SmartphoneForm(forms.ModelForm):
    class Meta:
        model = Smartphone
        fields = '__all__'
    
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("Narx musbat bo'lishi kerak.")
        return price
    
    def clean_model(self):
        model = self.cleaned_data.get('model')
        if len(model) < 3:
            raise forms.ValidationError("Model nomi kamida 3 ta belgidan iborat bo'lishi kerak.")
        return model
    
    def clean_storage(self):
        storage = self.cleaned_data.get('memory')
        if storage not in [64, 128, 256, 512, 1024]:
            raise forms.ValidationError("Xotira hajmi faqat 64, 128, 256, 512 yoki 1024 GB bo'lishi mumkin.")
        return storage
    
    def clean_color(self):
        color = self.cleaned_data.get('color')
        if not color.isalpha():
            raise forms.ValidationError("Rang faqat harflardan iborat bo'lishi kerak.")
        return color
    
    
    
    
    
    