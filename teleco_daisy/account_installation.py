import json
import requests
from teleco_daisy.constants import Constants
from typing import List
from dataclasses import dataclass

@dataclass
class Installation:
    active_timer: str = None
    firmware_version: str = None
    id_account: int = 0
    id_installation: int = 0
    id_installation_device: int = 0
    id_session: str = None
    inst_code: str = None
    inst_description: str = None
    installation_order: int = 0
    weekend: str = None
    workdays: str = None
    latitude: float = 0.0
    longitude: float = 0.0

    def get_id_installation(self) -> int:
        return self.id_installation

    def set_id_installation(self, id_installation: int):
        self.id_installation = id_installation

    def get_id_account(self) -> int:
        return self.id_account

    def set_id_account(self, id_account: int):
        self.id_account = id_account

    def get_inst_code(self) -> str:
        return self.inst_code

    def set_inst_code(self, inst_code: str):
        self.inst_code = inst_code

    def get_inst_description(self) -> str:
        return self.inst_description

    def set_inst_description(self, inst_description: str):
        self.inst_description = inst_description

    def get_id_session(self) -> str:
        return self.id_session

    def set_id_session(self, id_session: str):
        self.id_session = id_session

    def get_installation_order(self) -> int:
        return self.installation_order

    def set_installation_order(self, installation_order: int):
        self.installation_order = installation_order

    def get_activetimer(self) -> str:
        return self.active_timer

    def set_activetimer(self, active_timer: str):
        self.active_timer = active_timer

    def get_weekend(self) -> str:
        return self.weekend

    def set_weekend(self, weekend: str):
        self.weekend = weekend

    def get_workdays(self) -> str:
        return self.workdays

    def set_workdays(self, workdays: str):
        self.workdays = workdays

    def get_firmware_version(self) -> str:
        return self.firmware_version

    def set_firmware_version(self, firmware_version: str):
        self.firmware_version = firmware_version

    def get_id_installation_device(self) -> int:
        return self.id_installation_device

    def set_id_installation_device(self, id_installation_device: int):
        self.id_installation_device = id_installation_device

    def get_latitude(self) -> float:
        return self.latitude

    def set_latitude(self, latitude: float):
        self.latitude = latitude

    def get_longitude(self) -> float:
        return self.longitude

    def set_longitude(self, longitude: float):
        self.longitude = longitude

    def print(self):
        print(json.dumps({
            "active_timer": self.active_timer,
            "firmware_version": self.firmware_version,
            "id_account": self.id_account,
            "id_installation": self.id_installation,
            "id_installation_device": self.id_installation_device,  
            "id_session": self.id_session,
            "inst_code": self.inst_code,
            "inst_description": self.inst_description,
            "installation_order": self.installation_order,
            "weekend": self.weekend,
            "workdays": self.workdays,
            "latitude": self.latitude,
            "longitude": self.longitude,    
       }))

class AccountInstallation:
    def __init__(self, id_account: int, id_session: str):
        self.id_account = id_account
        self.id_session = id_session
        self.installation_list: List[Installation] = []

    def get_id_account(self) -> int:
        return self.id_account

    def set_id_account(self, id_account: int):
        self.id_account = id_account

    def get_id_session(self) -> str:
        return self.id_session

    def set_id_session(self, id_session: str):
        self.id_session = id_session

    def get_installation_list(self) -> List[Installation]:
        return self.installation_list

    def set_installation_list(self, installation_list: List[Installation]):
        self.installation_list = installation_list

    def list(self, session: requests.Session):
        response = session.post(
            f"{Constants.BASE_URL}{Constants.ENDPOINT_ACCOUNT_INSTALLATION_LIST}",
            json={
                "idAccount": self.id_account,
                "idSession": self.id_session,
            },
        )

        try:
            json_data = response.json()
        except json.decoder.JSONDecodeError:
            raise Exception("Failed to decode JSON response")
        
        if response.status_code != 200 or json_data.get("codEsito") != "S":
            raise Exception("Failed to get account installation list: {}".format(json_data.get("msgEsito")))
        
        self.installation_list = []
        for i in json_data.get("valRisultato").get("installationList"):
            installation = Installation()
            for attr in i:
                if attr == "activetimer": installation.set_activetimer(i.get("activetimer"))
                elif attr == "firmwareVersion": installation.set_firmware_version(i.get("firmwareVersion"))
                elif attr == "idAccount": installation.set_id_account(i.get("idAccount"))
                elif attr == "idInstallation": installation.set_id_installation(i.get("idInstallation"))
                elif attr == "idInstallationDevice": installation.set_id_installation_device(i.get("idInstallationDevice"))
                elif attr == "idSession": installation.set_id_session(i.get("idSession"))
                elif attr == "instCode": installation.set_inst_code(i.get("instCode"))
                elif attr == "instDescription": installation.set_inst_description(i.get("instDescription"))
                elif attr == "installationOrder": installation.set_installation_order(i.get("installationOrder"))
                elif attr == "weekend": installation.set_weekend(i.get("weekend"))
                elif attr == "workdays": installation.set_workdays(i.get("workdays"))
                elif attr == "latitude": installation.set_latitude(i.get("latitude"))
                elif attr == "longitude": installation.set_longitude(i.get("longitude"))

            if installation.get_id_account() == 0:
                installation.id_account = None

            self.installation_list.append(installation)

    def pair(self, session: requests.Session, installation: Installation):
        response = session.post(
            f"{Constants.BASE_URL}{Constants.ENDPOINT_ACCOUNT_INSTALLATION_PAIR}",
            json={
                "activeTimer": installation.get_activetimer(),
                "firmwareVersion": installation.get_firmware_version(),
                "idAccount": self.id_account,
                "idInstallation": installation.get_id_installation(),
                "idInstallationDevice": installation.get_id_installation_device(),
                "idSession": self.id_session,
                "instCode": installation.get_inst_code(),
                "instDescription": installation.get_inst_description(),
                "installationOrder": installation.get_installation_order(),
                "weekend": installation.get_weekend(),
                "workdays": installation.get_workdays(),
                "latitude": installation.get_latitude(),
                "longitude": installation.get_longitude(),
            },
        )

        try:
            json_data = response.json()
        except json.decoder.JSONDecodeError:
            raise Exception("Failed to decode JSON response")
        
        if response.status_code != 200 or json_data.get("codEsito") != "S":
            raise Exception("Failed to pair account installation: {}".format(json_data.get("msgEsito")))

    def print(self):
        print(json.dumps({
            "id_account": self.id_account,
            "id_session": self.id_session,
            "installation_list": [i.__dict__ for i in self.installation_list],        
       }))

    def unpair(self, session: requests.Session, id_installation: int):
        response = session.post(
            f"{Constants.BASE_URL}{Constants.ENDPOINT_ACCOUNT_INSTALLATION_UNPAIR}",
            json={
                "idAccount": self.id_account,
                "idInstallation": id_installation,
                "idSession": self.id_session,
            },
        )

        try:
            json_data = response.json()
        except json.decoder.JSONDecodeError:
            raise Exception("Failed to decode JSON response")
        
        if response.status_code != 200 or json_data.get("codEsito") != "S":
            raise Exception("Failed to unpair account installation: {}".format(json_data.get("msgEsito")))
