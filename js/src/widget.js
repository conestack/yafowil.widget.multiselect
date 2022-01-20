import $ from 'jquery';

export class MultiselectWidget {
    static initialize(context) {
        $('select.multiselect', context).each(function() {
            new MultiselectWidget($(this));
        });
    }

    constructor(elem) {
        this.elem = elem;
        this.elem.multiSelect();
    }
}
