from  dataclasses import dataclass
import json

"""
"""


"""
Scenario 2:

Get data from ServiceOne API, convert the response to a class or dict, send to ServiceTwo class, which sends to ServiceTwo API.

"""


class Mediator():
    def __init__(self, port, adaptor):
        self.port = port
        self.adaptor = adaptor
        
        
    def get_from_my_service(self, payload):
        pass
    
    
    def send_to_my_service(self, payload):
        pass


    def send_to_other_service():
        pass
    
    
    def get_from_other_service():
        pass


@dataclass
class APIOne():
    
    
    def __init__(self):
        self.payload = ""
               
    def get_from_my_service(self, payload: json):
        """request.get()"""
        
        with open('/home/dmarble/git/api-translator/static/api_one.json', 'r') as f:
           self.payload = json.loads(f.read())
    
    
    def send_to_my_service(self, payload: json):
        """request.post()"""
        pass


    def send_to_other_service(self, payload: dict) ->dict:
        """Dict of the data which I can send over to an other class built"""
        pass
    
    
    def get_from_other_service(self, payload: dict):
        """Process a dict key and value pairs into what I need for my service's payload"""
        pass
    
    
    def __str__(self):
        return f"{self.payload['Get_Employee']['Response']['Properties']['id']}"


@dataclass
class APITwo():
    
    def __init__(self):
        self.payload = ""
           
    def get_from_my_service(self, payload: json):
        """request.get()"""
        
        with open('/home/dmarble/git/api-translator/static/api_two.json', 'r') as f:
           self.payload = json.loads(f.read())
    
    
    def send_to_my_service(self, payload: json):
        """request.post()"""
        pass


    def send_to_other_service(self, payload: dict) ->dict:
        """Dict of the data which I can send over to an other class built"""
        pass
    
    
    def get_from_other_service(self, payload: dict):
        """Process a dict key and value pairs into what I need for my service's payload"""
        pass
    
    
    def __str__(self):
        return f"{self.payload['Get_Employee']['Response']['Properties']['id']}"



"""
The question becomes, when do I need a payload and when do I have the translated-to class send the data over to the service?

Are there any of these methods which are really private? I expect there to alway be more methods added per service but not exposed.

This may be a question of when I am asking to send directly to the port from an adaptor and when I am asking or telling my service something.

"""


if __name__ == '__main__':
        
    """
    Condition 1: 
        1. I send a command of some kind into my adaptor
        2. This captures data and stores it locally to itself.
        3. The send to other service calls what ....
        4. The other service somehow gets this adjusted data
        5. The second class, the port, sends its request to the service itself.
    """    
        
    mediator = Mediator(APIOne, APITwo)
    
    mediator.adaptor.get_from_my_service('{username}')
    mediator.adaptor.send_to_other_service() """Does this invoke something? Take a parameter? Only possible as a private method?"""
    mediator.port.get_from_other_service()
    mediator.port.send_to_my_service()