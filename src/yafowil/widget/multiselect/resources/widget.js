var yafowil_multiselect = (function (exports, $) {
    'use strict';

    class MultiselectWidget {
        static initialize(context) {
            $('select.multiselect', context).each(function() {
                if ($(this).parents('.arraytemplate').length) {
                    return;
                }
                new MultiselectWidget($(this));
            });
        }
        constructor(elem) {
            elem.data('yafowil-multiselect', this);
            this.elem = elem;
            this.elem.multiSelect();
        }
    }
    function multiselect_on_array_add(inst, context) {
        MultiselectWidget.initialize(context);
    }
    function register_array_subscribers() {
        if (window.yafowil_array === undefined) {
            return;
        }
        window.yafowil_array.on_array_event('on_add', multiselect_on_array_add);
    }

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

    exports.MultiselectWidget = MultiselectWidget;
    exports.multiselect_on_array_add = multiselect_on_array_add;
    exports.register_array_subscribers = register_array_subscribers;

    Object.defineProperty(exports, '__esModule', { value: true });


    window.yafowil = window.yafowil || {};
    window.yafowil.multiselect = exports;


    return exports;

})({}, jQuery);
