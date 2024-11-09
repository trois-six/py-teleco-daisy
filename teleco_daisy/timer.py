import json
import requests
from teleco_daisy.constants import Constants
from typing import List
from dataclasses import dataclass

@dataclass
class Timer:
    alba_tramonto: int = 0
    command_param: str = None
    crepuscolare: str = None
    crepuscolare_offset: int = 0
    giorni: str = None
    id_installation_device_command: int = 0
    id_installation_device_timer: int = 0
    info: str = None
    timer_active: str = None
    timer_date: str = None
    timer_date_expire: str = None
    timer_order: int = 0

    def get_alba_tramonto(self) -> int:
        return self.alba_tramonto

    def set_alba_tramonto(self, alba_tramonto: int):
        self.alba_tramonto = alba_tramonto

    def get_command_param(self) -> str:
        return self.command_param

    def set_command_param(self, command_param: str):
        self.command_param = command_param

    def get_crepuscolare(self) -> str:
        return self.crepuscolare

    def set_crepuscolare(self, crepuscolare: str):
        self.crepuscolare = crepuscolare

    def get_crepuscolare_offset(self) -> int:
        return self.crepuscolare_offset

    def set_crepuscolare_offset(self, crepuscolare_offset: int):
        self.crepuscolare_offset = crepuscolare_offset

    def get_giorni(self) -> str:
        return self.giorni

    def set_giorni(self, giorni: str):
        self.giorni = giorni

    def get_id_installation_device_command(self) -> int:
        return self.id_installation_device_command

    def set_id_installation_device_command(self, id_installation_device_command: int):
        self.id_installation_device_command = id_installation_device_command

    def get_id_installation_device_timer(self) -> int:
        return self.id_installation_device_timer

    def set_id_installation_device_timer(self, id_installation_device_timer: int):
        self.id_installation_device_timer = id_installation_device_timer

    def get_info(self) -> str:
        return self.info

    def set_info(self, info: str):
        self.info = info

    def get_timer_active(self) -> str:
        return self.timer_active

    def set_timer_active(self, timer_active: str):
        self.timerActive = timer_active

    def get_timer_date(self) -> str:
        return self.timer_date

    def set_timer_date(self, timer_date: str):
        self.timerDate = timer_date

    def get_timer_date_expire(self) -> str:
        return self.timer_date_expire

    def set_timer_date_expire(self, timer_date_expire: str):
        self.timer_date_expire = timer_date_expire

    def get_timer_order(self) -> int:
        return self.timer_order

    def set_timer_order(self, timer_order: int):
        self.timer_order = timer_order
    
    def print(self):
        print(json.dumps({
            "alba_tramonto": self.alba_tramonto,
            "command_param": self.command_param,
            "crepuscolare": self.crepuscolare,
            "crepuscolare_offset": self.crepuscolare_offset,
            "giorni": self.giorni,
            "id_installation_device_command": self.id_installation_device_command,
            "id_installation_device_timer": self.id_installation_device_timer,
            "info": self.info,
            "timer_active": self.timer_active,
            "timer_date": self.timer_date,
            "timer_date_expire": self.timer_date_expire,
            "timer_order": self.timer_order
        }))

@dataclass
class TimerSetup:
    id_account: int = 0
    id_installation: int = 0
    id_installation_device: int = 0
    id_session: str = None
    timer_list: List[Timer] = None

@dataclass
class Command:
    commandAction: str = None
    commandId: int = 0
    commandIndex: int = 0
    commandParam: str = None
    commandProcessed: int = 0
    commandReceivedUR: str = None
    commandStatus: int = 0
    commandreceived: int = 0
    deviceCode: str = None
    idDevicetypeCommandModel: int = 0
    idInstallationDevice: int = 0
    idInstallationDeviceCommand: int = 0
    lowlevelCommand: str = None

    def get_command_action(self) -> str:
        return self.commandAction

    def set_command_action(self, commandAction: str):
        self.commandAction = commandAction

    def get_command_id(self) -> int:
        return self.commandId

    def set_command_id(self, commandId: int):
        self.commandId = commandId

    def get_command_index(self) -> int:
        return self.commandIndex

    def set_command_index(self, commandIndex: int):
        self.commandIndex = commandIndex

    def get_command_param(self) -> str:
        return self.commandParam

    def set_command_param(self, commandParam: str):
        self.commandParam = commandParam

    def get_command_processed(self) -> int:
        return self.commandProcessed

    def set_command_processed(self, commandProcessed: int):
        self.commandProcessed = commandProcessed

    def get_command_received_ur(self) -> str:
        return self.commandReceivedUR

    def set_command_received_ur(self, commandReceivedUR: str):
        self.commandReceivedUR = commandReceivedUR

    def get_commandreceived(self) -> int:
        return self.commandreceived

    def set_commandreceived(self, commandreceived: int):
        self.commandreceived = commandreceived

    def get_command_status(self) -> int:
        return self.commandStatus

    def set_command_status(self, commandStatus: int):
        self.commandStatus = commandStatus

    def get_id_devicetype_command_model(self) -> int:
        return self.idDevicetypeCommandModel

    def set_id_devicetype_command_model(self, idDevicetypeCommandModel: int):
        self.idDevicetypeCommandModel = idDevicetypeCommandModel

    def get_id_installation_device(self) -> int:
        return self.idInstallationDevice

    def set_id_installation_device(self, idInstallationDevice: int):
        self.idInstallationDevice = idInstallationDevice

    def get_id_installation_device_command(self) -> int:
        return self.idInstallationDeviceCommand

    def set_id_installation_device_command(self, idInstallationDeviceCommand: int):
        self.idInstallationDeviceCommand = idInstallationDeviceCommand

    def get_device_code(self) -> str:
        return self.deviceCode

    def set_device_code(self, deviceCode: str):
        self.deviceCode = deviceCode

    def get_lowlevel_command(self) -> str:
        return self.lowlevelCommand

    def set_lowlevel_command(self, lowlevelCommand: str):
        self.lowlevelCommand = lowlevelCommand

@dataclass
class Device:
    def __init__(self, id_account: int, id_session: str, id_installation: int, id_installation_device: int):
        self.id_installation = id_installation
        self.id_installation_device = id_installation_device
        self.id_account = id_account
        self.id_session = id_session
        self.timer_list: List[Timer] = []
        self.command_list: List[Command] = []

    def timer_list(self, session: requests.Session):
        response = session.post(
            f"{Constants.BASE_URL}{Constants.ENDPOINT_TIMER_DEVICE_LIST}",
            json={
                "idAccount": self.id_account,
                "idSession": self.id_session,
                "idInstallation": self.id_installation,
                "idInstallationDevice": self.id_installation_device,
            },
        )

        try:
            json_data = response.json()
        except json.decoder.JSONDecodeError:
            raise Exception("Failed to decode JSON response")
        
        if response.status_code != 200 or json_data.get("codEsito") != "S":
            raise Exception("Failed to get timer device list: {}".format(json_data.get("msgEsito")))
        
        self.timer_list = []
        for i in json_data.get("valRisultato").get("timerList"):
            timer = Timer()
            for attr in i:
                if attr == "albaTramonto": timer.set_alba_tramonto(i.get("albaTramonto"))
                elif attr == "commandParam": timer.set_command_param(i.get("commandParam"))
                elif attr == "crepuscolare": timer.set_crepuscolare(i.get("crepuscolare"))
                elif attr == "crepuscolareOffset": timer.set_crepuscolare_offset(i.get("crepuscolareOffset"))
                elif attr == "giorni": timer.set_giorni(i.get("giorni"))
                elif attr == "idInstallationDeviceCommand": timer.set_id_installation_device_command(i.get("idInstallationDeviceCommand"))
                elif attr == "idInstallationDeviceTimer": timer.set_id_installation_device_timer(i.get("idInstallationDeviceTimer"))
                elif attr == "info": timer.set_info(i.get("info"))
                elif attr == "timerActive": timer.set_timer_active(i.get("timerActive"))
                elif attr == "timerDate": timer.set_timer_date(i.get("timerDate"))
                elif attr == "timerDateExpire": timer.set_timer_date_expire(i.get("timerDateExpire"))
                elif attr == "timerOrder": timer.set_timer_order(i.get("timerOrder"))

            if timer.get_id_account() == 0:
                timer.id_account = None

            self.timer_list.append(timer)

    def print(self):
        print(json.dumps({
            "id_installation": self.id_installation,
            "id_installation_device": self.id_installation_device,
            "id_account": self.id_account,
            "id_session": self.id_session,
            "timer_list": [i.__dict__ for i in self.timer_list],        
       }))
        
    def setup(self, session: requests.Session, timer_list: List[Timer]):
        response = session.post(
            f"{Constants.BASE_URL}{Constants.ENDPOINT_TIMER_DEVICE_SETUP}",
            json={
                "idAccount": self.id_account,
                "idSession": self.id_session,
                "idInstallation": self.id_installation,
                "idInstallationDevice": self.id_installation_device,
                "timerList": timer_list,
            },
        )

        try:
            json_data = response.json()
        except json.decoder.JSONDecodeError:
            raise Exception("Failed to decode JSON response")
        
        if response.status_code != 200 or json_data.get("codEsito") != "S":
            raise Exception("Failed to set timer device setup: {}".format(json_data.get("msgEsito")))

    def command_list(self, session: requests.Session):
        response = session.post(
            f"{Constants.BASE_URL}{Constants.ENDPOINT_COMMAND_DEVICE_LIST}",
            json={
                "idAccount": self.id_account,
                "idSession": self.id_session,
                "idInstallation": self.id_installation,
                "idInstallationDevice": self.id_installation_device,
            },
        )

        try:
            json_data = response.json()
        except json.decoder.JSONDecodeError:
            raise Exception("Failed to decode JSON response")
        
        if response.status_code != 200 or json_data.get("codEsito") != "S":
            raise Exception("Failed to get command device list: {}".format(json_data.get("msgEsito")))
        