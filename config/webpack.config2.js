var path = require('path');

var ExtractTextPlugin = require('extract-text-webpack-plugin');
var ManifestRevisionPlugin = require('manifest-revision-webpack-plugin');

var rootAssetPath = './app/static';

module.exports = {
    entry: {
        app_js: [
            rootAssetPath + '/src/main.js'
        ],
        app_css: [
            rootAssetPath + '/styles/main.css'
        ],
        app_vue: [
            rootAssetPath + '/scripts/App.vue'
        ]
    },
    output: {
        path: './app/static/scripts/dist/',
        publicPath: 'static/scripts/dist/',
        filename: 'bundle.js'
    },
    resolve: {
        extensions: ['', '.js', '.css']
    },
    module: {
        loaders: [
            {
                test: /\.js$/i, loader: 'babel',
                exclude: /node_modules/
            },
            {
                test: /\.css$/i,
                loader: ExtractTextPlugin.extract('style-loader', 'css-loader')
            },
            // {
            //     test: /\.(jpe?g|png|gif|svg([\?]?.*))$/i,
            //     loaders: [
            //         // 'file?context=' + rootAssetPath + '&name=[path][name].[hash].[ext]',
            //         'image?bypassOnDebug&optimizationLevel=7&interlaced=false'
            //     ]
            // },
            { test: /\.json$/, loader: 'ignore-loader' },
            { test: /\.ico$/, loader: 'ignore-loader' },
            { test: /\.png$/, loader: 'ignore-loader' },
            { test: /\.jpg$/, loader: 'ignore-loader' },
            {
              test: /\.vue$/,
              loader: 'vue'
            }



        ]
    },
    plugins: [
        new ExtractTextPlugin('main.css'),
        new ManifestRevisionPlugin(path.join('build', 'manifest.json'), {
            rootAssetPath: rootAssetPath,
            ignorePaths: ['/styles', '/scripts']
        })
    ]
};
