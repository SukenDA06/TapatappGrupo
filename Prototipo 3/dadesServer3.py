class Account:
    def __init__(self, acc_id, user_name, passwd, mail):
        self.acc_id = acc_id
        self.user_name = user_name
        self.passwd = passwd
        self.mail = mail
    
    def __str__(self):
        return self.user_name + ":" + self.passwd + ":" + self.mail

accounts = [
    Account(acc_id=1, user_name="mama", passwd="12345", mail="test@gmail.com"),
    Account(acc_id=2, user_name="papa", passwd="123", mail="test2@gmail.com"),
]

class Infant:
    def __init__(self, inf_id, inf_name, avg_sleep, therapy_id, duration):
        self.inf_id = inf_id
        self.inf_name = inf_name
        self.avg_sleep = avg_sleep
        self.therapy_id = therapy_id
        self.duration = duration

    def __str__(self):
        return "Infant Id:" + str(self.inf_id) + " Name:" + self.inf_name

infants = [
    Infant(inf_id=1, inf_name="Carla Infant", avg_sleep=8, therapy_id=1, duration=6),
    Infant(inf_id=2, inf_name="Jake Infant", avg_sleep=10, therapy_id=2, duration=6)
]

class Tap:
    def __init__(self, inf_id, cond_id):
        self.inf_id = inf_id
        self.cond_id = cond_id
    
    def __str__(self):
        return " Infant Id:" + str(self.inf_id) + " Condition Id:" + str(self.cond_id)

Taps = [
    Tap(inf_id=1, cond_id=1),
    Tap(inf_id=2, cond_id=2)
]

relation_acc_infant = [
    {"acc_id": 1, "inf_id": 1, "role_id": 1},
    {"acc_id": 1, "inf_id": 1, "role_id": 2},
    {"acc_id": 2, "inf_id": 2, "role_id": 1},
    {"acc_id": 2, "inf_id": 2, "role_id": 2}
]

class Position:
    def __init__(self, user_name, role_type):
        self.user_name = user_name
        self.role_type = role_type

    def __str__(self):
        return "User Name: " + str(self.user_name) + " Role Type:" + self.role_type

positions = [
    Position(user_name="mama", role_type='Admin'),
    Position(user_name="papa", role_type='Tutor Mama Papa'),
    Position(user_name="guardian", role_type='Caregiver'),
    Position(user_name="monitor", role_type='Follow-up')
]

class Condition:
    def __init__(self, cond_id, inf_id, cond_name):
        self.cond_id = cond_id
        self.inf_id = inf_id
        self.cond_name = cond_name

    def __str__(self):
        return "Condition Id:" + str(self.cond_id) + " Name:" + self.cond_name + " Infant Id:" + str(self.inf_id)

conditions = [
    Condition(cond_id=1, inf_id=1, cond_name="sleep"),
    Condition(cond_id=2, inf_id=2, cond_name="awake"),
    Condition(cond_id=3, inf_id=1, cond_name="yes_eyepatch"),
    Condition(cond_id=4, inf_id=2, cond_name="no_eyepatch")
]

class Therapy:
    def __init__(self, therapy_id, inf_id, therapy_name):
        self.therapy_id = therapy_id
        self.inf_id = inf_id
        self.therapy_name = therapy_name

    def __str__(self):
        return "Therapy Id:" + str(self.therapy_id) + " Name:" + self.therapy_name

therapies = [
    Therapy(therapy_id=1, inf_id=1, therapy_name='Hour'),
    Therapy(therapy_id=2, inf_id=2, therapy_name='Percentage')
]