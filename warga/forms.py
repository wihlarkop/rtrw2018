from django import forms
from warga.models import Ktp, Kk, Ktpkk


class KTPForm(forms.ModelForm):
    class Meta:
            model = Ktp
            fields = '__all__'

    nik = forms.CharField(label='Masukkan NIK',
                          max_length=15,
                          widget=forms.TextInput(attrs={'class': 'form-control',
                                                        'id': 'nik',
                                                        'name': 'nik'}))
    nama = forms.CharField(label="Masukkan Nama",
                           max_length=255,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    tanggal_lahir = forms.DateField(label="Masukkan Tanggal Lahir",
                                    widget=forms.DateInput(attrs={'class': 'form-control',
                                                                  'type': 'date',
                                                                  }),
                                    input_formats=('%Y-%m-%d',))
    tempat_lahir = forms.CharField(label="Masukkan Tempat Lahir",
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    JENIS_KELAMIN = (
        ('L', 'Laki Laki'),
        ('P', 'Perempuan')
    )
    jenis_kelamin = forms.ChoiceField(label='Pilih Jenis Kelamin',
                                      choices=JENIS_KELAMIN,
                                      widget=forms.Select(attrs={'class': 'form-control'}))
    GOLDAR_CHOICE = (
        ('1', 'A'),
        ('2', 'B'),
        ('3', 'AB'),
        ('4', 'O'),
        ('5', '-'),
    )
    golongan_darah = forms.ChoiceField(label="Pilih Golongan Darah",
                                       choices=GOLDAR_CHOICE,
                                       widget=forms.Select(attrs={'class': 'form-control'}),)
    alamat = forms.CharField(label="Masukkan Alamat",
                             widget=forms.Textarea(attrs={"rows": 5, "cols": 50, 'class': 'form-control'}),)
    RT_CHOICES = (
        ('1', 'RT 01'),
        ('2', 'RT 02'),
        ('3', 'RT 03'),
        ('4', 'RT 04'),
        ('5', 'RT 05'),
        ('6', 'RT 06'),
        ('7', 'RT 07'),
        ('8', 'RT 08'),
        ('9', 'RT 09'),
    )
    rt = forms.ChoiceField(label="Pilih RT",
                           widget=forms.Select(attrs={'class': 'form-control'}),
                           choices=RT_CHOICES,)
    rw = forms.CharField(label="Pilih RW",
                         disabled=True,
                         initial='RW 016',
                         widget=forms.TextInput(attrs={'class': 'form-control'}))
    kecamatan = forms.CharField(disabled=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}),
                                initial='Grogol Petamburan')
    AGAMA_CHOICES = (
        ('1', 'Islam'),
        ('2', 'Kristen Protestan'),
        ('3', 'Hindu'),
        ('4', 'Budha'),
        ('5', 'Katolik'),
        ('6', 'Kong Hu Cu'),
        ('7', '-'),
    )
    agama = forms.ChoiceField(choices=AGAMA_CHOICES,
                              widget=forms.Select(attrs={'class': 'form-control'}))
    STATUS_PERKAWINAN = (
        ('BK', 'Belum Kawin'),
        ('K', 'Kawin '),
    )
    status_perkawinan = forms.ChoiceField(choices=STATUS_PERKAWINAN,
                                          widget=forms.Select(attrs={'class': 'form-control'}))
    pekerjaan = forms.CharField(max_length=20,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    KEWARGANEGARAAN_CHOICE = (
        ('WNI', 'Warga Negara Indonesia'),
        ('WNA', 'Warga Negara Asing'),
    )
    kewarganegaraan = forms.ChoiceField(choices=KEWARGANEGARAAN_CHOICE,
                                        widget=forms.Select(attrs={'class': 'form-control'}))
    masa_berlaku = forms.CharField(max_length=20,
                                   initial="Seumur Hidup",
                                   disabled=True,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))


class KkForm(forms.ModelForm):
    class Meta:
            model = Kk
            fields = '__all__'

    nomor_kk = forms.CharField(max_length=16,
                               label="Masukkan Nomor KK",
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    nik = forms.ModelChoiceField(queryset=Ktp.objects.all(),
                                 label="Pilih NIK",
                                 widget=forms.Select(attrs={'class': 'form-control'}))
    alamat = forms.CharField(label="Masukkan Alamat",
                             widget=forms.Textarea(attrs={"rows": 5, "cols": 50, 'class': 'form-control'}))
    RT_CHOICES = (
        ('1', 'RT 01'),
        ('2', 'RT 02'),
        ('3', 'RT 03'),
        ('4', 'RT 04'),
        ('5', 'RT 05'),
        ('6', 'RT 06'),
        ('7', 'RT 07'),
        ('8', 'RT 08'),
        ('9', 'RT 09'),
    )
    rt = forms.ChoiceField(label="Pilih RT",
                           widget=forms.Select(attrs={'class': 'form-control'}),
                           choices=RT_CHOICES)
    rw = forms.CharField(label="Pilih RW",
                         disabled=True,
                         initial='RW 016',
                         widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_kepala_keluarga = forms.BooleanField(label="Apakah Kepala Keluarga?",
                                            required=False,
                                            widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))