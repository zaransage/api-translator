from fastapi import FastAPI
from domain.core.Engine import Engine
from domain.ports.ServiceA import ServiceA
from domain.adaptors.ServiceB import ServiceB


"""
There is an argument that this main example could itself an adaptor to the Engine / Mediator.

In this case, we are using an API entry to the Mediator as a user interface but this does not need to be so.
The importane is that the invocation of Serice A asks the Mediator 'to do something' by sending a payload to a related port or adaptor.

The individual ports or adaptors in this case, each handle their own use implementations.

You would seldom want to change the Engine / Mediator behavior and only add more ports or adaptors as needed.
"""


def main():
    
    """We really only want this simple interface to let us decide what two services should talk"""
    
    mediator = Engine(ServiceA, ServiceB)  
    

    app = FastAPI()
    
    
    @app.get("/")
    def index():
        return f"OK"


    """Set up the initial routes to allow requests to the mediator to be send to the correct port or adaptor by REST call."""

    @app.get("/service/a/accounts/{account}")
    async def get_accounts(account):
        return mediator.port.get_from_port(account)
    
    @app.post("/service/a/accounts/{account}")
    async def post_accounts(account):
        return mediator.port.send_to_port(account)
    
    
    """Each port or adaptor has its own implementation and sends back the results to the mediator."""
    
    @app.get("/service/b/accounts/{account}")
    async def get_accounts(account):
        return mediator.adaptor.get_from_adaptor(account)
    
    @app.post("/service/b/accounts/{account}")
    async def post_accounts(account):
        return mediator.adaptor.send_to_adaptor(account)


if __name__ == '__main__':
    main()