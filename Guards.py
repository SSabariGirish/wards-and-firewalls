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
    ['P4s5word13', 'cupcake7', 'Th!5_i5_4_pWD!', 'QWERTY123'],
    ['Minimise all active windows on your screen', 'Leave your session open if you intend to return shortly', 'Turn off the monitor display no matter how short your break is', 'Lock your computer screen or fully log out of your session'],
    ['Provide them with your password to facilitate a quick resolution', 'Request that they send an official email to confirm their identity and request', 'Politely decline their request and report the incident through official channels', 'Change your password immediately after disclosing it to them'],
    ['Submit it to your IT department for proper inspection and handling', 'Insert it into your computer to try and identify the owner', 'Utilise it as additional personal storage space if the USB has the company logo on it', 'Leave it undisturbed where it was found since it is none of your business'],
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
    [
        'Requiring users to enter two completely separate passwords to access a single account',
        'Demanding multiple verification methods beyond a password to confirm identity', 
        'Mandating that all account passwords meet advanced complexity requirements set by the administrator',
        'Limiting login permissions to devices connected to a specific, pre-authorized Wi-Fi network'
    ],
    [
        'It works by automatically generating a new, complex password for every single login attempt',
        'It necessitates the successful presentation of more than one independent authentication factor', 
        'It verifies your login location against a list of approved countries before granting access',
        'It activates a proprietary encryption method for all data transferred during your online session'
    ],
    [
        'A specific biometric identifier, such as a retinal scan or your unique voiceprint pattern',
        'A pre-selected security question answer that you established during account setup',
        'A one-time security code delivered to your mobile device', 
        'Your personal device name that you registered when you first created the online account'
    ],
    [
        'Approve the request immediately to see which service it is from, then change that password',
        'Take no action on the notification; it is likely a system error that will resolve itself',
        'Decline the authentication request and promptly report the incident to your IT or security team', 
        'Investigate your account\'s login history to try and match the time of the unauthorized request'
    ],
    [
        'Keep the old phone powered on and connected to Wi-Fi solely for receiving MFA codes',
        'Migrate your MFA authenticator applications to the new device and reconfigure them for the respective accounts', 
        'Turn off MFA on all accounts before starting the phone transfer, then re-enable it afterwards to ensure a smooth transition',
        'Factory reset the old phone, which automatically transfers MFA authentications to the new device'
    ],
    [
        'Abandon the account and create a new one with a different email to ensure your security',
        'Contact the service provider\'s support department or utilise pre-generated backup codes', 
        'Wait for your mobile carrier to issue a new SIM card, which will automatically restore MFA access',
        'Systematically try every possible code combination, as most systems do not lock you out'
    ]
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
    [
        'A standard system maintenance script is running its nightly checks',
        'The system is verifying the administrator\'s password against a central server',
        'Someone is attempting a brute-force attack',
        'A recently installed security update is testing account credentials'
    ],
    [
        'The password file itself has likely become corrupted or is unreadable',
        'The guest account is performing a routine scan of system directories',
        'Guest users lack authorisation for sensitive data',
        'An automated auditing tool is checking the integrity of security files'
    ],
    [
        'The user likely has their keyboard\'s caps lock function enabled by mistake',
        'An automated attack is attempting to compromise the account',
        'A poor network connection is causing login data packets to be lost',
        'The user\'s account has been flagged for a mandatory password reset'
    ],
    [
        'A "port scan" to identify vulnerabilities',
        'A "network latency check" to measure connection response times',
        'A "firewall rule verification" for security policy compliance',
        'A "service heartbeat query" to ensure a system is still online'
    ],
    [
        'The system assumes Bob has temporary, delegated permissions from Alice',
        'Bob\'s user role has special privileges for financial auditing tasks',
        'Unauthorised and suspicious access to a private document',
        'The file\'s access control list has been improperly configured by IT'
    ],
    [
        'A large operating system update',
        'A scheduled off-site synchronisation',
        'Potential data exfiltration',
        'A routine company-wide cloud backup'
    ]
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
    [
        'To speed up the transfer of data across the network',
        'To regulate network communication',
        'To automatically update vulnerable software applications',
        'To encrypt files on the hard drive to prevent unauthorised access'
    ],
    [
        'Between your local network and the public internet',
        'Directly within the operating system\'s core kernel files',
        'On a dedicated server hosted by your internet service provider',
        'Inside the computer\'s central processing unit (CPU) for speed'
    ],
    [
        'The application from starting up or executing on the system',
        'The program from modifying critical system registry entries',
        'The program from reading or writing any files on the hard drive',
        'The program from establishing external connections'
    ],
    [
        'To enable data transmission matching the rule',
        'To temporarily halt all network traffic for a security scan',
        'To restrict an application to its most basic, core functions',
        'To create a detailed log entry for every permitted connection'
    ],
    [
        'A firewall is the modern term for what used to be antivirus software',
        'A firewall is for hardware protection, while antivirus is for software',
        'A firewall monitors network traffic; an antivirus detects and removes malware',
        'A firewall organises packets, while an antivirus cleans up temporary files'
    ],
    [
        'Information exchanged exclusively between devices on your local Wi-Fi',
        'Data originating from your network destined for external networks',
        'Connection requests initiated from the internet towards your computer',
        'Communication between two separate programmes running on a single device'
    ]
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
    [
        'To automatically adjust the website layout for mobile devices',
        'To prevent excessive requests and resource exhaustion',
        'To encrypt the connection between the user and the server',
        'To reduce the file size of images for faster loading times'
    ],
    [
        'An attempt to spread a computer virus to website visitors',
        'A targeted attack to steal data from the website\'s database',
        'A Distributed Denial of Service (DDoS) attack',
        'An automated attempt to log in using stolen usernames and passwords'
    ],
    [
        'All 150 actions are placed in a queue and processed in order',
        'The initial 100 actions are permitted, and subsequent ones are restricted or deferred',
        'The system sends an email warning the user about their activity',
        'The user\'s account is immediately and permanently banned from the service'
    ],
    [
        'A firewall filters traffic based on defined rules, whereas rate limiting manages the volume of requests over time',
        'A firewall inspects the content of data, while rate limiting only counts the number of requests',
        'Rate limiting is a software solution, whereas a firewall is always a dedicated piece of hardware',
        'A firewall prevents unauthorised access, while rate limiting authenticates user identities'
    ],
    [
        'A thorough inspection of every person entering a secure building',
        'A controlled flow system, like a single-lane bridge with traffic lights',
        'Making multiple backup copies of a house key for different family members',
        'Locking all doors and windows of a shop after it has closed for the day'
    ],
    [
        'By re-routing all incoming traffic through a much faster internet connection',
        'By mitigating or blocking an overwhelming volume of requests from one or multiple sources',
        'By identifying the attacker\'s location and reporting it directly to the authorities',
        'By automatically creating copies of the website on multiple servers to handle the load'
    ]
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
    [
        'To reduce the delay when sending messages across long distances',
        'To make video calls and file transfers significantly faster',
        'To guarantee message confidentiality between communicating parties',
        'To help service providers automatically scan messages for spam'
    ],
    [
        'E2EE ensures data remains encrypted from the sender\'s device to the recipient\'s device',
        'E2EE is the commercial term for standard transport encryption found on most websites',
        'E2EE uses data compression to hide information, rather than using any actual encryption',
        'E2EE is a method used only to decrypt data, while another system handles the encryption'
    ],
    [
        'X (formerly Twitter)',
        'Instagram',
        'Reddit',
        'WhatsApp'
    ],
    [
        'Storing your files within a single, large encrypted container on their servers',
        'Possessing the capability to reset user passwords and restore encrypted data',
        'Requiring users to connect via a specific VPN to upload or download their files',
        'Forcing all users to secure their accounts with multi-factor authentication (MFA)'
    ],
    [
        'The home address you used when you first registered for the account',
        'The exact text, images, and attachments included within the message',
        'Your login username, password, and any associated security questions',
        'Metadata such as timestamps and recipient information'
    ],
    [
        'They are used to reduce the overall size of messages to save data',
        'They are used to verify which country the service provider\'s servers are in',
        'They are cryptographic values essential for scrambling and unscrambling messages',
        'They help to find the fastest route for your messages across the internet'
    ]
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
    [
        'To increase the download speed of large files from the internet',
        'To secure and anonymise online connections and communication',
        'To act as a system-wide filter that automatically blocks online ads',
        'To get a faster and more stable connection to online game servers'
    ],
    [
        'A hidden folder on your computer for storing sensitive files securely',
        'A special private browser that is only accessible to active VPN users',
        'A secure, encrypted link between your device and a remote server',
        'A system that prioritises video streaming traffic over other data'
    ],
    [
        'It may compromise your data privacy by selling usage information',
        'They are required by law to have slower connection speeds than paid services',
        'They often use much weaker encryption standards compared to paid VPNs',
        'They are well-known for causing conflicts with other security software'
    ],
    [
        'Because coffee shops are legally required to offer secure, encrypted Wi-Fi',
        'Because a VPN allows you to use the Wi-Fi without needing the password',
        'Because VPNs safeguard your data from eavesdropping on unencrypted public networks',
        'Because public networks are configured to give VPN users a faster connection'
    ],
    [
        'To scramble your internet data so that other people cannot read it',
        'To make it appear you are in another country for streaming content',
        'To detect and eliminate malicious software from your device',
        'To hide your device\'s unique online identifier from visited websites'
    ],
    [
        'DataTunnel',
        'OpenVPN',
        'SecureLink',
        'NetGuard'
    ]
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
    [
        'To force users to create a new, more secure password on a monthly basis',
        'To automatically deny access after a specified number of failed login attempts',
        'To automatically delete accounts that have not been used for a long period',
        'To provide hints and memory aids to users who have forgotten their passwords'
    ],
    [
        'An attempt to trick users into revealing their sensitive login details',
        'The spread of a malicious virus or worm across the entire network',
        'Repeated, automated password guessing (Brute-force attack)',
        'Secretly listening to data being sent between a user and a website'
    ],
    [
        'A user must choose a new password for their account every 5 weeks',
        'The account is automatically hidden from public view after 5 days of inactivity',
        'The account will be temporarily suspended after 5 incorrect password entries',
        'A user will be logged out if their account is inactive for over 5 minutes'
    ],
    [
        'Having a rule that you must wear a different outfit every day of the week',
        'Inability to enter your residence after several attempts with an incorrect key',
        'Writing your own address on a parcel that you are also sending to yourself',
        'Setting your home Wi-Fi router to turn off automatically every single night'
    ],
    [
        'The total number of characters that a user\'s password must contain',
        'The duration an account remains inaccessible following excessive incorrect login attempts',
        'The amount of time before an unused account is permanently deleted forever',
        'The average time it should take a person to correctly type their password'
    ],
    [
        'Legitimate users inadvertently losing access to their accounts',
        'The website or application loading much more slowly for all users',
        'The system forcing users to create much longer and harder passwords',
        'The accidental removal of important user files from the locked account'
    ]
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
    [
        'Giving every user the same high-level access to all company data',
        'Allowing team members to share account credentials for easier collaboration',
        'Providing users with the minimum necessary permissions to perform their duties',
        'Ensuring that most users can only ever access publicly available information'
    ],
    [
        'The "Data Integrity" principle',
        'The "Data Availability" principle',
        'The "Least Privilege" principle',
        'The "Password Complexity" principle'
    ],
    [
        'It significantly increases the overall processing speed of the computer system',
        'It makes the process of installing new approved software much more straightforward',
        'It minimises the potential impact of a security breach on a compromised account',
        'It ensures all employees have access to the data sets needed for transparency'
    ],
    [
        'Remain logged in with their administrative account for quick access later',
        'Temporarily disable their own admin account entirely before logging off',
        'Transition to a standard user account with reduced privileges',
        'Use their admin powers to browse through various sensitive company files'
    ],
    [
        'A policy for ensuring fair distribution of available internet bandwidth',
        'A scheduled process that checks all of the system\'s files for viruses',
        'A procedure to confirm that all historical data backups are working correctly',
        'Regular review and verification of user access rights'
    ],
    [
        'The process by which a hacker successfully gains administrative-level access',
        'When users gradually accumulate more access rights than their current role necessitates',
        'The automated system that removes permissions that are no longer required',
        'When an administrator logs out of the system before a critical task is complete'
    ]
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
    [
        'A phone number field that has been restricted to only numeric digits',
        'An email address that has been confirmed through a verification link',
        'A password field that is immediately hashed before being stored or checked',
        'Input provided in a username or search field on a web form'
    ],
    [
        'A common mistake made by users who are unfamiliar with the login process',
        'An attempt to exploit a database vulnerability using an SQL injection technique',
        'A failed attempt by a user to guess their own forgotten login details',
        'A server-side error where the login script is not working as intended'
    ],
    [
        'By using strong encryption to make the website\'s source code unreadable',
        'By strictly segregating the structured query language commands from user-supplied data inputs',
        'By pre-loading common data to make the website respond much more quickly',
        'By creating a blacklist of dangerous SQL keywords to block in user input'
    ],
    [
        'Using a special function to strip out any potentially harmful characters',
        'Checking that the user\'s input contains only numbers before processing it',
        'Concatenating user-supplied strings directly into database queries',
        'Converting all database commands and user input into a single case'
    ],
    [
        'Only older programming languages that were designed before the internet',
        'Only a single language, Java, as it was designed with security in mind',
        'Only languages specifically created for managing and querying databases',
        'Most widely used modern programming languages support this feature'
    ],
    [
        'The collection of files used to restore a database after a system crash',
        'Pre-compiled SQL statements designed to securely integrate user data',
        'Database commands that a developer types directly into the live system',
        'Files that control all the colours and layout of a website\'s pages'
    ]
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
    [
        'A method for securely backing up a user\'s complete web Browse history',
        'A vulnerability allowing malicious scripts to be injected into web pages and executed in other users\' browsers',
        'A web development technique that optimises images to make pages load much faster',
        'A special networking protocol designed to get around corporate firewall restrictions'
    ],
    [
        'A sign that the website\'s server has a significant bug in its programming logic',
        'A failed attempt by a hacker to incorrectly guess a user\'s login password',
        'A clear indication of a Cross-Site Scripting (XSS) attack',
        'A common typing mistake made by a user who is not familiar with HTML code'
    ],
    [
        'The automatic translation of all user-submitted text into a binary format',
        'The process of filtering or neutralising potentially harmful characters and code from user-submitted data',
        'A procedure that converts all text entered by users into a single consistent case',
        'Securing all information sent from the user\'s browser to the website\'s server'
    ],
    [
        'The username and password fields on the website\'s secure login page',
        'Interactive elements such as search fields and user comment sections',
        'A simple web page that only contains a static gallery of pictures',
        'The site\'s underlying SSL/TLS certificate that provides the padlock icon'
    ],
    [
        'Upgrading the website\'s server with a larger amount of physical memory (RAM)',
        'Buying a faster and more reliable internet connection for the web server',
        'Rigorous validation and neutralisation (filtering or encoding) of user-generated content before display',
        'Storing the database of user passwords across several different physical locations'
    ],
    [
        'Only if the website is using an older, insecure version of the HTTPS protocol',
        'Yes, if the website fails to adequately process and render user input securely',
        'No, because the encryption provided by HTTPS automatically blocks all malicious scripts',
        'Only if the user is connecting to the website through a misconfigured VPN service'
    ]
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
    [
        'The process of encrypting all data that travels across the network',
        'The partitioning of a computer network into distinct, isolated sub-networks',
        'The practice of having duplicate network equipment in case of a failure',
        'The installation of antivirus software on every computer on the network'
    ],
    [
        'It makes it easier to automatically disable user accounts that are inactive',
        'It reduces the complexity of day-to-day network management for engineers',
        'It restricts the lateral movement of malware or threats in the event of a breach',
        'It provides a powerful filter that blocks most incoming spam from reaching users'
    ],
    [
        'Giving every person a master key that can open every door in a building',
        'The architectural design of a large building with compartmentalised, access-controlled areas',
        'Leaving all the doors and windows of a house unlocked for easier access',
        'Placing strong tape over a router\'s ports to physically block their use'
    ],
    [
        'It works by increasing the maximum possible internet speed for all devices',
        'It allows for the logical grouping of devices into isolated broadcast domains, irrespective of their physical connectivity',
        'It is a technology used specifically for encrypting and securing Wi-Fi signals',
        'It allows administrators to block certain users from accessing the internet'
    ],
    [
        'A malicious attack or compromise can rapidly propagate throughout the entire network infrastructure',
        'Every user on the network will be forced to remember multiple complex passwords',
        'The internet connection for the entire organisation will become noticeably slower',
        'The IP address for every computer will need to be changed on a daily basis'
    ],
    [
        'A load balancer that spreads incoming requests evenly across web servers',
        'A Domain Name System (DNS) server that converts website names to IP addresses',
        'A basic network switch or hub used to connect computers in the same office',
        'A security device or rule-set (e.g., Firewall or ACL) governing inter-segment traffic'
    ]
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
    [
        'A noticeable improvement in the website\'s overall loading speed',
        'Encrypted data transmission between client and server',
        'The ability to download free programs and files from the site',
        'Access to higher quality graphics and more modern web designs'
    ],
    [
        'Script',
        'Server',
        'Speed',
        'Secure'
    ],
    [
        'HyperText Markup Language (HTML) for structuring web page content',
        'File Transfer Protocol (FTP) for uploading and downloading files',
        'Simple Mail Transfer Protocol (SMTP) for sending electronic mail',
        'Transport Layer Security/Secure Sockets Layer (TLS/SSL)'
    ],
    [
        'A prominent padlock symbol is displayed in the browser\'s address bar',
        'The website\'s pages will always load much more quickly than other sites',
        'A series of pop-up windows appear to confirm the site\'s security status',
        'All of the text and links on the website will be coloured bright green'
    ],
    [
        'It is a primary factor used by search engines to mark websites as legitimate',
        'It includes a built-in feature that blocks annoying pop-up adverts and reduces misinformation',
        'It ensures the confidentiality and integrity of sensitive information during transmission',
        'It allows the website\'s servers to send out a larger number of emails with ZERO packet loss'
    ],
    [
        'The website will still work correctly but will operate at a much slower speed',
        'Your web browser will issue a security warning regarding the website\'s trustworthiness',
        'The connection will automatically downgrade to the standard, unsecure HTTP version',
        'Your browser will immediately delete all of the saved cookies for that website'
    ]
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
    [
        'It is a model where anyone or any device already inside the company network is trusted',
        'It functions by assuming all users are trustworthy until they do something suspicious',
        'It operates on the principle of "never trust, always verify," even within the network perimeter',
        'It is a model that only focuses on building a strong wall against outside attackers'
    ],
    [
        'Giving every employee a single master key that opens every door in the building',
        'Rigorous identity and context verification for every access attempt to any resource',
        'Letting people go anywhere they want inside after showing their ID once at the door',
        'Allowing access to secure areas based only on the uniform a person is wearing'
    ],
    [
        'Users are given broad access to all the resources they might possibly need for their job',
        'Access is dynamically determined by user identity, device attributes, and current contextual factors',
        'Access is granted based on what a user has accessed most frequently in the past',
        'All data is made available to everyone, and security simply watches what people do'
    ],
    [
        'The user\'s account is permanently deleted from the system without any warning',
        'The system will automatically grant the user even more access and permissions',
        'The system may trigger re-authentication challenges or temporarily restrict access',
        'The system only makes a note of the behaviour for someone to review later on'
    ],
    [
        'It completely removes the need for users to have or remember any passwords',
        'It mandates multiple forms of verification to confirm user identity, reducing reliance on a single factor',
        'It is a system that automatically helps users reset their forgotten passwords',
        'It ensures a user\'s account can never be locked out after too many failed logins'
    ],
    [
        'Access is granted based only on the device\'s unique network IP address',
        'Devices must comply with predefined security standards to be granted access',
        'Zero Trust only cares about securing the main network, not individual devices',
        'Its main job is to figure out if a login attempt is from a human or a bot'
    ]
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
    [
        'Keeping secure copies of data in waterproof servers located under the sea',
        'Relocating data backups to a geographical location outside the primary operating country',
        'Sending encrypted data for storage on servers located on an oil rig at sea',
        'The practice of storing all critical company data on servers hosted on ships'
    ],
    [
        'To take advantage of lower business tax rates available in another country',
        'To ensure business continuity and disaster recovery resilience',
        'Because the internet infrastructure in their own country is not reliable',
        'To save disk space on their main computer systems at the head office'
    ],
    [
        'The cost of electricity and server maintenance is often much higher abroad',
        'It may take a very long time to retrieve all of the company\'s data in an emergency',
        'Divergent data protection and privacy regulations in the foreign jurisdiction could apply',
        'There is a higher chance the data could be permanently lost or accidentally deleted'
    ],
    [
        'Combine all of the company\'s data into a single, large PDF document file',
        'Implement robust encryption to render the data unintelligible to unauthorised parties',
        'Place all the files into a single ZIP archive without using any password protection',
        'Send all of the backup files as a series of attachments in multiple emails'
    ],
    [
        '"Offshore" denotes the data\'s physical or legal residency in a foreign nation, whereas "cloud" broadly refers to internet-based storage services',
        'Offshore backups must be stored on systems that are never connected to the internet',
        'Cloud backup services are only allowed to run their backup jobs during the night',
        'Offshore backup services are legally required to delete all stored data every 30 days'
    ],
    [
        'Only send data that is not confidential or is already available to the public',
        'Periodically conduct restoration tests to verify data integrity and accessibility from the offshore site',
        'Always choose the country that offers the cheapest data storage, regardless of other factors',
        'Update the official documentation for the backup process only once every five years'
    ]
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
    [
        'To control which websites employees are allowed to visit from the office',
        'To scan incoming emails and block any that are identified as spam',
        'To secure web-facing applications by filtering malicious HTTP traffic',
        'To monitor server hardware and predict when components are likely to fail'
    ],
    [
        'A WAF is designed to protect computers that are not connected to the internet',
        'A WAF specifically analyses and protects web application layer protocols and content',
        'A WAF\'s only job is to scan for viruses on any connected USB flash drives',
        'A WAF cannot function properly unless connected to a traditional hardware firewall'
    ],
    [
        'An attacker tricking an employee into revealing their password over the phone',
        'Spear Phishing, Mass Phishing and Main-in-the-Middle vulnerabilities',
        'SQL injection and Cross-site scripting (XSS) vulnerabilities',
        'An unauthorised person following an employee through a secure office door'
    ],
    [
        'As a plugin or extension installed directly inside the user\'s web browser',
        'On the internal network, monitoring traffic after it has left the web server',
        'Positioned between internet clients and the web application they are attempting to access',
        'As part of the database software, checking queries just before they are run'
    ],
    [
        'Observation or learning mode',
        'Stealth blocking mode',
        'Secure traffic mode',
        'Passive analysis mode'
    ],
    [
        'It will treat the input as a normal search term and pass it to the website',
        'It will ignore the suspicious text and allow the request to proceed unchanged',
        'It will try to run the text as a command directly on its own database system',
        'It will identify and impede the request due to its suspicious nature'
    ]
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