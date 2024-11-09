import json
import requests
from teleco_daisy.constants import Constants
from dataclasses import dataclass

@dataclass
class User:
    device_description: str = None
    device_serial: str = None
    email: str = None
    id_app: str = "DAISY"
    password: str = None
    id_account: int = 0
    id_session: str = None

    def get_email(self) -> str:
        return self.email

    def set_email(self, email: str):
        self.email = email

    def get_pwd(self) -> str:
        return self.password

    def set_pwd(self, password: str):
        self.password = password

    def get_device_serial(self) -> str:
        return self.device_serial

    def set_device_serial(self, device_serial: str):
        self.device_serial = device_serial

    def get_device_description(self) -> str:
        return self.device_description

    def set_device_description(self, device_description: str):
        self.device_description = device_description

    def get_id_app(self) -> str:
        return self.id_app

    def set_id_app(self, id_app: str):
        self.id_app = id_app

    def login(self, session: requests.Session):
        response = session.post(
            f"{Constants.BASE_URL}{Constants.ENDPOINT_USER_LOGIN}",
            json={
                "deviceDescription": self.device_description,
                "deviceSerial": self.device_serial,
                "email": self.email,
                "pwd": self.password,
            },
        )

        try:
            json_data = response.json()
        except json.decoder.JSONDecodeError:
            raise Exception("Failed to decode JSON response")
        
        if response.status_code == 200 and json_data.get("codEsito") == "S":
            self.id_account = json_data.get("valRisultato").get("idAccount") 
            self.id_session = json_data.get("valRisultato").get("idSession")
        else:
            raise Exception("Login failed: {}".format(json_data.get("msgEsito")))
    
    def logout(self, session: requests.Session):
        response = session.post(
            f"{Constants.BASE_URL}{Constants.ENDPOINT_USER_LOGOUT}",
            json={
                "idSession": self.id_session,
            },
        )

        try:
            json_data = response.json()
        except json.decoder.JSONDecodeError:
            raise Exception("Failed to decode JSON response")
        
        if response.status_code != 200 or json_data.get("codEsito") != "S":
            raise Exception("Logout failed: {}".format(json_data.get("msgEsito")))

    def get_id_account(self) -> int:
        return self.id_account
    
    def get_id_session(self) -> str:
        return self.id_session
    
    def print(self):
        print(json.dumps({
            "device_description": self.device_description,
            "device_serial": self.device_serial,
            "email": self.email,
            "id_app": self.id_app,
            "id_account": self.id_account,
            "id_session": self.id_session,
        }))
    
    def change_password(self, session: requests.Session, new_password: str):
        response = session.post(
            f"{Constants.BASE_URL}{Constants.ENDPOINT_USER_CHANGE_PASSWORD}",
            json={
                "idSession": self.id_session,
                "idAccount": self.id_account,
                "pwdNew": new_password,
                "pwdOld": self.password,
            },
        )

        try:
            json_data = response.json()
        except json.decoder.JSONDecodeError:
            raise Exception("Failed to decode JSON response")
        
        if response.status_code == 200 and json_data.get("codEsito") == "S":
            self.password = new_password
        else:
            raise Exception("Failed to change password: {}".format(json_data.get("msgEsito")))
        
    def reset_password(self, session: requests.Session):
        response = session.post(
            f"{Constants.BASE_URL}{Constants.ENDPOINT_USER_RESET_PASSWORD}",
            json={
                "email": self.email,
            },
        )

        try:
            json_data = response.json()
        except json.decoder.JSONDecodeError:
            raise Exception("Failed to decode JSON response")
        
        if response.status_code != 200 or json_data.get("codEsito") != "S":
            raise Exception("Failed to reset password: {}".format(json_data.get("msgEsito")))

@dataclass
class RegistrationUser(User):
    email: str = None
    password: str = None
    account_source: str = None
    firstname: str = None
    flg_advert: str = None
    flg_banner: str = "S"
    lastname: str = None

    def register(self, session: requests.Session):
        response = session.post(
            f"{Constants.BASE_URL}{Constants.ENDPOINT_USER_REGISTRATION}",
            json={
                "email": self.username,
                "pwd": self.password,
                "firstname": self.firstname,
                "lastname": self.lastname,
                "accountSource": self.account_source,
                "flgAdvert": self.flg_advert,
            },
        )

        try:
            json_data = response.json()
        except json.decoder.JSONDecodeError:
            raise Exception("Failed to decode JSON response")
        
        if response.status_code != 200 or json_data.get("codEsito") != "S":
            raise Exception("Failed to register user: {}".format(json_data.get("msgEsito")))