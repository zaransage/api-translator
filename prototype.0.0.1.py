from  dataclasses import dataclass
import json

"""
"""


"""
Method to ask the source for data

Method to parse the data into the class

method to send the updated data to the source

method to pass data to mediator; why is this needed ......

"""

@dataclass
class APIOne():
    
    payload : str
    email : dict
       
    
    def parse_data_to_params(self, params):
        pass
    
    
    def ask_api_something(self):
        with open('/home/dmarble/git/api-translator/static/api_one.json', 'r') as f:
           self.payload = json.loads(f.read())
    
    
    def tell_api_something(self):
        pass


    def send_data_to_mediator(self):
        pass
    
    
    def send_params(self, payload):
        return self.payload
    
    def __str__(self):
        return f"{self.payload['Get_Employee']['Response']['Properties']['id']}"


class APITwo():
    
    def __init__(self):
        self.payload = ''
    
    
    def parse_data_to_params(self):
        pass
    
    
    def ask_api_something(self):
        with open('/home/dmarble/git/api-translator/static/api_two.json', 'r') as f:
            self.payload = f.readlines()
            
    
    def tell_api_something(self):
        pass


    def send_data_to_mediator(self):
        pass







"""
method to ask destination for data

method to parse the data into the class

method to send the updated data to the destination

method to pass to mediator?

"""


if __name__ == '__main__':
    a = APIOne()
    a.ask_api_something()
    
    b = APIOne()
    b.parse_data_to_params(a.send_params())
    
    print(b)