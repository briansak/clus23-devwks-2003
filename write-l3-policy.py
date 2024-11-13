from dotenv import load_dotenv
load_dotenv()
import meraki
import os

API_KEY = os.environ.get("api_key")
dashboard = meraki.DashboardAPI(API_KEY, suppress_logging=True)

pod_number = 'YOUR_POD_NUMBER'

new_acl = []
acl = dashboard.appliance.getNetworkApplianceFirewallInboundFirewallRules('N_646829496481208272')
for rule in acl["rules"]:
  if rule["comment"] != "Default rule":
    new_acl.append(rule)

new_acl.append({'comment': f'Allow Pod {pod_number} Access to Servers', 'policy': 'allow', 'protocol': 'tcp', 'destPort': '443', 'destCidr': 'Any', 'srcPort': 'Any', 'srcCidr': f'2003:{pod_number}::/32', 'syslogEnabled': False})

networks = dashboard.organizations.getOrganizationNetworks(646829496481091240, total_pages='all')
for network in networks:
  try: 
      response = dashboard.appliance.updateNetworkApplianceFirewallInboundFirewallRules(network['id'], rules = new_acl)
      print(f'Wrote firewall ACE to {network["name"]}')
  except meraki.exceptions.APIError as e:
      print(e.message)
