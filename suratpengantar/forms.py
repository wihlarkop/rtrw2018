from django import forms
from suratpengantar.models import Suratpengantar
from warga.models import Ktp

class SuratpengantarForm(forms.ModelForm):
    class Meta:
            model = Suratpengantar
            fields = '__all__'

    # nik = forms.CharField()
    # tujuan_surat = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # atas_nama = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))