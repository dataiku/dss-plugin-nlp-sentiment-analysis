PLUGIN_ID=sentiment-analysis
PLUGIN_VERSION=1.4.0

all:
	cat plugin.json|json_pp > /dev/null
	rm -rf dist
	mkdir dist
	zip -r dist/dss-plugin-${PLUGIN_ID}-${PLUGIN_VERSION}.zip code-env custom-recipes python-lib resource plugin.json
