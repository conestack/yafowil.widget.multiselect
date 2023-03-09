import $ from 'jquery';

import {MultiselectWidget} from './widget.js';
import {register_array_subscribers}  from './widget.js';

export * from './widget.js';

$(function() {
    if (window.ts !== undefined) {
        ts.ajax.register(MultiselectWidget.initialize, true);
    } else if (window.bdajax !== undefined) {
        bdajax.register(MultiselectWidget.initialize, true);
    } else {
        MultiselectWidget.initialize();
    }
    register_array_subscribers();
});
