isa = { 
    "bird": "animal", 
    "dog": "animal", 
    "sparrow": "bird" 
} 
has_property = { 
    "animal": ["cells"] 
} 

can = { 
    "dog": ["bark"], 
    "bird": ["fly"] 
} 
def get_superclass(concept):    
     return isa.get(concept, None) 
def inherits_property(concept, property_name):     
    if concept in has_property and property_name in has_property[concept]: 
        return True     
    parent = get_superclass(concept)    
    if parent: 
        return inherits_property(parent, property_name)    
        return False 
    print("Does sparrow have cells?", inherits_property("sparrow", "cells"))
    print("Does dog have cells?", inherits_property("dog", "cells"))
    print("Can sparrow bark?", inherits_property("sparrow", "bark")) 
    print("Can dog fly?", inherits_property("dog", "fly")) 
