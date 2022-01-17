# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.hitbtc import hitbtc


class fmfwio(hitbtc):

    def describe(self):
        return self.deep_extend(super(fmfwio, self).describe(), {
            'id': 'fmfwio',
            'name': 'FMFW.io',
            'countries': ['KN'],
            'urls': {
                'logo': 'https://user-images.githubusercontent.com/1294454/97296144-514fa300-1861-11eb-952b-3d55d492200b.jpg',
                'api': {
                    'public': 'https://api.fmfw.io',
                    'private': 'https://api.fmfw.io',
                },
                'www': 'https://fmfw.io',
                'doc': 'https://api.fmfw.io/api/2/explore/',
                'fees': 'https://fmfw.io/fees-and-limits',
                'referral': 'https://fmfw.io/referral/da948b21d6c92d69',
            },
            'fees': {
                'trading': {
                    'maker': self.parse_number('0.005'),
                    'taker': self.parse_number('0.005'),
                },
            },
        })