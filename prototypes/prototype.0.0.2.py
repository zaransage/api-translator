


"""
Scenario 1:

A REST API consumes the mediator / engine and the routes which ServiceOne talk to, send their payload into a route, right into ServiceOne Class.

The Mediator is invoked and passes mediator.adaptor.get_from_my_service(payload : json) or something similar

The Mediator then says something like: mediator.adaptor.send_to_port(payload :dict) which is an internal format.

The port then has a specifical call made like: mediator.port.send_to_port_service(payload: json) which speaks to the endpoint.

"""