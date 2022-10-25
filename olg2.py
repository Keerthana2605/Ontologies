from owlready2 import *

onto = get_ontology("http://test.org/onto.owl#")

with onto:
    class Outlook(Thing): pass

#print(Outlook.iri)

with onto:
    class  Lockout(Outlook): pass
    class Update(Outlook): pass
#print(Lockout.is_a)
#print(Update.is_a)

with onto:
    class adid(DataProperty):
        domain = [Outlook]
        range=[int]
    class gmail(DataProperty):
        domain = [Outlook]
        range=[str]
    class ZScalarEnable(DataProperty):
        domain = [Update]
        range = [bool]
    '''class adid(ObjectProperty, FunctionalProperty):
        domain = [Outlook]
        range=[Lockout,Update]
    class gmail(ObjectProperty, FunctionalProperty):
        domain = [Outlook]
        range=[Lockout,Update]
    class ZScalarEnable(ObjectProperty, FunctionalProperty):
        domain = [Update]
        range = [Outlook]'''
    class has_lockout(ObjectProperty, FunctionalProperty):
        domain = [Outlook]
        range = [Lockout]
    class has_update(ObjectProperty, FunctionalProperty):
        domain = [Outlook]
        range = [Update]

#onto.save('olg2.owl', format = "ntriples")

'''print(list(onto.classes()))
print(list(onto.properties()))
print(list(onto.object_properties()))
print(list(onto.data_properties()))
print(list(onto.annotation_properties()))

print(onto.search(subclass_of=[onto.Outlook]))
print(onto.search(subclass_of=[onto.Lockout]))
print(onto.search(subclass_of=[onto.Update]))
print(list(onto.search(object_properties=[onto.Outlook or onto.Lockout])))
print(list(onto.search(object_properties=[onto.Outlook]) and onto.search(object_properties=[onto.Update])))
print(list(onto.search(object_properties=[onto.Outlook]) or onto.search(object_properties=[onto.Update])))'''

#print(list(onto.object_properties()))
'''print(onto.search(data_property_of=[onto.Outlook]))
print(onto.search(property_of=[onto.Lockout]))
print(onto.search(subproperty_of=[onto.Update]))
'''

print(list(Outlook.subclasses()))
print(list(Outlook.descendants()))