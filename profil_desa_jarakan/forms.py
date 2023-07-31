import re
from datetime import datetime

from django import forms
from profil_desa_jarakan.module_helper import INDONESIA_MONTHS

class ContactForm(forms.Form):
    nama_mahasiswa = forms.CharField(label='Your Name', max_length=100)
    nik_mahasiswa = forms.CharField(label='Your NIK', max_length=16)


class SKTMForm(forms.Form):
    nama = forms.CharField(label='Your Name', max_length=100)
    nik = forms.CharField(label='Your NIK', max_length=16)
    jenis_kelamin = forms.CharField(label='Your JK', max_length=16)
    tempat_lahir = forms.CharField(label='Your Birth place', max_length=100)
    tanggal_lahir = forms.CharField(label='Your BirthDate')
    status_perkawinan = forms.CharField(label='Your status', max_length=100)
    pekerjaan = forms.CharField(label='Your Job', max_length=100)
    alamat = forms.CharField(label='Your Address', max_length=100)

    def clean_nik(self):
        nik = self.cleaned_data['nik']
        nik_numbers = re.search(r'(\d{0,})', ''.join(re.findall(r'\d', nik))).groups()[0]
        if len(nik_numbers)!=16:
            raise forms.ValidationError(f'NIK harus 16 angka, yang anda masukan: {nik_numbers}')
        return nik_numbers

    def clean_tanggal_lahir(self):
        date_format = "%d/%m/%Y"
        date_object = datetime.strptime(self.cleaned_data['tanggal_lahir'], date_format).date()
        return f'{date_object.day} - {INDONESIA_MONTHS[date_object.month-1]} - {date_object.year}'

