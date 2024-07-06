from dataclasses import dataclass, field, fields, make_dataclass
from typing import Any, Dict
import json

"""
Scenario 3:

A REST API consumes the mediator / engine and the routes which ServiceOne talk to, send their payload into a route, right into ServiceOne Class.

The Mediator is invoked and passes mediator.adaptor.get_from_my_service(payload : json) or something similar

The Mediator then says something like: mediator.adaptor.send_to_port(payload :dict) which is an internal format.

The port then has a specifical call made like: mediator.port.send_to_my_service(payload: json) which speaks to the endpoint.

This time, some kind of flag is set, or perhaps is default, which automatically sends the payload from one of the mediator.adaptor.get_from_my_service(payload :json) and invokes
mediator.port.send_to_my_service(payload : json)

"""

class Harness():
    def __init__(self, signal_left, signl_right):
        self.signal_left = signal_left()
        self.signal_right = signl_right()
    
    
    def parse_left(self, payload):
        self.signal_left.parse(payload)
    
    
    def result_left(self):
        return self.signal_left.result()
    

    def parse_right(self, payload):
        self.signal_right.parse(payload)
    
    
    def result_right(self):
        return self.signal_right.result()
        

@dataclass
class APIOne:
    email: str = field(default=None)
    first_name: str = field(default=None)
    
    def parse(self, payload: Dict[str, Any]):
        properties = payload["Get_Employee"]["Response"]["Properties"]
        
        self.email = properties["email"]
        self.first_name = properties["first_name"]
    
    
    def result(self):
        return {"email":self.email, "first_name":self.first_name}
    
    
    def speak_to_my_third_party_device():
        return {"user":"dmarble", "group":"domain_users"}


@dataclass
class APITwo:
    email: str = field(default=None)
    first_name: str = field(default=None)
    
    def parse(self, payload: Dict[str, Any]):
        properties = payload["Employee_Search"]["Request"]["Parameters"]

        self.first_name = properties["first_name"]
        self.last_name = properties["last_name"]
        self.first_initial = str(self.first_name)[2]
        
        self.email = f"{self.first_initial}{self.last_name}@example.com"
    
    
    def result(self):
        return {"email":self.email, "first_name":self.first_name}
    
    
    def speak_to_my_third_party_device():
        return {"user":"dmarble", "group":"domain_users"}


if __name__ == '__main__':

    """This is an example of manual parsing."""

    payload_one = ""
    with open("./static/api_one.json", "r") as f:
        payload_one = json.load(f)
            
    my_api = APIOne()
    my_api.parse(payload_one)
    print(my_api.result())
    
    
    """This is an example of manual parsing."""
    
    payload_two = ""
    with open("./static/api_two.json", "r") as f:
        payload_two = json.load(f)
         
    my_api_two = APITwo()
    my_api_two.parse(payload_two)
    print(my_api_two.result())
    
    
    """This is an example of using the harness."""
    
    broker = Harness(APIOne, APITwo)
        
    broker.parse_left(payload_one)
    broker.parse_right(payload_two)
    
    print(broker.result_left())
    print(broker.result_right())