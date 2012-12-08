tucua
=====

[![Build Status](https://secure.travis-ci.org/anarchivist/tucua.png)](http://travis-ci.org/anarchivist/tucua)

This project provides a scraper that crawls the [SAA Thesaurus for Use in College and University Archives](http://www2.archivists.org/thesaurus) and makes the resulting thesaurus data available as JSON and SKOS RDF. It started as a fork of a [project by Ed Summers](https://github.com/edsu/saa-glossary) (@edsu) that scrapes the [SAA Glossary of Archival and Records Terminology](http://www2.archivists.org/glossary).

SKOS
----

Here's what the SKOS looks like for the concept *fields of study*:

```
<http://www2.archivists.org/thesaurus/terms/f/fields-of-study> a skos:Concept;
    mads:Source [ mads:citationNote "Academics";
            mads:citationSource "Thesaurus of university terms developed at Case Western Reserve University Archives (Chicago, IL : Society of American Archivists, 1986)";
            mads:citationStatus "found" ];
    skos:altLabel "Academics";
    skos:inScheme <http://www2.archivists.org/thesaurus>;
    skos:narrower <http://www2.archivists.org/thesaurus/terms/a/agriculture>,
        <http://www2.archivists.org/thesaurus/terms/a/archaeology>,
        <http://www2.archivists.org/thesaurus/terms/a/architecture-field-of-study>,
        <http://www2.archivists.org/thesaurus/terms/b/business-administration-field-of-study>,
        <http://www2.archivists.org/thesaurus/terms/e/economics>,
        <http://www2.archivists.org/thesaurus/terms/e/education-field-of-study>,
        <http://www2.archivists.org/thesaurus/terms/e/engineering>,
        <http://www2.archivists.org/thesaurus/terms/g/government-field-of-study>,
        <http://www2.archivists.org/thesaurus/terms/h/health-sciences>,
        <http://www2.archivists.org/thesaurus/terms/h/humanities>,
        <http://www2.archivists.org/thesaurus/terms/i/interdisciplinary-studies>,
        <http://www2.archivists.org/thesaurus/terms/l/law>,
        <http://www2.archivists.org/thesaurus/terms/m/mathematics>,
        <http://www2.archivists.org/thesaurus/terms/m/military-science>,
        <http://www2.archivists.org/thesaurus/terms/s/science>,
        <http://www2.archivists.org/thesaurus/terms/s/sex-education>,
        <http://www2.archivists.org/thesaurus/terms/s/social-sciences>,
        <http://www2.archivists.org/thesaurus/terms/s/statistics-field-of-study>,
        <http://www2.archivists.org/thesaurus/terms/t/technology-field-of-study>;
    skos:prefLabel "fields of study";
    skos:related <http://www2.archivists.org/thesaurus/terms/a/academic-departments>,
        <http://www2.archivists.org/thesaurus/terms/c/courses>,
        <http://www2.archivists.org/thesaurus/terms/c/curricula>;
    skos:topConceptOf <http://www2.archivists.org/thesaurus> .
```

JSON
----

The resulting JSON is a big dictionary where each glossary term is a key. Here
is what the term *fields of study* looks like:

```javascript
{
  "fields of study": {
    "scope_notes": [], 
    "narrower": [
      {
        "url": "http://www2.archivists.org/thesaurus/terms/a/agriculture", 
        "pref_label": "agriculture"
      }, 
      {
        "url": "http://www2.archivists.org/thesaurus/terms/a/archaeology", 
        "pref_label": "archaeology"
      }, 
      {
        "url": "http://www2.archivists.org/thesaurus/terms/a/architecture-field-of-study", 
        "pref_label": "architecture (field of study)"
      }, 
      {
        "url": "http://www2.archivists.org/thesaurus/terms/b/business-administration-field-of-study", 
        "pref_label": "business administration (field of study)"
      }, 
      {
        "url": "http://www2.archivists.org/thesaurus/terms/e/economics", 
        "pref_label": "economics"
      }, 
      {
        "url": "http://www2.archivists.org/thesaurus/terms/e/education-field-of-study", 
        "pref_label": "education (field of study)"
      }, 
      {
        "url": "http://www2.archivists.org/thesaurus/terms/e/engineering", 
        "pref_label": "engineering"
      }, 
      {
        "url": "http://www2.archivists.org/thesaurus/terms/g/government-field-of-study", 
        "pref_label": "government (field of study)"
      }, 
      {
        "url": "http://www2.archivists.org/thesaurus/terms/h/health-sciences", 
        "pref_label": "health sciences"
      }, 
      {
        "url": "http://www2.archivists.org/thesaurus/terms/h/humanities", 
        "pref_label": "humanities"
      }, 
      {
        "url": "http://www2.archivists.org/thesaurus/terms/i/interdisciplinary-studies", 
        "pref_label": "interdisciplinary studies"
      }, 
      {
        "url": "http://www2.archivists.org/thesaurus/terms/l/law", 
        "pref_label": "law"
      }, 
      {
        "url": "http://www2.archivists.org/thesaurus/terms/m/mathematics", 
        "pref_label": "mathematics"
      }, 
      {
        "url": "http://www2.archivists.org/thesaurus/terms/m/military-science", 
        "pref_label": "military science"
      }, 
      {
        "url": "http://www2.archivists.org/thesaurus/terms/s/science", 
        "pref_label": "science"
      }, 
      {
        "url": "http://www2.archivists.org/thesaurus/terms/s/sex-education", 
        "pref_label": "sex education"
      }, 
      {
        "url": "http://www2.archivists.org/thesaurus/terms/s/social-sciences", 
        "pref_label": "social sciences"
      }, 
      {
        "url": "http://www2.archivists.org/thesaurus/terms/s/statistics-field-of-study", 
        "pref_label": "statistics (field of study)"
      }, 
      {
        "url": "http://www2.archivists.org/thesaurus/terms/t/technology-field-of-study", 
        "pref_label": "technology (field of study)"
      }
    ], 
    "related": [
      {
        "url": "http://www2.archivists.org/thesaurus/terms/a/academic-departments", 
        "pref_label": "academic departments"
      }, 
      {
        "url": "http://www2.archivists.org/thesaurus/terms/c/courses", 
        "pref_label": "courses"
      }, 
      {
        "url": "http://www2.archivists.org/thesaurus/terms/c/curricula", 
        "pref_label": "curricula"
      }
    ], 
    "broader": [], 
    "pref_label": "fields of study", 
    "definition": null, 
    "source_terms": [
      {
        "source": "Thesaurus of university terms developed at Case Western Reserve University Archives (Chicago, IL : Society of American Archivists, 1986)", 
        "term": "Academics"
      }
    ], 
    "alt_label": [
      "Academics"
    ], 
    "url": "http://www2.archivists.org/thesaurus/terms/f/fields-of-study", 
    "notes": [], 
    "eigenvector_centrality": 1.6789519048867294e-05, 
    "distinguish_from": [], 
    "citations": []
  }
}
```

INSTALL
-------

The idea is that you can use the data as is here in GitHub, and I will 
periodically re-run the crawler. If you want to update the data yourself
follow these steps:

1. sudo apt-get install pip
1. pip install -r requirements.txt
1. ./scrape.py
1. make some tea
1. cat tucua.json

And if you want to re-generate the SKOS RDF:

1. ./skos.py
1. cat tucua.rdf
1. cat tucua.ttl
