import meraki
import json

API_KEY = 'API_KEY'
dashboard = meraki.DashboardAPI(API_KEY, suppress_logging=True)

network_id = 'NETWORK_ID'
response = dashboard.appliance.getNetworkApplianceSecurityEvents(network_id)

print(json.dumps(response, indent=4))
