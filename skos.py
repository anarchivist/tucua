#!/usr/bin/env python

import json
import rdflib
import lxml.html
import urlparse

tucua_base = "http://www2.archivists.org/thesaurus"
tucua = rdflib.Namespace(tucua_base)
tucua_url = rdflib.URIRef(tucua_base)

skos = rdflib.Namespace("http://www.w3.org/2004/02/skos/core#")
mads = rdflib.Namespace("http://www.loc.gov/mads/rdf/v1#")
dcterms = rdflib.Namespace("http://purl.org/dc/terms/")

graph = rdflib.Graph()
thesaurus = json.loads(open("tucua.json").read())

# Concept scheme 

graph.add((tucua_url, rdflib.RDF.type, skos.ConceptScheme))
graph.add((tucua_url, dcterms.title, rdflib.Literal("Thesaurus for Use in College and University Archives")))
graph.add((tucua_url, dcterms.publisher, rdflib.Literal("Society of American Archivists")))

# Add top concepts

doc = lxml.html.parse(tucua_base)
topconcepts = doc.findall('.//div[@id="main"]//div[@class="content"]/ul/li/a')

for t in topconcepts:
    concept_url = rdflib.URIRef(urlparse.urljoin('http://www2.archivists.org', t.attrib['href']))
    graph.add((concept_url, skos.topConceptOf, tucua_url))
    graph.add((tucua_url, skos.hasTopConcept, concept_url))

# Terms

for pref_label in thesaurus.keys():
    term = thesaurus[pref_label]
    uri = rdflib.URIRef(term["url"])
    graph.add((uri, rdflib.RDF.type, skos.Concept))
    graph.add((uri, skos.inScheme, tucua_url))
    graph.add((uri, skos.prefLabel, rdflib.Literal(pref_label)))
    
    if term["definition"] is not None:
        graph.add((uri, skos.definition, rdflib.Literal(term["definition"])))
    
    for alt_label in term["alt_label"]:
        graph.add((uri, skos.altLabel, rdflib.Literal(alt_label)))

    for b in term["broader"]:
        graph.add((uri, skos.broader, rdflib.URIRef(b["url"])))
    for n in term["narrower"]:
        graph.add((uri, skos.narrower, rdflib.URIRef(n["url"])))
    for r in term["related"]:
        graph.add((uri, skos.related, rdflib.URIRef(r["url"])))

    for n in term["scope_notes"]:
        graph.add((uri, skos.scopeNote, rdflib.Literal(n)))

    for n in term["notes"]:
        graph.add((uri, skos.note, rdflib.Literal(n)))

    for n in term["source_terms"]:
        bnode = rdflib.BNode()
        graph.add((uri, mads.Source, bnode))
        if n['source'] is not None:
            graph.add((bnode, mads.citationSource, rdflib.Literal(n['source'])))
        graph.add((bnode, mads.citationNote, rdflib.Literal(n['term'])))
        graph.add((bnode, mads.citationStatus, rdflib.Literal('found')))

graph.bind("skos", skos)
graph.bind('mads', mads)
graph.bind('dct', dcterms)
graph.serialize(open("tucua.rdf", "w"))
graph.serialize(open("tucua.ttl", "w"), format="turtle")
