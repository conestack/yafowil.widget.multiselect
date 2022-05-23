var yafowil_multiselect = (function (exports, $) {
    'use strict';

    class MultiselectWidget {
        static initialize(context) {
            $('select.multiselect', context).each(function() {
                new MultiselectWidget($(this));
            });
        }
        constructor(elem) {
            elem.data('yafowil-multiselect', this);
            this.elem = elem;
            this.elem.multiSelect();
        }
    }

    $(function() {
        if (window.ts !== undefined) {
            ts.ajax.register(MultiselectWidget.initialize, true);
        } else if (window.bdajax !== undefined) {
            bdajax.register(MultiselectWidget.initialize, true);
        } else {
            MultiselectWidget.initialize();
        }
    });

    exports.MultiselectWidget = MultiselectWidget;

    Object.defineProperty(exports, '__esModule', { value: true });


    window.yafowil = window.yafowil || {};
    window.yafowil.multiselect = exports;


    return exports;

})({}, jQuery);
