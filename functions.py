"""A collection of function for doing my project."""
#These functions assume that the message only consists of letters.

def encoder(message): 
    #Message is a string of the original message. Key is a number that helps encode the message.
    """Function is supposed to encode the original message and return the encoded message."""
    
    secretLetters = {"a" : "@", "E" : "3", "i" : "!", 
                     "O" : "0", "G" : "6", "S" : "$", 
                     "l" : "1", "v" : "^", "g" : "&"}
    key = 200
    
    #Modified from my A2.
    encoded = ""
    for char in message:
        if char in secretLetters:
            encoded += secretLetters[char]
        else:
            codePoint = ord(char) + key
            chr_key = chr(codePoint)
            encoded += chr_key
            
    return encoded

def decoder(encoded): 
    #Encoded is a string of the encoded message. Key is a number that helps decode the message.
    """Fuction is supposed to decode the encoded message and return the decoded message."""
    
    uncoveredLetters = {"@" : "a", "3" : "E", "!" : "i", 
                        "0" : "O", "6" : "G", "$" : "S", 
                        "1" : "l", "^" : "v", "&" : "g"}
    key = 200
    
    #Modified from my A2
    decoded = ""
    for char in encoded:
        if char in uncoveredLetters:
            decoded += uncoveredLetters[char]
        else:
            codePoint = ord(char) - key
            chr_key = chr(codePoint)
            decoded += chr_key
            
    return decoded
