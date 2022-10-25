from owlready2 import*

onto = get_ontology("http://test.org/onto.owl#")

with onto:
    class Outlook(Thing) : pass

    class has_for_adid(DataProperty): #data property adid
        range=[int]

    class has_for_gmail(DataProperty): #data property gmail
        range=[str]

    #considering lockout as subclass of outlook and using super() to inherit from outlook
    class Lockout(Outlook):
        def __init__(self):
            super(Lockout,self).__init__()

    #lockout_issue1 is the subclass of Lockout
    class Lockout_issue1(Lockout):
        def __init__(self):
            super(Lockout_issue1,self).__init__()

    #Update is subclass of Outlook
    class Update(Outlook):
        def __init__(self):
            super(Update,self).__init__()

    class has_for_zse(DataProperty): #data property ZScalarEnable
        range=[bool]

onto.save("try2.owl",format="rdfxml")