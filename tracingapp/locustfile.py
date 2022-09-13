from locust import HttpUser, task
import json
import random

class HelloWorldUser(HttpUser):
    access_token = None
    lokasi_qr = []
    user_account = []
    
    @task
    def list_lokasi(self):
        self.client.get("/lokasi")
    
    @task
    def get_lokasi(self):
        qr_code = random.choice(self.lokasi_qr)
        self.client.get("/lokasi/"+qr_code)
        
    @task
    def list_checkin(self):
        response = self.client.get(
            "/checkin",
            headers={
                "Authorization": f"Bearer {self.access_token}"
            }
        )
        if response.status_code == 401:
            self.relogin()
        
    @task
    def create_checkin(self):
        qr_code = random.choice(self.lokasi_qr)
        response = self.client.post(
            "/checkin/", 
            json={
                "lokasi_qr": qr_code
            },
            headers={
                "Authorization": f"Bearer {self.access_token}"
            }
        )
        if response.status_code == 401:
            self.relogin()
        
    
    @task
    def login(self):
        user = random.choice(self.user_account)
        self.client.post("/auth/token/", json={"username": user['username'], "password":user['password']})
        
    def relogin(self):
        while True:
            response = self.client.post("/auth/token/", json={"username":"admin", "password":"admin"})
            if response.status_code != 200:
                continue
            json_response_dict = response.json()
            self.access_token = json_response_dict['access']
            break    
        
    def on_start(self):
        self.relogin()    
        
        f_lokasi = open("MOCK_LOKASI.json").read()
        json_f_lokasi = json.loads(f_lokasi)
        for lokasi in json_f_lokasi:
            self.lokasi_qr.append(lokasi['qr'])
            
        f_user = open("MOCK_USER.json").read()
        json_f_user = json.loads(f_user)
        for user in json_f_user:
            self.user_account.append({
                "username": user['username'],
                "password": user['password']
            })
        
        