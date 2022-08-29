from core.client import Client, ClientMock

client = Client()
client_mock = ClientMock()

class MerchandService():
    ENDPOINT = '/merchands/'
    
    def get_merchand(self, id):
        return client.get(self.ENDPOINT + f'{int(id)}/')
    
    def get_merchands(self, params):
        return client.get(self.ENDPOINT, params)
    
    def get_merchands_mock(self):
        return client_mock.get('core/json/merchands.json')
    

class PaymentService():
    ENDPOINT = '/payments/'
    
    def get_payment(self, id):
        return client.get(self.ENDPOINT + f'{int(id)}/')
    
    def get_payments(self, params):
        return client.get(self.ENDPOINT, params)
    
    def get_payments_mock(self):
        return client_mock.get('core/json/payments.json')