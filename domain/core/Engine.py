from IEngine import IEngine


class Engine(IEngine):
    def __init__(self, port, adaptor):
        self.port = port
        self.adaptor = adaptor
        
    def send_to_port(self):
        """This allows a mediator to send contents of a call to a port"""
        self.port.send_to_port(self, payload=None)
    
    def get_from_port(self):
        """This allows a mediator to get data from a port"""
        self.port.get_from_port(self, payload=None)
    
    def send_to_adaptor(self):
        """This allows a mediator to send contents of a call to an adaptor"""
        self.adaptor.send_to_adaptor(self, payload=None)
    
    def get_from_adaptor(self):
        """This allows a mediator to get contents of a call from an adaptor"""
        self.adaptor.get_from_adaptor(self, payload=None)