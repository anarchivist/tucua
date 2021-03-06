#!/usr/bin/env python

import re
import json
import rdflib
import networkx
import urlparse
import lxml.html

SOURCES = {
    'Chapman': 'Chapman University vocabulary (unpublished)',
    'UIll': 'University of Illinois vocabulary (unpublished)',
    'LCSH': 'Library of Congress Subject Headings',
    'Harvard': 'Harvard University vocabulary (unpublished)',
    'CWR TUT': 'Thesaurus of university terms developed at Case Western Reserve University Archives (Chicago, IL : Society of American Archivists, 1986)',
    'MHC': 'Mount Holyoke College vocabulary (unpublished)',
    'UMich': 'University of Michigan vocabulary (unpublished)',
    'TUCUA': 'Thesaurus for Use in College and University Archives (Chicago, IL : Society of American Archivists, 2009)',
    'ERIC': 'Thesaurus of ERIC Descriptors'
}

def main():
    saa = {}
    for t in terms():
        print t['pref_label']
        saa[t['pref_label']] = t
    compute_centrality(saa)
    open("tucua.json", "w").write(json.dumps(saa, indent=2))

def terms():
    for url in term_urls():
        t = term(url)
        if t:
            yield t

def term_urls():
    for letter in [chr(i) for i in  range(97, 123)]:
        url = 'http://www2.archivists.org/thesaurus/terms/' + letter
        while True:
            doc = lxml.html.parse(url)
            for a in doc.xpath('.//a'):
                href = a.attrib['href']
                if re.match(r'^/thesaurus/terms/./.+$', href):
                    yield urlparse.urljoin("http://www2.archivists.org", href)
            next_page = doc.xpath('string(.//li[@class="pager-next"]/a/@href)')
            if next_page:
                url = urlparse.urljoin("http://www2.archivists.org/", next_page)
            else:
                break

def term(url):
    term = {
        'url': url, 
        'pref_label': None, 
        'definition': None,
        'alt_label': [], 
        'broader': [],
        'narrower': [],
        'related': [],
        #'distinguish_from': [],
        #'notes': [],
        'scope_notes': [],
        'source_terms': [],
        #'citations': []
        }
    doc = lxml.html.parse(url)
    main = doc.find('.//div/[@id="main"]')

    term['pref_label'] = main.find('.//h1[@class="title"]').text

    # The thesaurus doesn't have definitions AFAIK
    #
    # term['definition'] = main.find('.//div[@class="content"]/p')
    #
    # if term['definition'] != None:
    #     term['definition'] = term['definition'].text_content()
    #     term['definition'] = re.sub('^\(also.+?\), ', '', term['definition'])

    for e in main.xpath('.//div[@class="field field-type-text field-field-thesaurus-use-for"]/div[@class="field-items"]/div'):
        term['alt_label'].append(e.text.strip())

    for e in main.xpath(".//div[@class='field-items']//p"):
        term['notes'].append(e.text_content())
    
    for e in main.xpath('.//div[@class="field field-type-text field-field-thesaurus-source-term"]/div[@class="field-items"]/div'):
        st = {}
        text = e.text_content().strip()
        if text.count('(') == 0:
            st['term'] = text
            st['source'] = None
        else:
            st['term'], st['source'] =  text.rsplit('(', 1)
            st['term'] = st['term'].strip()
            if '(' in st['term'] and ')' not in st['term']:
                st['term'] += ')' 
            st['source'] = SOURCES[st['source'].strip(')')]
        term['source_terms'].append(st)

    for e in main.xpath('.//div[@class="field field-type-text field-field-thesaurus-scope-note"]/div[@class="field-items"]/div'):
        term['scope_notes'].append(e.text_content().strip())

    for e in main.xpath('.//div[@class="field field-type-text field-field-thesaurus-use-note"]/div[@class="field-items"]/div'):
        term['scope_notes'].append(e.text_content().strip())

    # for e in main.xpath('.//div[@class="citation"]'):
    #     c = citation(e)
    #     if c: term['citations'].append(c)

    term['broader'] = syndetic_links(doc, "broader", url)
    term['related'] = syndetic_links(doc, "related", url)
    term['distinguish_from'] = syndetic_links(doc, "distinguish", url)
    term['narrower'] = syndetic_links(doc, "narrower", url)

    return term

def syndetic_links(doc, label, url):
    links = []
    xpath = ".//div[@class='field field-type-nodereference field-field-thesaurus-" + label + "-term']//a"
    for a in doc.findall(xpath):
        links.append({
            'pref_label': a.text, 
            'url': urlparse.urljoin(url, a.attrib['href'])
            })
    return links 

def citation(cite):
    a = cite.find('a')
    url = urlparse.urljoin('http://www2.archivists.org/', a.attrib['href'])
    doc = lxml.html.parse(url)
    e = doc.find('.//div[@class="citation-source-node"]')
    if e == None: return
    source = e.find('.//p').text
    return {
      "quotation": cite.text_content().strip(),
      "source": source,
      "url": url
      }

def compute_centrality(saa):
    """adds eigenvector centrality measure to the thesaurus that is passed in
    """
    # build a networkx graph of the thesaurus
    g = networkx.Graph()
    for term in saa.values():
        for broader in term['broader']:
            g.add_edge(term['pref_label'], broader['pref_label'], type='broader')
        for narrower in term['narrower']:
            g.add_edge(term['pref_label'], narrower['pref_label'], type='narrower')
        for related in term['related']:
            g.add_edge(term['pref_label'], related['pref_label'], type='related')
    # calculate centrality
    centrality = networkx.eigenvector_centrality(g, max_iter=1000)

    # add centrality values to the thesaurus data structure
    # not all terms will have a centrality value if they are not connected
    for term in saa.values():
        term['eigenvector_centrality'] = centrality.get(term['pref_label'], None)

    return saa 

if __name__ == "__main__":
    main()
