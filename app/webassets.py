from flask_assets import Environment, Bundle

webassets = Environment()

bundles = {
    'common_js': Bundle('js/common.js',output='bundle/common.js'),
    'hello_js': Bundle('js/hello.js', output='bundle/hello.js'),
}

webassets.register(bundles)
