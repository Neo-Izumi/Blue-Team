dic_user = {}

class user_attribute:
    
    def __init__(self):
        self.alert = False
        self.alert_check = {
            'check': False,
            'mess': False
        }
        self.ca = False
        self.incident = False
        self.ftp = False
        self.ftp_process = 0
        self.pen = False
        self.pen_process = {
            'disconnect': False,
            'backup': False,
            'roll_back': False,
            'restore': False,
            'research': False,
            'netflow': False,
            'finish': False
        }
        self.rep = False
        self.rep_process = {
            'check': False,
            'snort': False,
            'kibana': False,
            'report': False,
            'finish': False
        }
        self.ssh = False
        self.ssh_process = {
            'ssh': False,
            'whitelist': False,
            'acl': False,
            'finish': False
        }