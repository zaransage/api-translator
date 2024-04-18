
class IEngine():
    def __init__(self, port, adaptor):
        self.port = port
        self.adaptor = adaptor
        
    def send_to_port(self):
        """This allows a mediator to send contents of a call to a port"""
        pass
    
    def get_from_port(self):
        """This allows a mediator to get data from a port"""
        pass
    
    def send_to_adaptor(self):
        """This allows a mediator to send contents of a call to an adaptor"""
        pass
    
    def get_from_adaptor(self):
        """This allows a mediator to get contents of a call from an adaptor"""
        pass