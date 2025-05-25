'''

@author Maurice Amon
'''
from techniques.FewShotTechnique import FewShotTechnique
from techniques.factory.components.fewshots.Fewshot import Fewshot


class PlaybookFewshot(Fewshot):

    first_shot = ('''Question: Create a playbook for the following scenario: 
                   A small e-commerce business, \"SwiftGadgets,\" wakes up to find all their
                    customer order files encrypted. A ransom note demands 5 Bitcoin for decryption. 
                   Employees cannot access critical business data, and customers are complaining about pending orders.
                   Response: 
                   **Response Steps:**
                      ***1. Isolate Affected Systems:***
                      Immediately disconnect infected computers and servers from the network.
                      Do not turn off the affected machines; keep them on for forensic analysis.
                      ***2. Assess the Impact:***
                      Identify affected files and systems.
                      Check if backups are available and verify their integrity.
                      ***3. Do Not Pay the Ransom (Yet):***
                      Contact a cybersecurity expert or law enforcement (FBI, local cybercrime unit).
                      Paying does not guarantee data recovery and could encourage further attacks.
                      ***4. Restore Systems:***
                      If a clean backup exists, wipe the infected machines and restore data.
                      If no backup is available, consult a cybersecurity expert to check for decryption solutions.
                      ***5. Strengthen Security:***
                      Update all passwords and enable multi-factor authentication (MFA).
                      Install endpoint protection and monitor for suspicious activity.
                      Educate employees about phishing and malware risks.
                      ***6. Communicate Transparently:***
                      Inform customers if their data was compromised.
                      Notify legal authorities and comply with data breach laws.\n\n''')

    second_shot = '''Question: Create a playbook for the following scenario:
                       The finance department at \"TechNova Inc.\" receives an urgent email from the CEO, 
                       asking for an immediate wire transfer of $100,000 to a new vendor. The email looks legitimate, 
                       but later, the real CEO denies sending it. 
                       The company has just been targeted by Business Email Compromise (BEC).
                       Response:
                       Response Steps:
                       ***1. Stop the Transaction Immediately:***
                             Call the bank to halt the transfer if possible.
                             Report the fraud to law enforcement and cybersecurity teams.
                       ***2. Investigate the Email:***
                             Check the sender's email domain (e.g., ceo@techn0va.com vs. ceo@technova.com).
                             Review email headers for signs of spoofing.
                             Analyze any links or attachments for malware.
                       ***3. Assess Damage and Notify Stakeholders:***
                             Identify if other employees received similar emails.
                             Inform the real CEO and leadership team.
                       ***4. Strengthen Email Security:***
                             Implement email authentication protocols (SPF, DKIM, DMARC).
                             Set up internal policies requiring verbal confirmation for large transactions.
                             Train employees on social engineering tactics.
                       ***5. Monitor for Further Attacks:***
                             Watch for follow-up phishing emails.
                             Audit recent financial transactions for anomalies.\n\n'''

    third_shot = '''Question: Create a playbook for the following scenario:
                    A disgruntled employee at "FinTechSecure" resigns and, before leaving, downloads thousands of customer records onto 
                    a USB drive. The IT team notices unusual file transfers but is unsure what data was taken.
                    Response:
                    Response Steps:
                    ***1. Confirm and Contain the Breach:***
                          Check logs for large file transfers and external storage use.
                          Disable the employee's access to all company systems.
                    ***2. Investigate the Scope:***
                          Identify what data was stolen and if it includes sensitive information.
                          Interview relevant employees who worked with the suspect.
                    ***3. Take Legal and Preventive Action:***
                          Consult legal teams to assess potential legal violations.
                          If customer data is involved, comply with breach notification laws.
                    ***4. Enhance Access Controls:***
                          Implement strict user access policies (least privilege principle).
                          Use Data Loss Prevention (DLP) tools to block unauthorized data transfers.
                    ***5. Monitor for Further Threats:***
                          Track any unusual logins from the ex-employee's credentials.
                          Ensure critical files are regularly audited.\n\n'''

    def __init__(self):
        self.initialize_fewshots()


    def initialize_fewshots(self):
        self._few_shot = f'''{self.first_shot} {self.second_shot} {self.third_shot}
        Question: Please write a playbook/incident-response for an employee in the following situation:
        The employee works as an assistant in a hospital where he's responsible for administrating the patients data. 
        While he was going to the office, he lost his laptop in the train. 
        The data of the patients were stored on this laptop together with other highly private data.'''
        print(self._few_shot)

    def get_prompt(self):
        return self._few_shot