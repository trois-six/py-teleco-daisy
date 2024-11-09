from teleco_daisy.user import User, RegistrationUser
from teleco_daisy.account_installation import Installation, AccountInstallation
from teleco_daisy.timer import Device, TimerSetup
from teleco_daisy.constants import Constants
from typing import List
import requests
from requests_toolbelt.utils import dump

def logging_hook(response, *args, **kwargs):
    data = dump.dump_all(response)
    print(data.decode('utf-8'))

class CloudService:
    def __init__(self, debug: bool = False):
        self.s = requests.Session()
        self.s.headers.update({"Content-Type": "application/json; charset=UTF-8"})
        self.s.auth = (Constants.USERNAME, Constants.PASSWORD)
        self.user = None
        self.account_installation = None
        self.devices: List[Device] = []

        if debug:
            self.s.hooks["response"] = [logging_hook]

    def AccountInstallationList(self):
        if self.user is None or self.user.get_id_session() is None:
            raise Exception("User must login first")
        
        self.account_installation = AccountInstallation(self.user.get_id_account(), self.user.get_id_session())
        self.account_installation.list(self.s)

    def AccountInstallationPair(self, 
            active_timer: str,
            firmware_version: str,
            id_installation: int,
            id_installation_device: int,
            inst_code: str,
            inst_description: str,
            installation_order: int,
            weekend: str,
            workdays: str,
            latitude: float,
            longitude: float):
        if self.user is None or self.user.get_id_session() is None:
            raise Exception("User must login first")
        
        self.account_installation = AccountInstallation(self.user.get_id_account(), self.user.get_id_session())
        self.account_installation.pair(self.s, Installation(
            active_timer = active_timer,
            firmware_version = firmware_version,
            id_installation = id_installation,
            id_installation_device = id_installation_device,
            inst_code = inst_code,
            inst_description = inst_description,
            installation_order = installation_order,
            weekend = weekend,
            workdays = workdays,
            latitude = latitude,
            longitude = longitude,
        ))

    def AccountInstallationPrint(self):
        if self.account_installation is None:
            raise Exception("Account installation list must be done first")
        
        self.account_installation.print()

    def AccountInstallationUnpair(self, id_installation: int):
        if self.user is None or self.user.get_id_session() is None:
            raise Exception("User must login first")
        
        self.account_installation = AccountInstallation(self.user.get_id_account(), self.user.get_id_session())
        self.account_installation.unpair(self.s, id_installation)

    def AccountLogin(self, username: str, password: str):
        self.user = User(email=username, password=password)
        self.user.set_device_serial("0000000000000000")
        self.user.set_device_description("Teleco Daisy Python Client")
        self.user.set_id_app(None)
        self.user.login(self.s)

    def AccountLogout(self):
        if self.user is None or self.user.get_id_session() is None:
            raise Exception("User not logged in")
        
        self.user.logout(self.s)

    def AccountRegistration(self, username: str, password: str, firstname: str, lastname: str, account_source: str):
        if self.user is None or self.user.get_id_session() is None:
            raise Exception("User not logged in")
        
        RegistrationUser(email=username, password=password, firstname=firstname, lastname=lastname, account_source=account_source).register(self.s)

    def AccountPrint(self):
        if self.user is None or self.user.get_id_session() is None:
            raise Exception("User not logged in")

        self.user.print()

    def ChangePassword(self, new_password: str):
        if self.user is None or self.user.get_id_session() is None:
            raise Exception("User not logged in")

        self.user.change_password(self.s, new_password)

    def ResetPassword(self, username: str):
        self.user = User(email=username)
        self.user.reset_password(self.s)
    
    def TimerDeviceList(self):
        if self.user is None or self.user.get_id_session() is None:
            raise Exception("User must login first")
        
        self.devices = []
        for installation in self.account_installation.get_installation_list():
            device = Device(
                id_installation=installation.get_id_installation(),
                id_installation_device=installation.get_id_installation_device(),
                id_account=self.user.get_id_account(),
                id_session=self.user.get_id_session()
            )

            device.timer_list(self.s)
            self.devices.append(device)

    def TimerDevicePrint(self):
        if len(self.devices) == 0:
            raise Exception("Timer device list must be done first")
        
        for device in self.devices:
            device.print()

    def TimerDeviceSetup(self, timer_setup: TimerSetup):
        if self.user is None or self.user.get_id_session() is None:
            raise Exception("User must login first")
        
        device = Device(
            id_installation=timer_setup.id_installation,
            id_installation_device=timer_setup.id_installation_device,
            id_account=timer_setup.id_account,
            id_session=timer_setup.id_session
        )

        # Setup timer for device
        device.setup(self.s, timer_setup.timer_list)

        # Update state of device
        for d in self.devices:
            if d.get_id_installation() == timer_setup.id_installation and d.get_id_installation_device() == timer_setup.id_installation_device:
                d.timer_list(self.s)

    def CommandDeviceList(self):
        if self.user is None or self.user.get_id_session() is None:
            raise Exception("User must login first")
               
        #TODO: Implement command device list