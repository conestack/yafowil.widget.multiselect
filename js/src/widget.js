import $ from 'jquery';

export class MultiselectWidget {
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
