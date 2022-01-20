import $ from 'jquery';

import {MultiselectWidget} from './widget.js';

export * from './widget.js';

$(function() {
    if (window.ts !== undefined) {
        ts.ajax.register(MultiselectWidget.initialize, true);
    } else {
        MultiselectWidget.initialize();
    }
});
