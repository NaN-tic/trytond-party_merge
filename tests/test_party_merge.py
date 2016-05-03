# -*- coding: utf-8 -*-
"""
    tests/test_party.py

    :copyright: (C) 2014 by Openlabs Technologies & Consulting (P) Limited
    :copyright: (C) 2016 by NaN·tic Projectes de programari lliure
    :license: BSD, see LICENSE for more details.
"""
from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import POOL, DB_NAME, USER, CONTEXT
import trytond.tests.test_tryton
from trytond.transaction import Transaction
import unittest


class PartyMergeTestCase(ModuleTestCase):
    'Test Party'
    module = 'party_merge'

    def setUp(self):
        super(PartyMergeTestCase, self).setUp()
        self.Party = POOL.get('party.party')

    def test0005_merge_parties(self):
        'Test party merge function'
        with Transaction().start(DB_NAME, USER, context=CONTEXT):
            party1, party2, party3 = self.Party.create([{
                'name': 'Party 1',
                'addresses': [('create', [{
                    'name': 'party1',
                    'street': 'ST2',
                    'city': 'New Delhi',
                }])]
            }, {
                'name': 'Party 2',
                'addresses': [('create', [{
                    'name': 'party2',
                    'street': 'ST2',
                    'city': 'Mumbai',
                }])]
            }, {
                'name': 'Party 3',
                'addresses': [('create', [{
                    'name': 'party3',
                    'street': 'ST2',
                    'city': 'New Delhi',
                }])]
            }])

            # Merge party2, party3 to party1
            party2.merge_into(party1)
            party3.merge_into(party1)

            self.assertEqual(len(party1.addresses), 3)


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        PartyMergeTestCase))
    return suite
