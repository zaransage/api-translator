from dataclasses import dataclass, field, fields, make_dataclass
from typing import Any, Dict
import json

"""
Scenario 4:

Now we want to see if we need to maintain state within the harness.

There are some conditions you can just invoke a call from one side and have it submit commands to the other.

I am not sure we need a state, this is an experiment.
I am not sure we need to translate between both of these sides or if we are okay with leaving a side off.

"""


class State():
    
    def __init__(self):
        self.state = {}
    

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
    #print(my_api.result())
    
    
    """This is an example of manual parsing."""
    
    payload_two = ""
    with open("./static/api_two.json", "r") as f:
        payload_two = json.load(f)
         
    my_api_two = APITwo()
    my_api_two.parse(payload_two)
    #print(my_api_two.result())
    
    
    """This is an example of using the harness."""
    
    broker = Harness(APIOne, APITwo)
        
    broker.parse_left(payload_one)
    broker.parse_right(payload_two)
    
    #print(broker.result_left())
    #print(broker.result_right())
    
    """Experiment 1"""
    """We have an interesting idea that the classes can actually directly be parsed"""
    
    # broker.parse_right(broker.result_left())
    
    """Experiment 2"""
    """The trouble is, we might have to handle 'native parsing' between our classes and between the JSON sources"""
    
    state = {}
    
    state["email"] = (broker.result_left()["email"], broker.result_right()["email"])
    
    """Does it matter I have this? Where I can re-parse this class specific return?"""
    """Do I actually need to have a new function to just parse between the classes, using the class to standardize between responses?"""
    
    #print(state)
    
    
    """Experiment 3"""
    """It is entirely possible the idea is to just have a single side with a unified interface and handle the payload later"""
    
    new_broker = Harness(APITwo, APIOne)
    
    broker.result_left()
    new_broker.result_left()