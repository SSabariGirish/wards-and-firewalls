import random


def roll_d20():
    # Returns a random integer between 1 and 20
    return random.randint(1, 20)


class Thief:
    def __init__(self):
        self.guild_gold = 15
        self.has_access = False
        self.weaknesses_found = 0

        # Failure Countdown
        self.extreme_wounds = 0
        self.phishing_countdown = 0
        self.walls_countdown = 0
        self.ratcaller_countdown = 0
        self.knaves_countdown = 0
        self.bnb_countdown = 0
        self.blade_countdown = 0
        self.grain_countdown = 0
        self.pestilence_countdown = 0

        # List of Cards Drawn
        self.card_headers_medieval = [thief_attack_header_medieval[0], thief_attack_header_medieval[1]]
        self.card_explanations_medieval = [thief_attack_explanation_medieval[0], thief_attack_explanation_medieval[1]]
        self.card_headers_real_life = [thief_attack_header_real_life[0], thief_attack_header_real_life[1]]
        self.card_explanations_real_life = [thief_attack_explanation_real_life[0], thief_attack_explanation_real_life[1]]
        self.card_cost = [thief_attack_cost[0], thief_attack_cost[1]]
        self.card_img = [thief_image_list[0], thief_image_list[1]]
        self.rl_card_img = [thief_rl_image_list[0], thief_rl_image_list[1]]

    def snake_effect(self, scribe_training, twin):
        if self.phishing_countdown > 0:
            self.phishing_countdown += 2
            return False
        print('Rolling D20..... \n\n')
        roll_val = roll_d20()
        print(f'You have rolled: {roll_val} \n\n')
        if scribe_training > 0 and twin > 0:
            if roll_val > 19:
                self.has_access = True
                self.weaknesses_found += 1
                return True
            else:
                self.phishing_countdown += 2
                return False
        elif scribe_training > 0:
            if roll_val > 16:
                self.has_access = True
                self.weaknesses_found += 1
                return True
            else:
                self.phishing_countdown += 2
                return False
        else:
            if roll_val > 10:
                self.has_access = True
                self.weaknesses_found += 1
                return True
            else:
                self.phishing_countdown += 2
                return False

    def alehouse_effect(self, scribe_training, twin):
        if self.phishing_countdown > 0:
            self.phishing_countdown += 2
            return False

        print('Rolling D20..... \n\n')
        roll_val = roll_d20()
        print(f'You have rolled: {roll_val} \n\n')

        if scribe_training > 0 and twin > 0:
            if roll_val > 19:
                self.has_access = True
                self.weaknesses_found += 1
                return True
            else:
                self.phishing_countdown += 2
                return False
        elif scribe_training > 0:
            if roll_val > 16:
                self.has_access = True
                self.weaknesses_found += 1
                return True
            else:
                self.phishing_countdown += 2
                return False
        else:
            if roll_val > 5:
                self.has_access = True
                self.weaknesses_found += 1
                return True
            else:
                self.phishing_countdown += 2
                return False

    def loose_wall_effect(self, gargoyles, flames, doctrine):

        if not self.has_access or self.walls_countdown > 0:
            self.walls_countdown += 5
            if not self.has_access:
                print('You tried to loosen the walls from the OUTSIDE!!! \n')
            return False

        print('Rolling D20..... \n\n')
        roll_val = roll_d20()
        print(f'You have rolled: {roll_val} \n\n')

        if gargoyles > 0 or flames > 0 or doctrine > 0:

            if roll_val > 12:
                self.weaknesses_found += 1
                self.has_access = True
                self.guild_gold += 25
                return True
            else:
                self.walls_countdown += 5
                return False
        else:
            if roll_val > 6:
                self.weaknesses_found += 1
                self.has_access = True
                self.guild_gold += 25
                return True
            else:
                self.walls_countdown += 5
                return False

    def brats_effect(self, flames, crier, gargoyles, bastion, walls, doctrine):
        print('Rolling D20..... \n\n')
        roll_val = roll_d20()
        print(f'You have rolled: {roll_val} \n\n')
        if crier > 0:
            if roll_val > 19:
                self.weaknesses_found += 1
                return True
            else:
                return False
        elif flames > 0 or bastion > 0 or  walls > 0:
            if roll_val > 15:
                self.weaknesses_found += 1
                return True
            else:
                return False
        elif gargoyles > 0 or doctrine > 0:
            if roll_val > 7:
                self.weaknesses_found += 1
                return True
            else:
                return False
        else:
            self.weaknesses_found += 1
            return True

    def ratcaller_effect(self, borough, gargoyles, flames, squire, walls, doctrine, scribe_training):
        if self.ratcaller_countdown > 0:
            self.ratcaller_countdown += 5
            return False

        print('Rolling D20..... \n\n')
        roll_val = roll_d20()
        print(f'You have rolled: {roll_val} \n\n')
        if borough > 0:
            if roll_val > 19:
                self.weaknesses_found += 1
                return True
            else:
                self.ratcaller_countdown += 5
                return False
        elif gargoyles > 0 or flames > 0 or squire > 0 or walls > 0 or doctrine > 0:
            if roll_val > 15:
                self.weaknesses_found += 1
                return True
            else:
                self.ratcaller_countdown += 5
                return False
        elif scribe_training > 0:
            if roll_val > 7:
                self.weaknesses_found += 1
                return True
            else:
                self.ratcaller_countdown += 5
                return False
        else:
            self.weaknesses_found += 1
            return True

    def knave_effect(self,  cipher, tunnels, vanguard):
        if self.knaves_countdown > 0:
            self.knaves_countdown += 10
            return False

        print('Rolling D20..... \n\n')
        roll_val = roll_d20()
        print(f'You have rolled: {roll_val} \n\n')
        if cipher > 0 or vanguard > 0 or tunnels > 0:
            if roll_val > 19:
                self.guild_gold += 20
                self.weaknesses_found += 1
                return True
            else:
                self.knaves_countdown += 5
                return False
        else:
            if roll_val > 8:
                self.guild_gold += 20
                self.weaknesses_found += 1
                return True
            else:
                self.knaves_countdown += 5
                return False

    def bnb_effect(self, iron, twin, crier, gargoyles, doctrine, flames):

        # Income generated by informing castle weaknesses
        def bnb_income():
            if self.weaknesses_found == 1:
                self.guild_gold += 5
            elif self.weaknesses_found <= 3:
                self.guild_gold += 15
            else:
                self.guild_gold += 30

            self.weaknesses_found = 0

        if self.bnb_countdown > 0 or self.weaknesses_found == 0:
            self.bnb_countdown += 15
            self.guild_gold = 0
            self.extreme_wounds += 5
            return False

        print('Rolling D20..... \n\n')
        roll_val = roll_d20()
        print(f'You have rolled: {roll_val} \n\n')
        if iron > 0:
            if roll_val > 19:
                bnb_income()
                return True
            else:
                self.bnb_countdown += 15
                self.guild_gold = 0
                self.extreme_wounds += 5
                return False
        elif twin > 0 or crier > 0 or gargoyles > 0 or doctrine > 0 or flames > 0:
            if roll_val > 16:
                bnb_income()
                return True
            else:
                self.bnb_countdown += 15
                self.guild_gold = 0
                self.extreme_wounds += 5
                return False
        else:
            if self.has_access:
                if roll_val > 8:
                    bnb_income()
                    return True
                else:
                    self.bnb_countdown += 15
                    self.guild_gold = 0
                    self.extreme_wounds += 5
                    return False
            else:
                if roll_val > 12:
                    bnb_income()
                    return True
                else:
                    self.bnb_countdown += 15
                    self.guild_gold = 0
                    self.extreme_wounds += 5
                    return False

    def rags_effect(self, squire, doctrine, gargoyles, twin, walls, flames):
        if not self.has_access:
            self.extreme_wounds += 5
            return False
        else:
            print('Rolling D20..... \n\n')
            roll_val = roll_d20()
            print(f'You have rolled: {roll_val} \n\n')
            if squire > 0 or doctrine > 0 or walls > 0:
                if roll_val > 18:
                    self.weaknesses_found += 1
                    self.guild_gold += 50
                    return True
                else:
                    self.has_access = False
                    self.extreme_wounds += 5
                    return False
            elif gargoyles > 0 or twin > 0 or flames > 0:
                if roll_val > 15:
                    self.weaknesses_found += 1
                    self.guild_gold += 50
                    return True
                else:
                    self.has_access = False
                    self.extreme_wounds += 5
                    return False
            else:
                if roll_val > 8:
                    self.weaknesses_found += 1
                    self.guild_gold += 50
                    return True
                else:
                    self.has_access = False
                    self.extreme_wounds += 5
                    return False

    def cipher_effect(self, snare, ink, bastion, gargoyles, doctrine):

        print('Rolling D20..... \n\n')
        roll_val = roll_d20()
        print(f'You have rolled: {roll_val} \n\n')
        if snare > 0:
            if roll_val > 19:
                self.weaknesses_found += 1
                self.guild_gold += 30
                return True
            else:
                return False
        elif ink > 0 or bastion > 0 or gargoyles > 0 or doctrine > 0:
            if roll_val > 15:
                self.weaknesses_found += 1
                self.guild_gold += 30
                return True
            else:
                return False
        else:
            self.weaknesses_found += 1
            self.guild_gold += 30
            return True

    def scroll_effect(self, ink, bastion, gargoyles, doctrine):

        print('Rolling D20..... \n\n')
        roll_val = roll_d20()
        print(f'You have rolled: {roll_val} \n\n')
        if ink > 0:
            if roll_val > 18:
                self.weaknesses_found += 1
                self.guild_gold += 50
                return True
            else:
                return False
        elif bastion > 0 or gargoyles > 0 or doctrine > 0:
            if roll_val > 15:
                self.weaknesses_found += 1
                self.guild_gold += 50
                return True
            else:
                return False
        else:
            if roll_val > 8:
                self.weaknesses_found += 1
                self.guild_gold += 50
                return True
            else:
                return False

    def blade_effect(self, vanguard, scribe_training, sewers, twin, gargoyles, doctrine):
        if self.blade_countdown > 0:
            self.blade_countdown += 5
            return False

        print('Rolling D20..... \n\n')
        roll_val = roll_d20()
        print(f'You have rolled: {roll_val} \n\n')
        if vanguard > 0:
            if roll_val > 19:
                self.weaknesses_found += 1
                self.has_access = True
                self.guild_gold += 35
                return True
            else:
                self.blade_countdown += 5
                return False
        elif scribe_training > 0:
            if roll_val > 16:
                self.weaknesses_found += 1
                self.has_access = True
                self.guild_gold += 35
                return True
            else:
                self.blade_countdown += 5
                return False
        elif sewers > 0 or twin > 0 or gargoyles > 0 or doctrine > 0:
            if roll_val > 12:
                self.weaknesses_found += 1
                self.has_access = True
                self.guild_gold += 35
                return True
            else:
                self.blade_countdown += 5
                return False
        else:
            self.weaknesses_found += 1
            self.has_access = True
            self.guild_gold += 35
            return True

    def grain_effect(self, gargoyles, doctrine, walls, flames, bastion):
        if self.grain_countdown > 0:
            self.grain_countdown += 5
            return False

        print('Rolling D20..... \n\n')
        roll_val = roll_d20()
        print(f'You have rolled: {roll_val} \n\n')
        if doctrine > 0:
            if roll_val > 19:
                self.weaknesses_found += 1
                return True
            else:
                self.grain_countdown += 5
                return False
        elif gargoyles > 0 or walls > 0:
            if roll_val > 16:
                self.weaknesses_found += 1
                return True
            else:
                self.grain_countdown += 5
                return False
        elif flames > 0 or bastion > 0:
            if roll_val > 12:
                self.weaknesses_found += 1
                return True
            else:
                self.grain_countdown += 5
                return False
        else:
            if roll_val > 6:
                self.weaknesses_found += 1
                return True
            else:
                self.grain_countdown += 5
                return False

    def blight_effect(self, walls, gargoyles, doctrine, flames, bastion, scribe_training):
        if self.pestilence_countdown > 0:
            self.pestilence_countdown += 10000
            self.extreme_wounds += 3
            self.guild_gold = 0
            return False

        print('Rolling D20..... \n\n')
        roll_val = roll_d20()
        print(f'You have rolled: {roll_val} \n\n')
        if walls > 0:
            if roll_val > 18:
                self.weaknesses_found += 1
                self.guild_gold += 55
                return True
            else:
                self.pestilence_countdown += 10000
                self.extreme_wounds += 3
                self.guild_gold = 0
                return False
        elif gargoyles > 0 or doctrine > 0:
            if roll_val > 16:
                self.weaknesses_found += 1
                self.guild_gold += 55
                return True
            else:
                self.pestilence_countdown += 10000
                self.extreme_wounds += 3
                self.guild_gold = 0
                return False
        elif flames > 0 or bastion > 0 or scribe_training > 0:
            if roll_val > 12:
                self.weaknesses_found += 1
                self.guild_gold += 55
                return True
            else:
                self.pestilence_countdown += 10000
                self.extreme_wounds += 3
                self.guild_gold = 0
                return False
        else:
            self.weaknesses_found += 1
            self.guild_gold += 55
            return True

    def deteriorate(self):
        self.phishing_countdown = self.phishing_countdown - 1 if self.phishing_countdown > 0 else self.phishing_countdown
        self.walls_countdown = self.walls_countdown - 1 if self.walls_countdown > 0 else self.walls_countdown
        self.ratcaller_countdown = self.ratcaller_countdown - 1 if self.ratcaller_countdown > 0 else self.ratcaller_countdown
        self.knaves_countdown = self.knaves_countdown - 1 if self.knaves_countdown > 0 else self.knaves_countdown
        self.bnb_countdown = self.bnb_countdown - 1 if self.bnb_countdown > 0 else self.bnb_countdown
        self.blade_countdown = self.blade_countdown - 1 if self.blade_countdown > 0 else self.blade_countdown
        self.grain_countdown = self.grain_countdown - 1 if self.grain_countdown > 0 else self.grain_countdown
        self.pestilence_countdown = self.pestilence_countdown - 1 if self.pestilence_countdown > 0 else self.pestilence_countdown


thief_attack_header_real_life = ["Mass Phishing", "Spear Phishing", "Backdoor", "DoS", "Ransomware",
                                 "Man-in-the-Middle", "Brute Force", "Privilege Escalation", "SQL Injection", "XSS",
                                 "Session Hijacking",
                                 "Supply Chain Attack", "Worms"]

thief_attack_header_medieval = ["Snake Oil Salesman", "Alehouse Swindler", "Loosened Castle Walls", "Clatter of Brats",
                                "The Ratcaller of Elwood", "Whispering Knaves", "Brigands and Bandits", "Rags to Riches",
                                "The Cipherbane", "Poisoned Scroll",
                                "Blade of the Doppelganger", "Grains of Malice", "The Mourning Blightweaver"]

thief_attack_cost = [5, 8, 10, 12, 20, 22, 20, 25, 30, 35, 40, 45, 50]

thief_image_list = [
     f"static/images/Thieves/{name}.jpg"
     for name in thief_attack_header_medieval
]

thief_rl_image_list = [
    f"static/images/Thieves RL/{name}.jpg"
     for name in thief_attack_header_real_life
]

thief_attack_explanation_medieval = [
    '''
    Cost: 5 Gold
    
    You masquerade as a snake oil salesmen and sell fake medicine to unsuspecting guards

    If you succeed,
        The guard drinks and faints, they steal his official clothes and armour, leaving him with similar-looking faulty armour
        You now have access to the castle
        Weakness registered
    
    Real life equivalent - Mass Phishing 
''',
    '''
    Cost: 8 Gold
    
    You perform reconnaissance of the people in the kingdom and note an important nobleman
    You strike a friendship with the nobleman at the Alehouse
    
    If you succeed,
        One night you get the nobleman incredibly drunk, and steal his important keys and insignia
        You now have access to the castle
        Weakness registered
    
    Real life equivalent - Spear Phishing 
''',
    '''
    Requires castle access to be played !!
    Cost: 10 Gold
    
    You observe a set of loose stones in the castle wall
    You can now remove them silently to access the castle without alerting the guards
    You immediately steal 25 Gold from the Castle
    
    If successful, you now steal 50% more Gold from the Castle and the Kingdom spends 50% more on fines and cleanses until 
    The Ironbound Doctrine, The Whispering Gargoyles or The Flaming Battlements are activated    
    
    Real life equivalent - Network Backdoors    
''',
    '''
    Cost: 12 Gold
    
    You see a massive group of children from nearby dwellings playing
    You hire them to disturb the gate guards repeatedly
    
    If successful,
        Travelling salesmen will no longer approach the kingdom and will leave for the next kingdom
        kingdom will earn only 20% Gold in the next turn
        Weakness registered   
    
    Real life equivalent - Denial of Service (Dos)  
''',
    '''
    Cost: 20 Gold
    
    You hire The Ratcaller of Elwood to lure rats into the castle
    
    If successful,
        The rats block access to the granary, leaving the kingdom with limited food supply
        You hold the grains for ransom, demanding 200 Gold
        If guards do not have enough money, the rats eat the grains and the game is instantly over
        The Kingdom earns only 25% Gold in their next turn
        Weakness registered
    
    Real life equivalent - Ransomware     
''',
    '''
    Cost: 22 Gold
    
    You observe a messenger leave the castle and follow him
    You follow him and while he sleeps, you decide to change the sensitive message to sour the relationship between the kingdoms
    
    If you succeed,
        You reroute the kingdom's money to yourself
        Steal 20 Gold
        Weakness registered
        kingdom will earn only 60% Gold in their next turn
    
    Real life equivalent - Man in the Middle (MITM)     
''',
    '''
    Cost: 20 Gold
    
    Earn: 5 Gold (1 weakness) / 15 Gold (2 or 3 weaknesses) / 30 Gold (4 and more weaknesses)
    You sell information of the kingdom to Brigands and Bandits
    Brigands and bandits arrive at the castle with huge numbers and throw heavy stones at the gate, trying to break it down by force
    
    If Brigands and Bandits succeed,
        Kingdom loses 70% of its gold
        Next upgrade costs 6x the Gold
    
    Real life equivalent - Brute Force and Initial Access Brokerage (IAB)   
''',
    '''
    Requires access to the Castle !
    Cost: 25 Gold
    
    You impersonate the nobleman and attempt to convince other nobles to give you access to the royal vault
    
    If you succeed,
        You steal 50 Gold from the Castle's Royal Vault
        Weakness registered
    
    Real life equivalent - Privilege Escalation    
''',
    '''
    Cost: 30 Gold
    
    You discover the Undead Oracle named The Cipherbane who speaks in an ancient language and allows access to the Royal Vault
    If you speak a few words in the Sylvan tongue, the lock may provide secrets from the vault
    You use this to know the secrets of other nobles using the vault or uses the access to poison the artefacts in the Vault
    
    If you succeed,
        You steal 30 Gold from the Royal Vault
        Kingdom has to additionally pay 60 Gold as fines to the Empire
        Weakness registered
    
    Real life equivalent - SQL Injection    
''',
    '''
    Cost: 35 Gold
    
    You sneak behind the Royal Scribe and enchant a few royal scrolls carrying information to the nearby kingdom's Mayor
    Once the neighbouring Mayor opens the scroll, a mind control spell activates that poisons the mayor's mind
    
    If you succeed,
        You steal 50 Gold from the Castle during the chaos 
        kingdom will earn only 50% Gold in their next withdrawal
        Weakness registered
    
    Real life equivalent - Cross Site Scripting (XSS)    
''',
    '''
    Cost: 40 Gold
    
    You hire Sorlin the Seer
    Sorlin masquerades as a travelling Salesman and sells a secretly enchanted sword to a nobleman
    Using the connection with the sword, he mimics the noble's appearance
    You divert the real noble's attention with your wares and Sorlin attends the banquet, gaining sensitive information
    
    If successful,
        Sorlin loosens a few stones on the Castle wall
        Weakness registered
        Sorlin steals 35 Gold from the Castle
        Kingdom pays 30 Gold as a fine to the Empire
    
    Real life equivalent - Session Hijacking       
''',
    '''
    Cost: 45 Gold
    
    You learn that the kingdom purchases grains from the neighbouring kingdom
    You poison these grains which are then sent to the kingdom
    Upon sowing poisoned grains, folk fall ill and other grains become spoilt
    
    If successful,
        Weakness registered
        The Kingdom pays 70 Gold to magically purify their grains and heal their folk
        They earn only 15% of the maximum intended income in the next turn
        The neighbouring kingdom offers you 40 Gold for your service
    
    Real life equivalent - Supply Chain Attack        
''',
    '''
    Cost: 50 Gold
    
    You hire Dreizar of Thornmere, a vengeful necromancer 
    Dreizar unleashes multiple poisonous and magically enhanced undead warriors into the kingdom
    The undead warriors cause a pestilence which quickly spreads among the Townsfolk
    In the chaos, the undead grab many secret scrolls and bring them back to the necromancer
    
    If successful,
        Weakness registered
        You steal 55 Gold from the Castle
        The Kingdom additionally pays 80 Gold to clean its towns
        The Kingdom earns 10% Gold in the next turn
    
    Real life equivalent - Worms    
'''
]

thief_attack_explanation_real_life = [
    'Cybercriminals send fake emails to many people, hoping someone will click on a link or give away personal or professional information'
    '\n\nCan be minimised by proper Social Engineering awareness Training'
    '\n\nMostly focus on fake invoices and banking scams',

    'Cybercriminals target a specific person, often pretending to be someone they trust or eventually gain their trust, to trick them into giving up sensitive information'
    '\n\nCan be minimised by proper Social Engineering awareness Training'
    '\n\nHighly customised and is far more dangerous than Mass Phishing',
    
    'A secret way for hackers to get into a system or computer without being noticed, often by exploiting weaknesses'
    '\n\nCan be spotted at the earliest by efficient and updated implementations of IDSs, Firewalls and Zero Trust Architecture'
    '\n\nCreate easy pathways for hackers to exfiltrate data',
    
    'Hackers flood a website or server with too much traffic, causing it to crash and stop working'
    '\n\nCan be mitigated by Rate Limiting requests'
    '\n\nIDSs, Firewalls, Web Application Firewalls, Network Segmentation and ZTA offer moderate support against DoS attacks'
    '\n\nOften used as a distraction while hackers execute an attack on another part of the network',
    
    'A type of malware that locks or encrypts your files, and the hacker demands money to unlock them'
    '\n\nTheir effects are significantly minimised via Offshore Data Backups'
    '\n\nNetwork Segmentation, IDSs, Firewalls and ZTA offer moderate support against Ransomware'
    '\n\nHas been on a significant rise since mid 2010s with the emergence of Ransomware-as-a-Service models',
    
    'A hacker secretly intercepts and alters communication between two people or systems without them knowing'
    '\n\nSignificantly mitigated by the use of End-to-end Encryption, HTTPS and VPN'
    '\n\nMITM is mostly involved in Corporate Espionage and are a go-to technique used by Advannced Persistent Threats',
    
    'Hackers try every possible password combination until they guess the correct one, usually through automated tools'
    '\n\nSignificantly minimised by Account Lockout policies'
    '\n\nMFA, Firewalls and IDSs offer moderate support against Brute Force attacks'
    '\n\nIAB - A significant number of times, smaller hacker groups sell information of the weaknesses of an organisation to a bigger hacking group who execute a mass attack',

    'A hacker gains higher access or permissions on a system, allowing them to control more or sensitive parts of it'
    '\n\nNetwork Segmentation and Least-Privileged Access can significantly mitigate the impact of Privilege Escalation'
    '\n\nFirewalls, IDSs, ZTA and MFA offer moderate support against Privilege Escalation'
    '\n\nThis attack is primarily used in tandem with other attacks to deliver a more significant impact to the victim(s)',
    
    'Hackers use malicious code to trick a website\'s database into giving them access to information, like usernames and passwords'
    '\n\nSignificantly mitigated by Parameterised Queries'
    '\n\nInput Sanitisation and Web Wpplication Firewalls offer moderate support against SQL Injection'
    '\n\nIf access to the database is not logged and moderated, hackers may be able to delete the entire database and severely impair the organisation(s)',
    
    'Hackers insert malicious code into a website so that when someone visits it, the code can steal their data or download malware into their systems'
    '\n\nSignificantly mitigated by Input Sanitisation'
    '\n\nWeb Application Firewalls, IDSs and ZTA offer moderate support against XSS'
    '\n\nXSS has a very wide scope and can be used in tandem with Session Hijacking',
    
    'Hackers steal a person\'s login session to impersonate them and gain unauthorised access to their accounts'
    '\n\nSignificantly mitigated by HTTPS and Cyber Awareness Trainings'
    '\n\nVPNs, MFA, IDSs and ZTA offer moderate support against Session Hijacking'
    '\n\nThis enables an attacker to bypass any forms of authentication and maintain access until the session cookie expires',
    
    'Hackers target a company\'s suppliers or partners to secretly insert malicious software into trusted software or products'
    '\n\nSignificantly mitigated by Zero Trust Architecture'
    '\n\nNetwork Segmentation, IDSs, Firewalls and Web Application Firewalls offer moderate support against Supply Chain Attacks'
    '\n\nOften used to target high end companies that uphold strong security principles, but have suppliers that are pretty lax with their cybersecurity measures',
    
    'Self-replicating malware that spreads quickly across the network with minimal user interaction'
    '\n\nSignificantly mitigated by Network Segmentation'
    '\n\nZero Trust Architecture, IDSs, Web Application Firewalls and Cyber Awareness Trainings offer moderate support against Worms'
    '\n\nWorms are often used by attackers to spread malicious software and overload a network simultaneouy with minimal efforts'
]

phishing_questions = ['An attacker wants their phishing email to look credible. Which tactic helps increase the email\'s legitimacy?',
                      'An attacker wants to send a phishing email pretending to be IT support. When would be the most strategic time to send it?',
                      'An attacker is planning a social engineering campaign. Which of these targets is most valuable for initial compromise?',
                      'Which subject line is most likely to entice a user to open a phishing email?',
                      'When calling a target and pretending to be from IT, what technique builds the most credibility?',
                      'An attacker enters a building with fake ID and clipboard. What tactic are they using?',
                      'An attacker wants to avoid spam filters. Which tactic helps evade automated detection?',
                      'What emotional trigger is most effective in phishing?',
                      'What makes spear phishing more effective than mass phishing?',
                      'Which method is NOT commonly used for social engineering?']

phishing_answers = [['Use Arial font to look friendly','Mimic the tone and branding of a real company','Use all caps in the subject line','Add a few spelling mistakes to give a sense of urgency'],
                    ['Saturday at midnight','During a public holiday','Monday morning at 9 AM','Friday evening at 5 PM'],
                    ['A new HR employee with access to onboarding portals','The janitor\'s shared desktop','A CEO\'s spouse','A system already running Linux'],
                    ['RE: Weekend Updates','FYI - Updated Policies','Setting Up a Meeting','Important: Action Required - Password Expiring Today'],
                    ['Asking how their weekend was','Tell them they have won a gift card','Using a robotic voice','Referring to internal systems or ticket numbers'],
                    ['Piggybacking','Pretexting','Shoulder surfing','Tailgating'],
                    ['Attach malware as a .exe file','Use alternating text case to bypass detection','Include a .pdf file with a link inside','Send from a malicious domain'],
                    ['Curiosity','Boredom','Pain','Joy'],
                    ['Cheaper','Involves humour','Goes viral easily','Customised to the target\'s details'],
                    ['Packet Sniffing','USB drop','SMS phishing (smishing)','Voice phishing (vishing)']]

phishing_q_response = ['Mimicking tone and branding increases the chance the target will trust the message','People are catching up on email Monday mornings, making them more likely to skim and click links',
                       'HR employees often receive attachments and interact with new people—prime targets for phishing','Urgency + relevance (passwords) increase click rates — a known attacker tactic',
                       'Effective attackers learn internal jargon to make their pretext believable','Pretexting means creating a fake identity or reason for access (e.g., posing as maintenance)',
                       'Embedding links in PDFs is harder to scan and often bypasses email filters','Links like “Here’s a photo of you!” or “Suspicious login detected” use curiosity to bait clicks',
                       'Tailoring attacks to individuals (e.g., using their boss\' name or job info) increases credibility','Packet sniffing is a technical method, not a human-manipulation (social engineering) technique']

phishing_answer_key = [1,2,0,3,3,1,2,0,3,0]

backdoor_questions = [
    'Imagine someone sneaks into a house and leaves a hidden key for later. In computer terms, what is that hidden way back in called?',
    'If an attacker wants to hide their special "door" into your computer, what kind of door would they pick?',
    'What is a simple tool an attacker might use to control your computer from far away?',
    'How can an attacker make their secret connection look like normal internet traffic so it\'s not easily noticed?',
    'To make sure their secret "door" stays open even if the computer restarts, what should an attacker do?',
    'Why might an attacker want your computer to "call them" instead of them trying to "call into" your computer?',
]

backdoor_answers = [
    ['A strong firewall','A regular password','An antivirus update','A secret backdoor'],
    ['A door that opens loudly','A hidden door that uses a common path','A door that sends an alarm','A front door with a big sign'],
    ['An email client','A chat program','A word processor','A backdoor'],
    ['Make it look like you are just browsing the internet','Turn off the internet connection','Send very obvious messages','Send lots of spam emails'],
    ['Make it start automatically when the computer turns on','Hide it in a picture file','Save it to a USB stick','Put it in a temporary folder'],
    ['It needs you to click on something','It often goes around typical security walls','It\'s easier to type','It makes more noise'],
]

backdoor_q_response = [
    'A backdoor is like a secret hidden way for an attacker to get back into a system they\'ve already messed with, without being seen',
    'Attackers try to use uncommon or tricky ways to set up backdoors, so they aren\'t easily found by normal checks',
    'Netcat is a very basic but powerful tool that hackers can use to talk to computers remotely, like a simple walkie-talkie for computers',
    'By making the backdoor traffic look like normal web browsing (using common ports like 80 or 443), attackers can blend in and avoid suspicion',
    'To make sure a backdoor works even after a computer is turned off and on again, attackers set it up to start automatically when the computer boots up',
    'An attacker might prefer a reverse shell because it can often sneak past firewalls that usually block incoming connections, as your computer is reaching out to them',
]

backdoor_answer_key = [3,1,3,0,0,1]

dos_questions = [
    'What is the main goal of a DoS attack?',
    'Imagine many zombie-like computers working together to attack a website. What is this group called?',
    'Which common internet service, like looking up website names, can be tricked to make a DoS attack bigger?',
    'How do attackers try to hide who they are when doing a DoS attack?',
    'When would a DoS attack cause the most problems for a website?',
    'Why might someone use a DoS attack as a distraction, like a magic trick?']

dos_answers = [
    ['To upload a malware','To steal passwords','To make a website or service crash and stop working','To send annoying pop-ups'],
    ['A single hacker','Undead soldiers','A botnet','A computer club'],
    ['Email sending (SMTP)','File sharing (FTP)','Website Browse (HTTPS)','Domain Name System (DNS)'],
    ['By using their real name','By changing their computer\'s visible address','By sending only small amounts of data','By using very strong passwords'],
    ['Late at night when no one is using it','During its busiest time, like a big sale','Early morning on a weekend','Only for a few seconds'],
    ['To make the website more popular','To make security guards focus on the attack while they do something else','To install new software','To get free internet access']]

dos_q_response = [
    'The primary goal of a DoS attack is to overwhelm a target with too much traffic, making it unavailable to legitimate users',
    'A botnet is a network of hijacked computers controlled by an attacker, used to launch large-scale attacks like DDoS, which is more dangerous compared to DoS',
    'Attackers can abuse the Domain Name System (DNS) by sending small requests that result in large responses directed at the victim, amplifying the attack',
    'Attackers often use IP spoofing to change the visible address of the attacking computers, making it harder to trace them back',
    'A DoS attack is most effective when it hits during peak usage times, causing maximum disruption and financial loss',
    'Attackers sometimes use a DoS attack as a diversion to keep security teams busy while they attempt another, more sneaky, breach elsewhere']

dos_answer_key = [2,2,3,1,1,1]

ransomware_questions = [
    "What does ransomware mainly try to do to your computer files?",
    "If your computer gets ransomware, what is the criminal usually asking for?",
    "How does ransomware often get onto a computer in the first place?",
    "What kind of important files does ransomware typically lock up?",
    "Why do criminals want you to pay with special internet money (cryptocurrency) for ransomware?",
    "If a ransomware message has a timer counting down, what is it trying to make you feel?",
    "What is a 'botnet' in a ransomware attack?",
    "What is a smart way to protect your files from ransomware, even if you get infected?",
    "What does 'double extortion' mean in a ransomware attack?",
    "Why might a ransomware attacker decide NOT to attack a hospital?"
]
ransomware_answers = [
    ['Delete them completely','Lock them so you can\'t open them unless you pay','Make them faster','Change their colors'],
    ['Money','A new keyboard','More computer memory','A thank you note'],
    ['By turning on your computer','By clicking on a bad link or opening a strange email attachment','Through a strong password','By downloading a movie legally'],
    ['Game saves only','Web browser history','Important documents, photos, and databases','Pictures and videos of cats'],
    ['Because it\'s easy to trace back to them','Because it\'s very fast','Because it\'s harder to track and keeps them anonymous','Because it\'s cheap to buy'],
    ['Panicked and urgent to pay','Happy and relaxed','Confused about the time','Like you have plenty of time'],
    ['A group of friendly computers helping you','A new type of antivirus software','A network of hijacked computers controlled by the attacker','A single, very powerful computer'],
    ['Make regular backup copies of your important files','Never turn off your computer','Always keep your internet disconnected','Print everything out on paper'],
    ['Attacking two different computers','Encrypting files AND threatening to release your private data','Encrypting files twice as strong','Asking for money twice'],
    ['Hospitals are easy targets','Hospitals always pay quickly','Attacking hospitals could cause a lot of public anger and trouble for the attacker','They don\'t have valuable information']
]
ransomware_q_response = [
    "Ransomware's main goal is to lock or encrypt your files so you can't use them, forcing you to pay to get them back",
    "Criminals use ransomware to demand money (a 'ransom') in exchange for unlocking your files",
    "Ransomware often spreads when you click on a bad link or open a malicious email attachment, accidentally letting it onto your computer",
    "Ransomware aims for files that are most important to you or a business, like documents, photos, or business databases",
    "Attackers prefer cryptocurrency because it's designed to be difficult to trace, allowing them to receive payments anonymously",
    "A countdown timer is a trick to create urgency and pressure you into paying quickly before your files are permanently lost",
    "In a ransomware attack, a botnet is a group of compromised computers (often belonging to other victims) that criminals control to help spread the ransomware or launch other attacks",
    "Making regular backup copies of your important files is crucial, because if ransomware locks your originals, you can restore them from your backups without paying",
    "Double extortion means the attacker not only encrypts your files but also steals a copy of your sensitive data and threatens to publish it if you don't pay the ransom",
    "Attackers might avoid hospitals because causing harm to such a critical service can lead to huge public backlash and increased attention from law enforcement, making it riskier for them"
]
ransomware_answer_key = [1,0,1,2,2,0,2,0,1,2]

mitm_questions = [
    "Imagine someone secretly listening in on your phone call without you knowing. What is this like in computer terms?",
    "Which type of Wi-Fi connection is easiest for a secret listener to spy on?",
    "If someone wants to pretend to be your router to steal your internet traffic, what trick might they use?",
    "Why would a hacker pretend to be another computer on your home network?",
    "Which basic internet rule is often broken to redirect your computer's messages?",
    "Why does a website address starting with 'HTTPS' make it harder for someone to secretly listen in?",
    "What might a bad guy do to get around 'HTTPS' and still spy on your internet Browse?",
    "Why would a hacker set up a fake public Wi-Fi hotspot in a coffee shop?",
    "What simple tool might a hacker use to see all the internet messages passing through their computer?",
    "What's one common thing a hacker tries to steal in a MITM attack?"
]

mitm_answers = [
    ['Sending you too many emails','A secret listener between you and what you\'re talking to','Blocking your social media','Making your computer run faster'],
    ['Your work Wi-Fi that needs a special login','A public Wi-Fi that asks for no password','A Wi-Fi network that only lets you visit one website','Your home Wi-Fi with a strong password'],
    ['Send false network messages to trick your computer','Turn off your internet for a minute','Pretend to be your computer\'s friend','Send you a text message'],
    ['To make your computer slower','To share their files with you','To help you fix your computer','To redirect your internet traffic through their computer'],
    ['The rule for finding devices on a local network (ARP)','The rule for sending big files (FTP)','The rule for secure websites (HTTPS)','The rule for sending emails (SMTP)'],
    ['It makes your connection private and scrambled','It makes your keyboard light up','It warns you about bad weather','It makes the website load slower'],
    ['Make your computer restart quickly','Try to make your connection less secure (like from HTTPS to HTTP)','Send you a pop-up ad','Tell you to update your web browser'],
    ['To find lost phones','To give everyone free internet','To secretly spy on people who connect to it','To make their own internet faster'],
    ['A tool that checks their computer\'s battery life','A simple program that shows network messages','A game on their phone','A word processor'],
    ['The amount of space on your hard drive','Your favorite song downloads','Your login names and passwords','The time of day']
]

mitm_q_response = [
    "A Man-in-the-Middle (MITM) attack is like a secret listener who places themselves between two people or computers that are trying to talk, so they can see or change what's being said",
    "Open public Wi-Fi networks are most vulnerable because they don't usually encrypt your connection, making it easy for an attacker to listen in",
    "Attackers can use false network messages (like ARP spoofing) to trick your computer into sending its internet traffic to the attacker's device instead of the real router",
    "A hacker might pretend to be another device on your network (like your router) to redirect all your internet traffic through their computer, so they can see everything",
    "The Address Resolution Protocol (ARP) is a basic rule used on local networks, and it's often tricked in MITM attacks to reroute where your computer sends its messages",
    "HTTPS makes your internet connection private by scrambling (encrypting) the information, so even if someone listens in, they can't understand what you're sending",
    "A common trick is to try and force your browser to use a less secure connection (like HTTP instead of HTTPS), or use fake security certificates to pretend they are the real website",
    "Attackers set up fake Wi-Fi hotspots to lure unsuspecting users into connecting. Once connected, the attacker can spy on all their internet activity",
    "A hacker might use a network analyzer or 'sniffer' (like Wireshark) to capture and read all the internet messages that pass through their computer during an attack",
    "In a MITM attack, hackers often try to steal sensitive information like login names and passwords because they are very valuable"
]

mitm_answer_key = [1,1,0,3,0,0,1,2,1,2]

brute_force_questions = [
    "What is a brute force attack trying to do?",
    "If a website asks for your password, and an attacker keeps trying many guesses, what kind of attack is that?",
    "Which kind of password is easiest for a brute force attack to guess?",
    "What makes a password strong against brute force attacks?",
    "What kind of computer tool might an attacker use to automatically guess many passwords?",
    "What can a website do to stop someone from making too many password guesses?",
    "What is a 'dictionary attack' for guessing passwords?",
    "Why would an attacker use a list of common words or passwords instead of just random letters?",
    "How can attackers try to avoid getting caught when guessing passwords many times?",
    "What is 'credential stuffing'?"
]

brute_force_answers = [
    ['Make your computer slow','Find your correct password by trying many guesses','Send you annoying emails','Make your screen blink'],
    ['A brute force attack','A secret message attack','A friendly hack','A network boost'],
    ['A short password like "123456"','Your dog\'s name','A very long password with mixed letters, numbers, and symbols','A password that changes every hour'],
    ['Using only common words','Being very long and having different types of characters (like symbols and numbers)','Being very short','Being your birthday'],
    ['A painting program','A music player','A program that guesses passwords very fast','A video game'],
    ['Give them more guesses','Lock their account or make them wait after too many wrong guesses','Send them a funny picture','Tell them a secret password'],
    ['Using a list of common words or passwords to guess','Trying every possible number combination','Sending a virus to your computer','Turning off your internet connection'],
    ['Because it\'s more likely to guess a real password quickly','Because it\'s against the rules to guess randomly','Because it makes the computer faster','Because it sends less data'],
    ['Guess passwords very slowly and from different locations','Tell the website what they are doing','Only guess during the daytime','Send only one guess per day'],
    ['Creating many new fake accounts','Using stolen username and password pairs from other websites to log in','Giving someone your login details on purpose','Filling out a form very fast']
]

brute_force_q_response = [
    "A brute force attack tries to find the correct password or login by trying every possible combination or common guesses",
    "When an attacker keeps trying many different password guesses on a login page, that's a brute force attack",
    "A short password like '123456' is very easy for a brute force attack because it has very few combinations",
    "A long password with mixed characters (letters, numbers, symbols) is much harder to guess because it has too many possible combinations for a brute force attack to try quickly",
    "Attackers use programs that guesses passwords very fast (like Hydra) to automate trying thousands or millions of combinations",
    "Websites can lock an account or make someone wait after too many wrong guesses to stop brute force attacks",
    "A dictionary attack is a type of brute force where the attacker uses a list of common words, names, or previously leaked passwords instead of trying every random combination",
    "Attackers use lists of common words or passwords because people often choose simple passwords, making it more efficient to guess a real password quickly",
    "Attackers might guess passwords very slowly or use different computers (proxies) to avoid getting detected by security systems that look for many guesses from one place",
    "Credential stuffing is when attackers use username and password combinations that were stolen from *other* websites. They try these stolen logins on *your* website, hoping you reused the same password, which is often much faster than guessing"
]

brute_force_answer_key = [1,0,0,1,2,1,0,0,0,1]

priv_esc_questions = [
    "When a hacker gets into a computer, what is their main goal with 'privilege escalation'?",
    "If a normal user suddenly gets the powerful rights of an administrator, what kind of privilege escalation is that?",
    "Why would a hacker look for old software that hasn't been updated on a computer?",
    "A hacker gets access to a regular user's account. What's the next big thing they might try to find to get more power?",
    "Which special account usually has full control over a computer system?",
    "In systems like Linux, what's a common trick to get higher power by finding badly set up programs?",
    "Why might a hacker care about certain programs that have a special 'sticky bit' (like SUID) turned on?",
    "What kind of tool can help a hacker find ways to get more power on a computer?",
    "In Windows computers, which well-known tool is often used to help a hacker gain administrator rights?",
    "Why is it so important for a hacker to get more power (privilege escalation) before they do something big like steal a lot of data or lock all your files with ransomware?"
]

priv_esc_answers = [
    ['To make the computer run slower','To gain higher access than they started with','To delete harmless files','To change the computer\'s wallpaper'],
    ['Moving files between folders','A normal user becoming an administrator','Sharing a printer','Connecting to a different Wi-Fi network'],
    ['Because old software is usually faster','Because old software might have known weak spots they can use','Because it looks nicer','Because it helps the computer cool down'],
    ['Their favorite music playlist','Saved logins or password clues','Their last search history','The name of their desktop background'],
    ['The "Guest" account','Any regular user account','A temporary login','The "Administrator" or "Root" account'],
    ['Turning on the screen saver','Finding programs that run with too much power','Changing the clock time','Restarting the computer often'],
    ['Because they always crash the computer','Because they might let a normal user do powerful things they shouldn\'t','Because they make the internet faster','Because they help clean up old files'],
    ['A common web browser','A tool that checks for ways to get more power (like Linux Exploit Suggester)','A simple calculator','A drawing program'],
    ['Microsoft Word','Metasploit','Adobe Reader','A basic chat application'],
    ['Because it\'s required to access more important parts of the system or do big damage','Because it makes the attack less noticeable','Because it deletes evidence automatically','Because it makes the computer immune to antivirus software']
]

priv_esc_q_response = [
    "Privilege escalation is when an attacker gets a higher level of control on a computer than they first had, like moving from a regular user to an administrator",
    "When a normal user gains the powerful rights of an administrator, that's called vertical privilege escalation because they move 'up' in power",
    "Attackers look for old or unpatched software because it often has known weaknesses (vulnerabilities) that they can use to break in or get more control",
    "After getting into a user account, hackers look for saved logins or password clues that might let them become an administrator or access other important parts of the system",
    "The 'Administrator' (on Windows) or 'Root' (on Linux) account has full control over almost everything on the computer, which is what hackers want",
    "In Linux, hackers often try to get higher power by finding programs that are badly set up to run with too much power (like misconfigured SUID binaries) that a normal user can abuse",
    "Attackers care about programs with a special 'sticky bit' (like SUID) because if they are misconfigured, a regular user might be able to run them with powerful administrator rights, even if they shouldn't",
    "Tools like Linux Exploit Suggester are designed to scan a computer and point out known ways a hacker might be able to get more powerful access",
    "Metasploit is a very common tool in Windows that helps hackers automatically use known tricks to gain administrator rights on a computer",
    "Privilege escalation is a critical step because it gives attackers the necessary power to access sensitive data, install malware like ransomware across a network, or hide their tracks more effectively"
]

priv_esc_answer_key = [1,1,1,1,3,1,1,1,1,0]

sql_injection_questions = [
    "What is a hacker trying to do with a SQL Injection attack?",
    "If a website asks for your name, and a hacker types in `' OR '1'='1`, what are they trying to do?",
    "What kind of common mistake in website code makes SQL Injection possible?",
    "Why is it bad if an attacker can see error messages from the database during an attack?",
    "What is 'Blind SQL Injection'?",
    "Which part of a website is most likely to be weak to SQL Injection?",
    "What can a hacker do if they successfully use `UNION SELECT` in a SQL Injection?",
    "How does 'input sanitisation' help stop SQL Injection?",
    "Why are 'parameterised queries' a strong defense against SQL Injection?",
    "What information might a hacker gain from a successful SQL Injection attack?"
]

sql_injection_answers = [
    ['To secretly access or control the website\'s database','To make the website faster','To change the website\'s colors','To send spam emails'],
    ['To help the website remember them','To trick the login and get in without a password','To make the website load slower','To confuse the website\'s computer'],
    ['Not checking what users type into forms very carefully','Using too many pictures','Having too many links','Using old versions of web browsers'],
    ['Because it helps the website run faster','Because it fixes the website\'s problems','Because it tells the hacker useful secrets about the database','Because it makes the website look bad'],
    ['When the hacker cannot see direct results but can figure things out by how the website acts','When the hacker guesses passwords very quickly','When the hacker can see all the database information directly','When the hacker uses a special type of virus'],
    ['A simple blog post page','A page where you can fill out forms and search for things','A page with lots of pictures','A page that only shows the weather'],
    ['They can make the website play music','They can change the website\'s colors','They can combine their own questions with the website\'s to steal more data','They can delete pictures from the website'],
    ['It makes the website easier to use','It blocks bad characters from changing the database\'s commands','It adds firewalls to the website','It cleans up the database'],
    ['They make the database run faster','They show more advertisements','They treat everything a user types as simple text, not commands','They hide the website\'s real address'],
    ['How many times someone visited the website','Secret user information like passwords or private data','The website\'s design files','The weather forecast']
]

sql_injection_q_response = [
    "A hacker uses SQL Injection to secretly control or get information from a website's database, which holds all its important data",
    "Typing `' OR '1'='1` is a common trick to bypass login screens. It makes the computer think a condition is always true, letting the hacker in without the correct password",
    "SQL Injection happens when a website doesn't carefully check what users type into forms, allowing hackers to insert harmful code into database commands",
    "Database error messages can be very helpful to a hacker because they often reveal clues about how the database is built, which helps the hacker plan their next moves",
    "Blind SQL Injection is when a hacker can't see the direct results of their commands, but they can figure out information by observing small changes, like if a page loads slower or differently",
    "Any part of a website where you can fill out forms or search for things is potentially vulnerable to SQL Injection if the input isn't handled safely",
    "If a hacker uses `UNION SELECT` successfully, it means they can combine their own database questions with the website's original questions to steal more data from different parts of the database",
    "Input sanitisation helps stop SQL Injection by cleaning or blocking dangerous characters that hackers might try to type into forms, preventing them from messing with the database commands",
    "Parameterised queries are a strong defense because they tell the database to treat everything a user types as just plain text (data), not as instructions or commands, which stops the injection from working",
    "From a successful SQL Injection, a hacker can gain access to secret user information like usernames, passwords, emails, or other private data stored in the database"
]

sql_injection_answer_key = [0, 1, 0, 2, 0, 1, 2, 1, 2, 1]

xss_questions = [
    "What does XSS stand for?",
    "What is the main goal of a hacker using XSS?",
    "Which part of a website does XSS usually attack?",
    "If a website lets you type comments and doesn't check them, what could a hacker put in that comment box for XSS?",
    "What kind of damage can an XSS attack cause to a website user?",
    "Why is XSS sometimes called 'client-side' scripting?",
    "What happens in a 'reflected XSS' attack?",
    "What happens in a 'stored XSS' attack?",
    "How can website developers protect against XSS attacks?",
    "Why might an XSS attack be used to steal 'cookies'?"
]

xss_answers = [
    ['Xerox Security System','Cross-Site Scripting','Extra Safe Security','Excellent Server Safety'],
    ['To run malicious code in a user\'s web browser','To make the website faster','To change the website\'s look for everyone','To delete files from the server'],
    ['The user\'s web browser and the pages they see','The database server','The website\'s firewall','The network router'],
    ['Just random numbers','Harmful code (like JavaScript)','A long paragraph of text','A simple image file'],
    ['Make their internet slow','Change their computer\'s desktop background','Take over their web browser or steal their information','Give them a virus on their hard drive'],
    ['Because the malicious code runs in the user\'s own web browser','Because it uses a special program on the hacker\'s computer','Because it attacks the server computer','Because it only works on very old computers'],
    ['The hacker sends a virus through email','The malicious code is reflected back to the user from the website and runs','The malicious code is permanently saved on the website','The website changes its own code'],
    ['The malicious code is hidden in a picture','The hacker only uses it on their own computer','The malicious code is saved on the website and seen by many users later','The malicious code is only seen once and then disappears'],
    ['By telling users to use different web browsers','By making the website black and white','By carefully checking and cleaning any input users type into forms','By never using comments sections'],
    ['Because cookies make pictures load better','Because cookies help websites run faster','Because cookies contain sensitive information like login sessions','Because cookies tell the hacker your location']
]

xss_q_response = [
    "XSS stands for Cross-Site Scripting, which is a type of attack where malicious scripts are injected into trusted websites",
    "The main goal of an XSS attack is to run malicious code in a user's web browser, allowing the hacker to steal information or control their session",
    "XSS usually attacks the user's web browser and the web pages they see, by injecting harmful scripts into legitimate content",
    "If a website doesn't check user comments, a hacker could put harmful code (like JavaScript) into the comment box, which then runs in other users' browsers",
    "An XSS attack can take over a user's web browser session, steal their cookies (which can contain login information), or redirect them to malicious sites",
    "XSS is called 'client-side' because the malicious code runs in the user's (client's) own web browser, not on the website's main server",
    "In a reflected XSS attack, the malicious code is sent to the website, immediately bounced back (reflected) to the user's browser, and then executed",
    "In a stored XSS attack, the malicious code is permanently saved (stored) on the legitimate website (e.g., in a comment or forum post) and seen by many users later when they visit that page",
    "Website developers can protect against XSS by carefully checking and cleaning (sanitising/validating) any input users type into forms to remove harmful code",
    "XSS attacks are often used to steal 'cookies' because cookies can contain sensitive information like login sessions, which allows the hacker to pretend to be the user without needing their password"
]

xss_answer_key = [1,0,0,1,2,0,1,2,2,2]

session_hijack_questions = [
    "What is the main goal of a 'session hijacking' attack?",
    "Which piece of information does a hacker steal to hijack your session?",
    "Why are these special IDs (session IDs) such a big target for hackers?",
    "How might a hacker use a public Wi-Fi network (like in a coffee shop) to hijack your session?",
    "What kind of attack involves a hacker secretly intercepting your active internet connection?",
    "Why does using 'HTTPS' (the lock icon in your browser) help protect against session hijacking?",
    "What is 'session fixation'?",
    "After successfully stealing your session, what can a hacker typically do?",
    "Why is it important for session IDs to be long, random, and hard to guess?",
    "How can cookies (small files websites put on your computer) make you vulnerable to session hijacking if they are not secure?"
]

session_hijack_answers = [
    ['To make your internet connection faster','To secretly take over your active login on a website','To send you too many pop-up ads','To make your computer crash'],
    ['Your email address','Your unique session ID (like a temporary pass)','Your computer\'s name','The website\'s color settings'],
    ['They help the website load pictures faster','Because with a session ID, a hacker can pretend to be you without your password','They tell the website what language you prefer','They are used to play music on the website'],
    ['By sending you a text message','By secretly listening to the unencrypted internet traffic to steal your session ID','By installing new software on your phone','By making the Wi-Fi signal weaker'],
    ['A Denial of Service (DoS) attack','A virus attack','A Man-in-the-Middle (MITM) attack','A phishing scam'],
    ['It makes the website text bigger','It hides your mouse cursor','It encrypts your internet traffic, so others can\'t easily see your session ID','It prevents you from downloading files'],
    ['When a hacker gives you a specific session ID, and then uses it to log in as you after you use it','When you forget your password and need to reset it','When the website automatically logs you out','When your internet connection keeps breaking'],
    ['Access your email account only','Change your desktop background','Access your account and do things as if they were you','Give you a special award'],
    ['Because shorter IDs are easier to remember','Because random IDs make it hard for hackers to guess your active login','Because it makes the website look more professional','Because it helps the website run on older computers'],
    ['If cookies are not properly secured, hackers can steal the session ID inside them','Secure cookies block pop-up ads','Insecure cookies automatically delete your browser history','Cookies prevent websites from working correctly']
]

session_hijack_q_response = [
    "The main goal of session hijacking is for a hacker to secretly take over your active login on a website or app without needing your password",
    "A hacker steals your unique session ID (like a temporary key) that your browser uses to tell the website who you are, allowing them to impersonate you",
    "Session IDs are big targets because if a hacker gets one, they can pretend to be you on the website, accessing your account without needing your username and password",
    "On public Wi-Fi, a hacker might secretly listen to unencrypted internet traffic to snatch your session ID as it travels between your device and the website",
    "A Man-in-the-Middle (MITM) attack involves a hacker secretly placing themselves between your device and the website to intercept your internet connection and steal your session token",
    "HTTPS (secure websites) encrypts all your internet traffic, including your session ID, making it much harder for a hacker to steal it while it's being sent",
    "Session fixation is a trick where a hacker gives you a specific session ID, then takes over your login after you use it and successfully log into the website",
    "After hijacking your session, a hacker can access your account and do anything you could do on that website, like view private information or make purchases",
    "Session IDs must be long, random, and hard to guess so hackers can't easily predict or force their way into your active login sessions",
    "If cookies are not properly secured, a hacker can steal the session ID stored inside them, which then allows them to use that ID to take over your active login session"
]

session_hijack_answer_key = [1,1,1,1,2,2,0,2,1,0]

supply_chain_questions = [
    "What is the main goal of a supply chain attack?",
    "Why might a hacker attack a small company that provides software to a bigger company, instead of the big company directly?",
    "Which of these is a common way a supply chain attack happens?",
    "Why are supply chain attacks particularly hard to spot and defend against?",
    "If a hacker secretly puts bad code into a popular software program *before* it's even sold or given to users, what is that called?",
    "What kind of widely used software part is often a target in these attacks?",
    "Why would a hacker hide harmful code inside a free (open-source) software part that many programs use?",
    "How can a supply chain attack stay hidden for a long time without being noticed?",
    "Imagine hackers waiting at a specific water hole for animals. In cyber, what's a 'watering hole' attack in supply chains?",
    "What can hackers do if they manage to put bad code into a software update that many people download?"
]

supply_chain_answers = [
    ['To make a network very busy','To test how quickly a company responds to attacks','To secretly get into big companies by attacking smaller, trusted partners','To launch a simple denial of service attack'],
    ['Because small companies use older computers','Because small companies often have weaker security, making them an easier way in','Because small companies have more publicly available information','Because small companies have faster internet connections'],
    ['Physically breaking into a company\'s office','Sending a lot of spam emails to employees','Putting secret bad code into a trusted software update','Changing the company\'s website colors'],
    ['They only happen late at night','They always make a computer crash right away','They secretly use things you already trust, like software updates','They only affect very old computers'],
    ['A secret message','A Trojan horse update','A compromise before distribution','An insider leak'],
    ['The computer\'s serial number','Small text fonts on websites','Free software parts (like open-source libraries) that many apps use','Smartphone apps you download from stores'],
    ['To make the software download faster','To add annoying advertisements','To infect every single application that uses that hidden bad code','To make the free software more popular'],
    ['They make the computer screen turn blue','The bad parts look like normal, trusted software and are digitally signed','They slow down how you use the computer','They make the internet connection very slow'],
    ['Attacking a website that many employees of a target company often visit to infect them','Sending fake job offers to employees','Flooding a vendor\'s server with too many requests','Stealing a CEO\'s personal laptop'],
    ['They can get control over many devices because those updates are trusted','They can only make the software run slower','They can only change the desktop background','They can only block access to social media']
]

supply_chain_q_response = [
    "The main goal of a supply chain attack is to secretly get into bigger companies by first attacking a smaller, less secure company or software component that the bigger company trusts",
    "Hackers target smaller vendors because these companies often have weaker security, making them an easier path to reach the larger, more protected target organisation",
    "A common method is for attackers to put secret bad code into trusted software updates or programs that many people then download and install, letting the bad code in",
    "Supply chain attacks are dangerous because they exploit trust in third-party tools or software, meaning the bad code comes from a source you already believe is safe, making it very hard to detect",
    "When a hacker puts bad code into software *before* it's given to users, it's called a pre-distribution compromise",
    "Free software parts (like open-source libraries) are often targeted because they are used in many different programs, so compromising one can affect thousands of applications",
    "A hacker would hide harmful code in a widely used free software part to infect every single application that depends on that code, spreading their attack far and wide",
    "Supply chain attacks can stay hidden because the malicious components often appear to be normal, trusted software (sometimes even digitally signed), so security systems don't flag them as dangerous",
    "A 'watering hole' attack in supply chains means hackers infect a website that employees of a target company (or its trusted partners) are known to visit frequently, hoping they'll get infected there",
    "If hackers compromise software updates, they gain control over many devices because those updates are seen as legitimate and are given high trust and permissions during installation"
]

supply_chain_answer_key = [2,1,2,2,2,2,2,1,0,0]

worm_questions = [
    "What makes a computer worm good at spreading by itself?",
    "What is a main difference between a 'worm' and a regular 'virus'?",
    "Why might a hacker choose to use a worm instead of a 'Trojan horse' for a big attack?",
    "How do computer worms typically move from one computer to another in a network?",
    "Which type of problem in network rules (protocols) can a worm use to spread to other unpatched computers?",
    "Why is email a common way for worms to spread?",
    "Besides just spreading, what else might a hacker want a worm to do to your computer?",
    "What would help a worm spread without being easily noticed by security tools?",
    "Why do some worms try to connect to many random internet addresses (IPs)?",
    "Which problem in how a company's computers are set up makes it easier for worms to spread inside?"
]

worm_answers = [
    ['They need someone to click on them','They require special permission to run','They can copy themselves to other computers without help from a user','They can only spread to one computer at a time'],
    ['A virus can spread without a host file, but a worm needs one','A worm can copy itself without needing to attach to another program','A worm is much bigger in size than a virus','A virus is always easier to detect than a worm'],
    ['Because worms are less powerful','Because worms only affect mobile devices','Because worms can travel between computers on their own','Because Trojan horses are never detected'],
    ['By sending text messages to other computers','By physically connecting a USB drive to every computer','By using weak spots (vulnerabilities) in network connections','By only spreading through social media posts'],
    ['A common file sharing rule (SMB)','A secure website rule (TLS)','An email sending rule (SMTP)','A secure remote access rule (SSH)'],
    ['Email content is always blocked by firewalls','Email is always encrypted so it\'s safe','People often open attachments or click links in emails without thinking','Email cannot be scanned for threats'],
    ['To make the computer run faster','To delete system logs','To steal information or install other bad software','To increase its own spreading speed'],
    ['By sending constant alerts to the user','By making the computer reboot often','By using small, hidden data packets and encryption to look normal','By changing the desktop wallpaper to a bright color'],
    ['To find vulnerable computers quickly, anywhere on the internet','To crash internet routers','To pretend to be a different type of attack','To hide its real location from security teams'],
    ['Having too many web browser extensions','Having a simple, flat network where all computers can easily talk to each other','Having strong passwords on every computer','Having disabled pop-up blockers']
]

worm_q_response = [
    "Worms are good at spreading by themselves because they can copy themselves to other computers without a user needing to do anything specific, like clicking a file",
    "A main difference is that a worm can copy itself without needing to attach to another program (a host file), while a traditional virus usually needs to infect a file to spread",
    "A hacker might choose a worm for a big attack because worms can travel between computers on their own, automatically spreading without needing users to open files or be tricked each time",
    "Worms commonly spread by using weak spots (vulnerabilities) in network connections or software, allowing them to jump from one computer to another",
    "A worm might exploit problems in the Server Message Block (SMB) protocol, a common file sharing rule, to spread to other computers that haven't fixed those weaknesses",
    "Email is a common way for worms to spread because people often open attachments or click links in emails out of curiosity or trust, accidentally activating the worm",
    "Besides just spreading, a hacker might want a worm to steal information or install other bad software (like a backdoor) to cause more damage or gain control",
    "To spread undetected, a worm would try to use small, hidden data packets and encryption so its activity looks normal and isn't flagged by security systems",
    "Some worms scan random internet addresses to find vulnerable computers quickly, anywhere on the internet, casting a wide net to find new targets",
    "A simple, flat network where all computers can easily talk to each other makes it easier for worms to spread internally, as there are fewer barriers to stop them once inside"
]

worm_answer_key = [2,1,2,2,0,2,2,2,0,1]
