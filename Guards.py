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

training_answers = [['Click the link and update details immediately','Forward it to your friends to warn them','Delete the email','Contact the bank through official channels to verify'],
                    ['Password123','cupcake7','Th!5_i5_4_pWD!','QWERTY123'],
                    ['Minimise all windows','Leave it open if you are quick','Turn off the monitor','Lock the screen or log out'],
                    ['Give them the password to fix it quickly','Ask them to send an official email','Refuse and report the incident','Change your password after telling them'],
                    ['Take it to IT for inspection','Plug it in to find the owner','Use it for extra storage','Leave it where it was'],
                    ['http://secure-login.com','https://yourbank.com','https://y0ur64nk.com','https://www.freebankaccess.net/joiningbonus.exe']]

training_q_response = ['Always verify suspicious requests directly with the organisation', 'A strong password includes symbols, numbers, and upper/lowercase characters',
                       'Locking prevents unauthorised access when you are away','Legitimate IT staff will never ask for your password',
                       'Unknown USBs may contain malware — report them to IT', 'Always look for HTTPS and a legitimate domain name']

training_answer_key = [3,2,3,2,0,1]

mfa_questions = [
    'What does MFA mean for your online accounts?',
    'Why is using MFA much safer than just a password?',
    'When using MFA, what is an example of "something you have"?',
    'If you get an MFA message on your phone that you did NOT ask for, what should you do?',
    'You get a new phone. What\'s the best way to handle your MFA apps on the old and new phones?',
    'What should you do if your phone, which you use for MFA, is lost or broken?'
]

mfa_answers = [
    ['Using only a username','Using a password and something else to prove it\'s you','Using a very long password','Only logging in from home'],
    ['It makes your password impossible to guess','It requires more than one way to prove who you are, making it harder for hackers','It creates a backup of all your files','It makes your internet connection faster'],
    ['Your fingerprint','Your birthday','A security code sent to your phone','Your favorite color'],
    ['Approve the message quickly','Ignore the message and hope it goes away','Deny the message and tell your IT support or security team','Try to guess what caused the message'],
    ['Keep using the old phone forever','Transfer your MFA apps to the new phone and set them up again','Turn off MFA on all your accounts','Throw away the old phone without checking anything'],
    ['Stop using that online account forever','Contact the service\'s support or use a backup code if you have one','Buy a brand new phone number','Try to guess the security code until it works']
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
    'If a "guest" user on a computer tries to open a hidden file that stores passwords, what\'s wrong with that activity?',
    'Someone tries to log into an account, failing 5 times in just 10 seconds. What could this rapid failure suggest?',
    'Think of your computer as a house. What is it called when someone quickly tries to knock on all your "doors" (ports) to see which ones are open?',
    'If "Bob" (who is not "Alice") opens "Alice\'s private financial report" file, why might a security system flag this?',
    'Suddenly, a huge amount of data is sent *out* of your company\'s network to a strange place on the internet. What is the biggest concern here?'
]

ids_answers = [
    ['The computer is running slow','The admin forgot their password','Someone is trying to guess the admin password or break in','The internet is temporarily down'],
    ['The file is too big','The guest user is trying to make friends','Guest users should not be accessing sensitive system files','The user is just trying to delete old files'],
    ['The user is typing too fast','Someone is trying to guess the password over and over (a brute-force attack)','The keyboard is broken','The system is asking for a new password'],
    ['A "port scan" to find open weaknesses','A "data backup"','A "network speed test"','A "software update"'],
    ['Alice shared the file correctly','Bob is just curious','It\'s suspicious because Bob shouldn\'t access Alice\'s private file','The file is very old'],
    ['The internet bill will be higher','The network is just being tested','Important company data might be stolen (Data Exfiltration)','A new printer is being installed']
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
    ['To make your computer run faster','To block unwanted network traffic','To organize your computer files','To create backup copies of your data'],
    ['Between your home network and the internet','Inside your CPU','Decided by your ISP','Far away on a different server to protect your device'],
    ['The program from starting','The program from saving files','The program from closing','The program from connecting to the internet'],
    ['Downloading updates for the game','Making your computer quieter','Blocking the game\'s connection to the internet','Changing the game\'s graphics settings'],
    ['They both do exactly the same job','An antivirus is for old computers, a firewall is for new ones','A firewall fixes viruses, an antivirus blocks websites','A firewall controls network traffic, an antivirus deals with malicious software on your computer'],
    ['Traffic that stays inside your network','Traffic leaving your network to the internet','Traffic coming into your network','Traffic between two websites']
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
    ['To make the website look nicer','To stop hackers from sending too many requests too quickly','To encrypt all information sent by users','To speed up how fast pages load'],
    ['A virus spreading','A Brute Force attack','A big flood of traffic (DDoS attack)','Someone trying to steal passwords'],
    ['All 150 actions are allowed','Only the first 100 actions are allowed, and the rest are blocked or delayed','The person gets a warning message','The person is immediately banned from the website'],
    ['A firewall blocks specific bad users, while rate limiting controls how *much* activity is allowed','A firewall only works for incoming internet, rate limiting for outgoing','Rate limiting only protects against viruses','A firewall always encrypts data'],
    ['Checking someone\'s bag before they enter a building','A traffic light letting only a certain number of cars go through each minute','Making a copy of important documents','Locking all doors at night'],
    ['It makes the internet connection faster','By slowing down or blocking too many requests from one source or many sources','By showing special warnings to the hacker','By making sure the website is always online']
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
    ['Preventing server overload','Speeding up data transmission','Ensuring only the sender and receiver can read the message','Allowing companies to monitor communication'],
    ['E2EE encrypts the message all the way from you to the person you\'re sending it to, not just while it\'s traveling','There is no difference between the two','E2EE doesn\'t encrypt at all','E2EE only encrypts data during download'],
    ['X/Twitter','Instagram','Reddit','WhatsApp'],
    ['Storing only encrypted ZIP files','Allowing the provider to reset your password and recover your files','Using a VPN while uploading','Using two-factor authentication'],
    ['Your home address','The exact content of your messages','Your password','When and to whom you sent a message'],
    ['They compress the message to save space','They identify the server\'s location','They are like secret codes used to scramble and unscramble messages','They make your internet connection faster']
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
    ['To make their internet much faster','To hide their online activity and keep their internet safe and private','To block all ads on every website','To play games better online'],
    ['A way to store files securely','A hidden webpage for secret messages','A secure, encrypted connection between your device and the VPN server','A way to slow down internet traffic'],
    ['It might sell your internet activity data to other companies','It will always give you very slow internet speeds','It uses very old security methods','It will make your computer crash often'],
    ['Because public Wi-Fi is already very secure','Because VPNs can find the password for public Wi-Fi','Because VPNs stop hackers from secretly watching what you do on unsecured networks','Because public Wi-Fi helps the VPN connect faster'],
    ['Encrypt your internet traffic','Help you access websites that are blocked in your country','Scan your computer for viruses and remove them','Hide your real internet address (IP address)'],
    ['ClosedVPN','OpenVPN','SlowVPN','BasicVPN']
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
    ['To make passwords expire faster','To automatically block access after too many wrong login tries','To delete old user accounts that are not used','To make users remember their passwords better'],
    ['A phishing scam','A virus infection','A hacker trying to guess the password many times (Brute-force attack)','Someone secretly listening to your connection'],
    ['The password must be changed every 5 weeks','The account is deleted after 5 days of not being used','The account will lock after 5 wrong password attempts','Users must stay logged in for at least 5 minutes a day'],
    ['Changing your clothes every day','Getting locked out of your house after trying the wrong key too many times','Posting a letter to yourself','Turning off your Wi-Fi at night'],
    ['How long your password must be','How long the account stays blocked after too many wrong tries','The time before your account is permanently deleted','The time it takes to type your password'],
    ['People getting accidentally locked out of their own accounts','The internet becomes slower','Passwords become much stronger','Important information gets lost from the computer']
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
    ['Giving users access to everything','Letting everyone share their passwords','Giving users only the access they absolutely need for their job','Allowing users to see only non-secret information'],
    ['The "Availability" principle','The "Redundancy" principle','The "Least Privilege" principle','The "Need-to-Know" principle'],
    ['It makes computers run faster','It makes it easier to install software','It limits the damage a hacker can do if they break into an account','It allows all users to see everything'],
    ['Stay logged in as the powerful admin all the time','Delete their special admin login','Switch to a regular user account with fewer powers','Browse secret files using their admin powers'],
    ['A way to speed up the internet','A type of virus scan','Checking for old backups','Access control auditing'],
    ['When hackers steal admin powers','When users slowly gain more access rights than they truly need for their job','When old permissions are automatically removed','When administrators log out too quickly']
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
    ['Their phone number','Their email address','The password they type in','Text typed into a username box on a login form'],
    ['A typo or typing mistake','An attempt to get in using an SQL injection trick','They forgot their password','A calculation error in the website\'s code'],
    ['By encrypting the website\'s code','By keeping the special SQL commands and the user\'s typed text strictly separate','By making the website load faster','By blocking all SQL commands from users'],
    ['Using special tools to clean up user input','Always checking if the user input is a number when it should be','Directly mixing what the user types with the database commands','Making sure all database commands are in lowercase'],
    ['Only old languages like Fortran','Python, PHP, and Java','Only very specific database languages','All of the above (most modern languages)'],
    ['Database backup files','SQL commands that are set up in advance to handle user input safely','Just regular SQL commands typed by a developer','Text files used for making websites look nice']
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
    'If a hacker types `<script>alert(\'Hacked!\')</script>` into a comment box on a website, what is this a clear sign of?',
    'What does "input sanitisation" mean when you\'re dealing with what users type into a website?',
    'Which part of a website is most likely to be open to an XSS attack if it\'s not careful?',
    'What is a really good way for website builders to stop XSS attacks?',
    'Can XSS attacks happen even on secure websites that use HTTPS (the one with the lock icon)?'
]

input_sanitisation_answers = [
    ['A way to backup browser history','A method to secretly put bad code into a website that runs in other users\' browsers','A technique to make web pages load faster','A firewall bypass method'],
    ['A math problem for the website','A forgotten password attempt','A clear attempt at an XSS (Cross-Site Scripting) attack','A typing error'],
    ['Converting text to a special code that only computers understand','Removing or cleaning up harmful characters and code from what users type','Changing all typed words to lowercase','Encrypting all information sent across webpages'],
    ['Login forms','Website search bars and comment sections','Pages that only show pictures','The website\'s security certificates'],
    ['Increase the computer\'s memory','Make the website\'s internet faster','Carefully check and clean (filter or encode) what users type before showing it on the website','Store passwords in multiple places'],
    ['Only if the website is very old','Yes, if the website doesn\'t properly clean up user input','No, HTTPS always blocks all XSS attacks','Only if you use a VPN to access the website']
]

input_sanitisation_q_response = [
    "XSS (Cross-Site Scripting) is a method where hackers secretly put bad code (scripts) into a website that then runs in other users' web browsers when they visit that page",
    "Typing `<script>alert(\'Hacked!\')</script>` into a comment box is a clear sign of an XSS (Cross-Site Scripting) attack attempt, as it tries to make your browser run the hacker's code",
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
    ['Encrypting all internet traffic','Dividing a computer network into smaller, separate sections','Creating extra backup copies of the network','Installing an antivirus program on every computer'],
    ['It automatically disables inactive user accounts','It makes administration easier for IT staff','It helps stop bad software (malware) from spreading everywhere if one part is attacked','It prevents most unwanted emails (phishing)'],
    ['Giving everyone keys to every door in a building','Separating rooms in a big house with locked doors and rules about who can enter each room','Always leaving all doors and windows open in a house','Taping off your Wi-Fi router when it\'s not being used'],
    ['It boosts the internet speed for all devices','It lets you group devices logically into isolated mini-networks, even if they\'re physically close','It provides secure wireless connections','It stops internet access for certain users'],
    ['A virus or other threat can spread easily and quickly across the *whole* network','Users will have too many passwords to remember','The internet connection will become very slow','Computer IP addresses will change too often'],
    ['A Load balancer','A DNS server','A Hub or a basic Switch','A Firewall or Access Control List (ACL)']
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
    ['Encrypted communication between your browser and the website\'s server','Faster loading times for web pages','The ability to download free software','More colourful website designs'],
    ['Script','Server','Speed','Secure'],
    ['HTML','FTP (File Transfer Protocol)','SMTP (Simple Mail Transfer Protocol)','TLS/SSL (Transport Layer Security/Secure Sockets Layer)'],
    ['A padlock icon appears in the browser\'s address bar','The website loads much faster than usual','It will have many pop-up warnings','The website\'s text will turn red'],
    ['It helps search engines find the website faster','It automatically blocks all pop-up ads','It keeps your passwords and personal information scrambled (encrypted) as you send them','It allows the website to send you more emails'],
    ['The website will still load normally but very slowly','Your web browser will show a warning message about the site not being secure','The website will automatically switch to HTTP connections','All your website cookies will be automatically deleted']
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
    ['It assumes everyone inside the network is automatically safe','It trusts all users by default, but checks their internet speed','It assumes no one should be trusted by default, even inside the company\'s network','It only blocks people from outside the company'],
    ['Giving the master key to just one employee','Checking everyone\'s ID and what they want to do *every time* they try to enter *any* room','Letting everyone walk freely inside a building once they get past the front door','Trusting anyone who wears a uniform'],
    ['Everyone automatically gets access to everything they might ever need','Access is given based on who they are, what device they are using, and what they are doing right now','Permission is given based on what they did last week','All resources are open to everyone, but their actions are recorded later'],
    ['The user\'s account is immediately deleted','The user automatically gets more permissions','The system might ask for re-verification or block access','The system just records the behavior to look at later'],
    ['It stops the need for usernames','It makes sure that proving who you are doesn\'t depend on just one thing (like only a password)','It automatically resets passwords','It prevents accounts from being locked out'],
    ['The computer\'s IP address is the most important thing','Computers and phones must meet certain security rules to be allowed access','Zero Trust mainly focuses on securing the entire network, not individual devices','It\'s mostly about checking if the user is a human or a robot']
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
    ['Storing data on computers that are underwater in the ocean','Storing data backups in a different country','Transferring files to an oil rig in the sea','Storing data on servers that are on ships'],
    ['To avoid paying taxes in their home country','To make sure their business can keep working if a disaster happens where they are','Because they don\'t trust their own IT people','To save space on their own computers'],
    ['The cost of electricity and storage might be higher','It might be harder to get the data back quickly','The privacy rules (laws) for data might be different in that other country','You might accidentally lose access to the data forever'],
    ['Convert all the data files into PDF format','Encrypt the data so it\'s scrambled and unreadable to others','Store them in a basic ZIP file without a password','Send them as attachments in an email'],
    ['"Offshore" specifically refers to the data\'s physical or legal location in another country, while "cloud" is just about storing it online','Offshore backups are always kept completely offline','Cloud backups only happen during non-working hours','Offshore backups automatically delete files after 30 days'],
    ['Only back up information that is not sensitive','Regularly test that they can get their data back from the offshore location','Only use the cheapest country available for storage','Only write down the backup steps once every few years']
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
    ['To stop internal employees from using the internet','To block unwanted emails','To filter and protect web applications from bad internet requests','To prevent computer hard drives from failing'],
    ['A WAF only works offline','A WAF understands and protects specific parts of websites (like forms)','A WAF only filters USB devices connected to computers','A WAF only works with physical firewall boxes'],
    ['Social engineering (tricking people)','Shoulder surfing (looking over someone\'s shoulder)','SQL injection and Cross-site scripting (XSS)','Tailgating (sneaking into a building)'],
    ['Inside the user\'s web browser','Behind the main server that hosts the website','Between internet users and the web application they are trying to reach','Directly inside the website\'s main database'],
    ['Learning/Monitor mode','Stealth Mode','Tunnel mode','Passive Mode'],
    ['It will print the text directly on the website','It will ignore it and forward the request as is','It will try to run that command on the database','It will flag or block it because it looks suspicious']
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