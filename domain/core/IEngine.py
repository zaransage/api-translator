

"""
The Engine is supposed to allow for a common signature between any two services.
The way it does this, is to accept the payload of a request per function call.

The mediator simply confines the amount of calls which can be made and makes the port or adaptor
handle all the implementation work.

The signatures today are very similar but you might find you want bi-directional communications, so this might be useful.
"""

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