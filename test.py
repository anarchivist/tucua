#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrape
import unittest

class SaaTests(unittest.TestCase):

    # def atest_term_urls(self):
    #     self.assertTrue(len(list(scrape.term_urls())) > 2000)

    def test_term(self):
        term = scrape.term("http://www2.archivists.org/thesaurus/terms/i/integration")
        self.assertEqual(term['pref_label'], 'integration')
        self.assertEqual(len(term['scope_notes']), 2)
        self.assertEqual(term['scope_notes'][1], 'Do not confuse with "mergers," which refers to the joining together of separate institutions.')

        self.assertEqual(len(term['broader']), 1)
        self.assertEqual(term['broader'][0]['pref_label'], 'corporate culture')
        self.assertEqual(term['broader'][0]['url'], 'http://www2.archivists.org/thesaurus/terms/c/corporate-culture')

        self.assertEqual(len(term['narrower']), 2)
        self.assertEqual(term['narrower'][0]['pref_label'], 'coeducation')
        self.assertEqual(term['narrower'][0]['url'], 'http://www2.archivists.org/thesaurus/terms/c/coeducation')

        self.assertEqual(len(term['related']), 2)
        self.assertEqual(term['related'][0]['pref_label'], 'equal opportunity')
        self.assertEqual(term['related'][0]['url'], 'http://www2.archivists.org/thesaurus/terms/e/equal-opportunity')
        self.assertEqual(term['related'][1]['pref_label'], 'discrimination')
        self.assertEqual(term['related'][1]['url'], 'http://www2.archivists.org/thesaurus/terms/d/discrimination')

    def test_alt_label(self):
        term = scrape.term("http://www2.archivists.org/thesaurus/terms/s/student-life")
        self.assertEqual(term['pref_label'], 'student life')
        self.assertEqual(len(term['alt_label']), 1)
        self.assertEqual(term['alt_label'][0], 'Students- Life')

    def test_source_terms(self):
        term = scrape.term("http://www2.archivists.org/thesaurus/terms/t/teaching")
        self.assertTrue(term)
        self.assertEqual(term['pref_label'], 'teaching')
        self.assertEqual(len(term['source_terms']), 2)
        self.assertEqual(term['source_terms'][0]['term'], 'Teaching')
        self.assertEqual(term['source_terms'][0]['source'], 'Thesaurus of university terms developed at Case Western Reserve University Archives (Chicago, IL : Society of American Archivists, 1986)')





if __name__ == "__main__":
    unittest.main()
