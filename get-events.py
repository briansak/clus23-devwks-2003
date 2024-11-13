from dotenv import load_dotenv
load_dotenv()
import meraki
import os

API_KEY = os.environ.get("api_key")
dashboard = meraki.DashboardAPI(API_KEY, suppress_logging=True)

network_id = 'YOUR_NETWORK_ID'

net_events = dashboard.networks.getNetworkEvents(network_id, productType='appliance', includedEventTypes=[{'sf_binary_block','sf_url_block','cf_block','nbar_block'}])
sec_events = dashboard.appliance.getNetworkApplianceSecurityEvents(network_id)

for event in sec_events:
    print (f'{"Event Type": <20}', f'{"Source IP": <25}', f'{"Destination IP": <25}')
    print (f'{"----------": <20}', f'{"---------": <25}', f'{"--------------": <25}')
    print (f'{event["eventType"]: <20}', f'{event["srcIp"]: <25}', f'{event["destIp"]: <25}')
    print (f'\nAlert: {event["message"]}\n')import meraki
import json

API_KEY = 'YOUR_API_KEY'
dashboard = meraki.DashboardAPI(API_KEY, suppress_logging=True)

network_id = 'YOUR_NETWORK_ID'

net_events = dashboard.networks.getNetworkEvents(network_id, productType='appliance', includedEventTypes=[{'sf_binary_block','sf_url_block','cf_block','nbar_block'}])
sec_events = dashboard.appliance.getNetworkApplianceSecurityEvents(network_id)

for event in sec_events:
    print (f'{"Event Type": <20}', f'{"Source IP": <25}', f'{"Destination IP": <25}')
    print (f'{"----------": <20}', f'{"---------": <25}', f'{"--------------": <25}')
    print (f'{event["eventType"]: <20}', f'{event["srcIp"]: <25}', f'{event["destIp"]: <25}')
    print (event["message"] + "\n")
