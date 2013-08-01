#!/usr/local/bin/python

import Showcard

number = raw_input("Pick a card (1-52):")

filename = "BMP"+number+".gif"
Showcard.display_file(filename)

    
