import re
from datetime import datetime

from django import forms
from profil_desa_jarakan.module_helper import INDONESIA_MONTHS

class ContactForm(forms.Form):
    nama_mahasiswa = forms.CharField(label='Your Name', max_length=100)
    nik_mahasiswa = forms.CharField(label='Your NIK', max_length=16)


class SKTMForm(forms.Form):
    nomor_surat = forms.CharField(label='No Surat', max_length=100, required=False)
    nama = forms.CharField(label='Your Name', max_length=100, required=False)
    nik = forms.CharField(label='Your NIK', max_length=16, required=False)
    jenis_kelamin = forms.CharField(label='Your JK', max_length=16, required=False)
    tempat_lahir = forms.CharField(label='Your Birth place', max_length=100, required=False)
    tanggal_lahir = forms.CharField(label='Your BirthDate', required=False)
    status_perkawinan = forms.CharField(label='Your status', max_length=100, required=False)
    pekerjaan = forms.CharField(label='Your Job', max_length=100, required=False)
    alamat = forms.CharField(label='Your Address', max_length=100, required=False)
    dusun = forms.CharField(label='Your Dusun', max_length=100, required=False)

    def clean_nik(self):
        nik = self.cleaned_data['nik']
        nik_numbers = re.search(r'(\d{0,})', ''.join(re.findall(r'\d', nik))).groups()[0]
        if len(nik_numbers)!=16:
            raise forms.ValidationError(f'NIK harus 16 angka, yang anda masukan: {nik_numbers}')
        return nik_numbers

    def clean_tanggal_lahir(self):
        date_format = "%Y-%m-%d"
        date_object = datetime.strptime(self.cleaned_data['tanggal_lahir'], date_format).date()
        return f'{date_object.day} - {INDONESIA_MONTHS[date_object.month-1]} - {date_object.year}'

class SuratNikahForm(forms.Form):
    kedudukan = forms.CharField(label='Your Name', max_length=100, required=False)
    nomor_surat = forms.CharField(label='No Surat', max_length=100, required=False)
    nama = forms.CharField(label='Your Name', max_length=100, required=False)
    nik = forms.CharField(label='Your NIK', max_length=16, required=False)
    jenis_kelamin = forms.CharField(label='Your JK', max_length=16, required=False)
    tempat_lahir = forms.CharField(label='Your Birth place', max_length=100, required=False)
    tanggal_lahir = forms.CharField(label='Your BirthDate', required=False)
    status_perkawinan = forms.CharField(label='Your status', max_length=100, required=False)
    pekerjaan = forms.CharField(label='Your Job', max_length=100, required=False)
    alamat = forms.CharField(label='Your Address', max_length=100, required=False)

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

class KematianForm(forms.Form):
    nomor_surat = forms.CharField(label='No Surat', max_length=100, required=False)
    nama = forms.CharField(label='Your Name', max_length=100, required=False)
    nik = forms.CharField(label='Your NIK', max_length=16, required=False)
    agama = forms.CharField(label='Your NIK', max_length=16, required=False)
    jenis_kelamin = forms.CharField(label='Your JK', max_length=16, required=False)
    tempat_lahir = forms.CharField(label='Your Birth place', max_length=100, required=False)
    tanggal_lahir = forms.CharField(label='Your BirthDate', required=False)
    status_perkawinan = forms.CharField(label='Your status', max_length=100, required=False)
    pekerjaan = forms.CharField(label='Your Job', max_length=100, required=False)
    alamat = forms.CharField(label='Your Address', max_length=100, required=False)
    dusun = forms.CharField(label='Your Dusun', max_length=100, required=False)
    hari_meninggal = forms.CharField(label='Your Dusun', max_length=100, required=False)
    jam_meninggal = forms.CharField(label='Your Dusun', max_length=100, required=False)
    tanggal_meninggal = forms.CharField(label='Your Dusun', max_length=100, required=False)


    def clean_nik(self):
        nik = self.cleaned_data['nik']
        nik_numbers = re.search(r'(\d{0,})', ''.join(re.findall(r'\d', nik))).groups()[0]
        if len(nik_numbers)!=16:
            raise forms.ValidationError(f'NIK harus 16 angka, yang anda masukan: {nik_numbers}')
        return nik_numbers

    def clean_tanggal_lahir(self):
        date_format = "%Y-%m-%d"
        date_object = datetime.strptime(self.cleaned_data['tanggal_lahir'], date_format).date()
        return f'{date_object.day} - {INDONESIA_MONTHS[date_object.month-1]} - {date_object.year}'

class UsahaForm(forms.Form):
    nomor_surat = forms.CharField(label='No Surat', max_length=100, required=False)
    nama = forms.CharField(label='Your Name', max_length=100, required=False)
    nik = forms.CharField(label='Your NIK', max_length=16, required=False)
    agama = forms.CharField(label='Your NIK', max_length=16, required=False)
    jenis_kelamin = forms.CharField(label='Your JK', max_length=16, required=False)
    tempat_lahir = forms.CharField(label='Your Birth place', max_length=100, required=False)
    tanggal_lahir = forms.CharField(label='Your BirthDate', required=False)
    status_perkawinan = forms.CharField(label='Your status', max_length=100, required=False)
    pekerjaan = forms.CharField(label='Your Job', max_length=100, required=False)
    alamat = forms.CharField(label='Your Address', max_length=100, required=False)
    dusun = forms.CharField(label='Your Dusun', max_length=100, required=False)
    nama_usaha = forms.CharField(label='Nama Usaha', max_length=100, required=False)
    bentuk_usaha = forms.CharField(label='Bentuk Usaha', max_length=100, required=False)
    tahun_usaha = forms.CharField(label='Tahun Usaha', max_length=100, required=False)
    jenis_usaha = forms.CharField(label='Jenis Usaha', max_length=100, required=False)
    alamat_usaha = forms.CharField(label='Alamat Usaha', max_length=100, required=False)


    def clean_nik(self):
        nik = self.cleaned_data['nik']
        nik_numbers = re.search(r'(\d{0,})', ''.join(re.findall(r'\d', nik))).groups()[0]
        if len(nik_numbers)!=16:
            raise forms.ValidationError(f'NIK harus 16 angka, yang anda masukan: {nik_numbers}')
        return nik_numbers

    def clean_tanggal_lahir(self):
        date_format = "%Y-%m-%d"
        date_object = datetime.strptime(self.cleaned_data['tanggal_lahir'], date_format).date()
        return f'{date_object.day} - {INDONESIA_MONTHS[date_object.month-1]} - {date_object.year}'

class InfoDesaForm(forms.Form):
    nama_desa = forms.CharField(max_length=100, required=False)
    kepala_desa = forms.CharField(max_length=100, required=False)
    email_desa = forms.CharField(max_length=100, required=False)
    telp_desa = forms.CharField(max_length=100, required=False)