import {MultiselectWidget} from '../src/widget.js';

window.yafowil_array = undefined;

QUnit.test('initialize', assert => {
    let el = $('<select />').addClass('multiselect').appendTo('body');
    MultiselectWidget.initialize();
    let wid = el.data('yafowil-multiselect');

    assert.ok(wid);
});
