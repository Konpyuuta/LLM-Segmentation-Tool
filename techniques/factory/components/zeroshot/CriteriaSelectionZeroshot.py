'''

@author Maurice Amon
'''
from techniques.factory.components.zeroshot.Zeroshot import Zeroshot


class CriteriaSelectionZeroshot(Zeroshot):

    _json_file = '''{
  "website": {
    "open-jobs": "For which technologies are employees required?",
    "company-type": "More external work (consulting) or more internal work?"
  },
  "social-media": {
    "linkedin": {
      "role-position": "role/job in the company",
      "company-type": "In which sector?",
      "company-size": "Size of the company?"
    },
    "facebook": {
      "criticism": "Criticism related to work or collegues, blackmailing etc."
    }
  },
  "data": {
    "type": "structured or unstructured? Documents? Relational or NoSQL-Databases?",
    "dataset-size": "What is the size of the dataset?"
  },
  "storage-medium": {
    "storage-location": "business computer, server or cloud?",
    "distribution": "Several storage mediums? RAID?"
  },
  "data-backup": {
    "target": "NAS, cloud or external harddrive?",
    "intervall": "How often should a backup be created?",
    "type": "Complete, incremental or differential?"
  },
  "operation-system": {
    "used-os": "Which operating systems (including version) does the company use?",
    "server-update": "If yes, which operation system is installed on the server?",
    "several-devices": "Are there several devices, which save critical data?"
  },
  "security": {
    "private-data": "Should the data be encrypted?",
    "data-protection-laws": "Are there data protection laws, relevant to the company?"
  },
  "data-recovery": {
    "speed": "How fast need the data to be recovered?",
  },
  "infrastructure": {
    "devices-in-network": "Are there several devices that are saving critical data?",
    "network-connection": "Are the computers connected to the network?"
  },
  "network-environment": {
    "central-administration": "Is Active Directory (AD) being used?",
    "automation": "Automating control of updates?"
  },
  "safety-regulations": {
    "scans": "Should reports be created frequently?"
  },
  "automation-installation": {
    "anti-virus": "Automated installation for how many devices?"
  },
  "internet-access": {
    "all-computers": "Do all computers have internet access?"
  },
  "existing-solutions": {
    "virus-protection": "Have been antivirus programs been installed previously?",
    "firewalls": "Are there already existing firewalls?"
  },
  "network-structure": {
    "router": "Which models?",
    "switches": "VLAN-support? Subnets?",
    "segmentation": "network segmentation required?",
    "locations": "Are several locations connected to each other?",
    "endpoint-devices": "How many endpoint devices are there?"
  },
  "usergroups-and-policies": {
    "amount-of-users": "How many users are there?",
    "access-rights": "Varying polices and user-groups?"
  },
  "functions": {
    "vpn-server": "Does the company use a VPN-server?",
    "intrusion-detection": "Intrusion Detection/Prevention?",
    "filtration": "Filtration of data traffic?"
  },
  "compliance-requirements": {
    "standards": "ISO 27001, DSGVO?",
    "log-saving": "Persistent saving of Logs?"
  },
  "Scalability": {
    "future": "Will the network grow in the future?"
  },
  "budget": {
    "firewall": "Financial conditions for firewall?",
    "costs-structure": "Longterm cheap or flexible?"
  },
  "update-strategies": {
    "date": "Updates at certain dates?",
    "restart": "Automated restart after updates?"
  },
  "cms": {
    "system": "Which CMS is being used?",
    "hosting": "Own server or Hosting-service?",
    "website-type": "Static oder dynamic?"
  },
  "hosting": {
    "server-type": "Physical, VPS or cloud?",
    "webserver": "Which Webserver?",
    "os": "Which operating system?",
    "dbms": "Which Database management system?"
  },
  "website-usage": {
    "importance": "Pure infoplattform or important services for clients?",
    "sensible-processes": "Client login, financial transactions?"
  },
  "system-architecture": {
    "type": "Webserver, application server, network devices?",
    "location": "Physical or cloud?"
  },
  "software-and-applications": {
    "installed-applications": "Which applications are installed?",
    "log-requirements": "Error logs, Access logs, Debug logs?"
  },
  "logging": {
    "type": "security logs, network logs?",
    "saving": "Where and how long should the logs be saved?",
    "automated-archiving": "Should the logs be persistently saved for a certain time?"
  },
  "logging-tools": {
    "central-tool": "ELK Stack, Graylog, Splunk, Fluentd?"
  },
  "network": {
    "data-transmission": "Are there systems that exchange data?",
    "firewall_vpn": "Are the firewalls of the VPN's influencing the logs?"
  },
  "email-infrastructure": {
    "provider": "Cloud-based or own mailserver?",
    "mailserver-technology": "Which Software?",
    "protocols": "SMTP, IMAP?"
  },
  "security-measures": {
    "endpoint-security": "Verification of mail attachments?",
    "whitelist-blacklist": "Are there Whitelists and Blacklists?"
  },
  "encryption": {
    "types": "Saved or transmitted data should be encrypted?",
    "key-management": "Centralized or Decentralized?",
    "technology": "Bitlocker etc.?"
  }
}
'''
    _prompt = '''Question: How do I install a firewall on the webserver of my company? 
                 Prompt: Which keys in the JSON-file above are of relevance for answering the Question?
                         Please answer with just a list of the keys. Avoid further explanations.'''

    def __init__(self):
        self.initialize()

    def initialize(self):
         self._instruction = f'''{self._json_file}\n\n{self._prompt}'''


    def get_prompt(self):
        return self._instruction