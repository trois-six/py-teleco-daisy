class ResponseValue:
    def __init__(self):
        self.codEsito = None
        self.msgEsito = None

    def get_cod_esito(self) -> str:
        return self.codEsito

    def set_cod_esito(self, codEsito: str):
        self.codEsito = codEsito

    def get_msg_esito(self) -> str:
        return self.msgEsito

    def set_msg_esito(self, msgEsito: str):
        self.msgEsito = msgEsito