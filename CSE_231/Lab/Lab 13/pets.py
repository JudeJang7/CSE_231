# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 10:43:29 2017

@author: xumatthe
"""


##
## Class PetError -- complete
##

class PetError( ValueError ):
    
    pass

##
## Class Pet -- not complete
##

class Pet( object ):
    
    def __init__( self, species=None, name="" ):
        
        species_list = ["dog", "cat", "horse", "gerbil", "hamster", "ferret"]
        
        if species.lower() in species_list:
            
            self.species_str = species.title()
            self.name_str = name.title()
            
        else:
            
            raise PetError()
            
    def __str__( self ):
        
        result_str = "species of {:s}".format(self.species_str)
        if self.name_str == "":
            result_str = "species of {:s}, {}".format(self.species_str, "unnamed")
        return result_str

##
## Class Dog -- not complete
##

class Dog( Pet ):
    def __init__(self, name = "", chases = "cats"):
        Pet.__init__(self, "dog", name)
        self.__chases = chases
        self.__name = name
    def __str__(self):
        return Pet.__str__(self) + ", named " + self.__name + ", chases " + self.__chases
    

##
## Class Cat -- not complete
##

class Cat( Pet ):
    def __init__(self, name = "", hates = "dogs"):
        Pet.__init__(self, "cat", name)
        self.__hates = hates
        self.__name = name
    def __str__(self):
        return Pet.__str__(self) + ", named " + self.__name + ", hates " + self.__hates
    
