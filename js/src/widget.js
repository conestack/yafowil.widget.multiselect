import $ from 'jquery';

export class MultiselectWidget {
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


//////////////////////////////////////////////////////////////////////////////
// yafowil.widget.array integration
//////////////////////////////////////////////////////////////////////////////

export function multiselect_on_array_add(inst, context) {
    MultiselectWidget.initialize(context);
}

export function register_array_subscribers() {
    if (window.yafowil_array === undefined) {
        return;
    }
    window.yafowil_array.on_array_event('on_add', multiselect_on_array_add);
}