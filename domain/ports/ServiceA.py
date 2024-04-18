from IPort import IPort


class ServiceA(IPort):
    def send_to_port(self, payload=None):
        """This allows a mediator to send contents of a call to a port"""
        pass
    
    def get_from_port(self, payload=None):
        """This allows a mediator to get data from a port"""
        pass
    
    def _capture_account_data(self):
        return '{"Account":"John Smith"}'