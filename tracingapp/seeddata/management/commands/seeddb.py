from django.core.management.base import BaseCommand, CommandError

from lokasi.models import Lokasi
from django.contrib.auth.models import User
from pengguna.models import Pengguna
import json

class Command(BaseCommand):
    help = 'Seed Data'

    def handle(self, *args, **options):
        user_mock = json.loads(open('MOCK_USER.json').read())
        for user_data in user_mock:
            exists = User.objects.filter(username = user_data["username"]).exists()
            if not exists:
                User.objects.create_user(user_data['username'], user_data['email_address'], user_data['password'])
        self.stdout.write(self.style.SUCCESS('Successfully saved user'))
        
        # Seed Admin
        exists = User.objects.filter(username="admin").exists()
        if not exists:
            admin_user = User.objects.create_user('admin', 'admin@admin.com', 'admin', is_staff=True, is_superuser=True)
            Pengguna.objects.create(
                user=admin_user,
                nik='3173020000000000',
                vaccine_1 = True,
                vaccine_2 = True
            )
        
        pengguna_mock = json.loads(open('MOCK_PENGGUNA.json').read())
        for pengguna_data in pengguna_mock:
            user = User.objects.get(id=pengguna_data['user'])
            
            exists = Pengguna.objects.filter(user=user).exists()
            if not exists:
                Pengguna.objects.create(
                    user = user,
                    nik = pengguna_data['nik'],
                    vaccine_1 = pengguna_data['vaccine_1'],
                    vaccine_2 = pengguna_data['vaccine_2']
                )
        self.stdout.write(self.style.SUCCESS('Successfully saved pengguna'))
        
        lokasi_mock = json.loads(open('MOCK_LOKASI.json').read())
        for lokasi_data in lokasi_mock:
            exists = Lokasi.objects.filter(id=lokasi_data['id']).exists()
            if not exists:
                Lokasi.objects.create(
                    id = lokasi_data['id'],
                    qr = lokasi_data['qr'],
                    nama = lokasi_data['nama'],
                    alamat = lokasi_data['alamat'],
                    kapasitas = lokasi_data['kapasitas']
                )
        self.stdout.write(self.style.SUCCESS('Successfully saved lokasi'))
            