from django.db import models
from warga.models import Ktp


class Suratpengantar(models.Model):
    nik = models.ForeignKey(Ktp, on_delete=models.CASCADE)
    tujuan_surat = models.CharField(max_length=12)
    atas_nama = models.CharField(max_length=255, null=True)
    is_ready = models.BooleanField(default=False)


    def __str__(self):
        return '{} {}'.format(self.nik, self.tujuan_surat)
