'''

@author Maurice Amon
'''
from techniques.factory.components.zeroshot.Zeroshot import Zeroshot


class ExampleCompanyZeroshot(Zeroshot):

    _example = '''
    '''

    _few_shot = ''''''

    def __init__(self):
        self.initialize()

    def initialize(self):
        self._instruction = '''JSON:
{
    "company-information": {
        "description": "More general information about the company like name, business type and registration number.",
        "name": "SwissTech Inc.",
        "business-type": {
            "description": "Details about the business type of the company.",
            "type": "AG"
        },
        "purpose": "Developing and implementing innovative IT solutions",
        "legal-number": "CHE-123.456.789",
        "board-members": {
            "description": "A list of all boardmembers of the company",
            "board-member-list": [
                {
                    "description": "Details about the specific board member such as their name and their role.",
                    "firstname": "Max",
                    "lastname": "Muster",
                    "role": {
                        "description": "The role the board-member has.",
                        "role-type": "Executive",
                        "is-active": "True"
                    }
                }
            ]
        },
        "office": {
            "description": "Locations of headquartes and branches of the company.",
            "headquarters": {
                "description": "An array of all offices the company has it's headquarters.",
                "headquarters": [
                    {
                        "name": "Main Office",
                        "legal-number": "CHE-123.456.789",
                        "legal-seat": "Zurich",
                        "purpose": "Main office and development center",
                        "status": "ACTIVE",
                        "departments": {
                            "description": "An array with all departments that are located in the headquarter.",
                            "department-list": [
                                {
                                    "name": "R&D",
                                    "department-head": {
                                        "description": "Details about the employee who is leading the department.",
                                        "firstname": "John",
                                        "lastname": "Doe",
                                        "role": "Department Head",
                                        "email": "john.doe@swisstech.ch",
                                        "phone": "+41 79 123 45 67"
                                    },
                                    "employees": {
                                        "description": "A list with all employees that are associated with the department.",
                                        "employee-list": [
                                            {
                                                "firstname": "Jane",
                                                "lastname": "Smith",
                                                "role": "Software Developer",
                                                "email": "jane.smith@swisstech.ch",
                                                "phone": "+41 79 123 45 68"
                                            }
                                        ]
                                    }
                                }
                            ]
                        },
                        "physical-access-control": {
                            "access-role-required": ["employee", "CEO"],
                            "controlled-entries": ["main door"],
                            "access-methods": ["RFID Badge", "Key"],
                            "monitoring": {
                                "installed-cameras": "true",
                                "camerage-coverage": "full",
                                "record-retention-time": "12 Months"
                            },
                            "visitor-management": {
                                "pre-registration-required": "true",
                                "identification": {
                                    "License-based-identification": "true",
                                    "biometric-identification": "false"
                                }
                            }
                        },
                        "address": {
                            "street": "Im Backofen",
                            "house-number": "16a",
                            "city": "Zurich",
                            "zip-code": 8000
                        },
                        "contact-info": {
                            "description": "Details about contact information for the specific headquarter.",
                            "email": "info@swisstech.ch",
                            "phone": "+41 44 123 45 67"
                        }
                    }
                ]
            },
            "branches": {
                "description": "An array of all offices the company has branches in.",
                "branches": [
                    {
                        "name": "Branch Office",
                        "legal-number": "CHE-987.654.321",
                        "legal-seat": "Geneva",
                        "purpose": "Sales and marketing office",
                        "status": "ACTIVE",
                        "departments": {
                            "description": "An array with all departments that are located in the branch.",
                            "department-list": [
                                {
                                    "name": "Sales",
                                    "department-head": {
                                        "description": "Details about the employee who is leading the department.",
                                        "firstname": "Alice",
                                        "lastname": "Johnson",
                                        "role": "Department Head",
                                        "email": "alice.johnson@swisstech.ch",
                                        "phone": "+41 22 123 45 67"
                                    },
                                    "employees": {
                                        "description": "A list with all employees that are associated with the department.",
                                        "employee-list": [
                                            {
                                                "firstname": "Bob",
                                                "lastname": "Williams",
                                                "role": "Sales Representative",
                                                "email": "bob.williams@swisstech.ch",
                                                "phone": "+41 22 123 45 68"
                                            }
                                        ]
                                    }
                                }
                            ]
                        },
                        "physical-access-control": {
                            "access-role-required": ["employee", "CEO"],
                            "controlled-entries": ["main door"],
                            "access-methods": ["RFID Badge", "Key"],
                            "monitoring": {
                                "installed-cameras": "true",
                                "camerage-coverage": "full",
                                "record-retention-time": "12 Months"
                            },
                            "visitor-management": {
                                "pre-registration-required": "true",
                                "identification": {
                                    "License-based-identification": "true",
                                    "biometric-identification": "false"
                                }
                            }
                        },
                        "address": {
                            "street": "Rue de la Croix-Rouge",
                            "house-number": "10",
                            "city": "Geneva",
                            "zip-code": 1201
                        },
                        "contact-info": {
                            "description": "Details about contact information for the specific headquarter.",
                            "email": "geneva@swisstech.ch",
                            "phone": "+41 22 123 45 67"
                        }
                    }
                ]
            }
        },
        "contact-info": {
            "description": "General contact-information like Email, phone number",
            "email": "info@swisstech.ch",
            "phone": "+41 44 123 45 67"
        },
        "publicly-avaiable-information": {
            "national-business-register": {
                "description": "Registration information in the national business register"
            },
            "linked-in": {
                "linked-in-description": "We are a leading IT company. Etc.",
                "linkedin-tagline": "Innovative IT solutions",
                "industry": "Information Technology",
                "linked-in-pages": ["https://linkedin.com/company/swisstech"],
                "employee-count-range": {
                    "start": 50,
                    "end": 100
                },
                "founded": {
                    "year": 2010
                },
                "staff-count": 75
            },
            "websites": [
                {
                    "description": "Details about the website provided by the company.",
                    "identifer": "Public company website.",
                    "cms": {
                        "description": "Details about the Content Management System (CMS) used for website.",
                        "system": "Wordpress",
                        "version": "5.8.1"
                    },
                    "hosting": {
                        "description": "Location where the website is hosted.",
                        "storage-id": "AWS S3",
                        "uri": "https://swisstech.ch"
                    },
                    "webserver": {
                        "description": "Used webserver technology.",
                        "system": "Apache"
                    },
                    "operating-system": {
                        "description": "Operating system used for the website.",
                        "operating-system-id": "Ubuntu 20.04"
                    },
                    "purpose": {
                        "description": "Main purpose/functions of the website, importance for business continuity.",
                        "purpose": "Public information platform of the company, e-shop functionality to order goods.",
                        "login-functionality": "yes",
                        "importance": "high"
                    },
                    "data": {
                        "description": "Type of data stored by the website (company information, customer information, payment data,...).",
                        "type": "customer-data"
                    },
                    "cookies": {
                        "description": "A list with all Cookies that the website is using.",
                        "cookie-list": [
                            {
                                "name": "session_id",
                                "value": "1234567890",
                                "domain": "swisstech.ch",
                                "path": "/",
                                "expires": "2024-03-16",
                                "http-only": "true",
                                "secure": "true",
                                "same-party": "true",
                                "session": "true",
                                "source-port": "443"
                            }
                        ]
                    },
                    "security-header": {
                        "description": "Values of the security header of the webpage.",
                        "name": "strict-transport-security",
                        "value": "max-age=31536000; includeSubDomains"
                    }
                }
            ]
        },
        "operational": {
            "description": "Operational details about the company.",
            "suppliers": {
                "description": "List of the suppliers",
                "supplier-array": [
                    {
                        "name": "Microsoft"
                    }
                ]
            },
            "clients": {
                "description": "List of the clients",
                "client-array": [
                    {
                        "name": "UBS"
                    }
                ]
            },
            "sales": {
                "description": "How much money does the company make?",
                "sales-volume": "10M CHF"
            }
        }
    },
    "security-management": {
        "description": "Details about how the company manages it's IT-Security Management.",
        "policies": {
            "description": "Policies and incident playbooks that are being implemented.",
            "standards": {
                "description": "List of the security standards that the company implements.",
                "standards-array": ["ISO 27001"]
            },
            "personal-training": {
                "security-awareness-training": {
                    "mandatory": "true",
                    "frequency": "quarterly",
                    "last-conducted": "2023-12-15",
                    "threats": ["Phishing-emails", "ransomware attacks"],
                    "target-groups": "IT Admin | CISO | DPO | Process Owner"
                },
                "onboarding-process": {
                    "mandatory-it-security-training": "true",
                    "role-based-access": "true",
                    "nda-contract": "true"
                },
                "offboarding-process": {
                    "access-revoked": "true",
                    "device-handing-in": "true",
                    "exit-interview": "true"
                }
            },
            "incident-plans": [
                {
                    "name": "incident1",
                    "playbook": "Incident Response Plan"
                }
            ]
        },
        "business-continuity-plan": {
            "metadata": {
                "last-update": "2023-12-15"
            },
            "disaster-recovery-plan": {
                "description": "Plan for disaster recovery",
                "metadata": {
                    "last-update": "2023-12-15"
                },
                "incident-response": [
                    {
                        "description": "Response to incidents",
                        "incident": {
                            "name": "Ransomware Attack",
                            "description": "Attack on company data",
                            "impact": "HIGH",
                            "detection": "Automated detection system"
                        },
                        "response": {
                            "name": "Incident Response Team",
                            "description": "Team responsible for responding to incidents"
                        }
                    }
                ]
            }
        },
        "risk-management": {
            "description": "Risk management process",
            "risk-scenarios": [
                {
                    "risk-name": "Phishing Attack on Executives",
                    "risk-source": "External",
                    "impact": "HIGH",
                    "likelihood": "MEDIUM",
                    "existing-controls": ["Spam Filter", "Security awareness", "MFA for email"]
                }
            ],
            "risk-review-frequency": "quarterly"
        },
        "antivirus-software": [
            {
                "name": "Symantec Endpoint Protection",
                "version": "14.2",
                "vendor": "Symantec",
                "device-names": ["PC-Max"],
                "protection-features": {
                    "description": "true",
                    "real-time-protection": true,
                    "ransomeware-protection": true,
                    "email-protection": true,
                    "sandboxing": false,
                    "web-protection": true
                }
            }
        ],
        "sec-measurements": {
            "description": "More general security measurements that are being implemented in the company.",
            "endpoint-security": {
                "hd-encryptions": [
                    {
                        "device-name": "PC-Max",
                        "tool": {
                            "tool-name": "BitLocker",
                            "version": "2.0",
                            "encryption-algorithm": "AES-256"
                        },
                        "hd-encryption-type": "Pin"
                    }
                ],
                "firewall": {
                    "firewall-device-list": [
                        {
                            "device-name": "PC-Max",
                            "tool": {
                                "name": "Windows Defender",
                                "version": "2.0",
                                "license": "Free"
                            },
                            "features": ["Packet Filtering", "Malware Protection"]
                        }
                    ]
                }
            },
            "allow-block-lists": {
                "description": "Does the company use White- and Blacklists to verify the sender?",
                "value": "Yes"
            }
        },
        "patch-management": {
            "policy": {
                "description": "Patch management policy",
                "roles-in-charge": ["IT Manager"]
            },
            "scope": {
                "covered-systems": ["PC", "Server"],
                "operating-system-ids": [1],
                "device-names": ["PC-Max"]
            },
            "software-tools": {
                "patch-management-software": "Automox",
                "automation-enabled": true
            },
            "process": {
                "patch-identification-frequency": "daily",
                "deployment-method": "automated",
                "rollback-option": "true"
            },
            "scheduling": {
                "patch-time-window": "Saturday 02:00 - 05:00"
            },
            "compliance": {
                "logging": "true",
                "complicance-threshold": "95%"
            }
        },
        "cyber-insurance": {
            "policy-id": "XY123",
            "insurance-company": "Allianz",
            "insurance-period": {
                "start-date": "2023-01-01",
                "end-date": "2024-01-01"
            },
            "coverage": {
                "total-amount": 1000000,
                "currency": "CHF",
                "coverage-scenarios": [
                    {
                        "description": "Covers the costs needed for legal actions as a response to a data breach",
                        "coverage-type": "Data breach",
                        "limit": 500000
                    }
                ]
            }
        }
    },
    "IT-Infrastructure": {
        "description": "Details about the IT-Infrastructure of the company.",
        "network-structure": {
            "description": "Details about the Network structure of the company.",
            "segmentation": {
                "description": "Details about how the network is segmentated.",
                "devices": {
                    "routers": [
                        {
                            "model": {
                                "model-name": "Cisco 881",
                                "model-number": "881",
                                "manufacturer": "Cisco",
                                "firmware": "15.4"
                            },
                            "configuration": {
                                "ipv4-address": "192.168.1.1",
                                "subnet_mask": "255.255.255.0",
                                "gateway-address": "192.168.1.254",
                                "dns-servers": ["8.8.8.8"]
                            },
                            "subnets": [
                                {
                                    "subnet-name": "XY",
                                    "ip-range": "192.168.1.0/24",
                                    "subnet-mask": "255.255.255.0",
                                    "gateway": "192.168.1.254",
                                    "devices": [
                                        {
                                            "device-name": "PC-Max",
                                            "device-type": "PC",
                                            "operating-system-id": 1,
                                            "mac-address": "00:2A:3B:6C:7D:04",
                                            "ip-address": "192.168.1.100"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            }
        }
    },
    "software": {
        "description": "Details about the OS and business applications the company uses.",
        "operating-systems": {
            "os-array": [
                {
                    "operating-system-id": 1,
                    "OS": "Windows 10",
                    "version": "20H2"
                }
            ]
        },
        "business-software": {
            "description": "Details about the business software the company uses",
            "bs-array": [
                {
                    "business-software-id": 1,
                    "name": "Microsoft Office",
                    "type": "Office suites"
                }
            ]
        },
        "cloud-platforms": {
            "description": "A list of all cloud services that the company uses.",
            "cloud-technology-array": [
                {
                    "cloud-id": 1,
                    "provider": "Microsoft",
                    "service-model": "SaaS"
                }
            ]
        }
    },
    "storage-management": {
        "description": "Details about how the company manages it's data persistence.",
        "DBMS": "SQL Server",
        "recovery-strategies": {
            "description": "Describes how lost data can be recovered.",
            "strategy-array": [
                {
                    "type": "Backup",
                    "intervall": "daily"
                }
            ]
        },
        "security-compliance": {
            "description": "Utilized security policies.",
            "standards": {
                "description": "An array of security policies the company implements.",
                "standard-array": ["ISO 27001"]
            },
            "access-control": {
                "description": "IAM, MFA or SSO"
            }
        },
        "monitoring": {
            "description": "Details about how and if the company creates logs of security-critical processes.",
            "procedures": "IT policies within the company",
            "logging": "SIEM"
        }
    },
    "data-management": {
        "description": "This key serves as an umbrella for all categories of data a KMU usually needs to handle.",
        "customer-data": {
            "description": "",
            "storage": {
                "description": "Depending on the type of storage just one element will be displayed here.",
                "storage-types": [
                    {
                        "storage-id": 1,
                        "device-name": "None",
                        "description": "Cloud TYPE",
                        "storage-type": "CLOUD",
                        "cloud-id": 1,
                        "deployment-privacy": "Private",
                        "storage-volume": "1TB"
                    }
                ]
            }
        },
        "employee-data": {
            "description": "",
            "storage": {
                "description": "Depending on the type of storage just one element will be displayed here.",
                "storage-types": [
                    {
                        "storage-id": 2,
                        "device-name": "EMP-Server",
                        "description": "Describes the type of storage that is provided..",
                        "storage-type": "DATABASE",
                        "database-type": "Relational Database",
                        "dbms": "PostgreSQL",
                        "cloud": {
                            "is-cloud-hosted": "False",
                            "cloud-id": "None",
                            "type": "None"
                        },
                        "storage-volume": "500GB"
                    }
                ]
            }
        },
        "financial-data": {
            "description": "",
            "storage": {
                "description": "Depending on the type of storage just one element will be displayed here.",
                "storage-types": [
                    {
                        "storage-id": 3,
                        "device-name": "None",
                        "description": "Cloud TYPE",
                        "storage-type": "CLOUD",
                        "provider": "AWS",
                        "service-model": "IaaS",
                        "deployment-privacy": "Private",
                        "storage-volume": "2TB"
                    }
                ]
            }
        }
    }
}

    Prompt: What are the weaknesses of the company above regarding it's IT security? Please think about your answer first and then create a list of the most important noun-words of said answer. Just think about one weakness. Your response should just contain the list of the most important words, no explanations.'''

    def get_prompt(self):
        return self._instruction