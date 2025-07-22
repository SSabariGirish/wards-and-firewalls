import Thieves as tf

class Guard:
     def __init__(self):
          self.kingdom_gold = 300
          self.income_multiplier = 1
          self.cost_multiplier = 1
          self.exfiltration_multiplier = 1

          # Kingdom Buffs
          self.has_training = 0
          self.has_mfa = 0
          self.has_ids = 0
          self.has_firewalls = 0
          self.has_rate_limiting = 0
          self.has_e2ee = 0
          self.has_vpn = 0
          self.has_acc_lockout = 0
          self.has_lpa = 0
          self.has_param_queries = 0
          self.has_input_sanitisation = 0
          self.has_net_segmentation = 0
          self.has_https = 0
          self.has_zta = 0
          self.has_offshore_backup = 0
          self.has_waf = 0

          # List of Cards Drawn
          self.card_headers_medieval = [guard_protection_header_medieval[0]]
          self.card_explanations_medieval = [guard_protection_explanation_medieval[0]]
          self.card_headers_real_life = [guard_protection_header_real_life[0]]
          self.card_explanations_real_life = [guard_protection_explanation_real_life[0]]
          self.card_image = [guard_image_list[0]]
          self.rl_card_image = [guard_rl_image_list[0]]
          self.card_cost = [guard_defence_cost[0]]
          self.maintenance_cost = [guard_maintenance_cost[0]]

     def scribe_training(self):
          cost = 10 * self.cost_multiplier
          if self.kingdom_gold < cost:
               return False
          else:
               self.kingdom_gold -= cost
               self.has_training += 5
               return True

     def twin_sigils(self):
          b_cost = 15 * self.cost_multiplier
          m_cost = 10 * self.cost_multiplier
          # Buying
          if self.has_mfa == 0:
               if self.kingdom_gold < b_cost:
                    return False
               else:
                    self.kingdom_gold -= b_cost
                    self.has_mfa += 5
                    return True
          # Maintenance
          else:
               if self.kingdom_gold < m_cost:
                    return False
               else:
                    self.kingdom_gold -= m_cost
                    self.has_mfa += 5
                    return True

     def gargoyles(self):
          b_cost = 100 * self.cost_multiplier
          m_cost = 60 * self.cost_multiplier
          # Buying
          if self.has_ids == 0:
               if self.kingdom_gold < b_cost:
                    return False
               else:
                    self.kingdom_gold -= b_cost
                    self.has_ids += 5
                    return True
          # Maintenance
          else:
               if self.kingdom_gold < m_cost:
                    return False
               else:
                    self.kingdom_gold -= m_cost
                    self.has_ids += 5
                    return True

     def battlements(self):
          b_cost = 35 * self.cost_multiplier
          m_cost = 20 * self.cost_multiplier
          # Buying
          if self.has_firewalls == 0:
               if self.kingdom_gold < b_cost:
                    return False
               else:
                    self.kingdom_gold -= b_cost
                    self.has_firewalls += 5
                    return True
          # Maintenance
          else:
               if self.kingdom_gold < m_cost:
                    return False
               else:
                    self.kingdom_gold -= m_cost
                    self.has_firewalls += 5
                    return True

     def crier(self):
          b_cost = 30 * self.cost_multiplier
          m_cost = 20 * self.cost_multiplier
          # Buying
          if self.has_rate_limiting == 0:
               if self.kingdom_gold < b_cost:
                    return False
               else:
                    self.kingdom_gold -= b_cost
                    self.has_rate_limiting += 5
                    return True
          # Maintenance
          else:
               if self.kingdom_gold < m_cost:
                    return False
               else:
                    self.kingdom_gold -= m_cost
                    self.has_rate_limiting += 5
                    return True

     def cipher(self):
          b_cost = 30 * self.cost_multiplier
          m_cost = 20 * self.cost_multiplier
          # Buying
          if self.has_e2ee == 0:
               if self.kingdom_gold < b_cost:
                    return False
               else:
                    self.kingdom_gold -= b_cost
                    self.has_e2ee += 5
                    return True
          # Maintenance
          else:
               if self.kingdom_gold < m_cost:
                    return False
               else:
                    self.kingdom_gold -= m_cost
                    self.has_e2ee += 5
                    return True

     def sewer(self):
          b_cost = 25 * self.cost_multiplier
          m_cost = 15 * self.cost_multiplier
          # Buying
          if self.has_vpn == 0:
               if self.kingdom_gold < b_cost:
                    return False
               else:
                    self.kingdom_gold -= b_cost
                    self.has_vpn += 5
                    return True
          # Maintenance
          else:
               if self.kingdom_gold < m_cost:
                    return False
               else:
                    self.kingdom_gold -= m_cost
                    self.has_vpn += 5
                    return True

     def iron_gate(self):
          cost = 15 * self.cost_multiplier
          if self.kingdom_gold < cost:
               return False
          else:
               self.kingdom_gold -= cost
               self.has_acc_lockout += 5
               return True

     def squire(self):
          b_cost = 15 * self.cost_multiplier
          m_cost = 10 * self.cost_multiplier
          # Buying
          if self.has_lpa == 0:
               if self.kingdom_gold < b_cost:
                    return False
               else:
                    self.kingdom_gold -= b_cost
                    self.has_lpa += 5
                    return True
          # Maintenance
          else:
               if self.kingdom_gold < m_cost:
                    return False
               else:
                    self.kingdom_gold -= m_cost
                    self.has_lpa += 5
                    return True

     def snare(self):
          b_cost = 35 * self.cost_multiplier
          m_cost = 20 * self.cost_multiplier
          # Buying
          if self.has_param_queries == 0:
               if self.kingdom_gold < b_cost:
                    return False
               else:
                    self.kingdom_gold -= b_cost
                    self.has_param_queries += 5
                    return True
          # Maintenance
          else:
               if self.kingdom_gold < m_cost:
                    return False
               else:
                    self.kingdom_gold -= m_cost
                    self.has_param_queries += 5
                    return True

     def ink(self):
          b_cost = 20 * self.cost_multiplier
          m_cost = 10 * self.cost_multiplier
          # Buying
          if self.has_input_sanitisation == 0:
               if self.kingdom_gold < b_cost:
                    return False
               else:
                    self.kingdom_gold -= b_cost
                    self.has_input_sanitisation += 5
                    return True
          # Maintenance
          else:
               if self.kingdom_gold < m_cost:
                    return False
               else:
                    self.kingdom_gold -= m_cost
                    self.has_input_sanitisation += 5
                    return True

     def walls(self):
          b_cost = 50 * self.cost_multiplier
          m_cost = 30 * self.cost_multiplier
          # Buying
          if self.has_net_segmentation == 0:
               if self.kingdom_gold < b_cost:
                    return False
               else:
                    self.kingdom_gold -= b_cost
                    self.has_net_segmentation += 5
                    return True
          # Maintenance
          else:
               if self.kingdom_gold < m_cost:
                    return False
               else:
                    self.kingdom_gold -= m_cost
                    self.has_net_segmentation += 5
                    return True

     def vanguard(self):
          b_cost = 30 * self.cost_multiplier
          m_cost = 20 * self.cost_multiplier
          # Buying
          if self.has_https == 0:
               if self.kingdom_gold < b_cost:
                    return False
               else:
                    self.kingdom_gold -= b_cost
                    self.has_https += 5
                    return True
          # Maintenance
          else:
               if self.kingdom_gold < m_cost:
                    return False
               else:
                    self.kingdom_gold -= m_cost
                    self.has_https += 5
                    return True

     def doctrine(self):
          b_cost = 125 * self.cost_multiplier
          m_cost = 80 * self.cost_multiplier
          # Buying
          if self.has_zta == 0:
               if self.kingdom_gold < b_cost:
                    return False
               else:
                    self.kingdom_gold -= b_cost
                    self.has_zta += 5
                    return True
          # Maintenance
          else:
               if self.kingdom_gold < m_cost:
                    return False
               else:
                    self.kingdom_gold -= m_cost
                    self.has_zta += 5
                    return True

     def borough(self):
          b_cost = 50 * self.cost_multiplier
          m_cost = 30 * self.cost_multiplier
          # Buying
          if self.has_offshore_backup == 0:
               if self.kingdom_gold < b_cost:
                    return False
               else:
                    self.kingdom_gold -= b_cost
                    self.has_offshore_backup += 5
                    return True
          # Maintenance
          else:
               if self.kingdom_gold < m_cost:
                    return False
               else:
                    self.kingdom_gold -= m_cost
                    self.has_offshore_backup += 5
                    return True

     def bastion(self):
          b_cost = 60 * self.cost_multiplier
          m_cost = 40 * self.cost_multiplier
          # Buying
          if self.has_waf == 0:
               if self.kingdom_gold < b_cost:
                    return False
               else:
                    self.kingdom_gold -= b_cost
                    self.has_waf += 5
                    return True
          # Maintenance
          else:
               if self.kingdom_gold < m_cost:
                    return False
               else:
                    self.kingdom_gold -= m_cost
                    self.has_waf += 5
                    return True

     def deteriorate(self):

          deteriorated = []

          deteriorated.append('Soldiers and Noblemen have forgotten the trainings provided by the Royal Scribe!\n') if self.has_training == 1 else None
          deteriorated.append('The Twin Seal Protocol has deteriorated!\n') if self.has_mfa == 1 else None
          deteriorated.append('The Whispering Gargoyles have run out of mana!\n') if self.has_ids == 1 else None
          deteriorated.append('The Flaming Battlements have run out of mana!\n') if self.has_firewalls == 1 else None
          deteriorated.append('The Town Crier\'s extra wages are unpaid, thus ending his services!\n') if self.has_rate_limiting == 1 else None
          deteriorated.append('The Royal Cipher has been cracked and has lost its effectiveness!\n') if self.has_e2ee == 1 else None
          deteriorated.append('The Sewer Tunnels are unusable now!\n') if self.has_vpn == 1 else None
          deteriorated.append('The Iron Gate has deteriorated!\n') if self.has_acc_lockout == 1 else None
          deteriorated.append('The Code of the Squire has been forgotten due to a recent scuffle!\n') if self.has_lpa == 1 else None
          deteriorated.append('The Sylvan Oracle Snare has run out of mana!\n') if self.has_param_queries == 1 else None
          deteriorated.append('The Ink Purification Ritual has run out of mana!\n') if self.has_input_sanitisation == 1 else None
          deteriorated.append('The Walls of Districts were broken in a recent attack!\n') if self.has_net_segmentation == 1 else None
          deteriorated.append('The Silver Vanguard have new demands and refuse to work until they are met!\n') if self.has_https == 1 else None
          deteriorated.append('The Ironbound Doctrine was lost in a fire!\n') if self.has_zta == 1 else None
          deteriorated.append('The Hidden Borough was burnt in a forest fire!\n') if self.has_offshore_backup == 1 else None
          deteriorated.append('The Dwarven Bastion has run out of mana!\n') if self.has_waf == 1 else None

          self.has_training = self.has_training - 1 if self.has_training > 0 else self.has_training
          self.has_mfa = self.has_mfa - 1 if self.has_mfa > 0 else self.has_mfa
          self.has_ids = self.has_ids - 1 if self.has_ids > 0 else self.has_ids
          self.has_firewalls = self.has_firewalls - 1 if self.has_firewalls > 0 else self.has_firewalls
          self.has_rate_limiting = self.has_rate_limiting - 1 if self.has_rate_limiting > 0 else self.has_rate_limiting
          self.has_e2ee = self.has_e2ee - 1 if self.has_e2ee > 0 else self.has_e2ee
          self.has_vpn = self.has_vpn - 1 if self.has_vpn > 0 else self.has_vpn
          self.has_acc_lockout = self.has_acc_lockout - 1 if self.has_acc_lockout > 0 else self.has_acc_lockout
          self.has_lpa = self.has_lpa - 1 if self.has_lpa > 0 else self.has_lpa
          self.has_param_queries = self.has_param_queries - 1 if self.has_param_queries > 0 else self.has_param_queries
          self.has_input_sanitisation = self.has_input_sanitisation - 1 if self.has_input_sanitisation > 0 else self.has_input_sanitisation
          self.has_net_segmentation = self.has_net_segmentation - 1 if self.has_net_segmentation > 0 else self.has_net_segmentation
          self.has_https = self.has_https - 1 if self.has_https > 0 else self.has_https
          self.has_zta = self.has_zta - 1 if self.has_zta > 0 else self.has_zta
          self.has_offshore_backup = self.has_offshore_backup - 1 if self.has_offshore_backup > 0 else self.has_offshore_backup
          self.has_waf = self.has_waf - 1 if self.has_waf >   0 else self.has_waf

          return deteriorated



guard_protection_header_real_life = ["Cyber Awareness Training", "Multi Factor Authentication", "Intrusion Detection Systems",
"Firewalls", "Rate Limiting", "End-to-end Encryption", "VPN", "Account Lockout", "Least Privileged Access", "Parameterised Queries",
"User Input Sanitisation", "Network Segmentation",  "Secure HTTPS Connections", "Zero Trust Architecture", "Offshore Data Backup",
"Web Application Firewall"]

guard_protection_header_medieval = ["Guild of Watchful Scribes", "Twin Seal Protocol", "The Whispering Gargoyles",
"The Flaming Battlements", "The Town Crier", "The Royal Cipher", "The Sewer Tunnels", "Iron Gate Lockdown", "Code of The Squire",
"The Sylvan Oracle Snare", "Ink Purification Ritual", "The Walled Districts", "The Silver Vanguard",
"The Ironbound Doctrine", "The Hidden Borough", "The Dwarven Bastion"]

guard_defence_cost = [10, 15, 100, 35, 30, 30, 25, 10, 15, 35, 20, 50, 30, 125, 50, 60]
guard_maintenance_cost = [10, 10, 60, 20, 20, 20, 15, 10, 10, 20, 10, 30, 20, 80, 30, 40]

guard_image_list = [
     f"static/images/Guards/{name}.jpg"
     for name in guard_protection_header_medieval
]

guard_rl_image_list = [
     f"static/images/Guards RL/{name}.jpg"
     for name in guard_protection_header_real_life
]

guard_protection_explanation_medieval = [
'''
    Cost: 10 Gold \n
    Maintenance: 10 Gold \n
    No more fools allowed in the kingdom \n
    You commission the Royal scribes to teach the Guards and Townsfolk about the activities of sly salesmen and Alehouse drunkards \n
    For the next 5 turns, Guards are less susceptible to Snake Oil Salesman and Alehouse Swindler \n
    By the 6th turn, the folk grow complacent once again \n
    Real life equivalent - Cyber Awareness Training \n
''',
'''
    Cost: 15 Gold \n
    Maintenance: 10 Gold \n
    Sigils are not safe enough!! \n
    All Townsfolk now carry their sigils and a secret passphrase which will be verified before they are allowed entrance \n
    Real life equivalent - Mult-Factor Authentication (MFA)\n
''',
'''
    Cost: 100 Gold\n
    Maintenance: 60 Gold\n
    Guards are now far more vigilant of uninvited guests\n
    Mystical Gargoyle statues gifted by the Saint Merlin scream to the Royal Protector when they see\n
    uninvited guests lurking in the shadows\n
    Real life equivalent - Intrusion Detection Systems (IDS)\n
''',
'''
    Cost: 35 Gold\n
    Maintenance: 20 Gold\n
    Enough of those scallywags!\n
    The castle's outer walls are now lined with mystical fire traps that scorch anyone or anything that tries to breach them\n
    Offers significant protection against multiple attacks by the Thief Guild\n
    Real life equivalent - Firewalls\n
''',
'''
    Cost: 30 Gold\n
    Maintenance: 20 Gold\n
    One at a time, folk! One at a time!\n
    The Royal Crier assists the guards. Only a certain amount of people can talk to the guards at a time\n
    The rest are asked to form a line and wait\n
    Real life equivalent - Rate Limiting\n
''',
'''
    Cost: 30 Gold\n
    Maintenance: 20 Gold\n
    You can always be more careful\n
    Messages between Kingdoms are always encoded with an unbreakable cipher\n
    Even the messengers do not know of the cipher\n
    Real life equivalent - End to End Encryption (E2EE)\n
''',
'''
    Cost: 25 Gold\n
    Maintenance: 15 Gold\n
    You can't steal what you can't see\n
    Hidden underground tunnels help the king's spies reach the kingdom away from prying eyes\n
    Real life equivalent - Virtual Private Network (VPN)\n
''',
'''
    Cost: 10 Gold\n
    Maintenance: 10 Gold\n
    Sticks and stones cannot break Iron\n
    If there are multiple failed attempts made to open the castle gate, the portcullis slams shut and remains locked\n
    Bandits and Brigands cannot enter through the main gate\n
    Real life equivalent - Account Lockout Policy\n
''',
'''
    Cost: 15 Gold\n
    Maintenance: 10 Gold\n
    In a fool's hands, even the finest of silk is no different from a torn rag \n
    A squire may polish a knight\'s armor but cannot wield his sword\n
    Townsfolk and guards may only access the places they need to use\n
    Real life equivalent - Least Privilege Access\n
''',
'''
    Cost: 35 Gold\n
    Maintenance: 20  Gold\n
    Do not underestimate the beings of the forest\n
    A magical trap woven into the lock prevents misuse of the Sylvan tongue\n
    Real life equivalent - Parameterised Queries\n
''',
'''
    Cost: 20 Gold\n
    Maintenance: 10 Gold\n
    Magical cleansing\n
    Scribes cleanse the scrolls of any hidden curses or malicious symbols that could corrupt the records\n
    Real life equivalent - Input Sanitisation\n
''',
'''
    Cost: 50 Gold\n
    Maintenance: 30 Gold\n
    Cities of Might, Bound by Stone\n
    The kingdom is divided into separate, walled districts\n
    Even if one district is attacked, the rest remain safe from the invasion\n
    Real life equivalent - Network Segmentation\n
''',
'''
    Cost: 30 Gold\n
    Maintenance: 20 Gold\n
    The messenger is of PARAMOUNT importance\n
    A unit of elite knights escorting royal messengers\n
    Ensure that correspondence reaches its destination untampered and trustworthy\n
    Real life equivalent - HTTPS\n
''',
'''
    Cost: 125 Gold\n
    Maintenance: 80 Gold\n
    Never Trust, Always Verify\n
    A decree that none may enter the castle without proof of identity\n
    Verifications are done at every step between districts and at random points\n
    Offers strong protection against most of the Thief Guild's attacks \n
    Real life equivalent - Zero Trust Architecture (ZTA)\n
''',
'''
    Cost: 50 Gold\n
    Maintenance: 30 Gold\n
    Emergency Rations\n
    A secret, fortified village far from the main kingdom\n
    Storing essential supplies and records in case of disaster\n
    Real life equivalent - Offshore Data Backup\n
''',
'''
    Cost: 60 Gold\n
    Maintenance: 40 Gold\n
    Pride of the Dwarves\n
    A legendary magical fortress built by dwarven master-smiths\n
    Reinforced with enchanted stone and magic that primarily protects the Inner Sanctums with rune-etched Gates and Logic Seals\n
    Can also offer limited support to the outer walls of the Castle\n
    Can stop Loose Castle Walls, Clatter of Brats, Bandits and Brigands, The Cipherbane and The Poisoned Scroll\n
    Real life equivalent - Web Application Firewall (WAF)\n
'''
]

guard_protection_explanation_real_life = [
'Educating employees on recognising and preventing cyber threats like phishing and social engineering'
'\n\nCan significantly mitigate the chances of Mass Phishing, Spear Phishing and all other forms of Phishing'
'\n\nOver 90% of successful Cyber Attacks initiate via different forms of Phishing'
'\n\nAlso offers moderate protection against Ransomware, Session Hijacking and Worms by enhancing users\' digital hygiene',

'Requiring multiple verification methods mostly a normal password and a One-Time-Password to access an account'
'\n\nCan be of significant help in stopping brute force attempts and work in tandem with regular Cyber Awareness Trainings'
'\n\nAuthenticator Apps, FIDO2 Security Keys and Smart Cards are front-runners in MFA'
'\n\nWorks in tandem with strong cyber awareness training and offers moderate protection against Privilege escalation and Session Hijacking',

'Monitors network traffic for suspicious activities and potential cyber threats'
'\n\nCannot ACT on a threat, but immediately detects and logs the suspicious actions and informs the security personnel'
'\n\nHigh scope for involvement of AI and ML in detecting common attack signatures and patterns'
'\n\nOffers strong protection against majority of cyber attacks through instant detection and flagging',

'Security barriers that filter and control incoming and outgoing network traffic'
'\n\nOffer significant protection against Worms and DDoS attacks and moderate protection against Backdoors and Brute Force attacks'
'\n\nNext Generation Firewalls have Machine learning capabilities and offer stronger protection against evolving threats'
'\n\nOffers moderate protection against DDoS, Ransomware, Worms, Backdoors, Brute Force, Supply Chain and Privilege Escalation attacks',

'Restricting the number of requests a user or IP can make to prevent abuse'
'\n\nOffers strong protection against Brute Force attacks and helps mitigate DDoS attacks by preventing request floods'
'\n\nEnsures service availability by preventing resource exhaustion'
'\n\nOffers dedicated protection against DDoS attacks',

'Encrypting data so only the sender and recipient can read it, even the service provider cannot'
'\n\nOffers maximum protection against Man-in-the-Middle attacks and unauthorised access during transit'
'\n\nEnsures strong privacy and confidentiality by providing verifiable data integrity'
'\n\nOffers dedicated protection against Man-in-the-Middle attacks',

'Encrypting internet traffic to secure communications and hide the user\'s IP address'
'\n\nOffers strong protection against eavesdropping  on public networks and IP address tracking'
'\n\nEnables secure remote access, helps bypass geo-restrictions, and enhances overall online privacy and data security'
'\n\nOffers dedicated protection against Man-in-the-Middle attacks and moderate protection against Session Hijacking',

'Temporarily disabling an account after multiple failed login attempts to significantly hamper brute-force attempts'
'\n\nSignificantly hinders Credential Stuffing attempts'
'\n\nSecures user accounts by preventing automated password guessing and reduces the risk of unauthorised access'
'\n\nOffers dedicated protection against Brute Force attacks',

'Granting users only the minimum access necessary to perform their tasks'
'\n\nOffers strong protection against Privilege Escalation attacks and significantly limits the damage from Malware and Lateral Movement'
'\n\nReduces the attack surface, minimises the impact of a breach, and improves overall security posture by containing attacks'
'\n\nOffers dedicated protection against Privilege Escalation attacks and some protection against Ransomware',

'A secure method to handle database queries, preventing SQL injection attacks'
'\n\nOffers maximum protection against SQL Injection attacks and prevents malicious code execution within databases'
'\n\nEnsures data integrity, prevents unauthorised database access by separating code from data'
'\n\nOffers dedicated protection against SQL Injection attacks',

'Filtering and validating user input to prevent security vulnerabilities like XSS and SQL injection'
'\n\nOffers strong protection against Cross-Site Scripting (XSS), SQL Injection and other code injection attacks'
'\n\nPrevents malicious code execution and protects data integrity by ensuring only safe and expected input is processed'
'\n\nOffers dedicated protection against XSS Attacks and moderate protection against SQL Injection attacks',

'Dividing a network into isolated sections to limit the spread of cyber threats'
'\n\nOffers strong containment against Worms, Ransomware, and Lateral Movement attempts, limiting the impact of a breach'
'\n\nReduces the attack surface and improves threat detection by enforcing granular access controls'
'\n\nOffers dedicated protection against Worms and Privilege Escalation attacks and moderate protection against Ransomware, DDoS and Supply Chain attacks',

'Encrypting web traffic using TLS to protect data transmitted between users and websites'
'\n\nOffers strong protection against Man-in-the-Middle attacks and data interception'
'\n\nVerifies website authenticity and builds user trust by displaying a secure connection indicator'
'\n\nOffers dedicated protection against Man-in-the-Middle attacks and Session Hijacking',

'A security model where no entity, inside or outside the network, is automatically trusted'
'\n\nOffers strong protection against insider threats, lateral movement, data breaches, and sophisticated, persistent attacks'
'\n\nEnforces granular access control and enforces continuous verification for all users and devices'
'\n\nOffers dedicated protection against Supply Chain attacks and strong protection against majority of cyber attacks, but is difficult and expensive to maintain',

'Storing backups in a geographically separate location to ensure data recovery after disasters'
'\n\nOffers maximum protection against data loss from natural disasters and large-scale cyberattacks like ransomware'
'\n\nEnsures business continuity, facilitates disaster recovery, and provides resilience against geographically targeted threats'
'\n\nOffers dedicated protection against Ransomware',

'Protects web applications from multiple cyber threats and API abuse'
'\n\nOffers maximum protection against web application-specific attacks like SQL Injection, XSS and other OWASP Top 10 vulnerabilities'
'\n\nInspects HTTP/S traffic at the application layer, filters malicious requests, and provides real-time threat intelligence for web-facing assets'
'\n\nOffers moderate protection against DDoS, SQL Injection, XSS, Supply Chain attacks and Worms'
]

training_questions = ['You receive an email from your bank asking you to "confirm your account details" via a link\n What should you do?',
                      'Which of the following is the most secure password?',
                      'What should you do when leaving your desk?',
                      'Someone calls claiming to be IT support and asks for your password to “fix an urgent issue”\n What should you do?',
                      'You find an unknown USB stick on your work desk\n What should you do?',
                      'Which URL is safest to enter sensitive information?']

training_answers = [
    ['Immediately click the link and proceed to update your details', 'Forward the email to several contacts to circulate a warning', 'Move the email to your junk or trash folder', 'Independently contact the bank using their official, known contact information to verify the request'],
    ['Password123', 'cupcake7', 'Th!5_i5_4_pWD!', 'QWERTY123'],
    ['Minimise all active windows on your screen', 'Leave your session open if you intend to return shortly', 'Simply turn off the monitor display', 'Lock your computer screen or fully log out of your session'],
    ['Provide them with your password to facilitate a quick resolution', 'Request that they send an official email to confirm their identity and request', 'Politely decline their request and report the incident through official channels', 'Change your password immediately after disclosing it to them'],
    ['Submit it to your IT department for proper inspection and handling', 'Insert it into your computer to try and identify the owner', 'Utilise it as additional personal storage space', 'Leave it undisturbed where it was found'],
    ['http://secure-login.com', 'https://yourbank.com', 'https://y0ur64nk.com', 'https://www.freebankaccess.net/joiningbonus.exe']
]

training_q_response = ['Always verify suspicious requests directly with the organisation', 'A strong password includes symbols, numbers, and upper/lowercase characters',
                       'Locking prevents unauthorised access when you are away','Legitimate IT staff will never ask for your password',
                       'Unknown USBs may contain malware — report them to IT', 'Always look for HTTPS and a legitimate domain name']

training_answer_key = [3,2,3,2,0,1]

mfa_questions = [
    'What does MFA mean for your online accounts?',
    'Why is using MFA much safer than just a password?',
    'When using MFA, what is an example of "something you have"?',
    'If you get an MFA message on your phone that you did NOT ask for, what should you do?',
    'You get a new phone. What is the best way to handle your MFA apps on the old and new phones?',
    'What should you do if your phone, which you use for MFA, is lost or broken?'
]

mfa_answers = [
    ['Requiring two distinct usernames for login', 'Demanding multiple verification methods beyond a password to confirm identity', 'Enforcing the use of exceptionally long and complex passwords', 'Restricting account access solely to pre-approved network connections'],
    ['It automatically generates a password that is inherently unguessable', 'It necessitates the successful presentation of more than one independent authentication factor', 'It creates an automatic backup of all associated digital files', 'It initiates automatic session encryption upon login'],
    ['Your unique biological characteristic (e.g., fingerprint)', 'Your date of birth', 'A one-time security code delivered to your mobile device', 'Your preferred colour setting'],
    ['Expeditiously approve the authentication request', 'Disregard the unexpected notification', 'Decline the authentication request and promptly report the incident to your IT or security team', 'Attempt to deduce the reason for the unsolicited message'],
    ['Continue to use the old mobile device indefinitely', 'Migrate your MFA authenticator applications to the new device and reconfigure them for the respective accounts', 'Temporarily disable MFA until the complete transition to the new phone is finalised', 'Dispose of the old mobile device without data migration'],
    ['Cease using that online account permanently', 'Contact the service provider\'s support department or utilise pre-generated backup codes', 'Inform your team and establish a new temporary account', 'Repeatedly attempt to guess the security code until successful']
]

mfa_q_response = [
    "MFA means Multi-Factor Authentication, where you use your password *plus* at least one other method (like a code from your phone) to prove it's really you",
    "MFA is safer because even if a hacker steals your password, they still need the second thing (like your phone or fingerprint) to get into your account",
    "'Something you have' refers to a physical item only you possess, like a security code sent to your phone, a physical security key, or a token generator",
    "If you get an MFA message you didn't ask for, you should deny it immediately and report it to your IT support or security team, as someone might be trying to hack into your account",
    "The best practice is to transfer your MFA apps and re-register them on your new phone and then remove them from the old device to keep your security strong",
    "If you lose access to your MFA phone, you should contact the service's support desk immediately or use any backup codes you were given when you set up MFA"
]

mfa_answer_key = [1,1,2,2,1,1]

ids_questions = [
    'Imagine your computer system suddenly showing many failed login attempts for a special "admin" account late at night. What might be happening?',
    'If a "guest" user on a computer tries to open a file that stores passwords, what is wrong with that activity?',
    'Someone tries to log into an account, failing 5 times in just 10 seconds. What could this rapid failure suggest?',
    'Think of your computer as a house. What is it called when someone quickly tries to knock on all your "doors" (ports) to see which ones are open?',
    'If "Bob" (who is not "Alice") opens "Alice\'s private financial report" file, why might a security system flag this?',
    'Suddenly, a huge amount of data is sent *out* of your company\'s network to a strange place on the internet. What is the biggest concern here?'
]

ids_answers = [
    ['There was a scheduled system maintenance', 'The admin account was accidentally locked', 'Someone is attempting a brute-force attack', 'A new security patch was deployed'],
    ['The file might be corrupted', 'The guest user is exploring system files', 'Guest users lack authorisation for sensitive data', 'The system is undergoing an audit'],
    ['The user is typing too fast', 'An automated attack is attempting to compromise the account', 'There is a network connectivity issue', 'The account has been temporarily suspended'],
    ['A "port scan" to identify vulnerabilities', 'A "network performance test"', 'A "firewall configuration check"', 'A "service availability probe"'],
    ['Alice granted Bob access previously', 'Bob is an authorised auditor', 'Unauthorised access to a private document', 'The file permissions are misconfigured'],
    ['Increased network traffic due to updates', 'Legitimate cloud synchronisation is occurring', 'Potential data exfiltration', 'Testing of a new backup system']
]

ids_q_response = [
    "Many failed login attempts, especially for a powerful account like 'admin' and at unusual times, often means someone is trying to guess the admin password or break in (a brute-force attempt)",
    "A guest user trying to open a password file is highly suspicious because guest users should not be accessing sensitive system files. This indicates an unauthorised attempt to gain control",
    "Many rapid login failures usually point to a brute-force attack, where a computer program is quickly trying different passwords to get into an account",
    "When someone quickly tries to check all your computer's \"doors\" (ports) to see which are open, it's called a 'port scan', a common first step for hackers looking for weaknesses",
    "It's suspicious because Bob shouldn't access Alice's private financial file. Security systems flag this to prevent unauthorised viewing or stealing of private information",
    "A large amount of data unexpectedly leaving the network is the biggest concern for Data Exfiltration, which means important company data might be stolen by an attacker"
]

ids_answer_key = [2,2,1,0,2,2]

firewall_questions = [
    'What is the primary purpose of a firewall?',
    'Where is a firewall typically located to protect a home network?',
    'If a firewall is blocking a program, what is it usually preventing?',
    'What does "ALLOW" mean in a firewall rule?',
    'What is the main difference between a firewall and an antivirus program?',
    'In firewall terms, what does "OUTBOUND" traffic refer to?'
]

firewall_answers = [
    ['To optimise system performance', 'To regulate network communication', 'To manage software installations', 'To encrypt local files'],
    ['Between your local network and the public internet', 'Integrated within your application software', 'On a remote cloud server', 'As part of your computer\'s display unit'],
    ['The program from launching', 'The program from altering system settings', 'The program from accessing your local storage', 'The program from establishing external connections'],
    ['To enable data transmission matching the rule', 'To prevent any network activity', 'To disable specific application features', 'To generate system logs'],
    ['They serve identical security functions', 'One protects hardware, the other protects software', 'A firewall monitors network traffic; an antivirus detects and removes malware', 'A firewall enhances internet speed; an antivirus organises files'],
    ['Data flowing within your local area network', 'Data originating from your network destined for external networks', 'Data entering your network from an external source', 'Data exchanged between different applications on the same device']
]

firewall_q_response = [
    "A firewall acts as a security barrier, checking and controlling data coming into and going out of your network or computer to keep it safe from threats.",
    "Firewalls are usually placed at the boundary between your internal network (like your home devices) and the external network (the internet) to filter traffic before it reaches your devices.",
    "A firewall's core function is to enforce security policies by stopping traffic that doesn't meet its rules, often blocking suspicious attempts to access your system.",
    "The 'ALLOW' action in a firewall rule means that any network traffic matching that rule's criteria will be permitted to pass through the firewall.",
    "A firewall controls what data goes in and out of your network, acting as a gatekeeper, while antivirus software scans for and removes malicious programs already on your device.",
    "Outbound traffic means data that is attempting to leave your computer or network and go to an external destination on the internet."
]

firewall_answer_key = [1, 0, 3, 2, 3, 1]

rate_limiting_questions = [
    'What is the main purpose of "rate limiting" on a website or app?',
    'If a website suddenly gets thousands of requests per second from many different computers, what kind of attack is likely happening that rate limiting could help with?',
    'A website has a rule: "No more than 100 actions per minute from one person". If someone tries to do 150 actions in that minute, what usually happens?',
    'How is "rate limiting" different from a "firewall" that blocks bad stuff?',
    'Which of these is a good real-world example of what "rate limiting" does?',
    'How can rate limiting help protect against a very big flood of internet traffic (a DDoS attack)?'
]

rate_limiting_answers = [
    ['To enhance the website\'s visual appeal', 'To prevent excessive requests and resource exhaustion', 'To encrypt all user data by default', 'To accelerate page rendering speed'],
    ['Malware propagation', 'A SQL injection attempt', 'A Distributed Denial of Service (DDoS) attack', 'Credential stuffing'],
    ['All 150 actions are processed immediately', 'The initial 100 actions are permitted, and subsequent ones are restricted or deferred', 'The user receives an automated notification', 'The user account is permanently suspended'],
    ['A firewall filters traffic based on defined rules, whereas rate limiting manages the volume of requests over time', 'A firewall operates exclusively on incoming internet traffic, while rate limiting handles outgoing traffic', 'Rate limiting solely guards against malware infections', 'A firewall is primarily for data encryption'],
    ['A security check of luggage at an airport entrance', 'A controlled flow system, like a single-lane bridge with traffic lights', 'Duplicating critical documents for archiving', 'Securing all entry points to a building overnight'],
    ['It optimises the internet connection bandwidth', 'By mitigating or blocking an overwhelming volume of requests from one or multiple sources', 'By displaying customised alerts to the perpetrator', 'By ensuring continuous website uptime through redundant servers']
]

rate_limiting_q_response = [
    "The main purpose of rate limiting is to stop hackers or abusive users from sending too many requests too quickly, which can overwhelm a website or app",
    "A massive flood of requests from many computers at once is the signature of a Distributed Denial of Service (DDoS) attack. Rate limiting helps by blocking or slowing down these overwhelming requests",
    "If a person tries to send more actions than allowed by rate limiting, only the first 100 actions are allowed, and the rest are blocked or delayed, protecting the website from overload",
    "A firewall often blocks or allows specific types of traffic or traffic from certain sources entirely, while rate limiting controls how *much* activity is allowed from a source within a given time, letting some legitimate traffic through but stopping excessive amounts",
    "A good example of rate limiting is a traffic light letting only a certain number of cars go through each minute, preventing traffic jams and keeping the flow controlled",
    "Rate limiting helps against a DDoS attack by slowing down or blocking too many requests that come in too quickly, whether from a single source or many, preventing the website from being overwhelmed"
]

rate_limiting_answer_key = [1,2,1,0,1,1]

e2ee_questions = [
    'What is the main purpose of End-to-End Encryption (E2EE)?',
    'How is E2EE different from simply encrypting information only when it travels on the internet?',
    'Which of these popular messaging apps is famous for using E2EE by default (meaning it\'s always on)?',
    'What action by a cloud service provider would break true End-to-End Encryption for your files?',
    'Even with E2EE, what kind of information about your messages can a service provider often still see?',
    'What is the super important role of "encryption keys" in E2EE?'
]

e2ee_answers = [
    ['To minimise server latency', 'To accelerate data transfer rates', 'To guarantee message confidentiality between communicating parties', 'To facilitate content moderation by service providers'],
    ['E2EE ensures data remains encrypted from the sender\'s device to the recipient\'s device, unlike transport encryption which only protects data in transit', 'There is no functional distinction between the two methods', 'E2EE does not involve any form of encryption', 'E2EE is exclusively for data decryption during retrieval'],
    ['X (formerly Twitter)', 'Instagram', 'Reddit', 'WhatsApp'],
    ['Storing data exclusively in encrypted archive formats', 'Possessing the capability to reset user passwords and restore encrypted data', 'Utilising a Virtual Private Network (VPN) during data upload', 'Implementing multi-factor authentication for account access'],
    ['Your physical address details', 'The precise content of your communications', 'Your account access credentials', 'Metadata such as timestamps and recipient information'],
    ['They compress message size to conserve bandwidth', 'They identify the geographical location of the server', 'They are cryptographic values essential for scrambling and unscrambling messages', 'They contribute to an improved internet connection speed']
]

e2ee_q_response = [
    "The main purpose of E2EE is to ensure that only the sender and the intended receiver can read the message, making it unreadable to anyone else, even the service provider",
    "E2EE is different because it encrypts the message all the way from you to the person you're sending it to, meaning the message stays scrambled and secret even on the service provider's servers, not just while it's moving",
    "WhatsApp (along with apps like Signal) is well-known for using E2EE by default for its messaging, keeping conversations private",
    "If a cloud provider can reset your password and recover your encrypted files, it means they hold the keys, which breaks the 'end-to-end' privacy of E2EE",
    "Even with E2EE, service providers can often still see message metadata, like when and to whom you sent a message, but not what the message actually says",
    "In E2EE, encryption keys are like secret codes that are used to scramble (encrypt) your message so no one else can read it, and then unscramble (decrypt) it for the intended recipient"
]

e2ee_answer_key = [2,0,3,1,3,2]

vpn_questions = [
    'What is the main reason people use a VPN?',
    'When people talk about a VPN creating a "tunnel," what do they mean?',
    'What is a big risk if you use a totally free VPN service?',
    'Why is it a really good idea to use a VPN when you connect to public Wi-Fi (like in a coffee shop)?',
    'Which of these tasks can a VPN *not* do?',
    'Which of these is a common and secure way that VPNs connect?'
]

vpn_answers = [
    ['To enhance web page loading speed', 'To secure and anonymise online communication', 'To automatically block all advertisements', 'To improve online gaming latency'],
    ['A method for secure file storage and sharing', 'A concealed web portal for private messaging', 'A secure, encrypted link between your device and a remote server', 'A mechanism to regulate internet traffic flow'],
    ['It may compromise your data privacy by selling usage information', 'It consistently provides extremely slow internet access', 'It exclusively utilises outdated security protocols', 'It frequently causes system instability and crashes'],
    ['Because public Wi-Fi typically offers inherent security features', 'Because VPNs can bypass public Wi-Fi password authentication', 'Because VPNs safeguard your data from eavesdropping on unencrypted public networks', 'Because public Wi-Fi boosts VPN connection speeds'],
    ['To encrypt your network traffic', 'To bypass geographical content restrictions', 'To detect and eliminate malicious software from your device', 'To mask your actual IP address'],
    ['SecureNet VPN', 'OpenVPN', 'RapidTunnel VPN', 'BasicLink VPN']
]

vpn_q_response = [
    "The main reason people use a VPN is to hide their online activity and keep their internet safe and private by encrypting their data and hiding their real location",
    "A VPN \"tunnel\" refers to a secure, encrypted connection between your device and the VPN server, which protects your internet traffic from being spied on",
    "A big risk with free VPNs is that they often might sell your internet activity data to other companies to make money, defeating the purpose of privacy",
    "It's smart to use a VPN on public Wi-Fi because these networks are often unsecured, and VPNs prevent hackers from secretly watching what you do or stealing your information",
    "A VPN's job is to secure your internet connection, but it cannot scan your computer for viruses and remove them; that's what antivirus software does",
    "OpenVPN is one of the most common, secure, and widely used ways that VPNs connect, known for its strong encryption"
]

vpn_answer_key = [1,2,0,2,2,1]

acc_lockout_questions = [
    'What is the main reason a website or app has an "account lockout" rule?',
    'What kind of attack is "account lockout" trying to stop the most?',
    'If a company sets an "account lockout threshold" to 5, what does that mean?',
    'Which of these is like what "account lockout" does?',
    'What does "account lockout duration" mean?',
    'What is a common problem if an account lockout rule is too strict?'
]

acc_lockout_answers = [
    ['To enforce regular password changes', 'To automatically deny access after a specified number of failed login attempts', 'To purge inactive user accounts', 'To enhance password memorability for users'],
    ['A phishing expedition', 'A system-wide malware infection', 'Repeated, automated password guessing (Brute-force attack)', 'Network traffic interception'],
    ['The password must be updated every 5 weeks', 'The account is archived after 5 days of inactivity', 'The account will be temporarily suspended after 5 incorrect password entries', 'Users are required to maintain an active session for a minimum of 5 minutes daily'],
    ['Daily wardrobe changes', 'Inability to enter your residence after several attempts with an incorrect key', 'Self-addressing a postal delivery', 'Disabling your wireless internet connection overnight'],
    ['The minimum required password length', 'The duration an account remains inaccessible following excessive incorrect login attempts', 'The period before an account is permanently deactivated', 'The estimated time required to input your password'],
    ['Legitimate users inadvertently losing access to their accounts', 'A reduction in overall internet speed', 'A significant increase in password complexity', 'The unintentional deletion of crucial data from the system']
]

acc_lockout_q_response = [
    "The main reason for account lockout is to automatically block access after too many wrong login tries, stopping hackers from guessing passwords over and over",
    "Account lockout is mainly designed to prevent a Brute-force attack, where a hacker repeatedly tries different passwords until they find the right one",
    "If the 'account lockout threshold' is 5, it means the account will automatically lock after 5 wrong password attempts in a row, to protect it",
    "Account lockout is like getting locked out of your house after trying the wrong key too many times; it stops further attempts to get in",
    "Account lockout duration means how long the account stays blocked (locked) after a user has made too many wrong password attempts",
    "A common problem with overly strict lockout rules is that people can get accidentally locked out of their own accounts if they just mistype their password a few times"
]

acc_lockout_answer_key = [1,2,2,1,1,0]

lpa_questions = [
    'What does the rule "Least Privileged Access" mean in computer security?',
    'A person at the front desk (receptionist) is given full access to everyone\'s salary information. Which security rule is being broken?',
    'Why is the idea of "least privilege" so important for keeping computers safe?',
    'If someone is a computer administrator (has high power), what should they do when they are *not* doing admin tasks?',
    'Regularly checking what each user can access (their permissions) is an example of what kind of security practice?',
    'What is "privilege creep" in computer security?'
]

lpa_answers = [
    ['Granting universal access to all system resources', 'Promoting password sharing among colleagues', 'Providing users with the minimum necessary permissions to perform their duties', 'Restricting users to viewing only public information'],
    ['The "Confidentiality" principle', 'The "Data Duplication" principle', 'The "Least Privilege" principle', 'The "Information Disclosure" principle'],
    ['It optimises system processing speed', 'It simplifies software installation procedures', 'It minimises the potential impact of a security breach on an compromised account', 'It enables all users to view comprehensive data sets'],
    ['Maintain continuous login as the administrative user', 'Deactivate their elevated administrative credentials', 'Transition to a standard user account with reduced privileges', 'Access confidential files using their administrative permissions'],
    ['A method for improving internet bandwidth', 'A routine scan for malicious software', 'Verification of historical data backups', 'Regular review and verification of user access rights'],
    ['When malicious actors acquire administrative permissions', 'When users gradually accumulate more access rights than their current role necessitates', 'When obsolete access permissions are automatically revoked', 'When system administrators log out prematurely']
]

lpa_q_response = [
    "The rule of Least Privileged Access (LPA) means giving users only the access they absolutely need for their job, and no more, to reduce risks",
    "Giving a receptionist full access to payroll information breaks the 'Least Privilege' principle because they don't need that access for their job",
    "Least privilege is important because if a hacker breaks into an account with limited powers, it limits the damage a hacker can do, as they can only access what that low-power account can",
    "According to LPA, an admin should switch to a regular user account with fewer powers when they are not actively doing admin tasks, reducing the risk if their account gets hacked",
    "Regularly checking user access levels is an example of Access control auditing, which helps ensure people don't keep access they no longer need",
    "'Privilege creep' happens when users slowly gain more access rights than they truly need for their job over time, often because their roles change but old permissions are not removed"
]

lpa_answer_key = [2,2,2,2,3,1]

param_queries_questions = [
    'Which type of information that a user types in is most likely to cause an SQL injection problem if it\'s not cleaned up?',
    'If someone types `admin\' OR \'1\'=\'1` into a login box, what does this usually suggest they are trying to do?',
    'How do "parameterised queries" help protect a website from SQL injection attacks?',
    'Which of these ways of handling user input makes an SQL injection attack *most* likely?',
    'Which common computer programming languages can use parameterised queries?',
    'In simple terms, what are "prepared statements" when we talk about SQL?'
]

param_queries_answers = [
    ['Their contact phone number', 'Their primary email address', 'The alphanumeric password they enter', 'Input provided in a username or search field on a web form'],
    ['An unintentional data entry error', 'An attempt to exploit a database vulnerability using an SQL injection technique', 'A user\'s forgotten login credentials', 'An internal script processing malfunction'],
    ['By encrypting the entire web application codebase', 'By strictly segregating the structured query language commands from user-supplied data inputs', 'By optimising the website\'s data loading performance', 'By disallowing all user-originated SQL commands'],
    ['Employing input validation and sanitisation routines', 'Validating that user input conforms to expected numeric types', 'Concatenating user-supplied strings directly into database queries', 'Standardising all database command syntax to lowercase'],
    ['Predominantly older programming languages such as Fortran', 'Common contemporary languages like Python, PHP, and Java', 'Only highly specialised database query languages', 'Most widely used modern programming languages support this feature'],
    ['Database backup and recovery files', 'Pre-compiled SQL statements designed to securely integrate user data', 'Raw SQL commands manually composed by a developer', 'Cascading Style Sheet (CSS) files for web page styling']
]

param_queries_q_response = [
    "A username field in a login form is very likely to be targeted because attackers try to use SQL injection to bypass authentication and get into accounts",
    "Typing `admin' OR '1'='1` is a classic SQL injection attempt trying to trick the database into thinking the login condition is always true, allowing access without the correct password",
    "Parameterised queries protect against SQL injection by keeping the special SQL commands and the user's typed text strictly separate, so the database knows what is a command and what is just data",
    "Directly mixing what the user types with the database commands (called string concatenation) is the practice that makes SQL injection most likely, as it allows malicious code to become part of the command",
    "All of the above (most modern languages) like Python, PHP, Java, C#, and many others, support parameterised queries through their database connection tools",
    "Prepared statements are like SQL commands that are set up in advance by the programme. They have special placeholders for user input, ensuring that the input is treated as data, not as part of the command, making it very safe"
]

param_queries_answer_key = [3,1,1,2,3,1]

input_sanitisation_questions = [
    'What exactly is "Cross-Site Scripting" (XSS) in simple terms?',
    'If a hacker types things within a <script> tag into a comment box on a website causing abnormal behaviour, what is this a clear sign of?',
    'What does "input sanitisation" mean when you are dealing with what users type into a website?',
    'Which part of a website is most likely to be open to an XSS attack if it\'s not careful?',
    'What is a really good way for website builders to stop XSS attacks?',
    'Can XSS attacks happen even on secure websites that use HTTPS (the one with the lock icon)?'
]

input_sanitisation_answers = [
    ['A technique for archiving browser navigation history', 'A vulnerability allowing malicious scripts to be injected into web pages and executed in other users\' browsers', 'A method designed to accelerate web page loading times', 'A protocol for bypassing network firewalls'],
    ['A complex computational error within the website\'s logic', 'An attempt to circumvent login credentials', 'A clear indication of a Cross-Site Scripting (XSS) attack', 'A simple typographical error by the user'],
    ['Converting textual data into an abstract binary format', 'The process of filtering or neutralising potentially harmful characters and code from user-submitted data', 'Transforming all entered text to lowercase characters', 'Encrypting all data transmitted between web pages'],
    ['Authentication forms for user logins', 'Interactive elements such as search fields and user comment sections', 'Web pages exclusively displaying static image content', 'The digital certificates used for website authentication'],
    ['Increasing the server\'s Random Access Memory (RAM)', 'Enhancing the website\'s internet connection speed', 'Rigorous validation and neutralisation (filtering or encoding) of user-generated content before display', 'Distributing password storage across multiple data centres'],
    ['Only if the website is utilising an outdated security protocol', 'Yes, if the website fails to adequately process and render user input securely', 'No, as HTTPS inherently prevents all forms of XSS exploitation', 'Only when accessing the website via a Virtual Private Network (VPN)']
]

input_sanitisation_q_response = [
    "XSS (Cross-Site Scripting) is a method where hackers secretly put bad code (scripts) into a website that then runs in other users' web browsers when they visit that page",
    "Typing the <script> tag into a comment box is a clear sign of an XSS (Cross-Site Scripting) attack attempt, as it tries to make your browser run the hacker's code",
    "Input sanitisation means removing or cleaning up harmful characters and code from what users type into a website, so their input can't be used for attacks",
    "Website search bars and comment sections are most likely open to XSS because they take what a user types and often show it directly back on the page, which can be exploited if not careful",
    "A really good way to stop XSS attacks is to carefully check and clean (filter or encode) what users type into forms before that information is displayed on the website",
    "Yes, XSS attacks can happen even on secure HTTPS websites if the website doesn't properly clean up user input before displaying it. HTTPS encrypts traffic but doesn't stop malicious code from running in your browser"
]

input_sanitisation_answer_key = [1,2,1,1,2,1]

net_segmentation_questions = [
    'What does "network segmentation" mean?',
    'Why is dividing a network into smaller parts considered a good security idea?',
    'Which of these is a good everyday example of what network segmentation does?',
    'How does something called a "VLAN" (Virtual LAN) help with splitting up a network?',
    'What is a big risk if a network is *not* properly divided (segmented)?',
    'What kind of device is usually put between different parts of a segmented network to control who can talk to whom?'
]

net_segmentation_answers = [
    ['The implementation of network-wide data encryption', 'The partitioning of a computer network into distinct, isolated sub-networks', 'The creation of redundant network infrastructure backups', 'The deployment of endpoint antivirus solutions on all devices'],
    ['It facilitates the automated deactivation of dormant user accounts', 'It simplifies routine network administration tasks for IT personnel', 'It restricts the lateral movement of malware or threats in the event of a breach', 'It prevents the majority of unsolicited commercial emails (spam)'],
    ['Granting universal access privileges to all building occupants', 'The architectural design of a large building with compartmentalised, access-controlled areas', 'Maintaining all entry points to a dwelling in an open state', 'Securing your wireless router with adhesive tape when not in use'],
    ['It enhances the overall internet throughput for all connected devices', 'It allows for the logical grouping of devices into isolated broadcast domains, irrespective of their physical connectivity', 'It establishes secure wireless communication channels', 'It restricts internet access for specific user profiles'],
    ['A malicious attack or compromise can rapidly propagate throughout the entire network infrastructure', 'Users will encounter an excessive number of passwords to manage', 'The overall internet connection speed will significantly decrease', 'Computer IP addresses will be subject to frequent changes'],
    ['A device that distributes network traffic across multiple servers', 'A server that translates domain names into IP addresses', 'A simple networking device that connects multiple computers', 'A security device or rule-set (e.g., Firewall or ACL) governing inter-segment traffic']
]

net_segmentation_q_response = [
    "Network segmentation means dividing a computer network into smaller, separate sections. This limits how information flows between different parts of the network",
    "Dividing a network is good because it helps stop bad software (malware) from spreading everywhere if one part of the network gets infected. It contains the damage",
    "A good everyday example is separating rooms in a big house with locked doors and rules about who can enter each room. If one room has a problem, it doesn't easily spread to others",
    "A VLAN (Virtual LAN) helps with segmentation by grouping devices logically into isolated mini-networks, even if those devices are physically connected to the same equipment. It keeps their traffic separate",
    "A big risk of a poorly divided network is that a virus or other threat can spread easily and quickly across the *whole* network once it gets into one computer",
    "In a segmented network, a Firewall or Access Control List (ACL) is typically placed between segments. These are like security checkpoints that control who can talk to whom and what kind of information can pass"
]

net_segmentation_answer_key = [1,2,1,1,0,3]

https_questions = [
    'What is the main thing HTTPS provides that regular HTTP does not?',
    'What does the "S" in HTTPS mean?',
    'Which special way of scrambling information (protocol) does HTTPS use to keep your data private?',
    'How can you usually tell if a website you\'re visiting is using HTTPS and is therefore more secure?',
    'Why is it super important for websites where you log in (like online banking or email) to use HTTPS?',
    'What happens if a website\'s HTTPS security certificate has run out or is not valid?'
]

https_answers = [
    ['Enhanced website performance', 'Encrypted data transmission between client and server', 'The capability to download complimentary software', 'More aesthetically pleasing website layouts'],
    ['Script', 'Server', 'Speed', 'Secure'],
    ['HyperText Markup Language (HTML)', 'File Transfer Protocol (FTP)', 'Simple Mail Transfer Protocol (SMTP)', 'Transport Layer Security/Secure Sockets Layer (TLS/SSL)'],
    ['A prominent padlock symbol is displayed in the browser\'s address bar', 'The website consistently loads at a significantly faster rate', 'Numerous unsolicited pop-up alerts are presented', 'The textual content of the website appears in red'],
    ['It improves the website\'s visibility in search engine results', 'It automatically suppresses all intrusive pop-up advertisements', 'It ensures the confidentiality and integrity of sensitive information like credentials during transmission', 'It enables the website to send a greater volume of electronic mail'],
    ['The website will continue to function but with considerably reduced performance', 'Your web browser will issue a security warning regarding the website\'s trustworthiness', 'The website will automatically revert to an unencrypted HTTP connection', 'All stored browser cookies for the website will be automatically purged']
]

https_q_response = [
    "The main thing HTTPS provides is encrypted communication between your browser and the website's server, meaning your data is scrambled so others can't easily read it",
    "The 'S' in HTTPS stands for Secure, indicating that the connection is protected using encryption technologies",
    "HTTPS uses TLS/SSL (Transport Layer Security/Secure Sockets Layer) to encrypt data, keeping it private as it travels between your computer and the website",
    "You can usually tell a website is using HTTPS because a padlock icon appears in the browser's address bar, often next to the website address",
    "Using HTTPS is super important for login pages because it keeps your passwords and personal information scrambled (encrypted) during transmission, preventing hackers from stealing them if they're listening",
    "If a website's HTTPS security certificate is expired or invalid, your web browser will show a warning message, telling you the site might not be secure and advising against proceeding"
]

https_answer_key = [0,3,3,0,2,1]

zta_questions = [
    'What is the main idea behind the "Zero Trust" security model?',
    'Which everyday example best explains how Zero Trust works?',
    'In a Zero Trust system, how do people usually get permission to use computer files or systems?',
    'What happens in a Zero Trust system if it notices something unusual or suspicious happening with a user?',
    'Why is using Multi-Factor Authentication (MFA) so important in a Zero Trust security setup?',
    'What part does the security health of a computer or phone (its "security posture") play in Zero Trust?'
]

zta_answers = [
    ['It automatically grants access to all internal network users', 'It relies on implicit trust for all users by default', 'It operates on the principle of "never trust, always verify," even within the network perimeter', 'It exclusively focuses on preventing external threats to the corporate network'],
    ['Distributing a single master key to all employees', 'Rigorous identity and context verification for every access attempt to any resource', 'Allowing unrestricted movement within a facility once initial entry is granted', 'Granting access based solely on occupational attire'],
    ['Every user is automatically granted access to all potentially required resources', 'Access is dynamically determined by user identity, device attributes, and current contextual factors', 'Permissions are assigned based on a user\'s historical activities', 'All resources are publicly accessible, with subsequent monitoring of actions'],
    ['The user\'s account is immediately terminated from the system', 'The system automatically elevates the user\'s access privileges', 'The system may trigger re-authentication challenges or temporarily restrict access', 'The system merely logs the unusual behaviour for retrospective analysis'],
    ['It eliminates the necessity for user credentials', 'It mandates multiple forms of verification to confirm user identity, reducing reliance on a single factor', 'It automates the process of password resets', 'It prevents user accounts from being subjected to lockout policies'],
    ['The device\'s network address is the sole determinant for access', 'Devices must comply with predefined security standards to be granted access', 'Zero Trust primarily secures the overarching network infrastructure, not individual endpoints', 'It is predominantly concerned with distinguishing between human and automated access attempts']
]

zta_q_response = [
    "The main idea of Zero Trust is to assume no one should be trusted by default, even inside the company's network. Every access request is verified",
    "Zero Trust is best explained by checking everyone's ID and what they want to do *every time* they try to enter *any* room, not just at the front door",
    "In Zero Trust, permission to use resources is usually given based on who the person is, what device they are using, and what they are doing right now, not just once when they first log in",
    "If unusual behavior is detected in a Zero Trust system, the system might ask the user to verify themselves again or block their access to protect information",
    "Multi-Factor Authentication (MFA) is crucial in Zero Trust because it makes sure that proving who you are doesn't depend on just one thing, adding layers of security for verification",
    "In Zero Trust, computers and phones must meet certain security rules (their 'security posture') to be allowed access, ensuring only healthy devices can connect to important resources"
]

zta_answer_key = [2,1,1,2,1,1]

offshore_backup_questions = [
    'What does "offshore data backup" usually mean for a company\'s information?',
    'Why do companies sometimes choose to store their important data backups in a different country?',
    'What is a possible risk or problem with storing data backups in another country?',
    'Before sending important company data backups to another country, what should you definitely do to the data?',
    'How is storing data "offshore" different from just using a regular "cloud backup" service?',
    'What is a really good practice for companies that use offshore data backups?'
]

offshore_backup_answers = [
    ['Storing data on submerged computer systems', 'Relocating data backups to a geographical location outside the primary operating country', 'Transmitting digital files to an offshore oil platform', 'Maintaining data on ship-borne servers'],
    ['To gain tax advantages in an alternative jurisdiction', 'To ensure business continuity and disaster recovery resilience', 'Due to a lack of confidence in domestic IT infrastructure', 'To conserve local storage capacity on company computers'],
    ['The operational costs associated with power consumption and storage infrastructure might be elevated', 'Expedited data retrieval in emergency scenarios might be challenging', 'Divergent data protection and privacy regulations in the foreign jurisdiction could apply', 'There is a risk of permanent data loss or inaccessibility'],
    ['Convert all data files into a portable document format (PDF)', 'Implement robust encryption to render the data unintelligible to unauthorised parties', 'Store the data in an unencrypted archive file (e.g., a basic ZIP)', 'Transmit the data as attachments via electronic mail'],
    ['"Offshore" denotes the data\'s physical or legal residency in a foreign nation, whereas "cloud" broadly refers to internet-based storage services', 'Offshore backups are invariably maintained in an entirely disconnected state', 'Cloud backup operations are exclusively conducted during non-business hours', 'Offshore backup policies mandate automatic file deletion after a 30-day period'],
    ['Only back up non-sensitive or publicly available information', 'Periodically conduct restoration tests to verify data integrity and accessibility from the offshore site', 'Prioritise the lowest cost country for data storage without other considerations', 'Document backup procedures only once every few years']
]

offshore_backup_q_response = [
    "Offshore data backup usually means storing data backups in a different country than where the company is located",
    "Companies use offshore data backups to ensure their business can keep working if a disaster happens (like a flood or fire) in their local area, providing a safe copy far away",
    "A possible risk is that the privacy rules (laws) for data might be different in that other country, which could affect how your data is protected",
    "Before sending backups offshore, you should definitely encrypt the data so it's scrambled and unreadable to anyone who isn't supposed to see it, keeping it safe during transit and storage",
    "'Offshore' specifically refers to the data's physical or legal location in another country, while 'cloud backup' is just about storing data online; a cloud backup *can* be offshore",
    "A really good practice for offshore backups is to regularly test that they can get their data back from the offshore location, to make sure the backups actually work when needed"
]

offshore_backup_answer_key = [1,1,2,1,0,1]

waf_questions = [
    'What is the main job of a Web Application Firewall (WAF)?',
    'How is a WAF different from a regular firewall you might have at home?',
    'Which of these common attacks on websites can a WAF help stop?',
    'Where is a WAF usually placed in the network setup?',
    'Which special setting lets a WAF watch for bad activity without actually blocking anything?',
    'If a WAF sees text like "SELECT * FROM users" in a search box, what will it likely do?'
]

waf_answers = [
    ['To restrict internal employee internet access', 'To intercept unsolicited email communications', 'To secure web-facing applications by filtering malicious HTTP traffic', 'To prevent hardware failures in computer systems'],
    ['A WAF functions exclusively in an offline environment', 'A WAF specifically analyses and protects web application layer protocols and content', 'A WAF is solely responsible for filtering data from USB-connected devices', 'A WAF only operates in conjunction with physical network firewalls'],
    ['Deceptive social engineering tactics', 'Visual eavesdropping (shoulder surfing)', 'SQL injection and Cross-site scripting (XSS) vulnerabilities', 'Unauthorised physical entry (tailgating)'],
    ['Within the end-user\'s web browser application', 'Immediately behind the origin web server hosting the application', 'Positioned between internet clients and the web application they are attempting to access', 'Directly integrated into the web application\'s primary database system'],
    ['Observation or learning mode', 'Covert operation mode', 'Encrypted tunnel mode', 'Non-blocking analytical mode'],
    ['It will display the text directly on the website interface', 'It will disregard the input and forward the request without modification', 'It will attempt to execute that string as a database command', 'It will identify and impede the request due to its suspicious nature']
]

waf_q_response = [
    "A WAF's main job is to filter and protect web applications from bad internet requests by sitting in front of them and checking all traffic",
    "A WAF is different because it understands and protects specific parts of websites (like forms, logins, and comments), looking deep into web traffic, unlike regular firewalls that mostly block by IP address or port",
    "A WAF can help stop common website attacks like SQL injection (trying to trick databases) and Cross-site scripting (XSS) (injecting bad code into web pages)",
    "A WAF is usually placed between internet users and the web application they are trying to reach, acting as a guard for the website",
    "The Learning/Monitor mode lets a WAF watch all traffic and identify potential threats without actually blocking anything. This helps fine-tune its rules",
    "If a WAF sees suspicious text like 'SELECT * FROM users' in a search box, it will likely flag or block it because it looks like an attempt to hack the database"
]

waf_answer_key = [2,1,2,2,0,3]