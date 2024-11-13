from dotenv import load_dotenv
load_dotenv()
import meraki
import os

API_KEY = os.environ.get("api_key")
dashboard = meraki.DashboardAPI(API_KEY, suppress_logging=True)

network_id = 'YOUR_NETWORK_ID'  #CHANGE ME!
name = 'Restrictive Policy'

try: 
    response = dashboard.networks.createNetworkGroupPolicy(
    network_id, name, 
    scheduling={'enabled': True, 'monday': {'active': True, 'from': '9:00', 'to': '17:00'}, 'tuesday': {'active': True, 'from': '9:00', 'to': '17:00'}, 'wednesday': {'active': True, 'from': '9:00', 'to': '17:00'}, 'thursday': {'active': True, 'from': '9:00', 'to': '17:00'}, 'friday': {'active': True, 'from': '9:00', 'to': '17:00'}, 'saturday': {'active': False, 'from': '0:00', 'to': '24:00'}, 'sunday': {'active': False, 'from': '0:00', 'to': '24:00'}}, 
    bandwidth={'settings': 'custom', 'bandwidthLimits': {'limitUp': 1000000, 'limitDown': 1000000}}, 
    firewallAndTrafficShaping={'settings': 'custom', 'trafficShapingRules': [{'definitions': [{'type': 'host', 'value': 'sportsball.com'}, {'type': 'port', 'value': '9090'}, {'type': 'ipRange', 'value': '192.1.0.0'}, {'type': 'ipRange', 'value': '192.1.0.0/16'}, {'type': 'ipRange', 'value': '10.1.0.0/16:80'}, {'type': 'localNet', 'value': '192.168.0.0/16'}], 'perClientBandwidthLimits': {'settings': 'custom', 'bandwidthLimits': {'limitUp': 1000000, 'limitDown': 1000000}}, 'dscpTagValue': 0, 'pcpTagValue': 0}], 'l3FirewallRules': [{'comment': 'Allow TCP traffic to subnet with HTTP servers.', 'policy': 'allow', 'protocol': 'tcp', 'destPort': '443', 'destCidr': '192.168.1.0/24'}], 'l7FirewallRules': [{'policy': 'deny', 'type': 'host', 'value': 'gambling.com'}, {'policy': 'deny', 'type': 'port', 'value': '23'}, {'policy': 'deny', 'type': 'ipRange', 'value': '10.11.11.00/24'}, {'policy': 'deny', 'type': 'ipRange', 'value': '10.11.12.00/24:5555'}]}
    ) 
    print("Your Group Policy has been created successfully.")
    print(f"Your Group Policy ID is named: {response['name']}")
    print(f"Your Group Policy ID is: {response['groupPolicyId']}") 
except meraki.exceptions.APIError as e:
  print(e.message)
