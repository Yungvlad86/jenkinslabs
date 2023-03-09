import Models
from Main import *

def test_createBD():
    assert createBD() == True

def test_fillClients():
    assert Models.Client.Name == True
    assert Models.Client.City == True
    assert Models.Client.Address == True

def test_fillOrders():
    assert Models.Order.Client_id == True
    assert Models.Order.Amount ==True
    assert Models.Order.Date == True
    assert Models.Order.Description == True
    
def test_countClients():
    fillBD()
    assert showClientsBD() >= 10

def test_countOrders():
    assert showOrdersBD() >= 10

