"""Test for my functions."""

from my_module.functions import encoder, decoder
##Encoded should return a string.
##Decoder should return a string.

sampleOgMessage = "HELLO"

def test_encoder():

    assert encoder(sampleOgMessage) != None

sampleEncodedMessage = "Đ3ĔĔ0"

def test_decoder():

    assert decoder(sampleEncodedMessage) != None
    



                 
    