from SimpleMediator import SimpleMediator
from MediatorProxy import MediatorProxy
from Component import Component
from Message import Message

my_mediator = SimpleMediator()
allowed = [0, 1]
my_mediator_proxy = MediatorProxy(allowed)

try:   
    c1 = Component(my_mediator_proxy, "XML")
    c2 = Component(my_mediator_proxy, "JSON")
    c1.send_message(c5.my_id, "CSV", "\{\}")
except Exception as e:
    print(e)


