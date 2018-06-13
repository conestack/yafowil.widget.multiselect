from node.utils import UNSET
from yafowil.base import ExtractionError
from yafowil.base import factory
from yafowil.compat import IS_PY2
from yafowil.tests import YafowilTestCase
from yafowil.tests import fxml
import yafowil.loader


if not IS_PY2:
    from importlib import reload


class TestMultiselectWidget(YafowilTestCase):

    def setUp(self):
        super(TestMultiselectWidget, self).setUp()
        from yafowil.widget.multiselect import widget
        reload(widget)

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
            'multiple="multiple" name="multi" required="required" />'
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
        self.assertEqual(widget(),
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


if __name__ == '__main__':
    unittest.main()                                          # pragma: no cover
