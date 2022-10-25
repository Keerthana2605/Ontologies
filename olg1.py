from tokenize import String
from turtle import update
from owlready2 import *
onto = get_ontology("http://test.org/onto.owl#")

with onto:
 class Outlook(Thing): pass
 class Lockout(Thing): pass
 class Update(Thing): pass

#set_log_level(9)
'''with onto:
    class TestClass(Thing):pass'''


with onto:
    class ADID(Outlook): pass
    class Gmail(Outlook):pass
    class ZScalarEnabled(Update): pass

Outlook.iri

with onto:
    class has_locout(ObjectProperty, FunctionalProperty):
        domain = [Outlook]
        range = [Lockout]

with onto:
    class has_update(Outlook >> Update, FunctionalProperty): pass

    '''class ADID(Outlook >> int, FunctionalProperty): pass  - should ADID and gmail be inherited objects like lines 16,17 or properties?
    class Gmail(Outlook >> String, FunctionalProperty): pass'''

#onto.save('a.owl', format = "ntriples")
#onto.save()

'''print(list(onto.classes()))
print(list(onto.properties()))
print(list(onto.object_properties()))
print(list(onto.data_properties()))
print(list(onto.annotation_properties()))'''

'''print(onto.search(subclass_of=[onto.Outlook]))
print(onto.search(subclass_of=[onto.Lockout]))
print(onto.search(subclass_of=[onto.Update]))
print(onto.search(subclass_of=[onto.Outlook or onto.Lockout]))
print(onto.search(subclass_of=[onto.Outlook]) and onto.search(subclass_of=[onto.Update]))
print(onto.search(subclass_of=[onto.Outlook]) or onto.search(subclass_of=[onto.Update]))'''

print(Outlook.subclasses())