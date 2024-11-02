from django import forms
from .models import Recurso

class Form_do_Recurso(forms.ModelForm):
    class Meta:
        model = Recurso
        fields = ['nome', 'descricao', 'status']

    def nome_em_branco(self):
        nome = self.cleaned_data.get('nome')
        if not nome:
            raise forms.ValidationError('O nome é obrigatório, por favor preencha todos os campos.')
        return nome
    
    def descricao_em_branco(self):
        descricao = self.cleaned_data.get('descricao')
        if not descricao:
            raise forms.ValidationError('Insira uma descrição para o recurso.')
        return descricao


    def status_em_branco(self):
        status = self.cleaned_data.get('status')
        if status not in ['ativo', 'inativo']:
            raise forms.ValidationError('Status inválido.')
        return status


