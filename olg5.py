from owlready2 import *

onto = get_ontology("http://test.org/onto.owl#")

with onto:
    class Outlook(Thing): pass

    class ADID(Outlook): pass
    class Gmail(Outlook): pass
    class ZScalarEnable(Outlook): pass

    AllDisjoint([ADID,Gmail,ZScalarEnable])

    class has_adid(ADID>>int, FunctionalProperty):
        pass
    class has_gmail(Gmail>>str, FunctionalProperty):
        pass
    class has_zse(ZScalarEnable>>bool,FunctionalProperty):
        pass

    class Lockout(ADID,Gmail):
        def __init__(self):
            super(Lockout,self).__init__()

    class Update(ADID,Gmail,ZScalarEnable):
        def __init__(self):
            super(Update,self).__init


    class has_ag(ObjectProperty,FunctionalProperty):
        domain = [ADID and Gmail]
        range = [Lockout]

    class has_agz(ObjectProperty, FunctionalProperty):
        domain = [ADID and Gmail and ZScalarEnable]
        range = [Update]

onto.save('olg5.owl', format='rdfxml')