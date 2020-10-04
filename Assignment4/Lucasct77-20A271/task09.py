# -*- coding: utf-8 -*-
"""Task09.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eDDHOQPTQK6iVd-Uj_ht5jwMqcO0FCpa

**Task 09: Data linking**
"""
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2020-2021/master/Assignment4/"

from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import RDF, RDFS, OWL

g1 = Graph()
g2 = Graph()
g3 = Graph()
g1.parse(github_storage + "resources/data03.rdf", format="xml")
g2.parse(github_storage + "resources/data04.rdf", format="xml")

"""Search for individuals in the two graphs and link them using the OWL: sameAs property, insert these matches in g3.
We consider that two individuals are the same if they have the same nickname and family name. Keep in mind that the URIs
 do not have to be the same for the same individual in the two graphs."""

g1.namespace_manager.bind('ns', Namespace("http://data.three.org#"), override=False)
g2.namespace_manager.bind('ns2', Namespace("http://data.four.org#"), override=False)

ns = Namespace("http://data.three.org#")
ns2 = Namespace("http://data.four.org#")
vcard = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

print(g1.serialize(format="turtle").decode("UTF-8"))
print(g2.serialize(format="turtle").decode("UTF-8"))

# For each person in g1, g2 compare Family and Given
for p1, b, c in g1.triples((None, RDF.type, ns.Person)):
    for p2, b2, c2 in g2.triples((None, RDF.type, ns2.Person)):
        if g1.value(subject=p1, predicate=vcard.Family) == g2.value(subject=p2, predicate=vcard.Family) and \
                g1.value(subject=p1, predicate=vcard.Given) == g2.value(subject=p2, predicate=vcard.Given):
            g3.add((p1, OWL.sameAs, p2))

print(g3.serialize(format="turtle").decode("UTF-8"))
