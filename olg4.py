from re import S
from xml.etree.ElementInclude import include
from owlready2 import *
from pyrsistent import s
from regex import D

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

#onto.save('olg4.owl', format='rdfxml')

'''print(list(onto.classes()))

print(list(onto.object_properties()))
print(list(onto.data_properties()))'''

print(list(onto.properties(Outlook)))

def ancestors(Class, include_self = True, include_constructs = False):
    s = set()
    Class._fill_ancestors(s, include_self, include_constructs)
    return s

'''print(ancestors(Lockout))
print(ancestors(Update))'''
print(ancestors(Lockout and Outlook))
print(ancestors(Update and Outlook))

def descendants(Class, include_self = True, only_loaded = False, world = None):
    s = set()
    if Class.namespace.world is owl_world:
      if world is None:
        import owlready2
        world = owlready2.default_world
      Class._fill_descendants(s, include_self, only_loaded, world, None)
    else:
      Class._fill_descendants(s, include_self, only_loaded, Class.namespace.world, Class.namespace.ontology)

    return s

'''print(descendants(Outlook))
print(descendants(ADID))
print(descendants(Gmail))
print(descendants(ZScalarEnable))'''