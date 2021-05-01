
class Address:
    def __init__(self, adr_type='HOME', country='', state='', street='', zipcode='', city=''):
        self.adr_type = adr_type
        self.country = country
        self.state = state
        self.street = street
        self.zipcode = zipcode
        self.city = city


class Tel:
    def __init__(self, number, tel_type='HOME'):
        self.tel_type = tel_type
        self.number = number


class EMail:
    def __init__(self, address, email_type='HOME'):
        self.email_type = email_type
        self.address = address


class Contact:
    def __init__(self, forename, surename, bday=None, nickname='', is_company=False, company='', addresses=None, emails=None, tels=None, note=''):
        self.forename = forename
        self.surename = surename
        self.bday = bday
        self.nickname = nickname
        self.is_company = is_company
        self.company = company
        self.addresses = addresses
        self.emails = emails
        self.tels = tels
        self.note = note
