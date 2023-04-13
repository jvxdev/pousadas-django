from django import forms

from pousadas.models import Pousada

class PousadaForm(forms.ModelForm):
    class Meta:
        model = Pousada
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o Nome da Pousada'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Digite uma Descrição para a Pousada'
            }),
            'estado': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o Estado da Pousada'
            }),
            'cidade': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite a Cidade da Pousada'
            }),
            'endereco': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o Endereço da Pousada'
            }),
            'cep': forms.TextInput(attrs={
                'class': 'form-control cep',
                'placeholder': 'Digite o CEP da Pousada'
            }),
            'quartos': forms.Select(attrs={'class': 'form-control'}),
            'banheiros': forms.Select(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control telefone',
                'placeholder': 'Digite um Telefone para contato'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite um E-mail para contato'
            })
        }