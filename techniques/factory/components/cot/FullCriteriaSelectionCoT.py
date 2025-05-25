'''

@author Maurice Amon
'''
from techniques.factory.components.cot.ChainOfThought import ChainOfThought


class FullCriteriaSelectionCoT(ChainOfThought):

    _cot_example = '''JSON:
{
    "company-information": {
        "name": "Name of the company",
        "business-type": "AG, GmbH etc.",
        "reg-number": "Registration number of the company.",

        "location": {
            "headquarter": "Location of the headquarter",
            "branch-1": "Location of branch 1",
            // ...
            "branch-n": "Location of branch n"
        },

        "contact-info": "contact information",

        "operational": {
            "suppliers": "List of the company's suppliers.",
            "clients": "List of the company's clients."
        },
        "sales-volume": "How much money?"
    }, 
    "organigramm": {

        "first-level": {
            "CEO": {

            }
        },
        "second-level": {
            "R&D": {

            },
            "Sales": {

            }
        }
    },    
    "CIA": {
        "confidentiality": {
            "data-protection-policies": "Are there data protection laws that are relevant?"
        },

        "integrity": {
            "encryption": "Encryption of the data?"
        },

        "avaiability": {
            "raid": "Does the company use RAID to ensure Avaiability? If yes, which type?",
            "duration": "How quickly should the data be recovered?"
        }
    },
    "data-properties": {
        "structure": "Structured or unstructured?",
        "type": {
            "files": "Documents, Images etc.",
            "databases": {
                "db-type": "Relational or NoSQL-Database?",
                "db-system":  "Postgres, Neo4J, etc. ?"
            }
        },
        "size": "How large is the size of the data?"
    },

    "backup-target" {
        "target": "NAS Cloud or external drive?",
        "intervall": "How often Backup should be created?",
        "distribution": "RAID techniques?",
        "type":  "Complete, incremental, differential?"
    },
    "endpoints": {
        "host_1": {
            "operating-system": {
                "name": "",
                "version": ""
            },
            "device-type": "",
            "firewall": {
                "name": "",
                "version": ""
            }
        },
        // ...
        "host_n": {
            "operating-system": {
                "name": "Android",
                "version": "14"
            },
            "device-type": "Smartphone",
            "firewall": {
                "name": "",
                "version": ""
            }
        }
    },
        "IT-Infrastructure": {

        "Network-structure": {
            "Segmentation": "Network segmentation?",
            "location": "Are several locations connected with each other?",
            "networks": {
                "LAN": "Does the company have a LAN?",
                "WAN": "Does the company have a WAN?",
                "VPN": "Does the company have a VPN?"
            } 
        },

        "hardware": {
            "Networking-devices": {
                "Routers": "Which models?",
                "Switches": "VLAN-Support? Subnets?"
            },
            "storages": {
                "NAS": "If avaiable, Which model?",
                "SAN": "Does the company have such a network?",
                "local-storages": "SSD's, HDD's?"
            },
            "terminals": {
                "amount": "How many terminals does the company have?",
                "types": "Computers, IoT-Devices, Mobile devices etc."
            }
        },

        "software": {
            "operating-systems": "Windows, Linux, MacOS?",
            "Business software": "ERP, CRM, Office suites?",
            "security-software": "Antivirus software, installed firewalls or intrusion detection systems etc.",
            "cloud-platforms": "AWS, Azure, Google Cloud etc. "
        },

        "storage-management": {
            "DBMS": "SQL, NoSQL, Datawarehouses etc.",
            "recovery-strategies": {
                "types": "RAID, Backups etc.",
                "intervall": "How often is a backup created? (if at all)"
            }

        "security-compliance": {
            "standards": "ISO 27001 etc.",
            "access-control": "IAM, MFA or SSO",
            "counter-measures": "Firewalls, Intrusion Prevention Systems etc."
        },

        "monitoring": {
            "procedures": "IT policies within the company",
            "logging": "SIEM, ELK Stack etc."
        }
    },
    "security-management": {
        "policies": {
            "standards": "Like ISO 27001 etc.",
            "incident-plans": "What plans are executed in case of an incident?"
        },
        "network-security": {
            "firewalls": "Network-based firewalls?",
            "intrusion-detection": "Any Intrusion Det. systems installed? Which one?",
            "intrusion-prevention": "Any intrusion prevention system? Which one?",
            "vpn": "Does the company have a VPN?",
            "wifi-protocols": "Which protocols are used?"
        },
        "endpoint-security": {
            "antivirus": "Which antivirus tools does the company have?",
            "device-encryption": "Like Bitlocker etc.",
            "endpoint-detection": ""
        },
        "iam": {
            "authentification": "simple passwords, MFA, biometric data etc.",
            "role-based access control": "",
            "sso": "yes or no?",
            "pam": "yes or no?"
        },
        "data-security": {
            "security-laws": "Are there laws related to sec that are relevant for the company?",
            "encryption": {
                "critical-data": "Which kind of data does the company keep private?",
                "uncritical-data": "Data that doesn't need to be private.",
                "key-management": "central or de-central?",
            }
        },
        "user-groups": {
            "user-number": "How many users are there?",
            "access-rights": "Do the groups have different access rights?"
        },
        "sec-measurements": {
            "endpoint-security": "Are mail attachments getting verified?",
            "white-black-lists": "Does the company use White- and Blacklists to verify the sender?"
        }   
    }
}

Question: How do I install a firewall on the webserver of my company? 
Prompt: Which keys in the JSON-file above are of relevance for answering the Question?
Please answer with a list of the keys in the following format: [key_1, key_2, ..., key_n].

Response: 

Let's think step by step. 
First, we need to check if there are already firewalls or other security applications installed in the company. They key that is revealing that is IT-Infrastructure.software.security-software, as well as
security-management.network-security.firewalls, security-management.network-security.intrusion-detection and security-management.network-security.intrusion-prevention.q  
An other point is that we need to know how the network is segmentated in order to know how proceed, so we also need IT-Infrastructure.Network-structure.Segmentation.
An other important point id what types of routers the company is using as it may influence the choice of firewall, so IT-Infrastructure.hardware.Networking-devices.Routers is needed too.
A VPN encrypts traffic between users and complements a firewall. It's important to know whether the company has a VPN or not, as having one requires a special configuration, so we also need
security-management.network-security.vpn . The last key that is required to create an instruction is security-management.iam.authentification as the authentification proccess influences what IAM-Controls 
we need for the firewall. The final list is:

- IT-Infrastructure.software.security-software  
- IT-Infrastructure.Network-structure.Segmentation  
- IT-Infrastructure.hardware.Networking-devices.Routers  
- security-management.network-security.firewalls  
- security-management.network-security.intrusion-detection  
- security-management.network-security.intrusion-prevention  
- security-management.network-security.vpn  
- security-management.iam.authentification
'''

    _prompt = '''Question: How can I create a backup of the critical data of my company? 
                 Prompt: Which keys in the JSON-file above are of relevance for answering the Question?
                 Please answer with a list of the keys in the following format: [key_1, key_2, ..., key_n].'''

    def __init__(self):
        self.initialize_cot()

    def initialize_cot(self):
        self.__cot = f'''{self._cot_example}\n\n{self._prompt}'''


    def get_prompt(self):
        return self.__cot