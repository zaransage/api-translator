
"""
In our first set of prototypes, the interfaces for the engine, the port and adaptor are very similar.
Future revisions might elect to reduce this down to as few as one or two.
"""

class IPort():
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