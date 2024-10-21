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


DOC_MULTISELECT_DEPRECATION = """
.. raw:: html

    <div class="alert alert-info">
        <i class="bi bi-info-circle-fill"></i>
        This widget has a newer version available:
        <a class="link-offset-3"
           href="../++widget++yafowil.widget.select2/index.html">
            yafowil.widget.select2
        </a>
    </div>
    <div class="alert alert-warning">
        <i class="bi bi-exclamation-triangle-fill"></i>
        <strong>Deprecation Notice:</strong>
        yafowil.widget.multiselect is 
        <strong>
            deprecated
        </strong>
        and will no longer receive support or further development.
    </div>
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
        'doc': DOC_MULTISELECT if factory.theme != 'bootstrap5'
               else DOC_MULTISELECT_DEPRECATION + DOC_MULTISELECT,
        'title': 'Multiselect Widget',
    }


def get_example():
    return [
        multiselect()
    ]
