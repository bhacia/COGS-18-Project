"""Script to run some part of my project."""

# This adds the directory above to our Python path
#   This is so that we can add import our custom python module code into this script
import sys
sys.path.append('../')

# Imports
from my_module.functions import encoder, decoder
from my_module.classes import Email

###
###

# PYTHON SCRIPT HERE

lizetteEmail = Email("HELLO How are you")
brigetteEmail = Email("i am doing greaty GREAT")

momEmail = Email("What will we watch tonight")
myEmail = Email("How about The Amazing Spiderman One")

Email.printOriginalMessage(lizetteEmail)
Email.printEncodedMessage(lizetteEmail)
Email.printDecodedMessage(lizetteEmail)

print("\n")

Email.printOriginalMessage(brigetteEmail)
Email.printEncodedMessage(brigetteEmail)
Email.printDecodedMessage(brigetteEmail)

print("\n")

Email.printOriginalMessage(momEmail)
Email.printEncodedMessage(momEmail)
Email.printDecodedMessage(momEmail)

print("\n")

Email.printOriginalMessage(myEmail)
Email.printEncodedMessage(myEmail)
Email.printDecodedMessage(myEmail)
