# -*- coding: utf-8 -*-
from yafowil.base import factory


DOC_MULTISELECT = """
Multiselect
-----------

Multiselect Widget using jQuery multiselect plugin.

.. code-block:: python

    vocab = (
        u'Weißburgunder',
        u'Welschriesling',
        u'Sauvingnon Blanc',
        u'Sämling',
        u'Scheurebe',
        u'Traminer',
        u'Morrilon',
        u'Muskateller',
    )
    multiselect = factory('#field:multiselect', props={
        'label': 'Select some items',
        'required': 'Selection is required',
        'vocabulary': vocab,
    })
"""

def multiselect():
    part = factory(u'fieldset', name='yafowilwidgetmultiselect')
    vocab = (
        u'Weißburgunder',
        u'Welschriesling',
        u'Sauvingnon Blanc',
        u'Sämling',
        u'Scheurebe',
        u'Traminer',
        u'Morrilon',
        u'Muskateller',
    )
    part['text'] = factory('#field:multiselect', props={
        'label': 'Select some items',
        'required': 'Selection is required',
        'vocabulary': vocab,
    })
    return {
        'widget': part,
        'doc': DOC_MULTISELECT,
        'title': 'Multiselect Widget',
    }


def get_example():
    return [
        multiselect()
    ]
