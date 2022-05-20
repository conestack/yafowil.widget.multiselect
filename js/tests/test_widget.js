import {MultiselectWidget} from '../src/widget.js';

QUnit.test('initialize', assert => {
    let el = $('<select />').addClass('multiselect').appendTo('body');
    MultiselectWidget.initialize();
    let wid = el.data('multiselect');

    assert.ok(wid);
});