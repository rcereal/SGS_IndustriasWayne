from django import forms
from .models import Recurso

class Form_do_Recurso(forms.ModelForm):
    class Meta:
        model = Recurso
        fields = ['nome', 'descricao', 'status']

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if not nome.strip():
            raise forms.ValidationError('O nome é obrigatório, por favor preencha todos os campos.')
        return nome

    def clean_descricao(self):
        descricao = self.cleaned_data.get('descricao')
        if not descricao.strip():
            raise forms.ValidationError('Insira uma descrição para o recurso.')
        return descricao

    def clean_status(self):
        status = self.cleaned_data.get('status')
        if status not in dict(self.Meta.model.STATUS_CHOICES):
            raise forms.ValidationError('Status inválido.')
        return status
