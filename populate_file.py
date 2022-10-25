from tkinter.messagebox import YES
from owlready2 import *
import csv,types

onto = get_ontology("olg5.owl").load()

f = open("populate_classes.csv")
reader = csv.reader(f)
next(reader)

with onto:
    for row in reader:
        id,ADID, Gmail, ZScalarEnable =row
        individual = onto.Outlook(id)

    if ADID:
        individual.ADID = int(ADID)

    if Gmail:
        individual.Gmail = str(Gmail)

    if ZScalarEnable:
        if ZScalarEnable == "True": ZScalarEnable = True

        else: ZScalarEnable = False
        individual.ZScalarEnable = ZScalarEnable
onto.save("populated.owl")