from owlready2 import *
import csv, types
onto = get_ontology("http://test.org/onto.owl")
#onto = Ontology("http://test.org/onto.owl")
#onto_classes = get_ontology("http://lesfleursdunormal.fr/static/_downloads/bacteria_classes.owl")
#onto_classes.imported_ontologies.append(onto)
f = open("test.csv")
reader = csv.reader(f)
print(reader)
next(reader)
with onto:
 for row in reader:
     id, parent, gram_positive, shape, grouping = row
     print(row)
     print(parent)
     if parent: parent = onto[parent]
     else: parent = Thing
     Class = types.new_class(id, (parent,))

'''if gram_positive:
     if gram_positive == "True": gram_positive = True
     else:
          gram_positive = False
     Class.gram_positive = gram_positive
if shape:
     shape_class = onto[shape]
     Class.has_shape = shape_class

if grouping:
     grouping_class = onto[grouping]
     Class.has_grouping.append(grouping_class)
onto.save("bacteria_classes.owl")'''
