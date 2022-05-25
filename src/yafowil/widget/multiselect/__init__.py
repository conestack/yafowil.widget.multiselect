from yafowil.base import factory
from yafowil.utils import entry_point
import os
import webresource as wr


resources_dir = os.path.join(os.path.dirname(__file__), 'resources')


##############################################################################
# Default
##############################################################################

# webresource ################################################################

scripts = wr.ResourceGroup(
    name='yafowil-multiselect-scripts',
    path='yafowil.widget.multiselect'
)
scripts.add(wr.ScriptResource(
    name='multiselect-js',
    depends='jquery-js',
    directory=os.path.join(resources_dir, 'multi-select', 'js'),
    resource='jquery.multi-select.js'
))
scripts.add(wr.ScriptResource(
    name='yafowil-multiselect-js',
    depends='multiselect-js',
    directory=resources_dir,
    resource='widget.js',
    compressed='widget.min.js'
))

styles = wr.ResourceGroup(
    name='yafowil-multiselect-styles',
    path='yafowil.widget.multiselect'
)
styles.add(wr.StyleResource(
    name='multiselect-css',
    directory=os.path.join(resources_dir, 'multi-select', 'css'),
    resource='multi-select.css'
))
styles.add(wr.StyleResource(
    name='yafowil-multiselect-css',
    depends='multiselect-css',
    directory=resources_dir,
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

    # Default
    factory.register_theme(
        'default', 'yafowil.widget.multiselect', resources_dir,
        js=js, css=css
    )
    factory.register_scripts('default', 'yafowil.widget.multiselect', scripts)
    factory.register_styles('default', 'yafowil.widget.multiselect', styles)
