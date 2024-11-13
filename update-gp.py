from dotenv import load_dotenv
load_dotenv()
import meraki
import os

API_KEY = os.environ.get("api_key")
dashboard = meraki.DashboardAPI(API_KEY, suppress_logging=True)

network_id = 'YOUR_NETWORK_ID'  #CHANGE ME!
group_policy_id = 'YOUR_GP_ID'  #CHANGE ME! (Default 100)

try: 
    response = dashboard.networks.updateNetworkGroupPolicy(
    network_id, group_policy_id, 
    scheduling={'enabled': True, 'monday': {'active': True, 'from': '17:00', 'to': '24:00'}, 'tuesday': {'active': True, 'from': '17:00', 'to': '24:00'}, 'wednesday': {'active': True, 'from': '17:00', 'to': '24:00'}, 'thursday': {'active': True, 'from': '17:00', 'to': '24:00'}, 'friday': {'active': True, 'from': '17:00', 'to': '24:00'}, 'saturday': {'active': True, 'from': '0:00', 'to': '24:00'}, 'sunday': {'active': True, 'from': '0:00', 'to': '24:00'}}, 
    bandwidth={'settings': 'custom', 'bandwidthLimits': {'limitUp': 500, 'limitDown': 500}}, 
    firewallAndTrafficShaping={'settings': 'custom', 'trafficShapingRules': [{'definitions': [{'type': 'host', 'value': 'peacock.com'}, {'type': 'host', 'value': 'tv.apple.com'}], 'perClientBandwidthLimits': {'settings': 'custom', 'bandwidthLimits': {'limitUp': 1000000, 'limitDown': 1000000}}, 'dscpTagValue': 32, 'pcpTagValue': 0}], 'l3FirewallRules': [{'comment': 'Allow TCP traffic to subnet with HTTP servers.', 'policy': 'allow', 'protocol': 'tcp', 'destPort': '443', 'destCidr': '192.168.1.0/24'}], 'l7FirewallRules': [{'policy': 'deny', 'type': 'host', 'value': 'corporate.com'}, {'policy': 'deny', 'type': 'host', 'value': 'work.com'}, {'policy': 'deny', 'type': 'ipRange', 'value': '10.11.11.00/24'}, {'policy': 'deny', 'type': 'ipRange', 'value': '10.11.12.00/24:5555'}]})
    print(f"Your policy named {response['name']} has been updated.")
except meraki.exceptions.APIError as e:
    print(e.message)
