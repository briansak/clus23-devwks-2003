import meraki

API_KEY = 'API_KEY'
dashboard = meraki.DashboardAPI(API_KEY, suppress_logging=True)

network_id = 'NETWORK_ID'
group_policy_id = 'GROUP_POLICY_ID'

response = dashboard.networks.updateNetworkGroupPolicy(
    network_id, group_policy_id, 
    scheduling={'enabled': True, 'monday': {'active': True, 'from': '17:00', 'to': '24:00'}, 'tuesday': {'active': True, 'from': '17:00', 'to': '24:00'}, 'wednesday': {'active': True, 'from': '17:00', 'to': '24:00'}, 'thursday': {'active': True, 'from': '17:00', 'to': '24:00'}, 'friday': {'active': True, 'from': '17:00', 'to': '24:00'}, 'saturday': {'active': True, 'from': '0:00', 'to': '24:00'}, 'sunday': {'active': True, 'from': '0:00', 'to': '24:00'}}, 
    bandwidth={'settings': 'custom', 'bandwidthLimits': {'limitUp': 500, 'limitDown': 500}}, 
    firewallAndTrafficShaping={'settings': 'custom', 'trafficShapingRules': [{'definitions': [{'type': 'host', 'value': 'hbomax.com'}, {'type': 'host', 'value': 'apple.com'}], 'perClientBandwidthLimits': {'settings': 'custom', 'bandwidthLimits': {'limitUp': 1000000, 'limitDown': 1000000}}, 'dscpTagValue': 32, 'pcpTagValue': 0}], 'l3FirewallRules': [{'comment': 'Allow TCP traffic to subnet with HTTP servers.', 'policy': 'allow', 'protocol': 'tcp', 'destPort': '443', 'destCidr': '192.168.1.0/24'}], 'l7FirewallRules': [{'policy': 'deny', 'type': 'host', 'value': 'corporate.com'}, {'policy': 'deny', 'type': 'host', 'value': 'work.com'}, {'policy': 'deny', 'type': 'ipRange', 'value': '10.11.11.00/24'}, {'policy': 'deny', 'type': 'ipRange', 'value': '10.11.12.00/24:5555'}]}
    )

print("Your Group Policy has been updated successfully.")
