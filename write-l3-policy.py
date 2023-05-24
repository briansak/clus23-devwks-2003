import meraki
import json

API_KEY = 'API_KEY'
dashboard = meraki.DashboardAPI(API_KEY, suppress_logging=True)

network_id = 'NETWORK_ID'

response = dashboard.appliance.updateNetworkApplianceFirewallInboundFirewallRules(
    network_id, 
    rules=[{'comment': 'Allow Cisco Access to Servers', 'policy': 'allow', 'protocol': 'tcp', 'destPort': '443', 'destCidr': 'Any', 'srcPort': 'Any', 'srcCidr': '2001:420::/32', 'syslogEnabled': False}]
)

print(json.dumps(response, indent=4))
