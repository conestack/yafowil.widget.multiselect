from yafowil.base import ExtractionError
from yafowil.base import factory
from yafowil.compat import IS_PY2
from yafowil.tests import YafowilTestCase
import os
import unittest


if not IS_PY2:
    from importlib import reload


def np(path):
    return path.replace('/', os.path.sep)


class TestMultiselectWidget(YafowilTestCase):

    def setUp(self):
        super(TestMultiselectWidget, self).setUp()
        from yafowil.widget import multiselect
        reload(multiselect.widget)
        multiselect.register()

    def test_edit_renderer(self):
        # Render widget
        widget = factory(
            'multiselect',
            name='multi',
            props={
                'required': True
            })
        self.assertEqual(widget(), (
            '<input id="exists-multi" name="multi-exists" type="hidden" '
            'value="exists" /><select class="multiselect" id="input-multi" '
            'multiple="multiple" name="multi" required="required"> </select>'
        ))

    def test_display_renderer(self):
        # Display renderer
        widget = factory(
            'multiselect',
            name='multi',
            value=['foo', 'bar'],
            props={
                'vocabulary': [('foo', 'Foo'), ('bar', 'Bar')]
            },
            mode='display')
        self.assertEqual(widget(), (
            '<ul class="display-multiselect" '
            'id="display-multi"><li>Foo</li><li>Bar</li></ul>'
        ))
        widget = factory('multiselect', 'multi', mode='display')
        self.assertEqual(
            widget(),
            '<div class="display-multiselect" id="display-multi"></div>'
        )

    def test_extraction(self):
        # Widget extraction
        widget = factory(
            'multiselect',
            name='multi',
            props={
                'required': True
            })

        request = {'multi': []}
        data = widget.extract(request)
        self.assertEqual(
            data.errors,
            [ExtractionError('Mandatory field was empty')]
        )
        self.assertEqual(data.extracted, [])

        request = {'multi': ['1']}
        data = widget.extract(request)
        self.assertEqual(data.errors, [])
        self.assertEqual(data.extracted, ['1'])

    def test_resources(self):
        factory.theme = 'default'
        resources = factory.get_resources('yafowil.widget.multiselect')
        self.assertTrue(
            resources.directory.endswith(np('/multiselect/resources'))
        )
        self.assertEqual(resources.path, 'yafowil-multiselect')

        scripts = resources.scripts
        self.assertEqual(len(scripts), 2)

        self.assertTrue(scripts[0].directory.endswith(
            np('/multiselect/resources/multi-select/js')
        ))
        self.assertEqual(scripts[0].path, 'yafowil-multiselect/multi-select/js')
        self.assertEqual(scripts[0].file_name, 'jquery.multi-select.js')
        self.assertTrue(os.path.exists(scripts[0].file_path))

        self.assertTrue(
            scripts[1].directory.endswith(np('/multiselect/resources'))
        )
        self.assertEqual(scripts[1].path, 'yafowil-multiselect')
        self.assertEqual(scripts[1].file_name, 'widget.min.js')
        self.assertTrue(os.path.exists(scripts[1].file_path))

        styles = resources.styles
        self.assertEqual(len(styles), 2)

        self.assertTrue(styles[0].directory.endswith(
            np('/multiselect/resources/multi-select/css')
        ))
        self.assertEqual(styles[0].path, 'yafowil-multiselect/multi-select/css')
        self.assertEqual(styles[0].file_name, 'multi-select.css')
        self.assertTrue(os.path.exists(styles[0].file_path))

        self.assertTrue(
            styles[1].directory.endswith(np('/multiselect/resources'))
        )
        self.assertEqual(styles[1].path, 'yafowil-multiselect')
        self.assertEqual(styles[1].file_name, 'widget.css')
        self.assertTrue(os.path.exists(styles[1].file_path))


if __name__ == '__main__':
    unittest.main()
