from django.db import models


class Ktp(models.Model):
    JENIS_KELAMIN = (
        ('L', 'Laki Laki'),
        ('P', 'Perempuan')
    )

    GOLDAR_CHOICE = (
        ('1', '-'),
        ('2', 'A'),
        ('3', 'B'),
        ('4', 'AB'),
        ('5', 'O'),
    )

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

    AGAMA_CHOICES = (
        ('1', '-'),
        ('2', 'Islam'),
        ('3', 'Kristen Protestan'),
        ('4', 'Hindu'),
        ('5', 'Budha'),
        ('6', 'Katolik'),
        ('7', 'Kong Hu Cu'),
    )

    STATUS_PERKAWINAN = (
        ('BK', 'Belum Kawin'),
        ('K', 'Kawin '),
    )

    KEWARGANEGARAAN_CHOICE = (
        ('WNI', 'Warga Negara Indonesia'),
        ('WNA', 'Warga Negara Asing')
    )

    nik = models.CharField(max_length=16,unique=True)
    nama = models.CharField(max_length=100, blank=False, null=False)
    tanggal_lahir = models.DateField()
    tempat_lahir = models.CharField(max_length=15)
    jenis_kelamin = models.CharField(max_length=10, choices=JENIS_KELAMIN)
    golongan_darah = models.CharField(max_length=2, choices=GOLDAR_CHOICE, default=1)
    alamat = models.CharField(max_length=50)
    rt = models.CharField(max_length=3, choices=RT_CHOICES, blank=True, null=True)
    rw = models.CharField(max_length=7, default="RW 016", blank=False, null=False)
    kecamatan = models.CharField(max_length=25, default="Grogol Petamburan")
    agama = models.CharField(max_length=15, choices=AGAMA_CHOICES, default=1)
    status_perkawinan = models.CharField(max_length=11, choices=STATUS_PERKAWINAN, default=1)
    pekerjaan = models.CharField(max_length=25)
    kewarganegaraan = models.CharField(max_length=3, choices=KEWARGANEGARAAN_CHOICE)
    masa_berlaku = models.CharField(max_length=15, default="Seumur Hidup", editable=False)
    scan_ktp = models.ImageField(blank=True, null=True,
                                 upload_to='scan_ktp/',
                                 default='/noimage.png')


    def __str__(self):
        return '{} {}'.format(self.nik, self.nama)


class Kk(models.Model):
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

    nomor_kk = models.CharField(max_length=16,unique=True)
    nik = models.ForeignKey(Ktp, on_delete=models.CASCADE, unique=True)
    alamat = models.TextField()
    rt = models.CharField(max_length=3, choices=RT_CHOICES)
    rw = models.CharField(max_length=7, default="RW 016")
    scan_kk = models.ImageField(blank=True, null=True,
                                 upload_to='scan_kk/',
                                 default='/noimage.png')
    is_kepala_keluarga = models.BooleanField(default=True)


    def __str__(self):
        return '{}, {}'.format(self.nomor_kk, self.nik.nama)
