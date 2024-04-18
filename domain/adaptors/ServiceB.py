from IAdaptor import IAdaptor

class ServiceB(IAdaptor):

    def send_to_adaptor(self, payload=None):
        """This allows a mediator to send contents of a call to an adaptor"""
        pass
    
    def get_from_adaptor(self, payload=None):
        """This allows a mediator to get contents of a call from an adaptor"""
        pass