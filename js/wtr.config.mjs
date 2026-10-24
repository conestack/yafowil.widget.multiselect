import {importMapsPlugin} from '@web/dev-server-import-maps';
import {playwrightLauncher} from '@web/test-runner-playwright';
const RESOURCE_DIR = './src/yafowil/widget/multiselect/resources';

export const importMap = {
    imports: {
        'jquery': './node_modules/jquery/dist-module/jquery.module.js',
        'multiselect': `${RESOURCE_DIR}/multi-select/js/jquery.multi-select.js`
    },
};

export default {
    nodeResolve: true,
    browsers: [
        playwrightLauncher({product: 'chromium'}),
    ],
    testFramework: {
        path: './node_modules/web-test-runner-qunit/dist/autorun.js',
        config: {
            noglobals: false
        }
    },
    files: [
        'js/tests/**/test_*.js'
    ],
    coverageConfig: {
        include: ['**/js/src/**/*.js'],
        exclude: ['**/node_modules/**', 'sources/**']
    },
    plugins: [
        importMapsPlugin({
            inject: {importMap},
        }),
    ],
}
