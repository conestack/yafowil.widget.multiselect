from yafowil.base import factory
from yafowil.utils import entry_point
import os
import webresource as wr


resources_dir = os.path.join(os.path.dirname(__file__), 'resources')


##############################################################################
# Default
##############################################################################

# webresource ################################################################

resources = wr.ResourceGroup(
    name='yafowil.widget.multiselect',
    directory=resources_dir,
    path='yafowil-multiselect'
)
resources.add(wr.ScriptResource(
    name='multiselect-js',
    depends='jquery-js',
    directory=os.path.join(resources_dir, 'multi-select', 'js'),
    path='yafowil-multiselect/multi-select/js',
    resource='jquery.multi-select.js'
))
resources.add(wr.ScriptResource(
    name='yafowil-multiselect-js',
    depends='multiselect-js',
    resource='widget.js',
    compressed='widget.min.js'
))
resources.add(wr.StyleResource(
    name='multiselect-css',
    directory=os.path.join(resources_dir, 'multi-select', 'css'),
    path='yafowil-multiselect/multi-select/css',
    resource='multi-select.css'
))
resources.add(wr.StyleResource(
    name='yafowil-multiselect-css',
    depends='multiselect-css',
    resource='widget.css'
))

# B/C resources ##############################################################

js = [{
    'group': 'yafowil.widget.multiselect.dependencies',
    'resource': 'multi-select/js/jquery.multi-select.js',
    'order': 20,
}, {
    'group': 'yafowil.widget.multiselect.common',
    'resource': 'widget.js',
    'order': 21,
}]
css = [{
    'group': 'yafowil.widget.multiselect.dependencies',
    'resource': 'multi-select/css/multi-select.css',
    'order': 20,
}, {
    'group': 'yafowil.widget.multiselect.common',
    'resource': 'widget.css',
    'order': 21,
}]


##############################################################################
# Registration
##############################################################################

@entry_point(order=10)
def register():
    from yafowil.widget.multiselect import widget  # noqa

    widget_name = 'yafowil.widget.multiselect'

    # Default
    factory.register_theme(
        'default',
        widget_name,
        resources_dir,
        js=js,
        css=css
    )
    factory.register_resources('default', widget_name, resources)
