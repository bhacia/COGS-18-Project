"""Classes used throughout project"""
from my_module.functions import encoder, decoder

class Email():
    
    def __init__(self, email):

        self.email = []
        self.email.append(email)
    
    def printOriginalMessage(self):
        
        print(self.email[0])
        
    def printEncodedMessage(self):
        
        encoded = encoder(self.email[0])
        self.email.append(encoded)
        print(encoded)
        
    def printDecodedMessage(self):
        
        decoded = decoder(self.email[1])
        self.email.append(decoded)
        print(decoded)