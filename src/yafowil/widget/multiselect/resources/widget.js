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
    function multiselect_on_array_add(inst, context) {
        MultiselectWidget.initialize(context);
    }
    function multiselect_on_array_index(inst, row, index) {
        $('select.multiselect', row).each(function() {
            let trigger = $(this),
                ref_name = trigger.data('reference-name'),
                base_id = inst.base_id(row),
                base_name = base_id.replace(/\-/g, '.');
            trigger.data('reference-name', inst.set_value_index(
                ref_name,
                base_name,
                index,
                '.'
            ));
        });
    }
    $(function() {
        if (yafowil_array === undefined) {
            return;
        }
        yafowil_array.on_array_event('on_add', multiselect_on_array_add);
        yafowil_array.on_array_event('on_index', multiselect_on_array_index);
    });

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
