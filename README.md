<p align="right">
بِسْــــــــــــــمِ اللَّهِ الرَّحْمَنِ الرَّحِيم 
</p>

# Login Register with Django :computer:
Belajar cara membuat login register pada Django menggunakan database MySql.

## Installation

Buat virtualenv terlebih dahulu (Windows)
```bash
virtualenv {nama_virtual}
```
Masuk kedalam virtual (Windows)
```bash
source {nama_virtual}/Scripts/activate
```
Jika menggunakan linux
```bash
virtualenv -p python3 {nama_virtual} ##untuk python3, ubuntu biasanya menggunakan ini
source {nama_virtual}/bin/activate
```
Install requirements menggunakan [pip](https://pip.pypa.io/en/stable/).
```bash
pip install --upgrade pip
pip install --upgrade setuptools
pip install -r requirements.txt
```
Buat database di phpmyadmin / sejenisnya dengan nama database <b>django_login</b> <br>
tetap pada terminal, jalankan perintah migrasi
```bash
python manage.py makemigrations && python manage.py migrate
```
Jalankan server
```bash
python manage.py runserver
```
