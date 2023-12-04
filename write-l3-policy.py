import meraki
import json

API_KEY = 'API_KEY'
dashboard = meraki.DashboardAPI(API_KEY, suppress_logging=True)

pod_number = 'YOUR_POD_NUMBER'
network_id = 'YOUR_NETWORK_ID'
org_id = 'YOUR_ORG_ID'

new_acl = []
acl = dashboard.appliance.getNetworkApplianceFirewallInboundFirewallRules('network_id')
for rule in acl["rules"]:
  if rule["comment"] != "Default rule":
    new_acl.append(rule)

new_acl.append({'comment': f'Allow Pod {pod_number} Access to Servers', 'policy': 'allow', 'protocol': 'tcp', 'destPort': '443', 'destCidr': 'Any', 'srcPort': 'Any', 'srcCidr': f'2003:{pod_number}::/32', 'syslogEnabled': False})

networks = dashboard.organizations.getOrganizationNetworks(org_id, total_pages='all')
for network in networks:
  response = dashboard.appliance.updateNetworkApplianceFirewallInboundFirewallRules(network['id'], rules = new_acl)
  print(f'Wrote firewall ACE to {network["name"]}')

print('All Done!')
