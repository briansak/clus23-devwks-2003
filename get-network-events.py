import meraki
import json

API_KEY = 'API_KEY'
dashboard = meraki.DashboardAPI(API_KEY, suppress_logging=True)

network_id = 'NETWORK_ID'

response = dashboard.networks.getNetworkEvents(
    network_id, productType='appliance', includedEventTypes=[{'sf_binary_block','sf_url_block','cf_block','nbar_block'}])

print(json.dumps(response, indent=4))
