QUnit.module('Multiselect', hooks => {
    let MultiselectWidget, register_array_subscribers;

    hooks.before(async () => {
        // INFO: This setup is necessary as jquery.multiselect.js does not have
        // an ES module variation.
        const jQueryModule = await import('jquery');
        // assign to global scope
        window.$ = window.jQuery = jQueryModule.default || jQueryModule;
        // ensure jQuery is ready before importing multiselect
        await import('multiselect');

        const modules = await import('../src/widget.js');
        MultiselectWidget = modules.MultiselectWidget;
        register_array_subscribers = modules.register_array_subscribers;
    });

    QUnit.test('initialize', assert => {
        let el = $('<select />').addClass('multiselect').appendTo('body');
        MultiselectWidget.initialize();
        let wid = el.data('yafowil-multiselect');
        assert.ok(wid);
        el.remove();
    });

    QUnit.test('register_array_subscribers', assert => {
        let _array_subscribers = {
            on_add: []
        };

        // window.yafowil_array is undefined - return
        register_array_subscribers();
        assert.deepEqual(_array_subscribers['on_add'], []);

        // patch yafowil_array
        window.yafowil_array = {
            on_array_event: function(evt_name, evt_function) {
                _array_subscribers[evt_name] = evt_function;
            },
            inside_template(elem) {
                return elem.parents('.arraytemplate').length > 0;
            }
        };
        register_array_subscribers();

        // create table DOM
        let table = $('<table />')
            .append($('<tr />'))
            .append($('<td />'))
            .appendTo('body');

        let el = $(`<select />`).addClass('multiselect');
        $('td', table).addClass('arraytemplate');
        el.appendTo($('td', table));

        // invoke array on_add - returns
        _array_subscribers['on_add'].apply(null, $('tr', table));
        let widget = el.data('yafowil-multiselect');
        assert.notOk(widget);
        $('td', table).removeClass('arraytemplate');

        // invoke array on_add
        el.attr('id', '');
        _array_subscribers['on_add'].apply(null, $('tr', table));
        widget = el.data('yafowil-multiselect');
        assert.ok(widget);
        table.remove();
        window.yafowil_array = undefined;
        _array_subscribers = undefined;

        table.remove();
    });
});
