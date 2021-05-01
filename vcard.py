import vobject


def create(contact):
    vcard = vobject.vCard()
    vcard.add('n').value = vobject.vcard.Name(
        family=contact.surename or '', given=contact.forename or '')
    if(contact.is_company):
        vcard.add('fn').value = contact.company
        vcard.add('X-ABShowAs').value = "COMPANY"
    else:
        vcard.add('fn').value = "{} {}".format(
            contact.forename, contact.surename)
    vcard.add('nickname').value = contact.nickname or ''
    vcard.add('org').value = [contact.company or '']
    vcard.add('note').value = contact.note or ''
    if(contact.addresses):
        for address in contact.addresses:
            adr = vcard.add('adr')
            adr.value = vobject.vcard.Address(
                street=address.street, city=address.city, code=address.zipcode, country=address.country, region=address.state)
            adr.type_param = address.adr_type
    if(contact.emails):
        for email in contact.emails:
            vemail = vcard.add('email')
            vemail.value = email.address
            vemail.type_param = email.email_type
    if(contact.tels):
        for tel in contact.tels:
            vtel = vcard.add('tel')
            vtel.value = tel.number
            vtel.type_param = tel.tel_type
    if(contact.bday):
        vcard.add('bday').value = contact.bday
    return vcard.serialize()
