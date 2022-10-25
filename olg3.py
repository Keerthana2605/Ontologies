from owlready2 import *

onto = get_ontology("http://test.org/onto.owl#")

with onto:
    class Outlook(Thing): pass

    class ADID(Thing): pass

    class km1234(ADID): pass
    class nv2345(ADID): pass

    class has_adid(ObjectProperty,FunctionalProperty):
        domain = [Outlook]
        range = [ADID]


    class Gmail(Thing): pass

    '''class keerthana1234(Gmail): pass
    class naimavahab2345(Gmail): pass'''

    #class km1234gmail.com(Gmail)

    class People(Thing): pass
    class KeerthanaM(People) :pass
    class NaimaVahab(People): pass

    class ZScalarEnable(Thing): pass
    class yes(ZScalarEnable): pass
    class no(ZScalarEnable):pass

    class Lockout(Thing):pass
    class Update(Thing): pass


    class has_adid_gmail(ObjectProperty,FunctionalProperty):
        domain = [ADID and Gmail]
        range = [Lockout]

    class used_by (ObjectProperty, FunctionalProperty):
        domain = [People]
        range = [Lockout]
        inverse = has_adid_gmail

    class Update(Thing): pass

