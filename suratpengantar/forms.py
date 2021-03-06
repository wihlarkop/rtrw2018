from django import forms
from suratpengantar.models import Suratpengantar
from warga.models import Ktp

class SuratpengantarForm(forms.ModelForm):
    class Meta:
            model = Suratpengantar
            fields = '__all__'

    nik = forms.ModelChoiceField(queryset=Ktp.objects.all(),
                                 widget=forms.Select(attrs={'class': 'form-control'}))
    tujuan_surat = forms.CharField(max_length=255,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    atas_nama = forms.CharField(max_length=255,
                                required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    scan_surat = forms.ImageField(label="Scan Surat",
                                  required=False,
                                  widget=forms.FileInput(attrs={'class': 'form-control'}))
    is_ready = forms.BooleanField(label="Status Surat Pengantar",
                                  required=False,
                                  widget=forms.CheckboxInput())
