import {importMapsPlugin} from '@web/dev-server-import-maps';
const RESOURCE_DIR = './src/yafowil/widget/multiselect/resources';

export default {
    nodeResolve: true,
    testFramework: {
        path: './node_modules/web-test-runner-qunit/dist/autorun.js',
        config: {
            noglobals: false
        }
    },
    files: [
        'js/tests/**/test_*.js'
    ],
    plugins: [
        importMapsPlugin({
            inject: {
                importMap: {
                    imports: {
                        'jquery': './node_modules/jquery/dist-module/jquery.module.js',
                        'multiselect': `${RESOURCE_DIR}/multi-select/js/jquery.multi-select.js`
                    },
                },
            },
        }),
    ],
}
