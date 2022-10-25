from git import Object
from owlready2 import*

onto = get_ontology("http://test.org/onto.owl#")

with onto:
    class Outlook(Thing) : pass
    class ADID(Thing): pass
    class Gmail(Thing): pass

    class has_for_adid(ObjectProperty):
        domain=[Outlook]
        range=[ADID]

    class is_property1_of(ObjectProperty):
        domain=[ADID]
        range=[Outlook]
        inverse_property=has_for_adid

    class has_for_gmail(ObjectProperty):
        domain=[Outlook]
        range=[Gmail]

    class is_property2_of(ObjectProperty):
        domain=[Gmail]
        range=[Outlook]
        inverse_property=has_for_gmail

    class Lockout(Outlook):
        def __init__(self):
            super(Lockout,self).__init__()

    class Lockout_issue1(Lockout):
        def __init__(self):
            super(Lockout_issue1,self).__init__()

    class Update(Outlook):
        def __init__(self):
            super(Update,self).__init__()

    class Zscalarenable(Update):pass

    class has_for_zse(Update>>Zscalarenable,ObjectProperty):
        pass

    class is_property3_of(Zscalarenable>>Update):
        inverse=has_for_zse

#onto.save("try1.owl",format="rdfxml")

'''print(list(Outlook.subclasses()))
print(list(Lockout.subclasses()))

print(list(Outlook.descendants()))
print(onto.search(subclass_of=[onto.Outlook,onto.Lockout]))
print(list(onto.object_properties()))'''
print(onto.search(object_properties=[onto.Outlook]))
