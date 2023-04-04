from django import forms


class TextoForm(forms.Form):
    titulo = forms.CharField(max_length=200)
    subtitulo = forms.CharField(max_length=100)
    dia = forms.DateField()
    imagen = forms.ImageField()
    contenido = forms.Textarea()


    

