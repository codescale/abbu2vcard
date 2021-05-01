import sqlite3
from re import search
from contact import Contact, Address, EMail, Tel
from datetime import date, timedelta

con = sqlite3.connect('AddressBook-v22.abcddb')


def get_type(label):
    v_type = label or '_$!<Home>!$_'
    match = search(r"_\$!<(.*)>!\$_", v_type)
    if match:
        v_type = match.group(1).upper()
    else:
        v_type = 'HOME'
    return v_type


def get_address(contact_id):
    cur = con.cursor()
    table = cur.execute("""
    Select postal.ZCOUNTRYNAME, postal.ZSTATE, postal.ZSTREET, postal.ZZIPCODE, postal.ZCITY, postal.ZLABEL
    from zabcdpostaladdress as postal where postal.zowner == :contact_id
    """, {"contact_id": contact_id})
    addresses = []
    for row in table:
        addresses.append(
            Address(get_type(row[5]), row[0] or '', row[1] or '', row[2] or '', row[3] or '', row[4] or ''))
    return addresses


def get_email(contact_id):
    cur = con.cursor()
    table = cur.execute("""
    Select email.ZADDRESS, email.ZLABEL from ZABCDEMAILADDRESS as email where email.zowner == :contact_id
    """, {"contact_id": contact_id})
    emails = []
    for row in table:
        emails.append(
            EMail(email_type=get_type(row[1]), address=row[0] or ''))
    return emails


def get_tel(contact_id):
    cur = con.cursor()
    table = cur.execute("""
    Select phone.ZFULLNUMBER, phone.ZLABEL from ZABCDPHONENUMBER as phone where phone.zowner == :contact_id
    """, {"contact_id": contact_id})
    tels = []
    for row in table:
        tels.append(
            Tel(tel_type=get_type(row[1]), number=row[0] or ''))
    return tels


def load():
    cur = con.cursor()
    table = cur.execute("""
      Select
      record.z_pk, record.zfirstname, record.zlastname, record.znickname,
      record.zbirthdayyear, record.zbirthdayyearless,
      record.zjobtitle, record.zorganization, record.zdisplayflags,
      note.ztext
      from zabcdrecord as record
      left join ZABCDNOTE as note on record.z_pk == note.zcontact
      where ZSORTINGFIRSTNAME not NULL;""")

    contacts = []
    for row in table:
        contact_id = row[0]
        addresses = get_address(contact_id)
        emails = get_email(contact_id)
        tels = get_tel(contact_id)

        is_company = False
        if(row[8] == 1):
            is_company = True

        contact = Contact(forename=row[1], surename=row[2], nickname=row[3], is_company=is_company,
                          company=row[7], addresses=addresses, emails=emails, tels=tels, note=row[9])
        if(row[4]):
            bday = date(row[4], 1, 1) + timedelta(seconds=row[5])
            contact.bday = "{}-{}-{}".format(bday.year, bday.month, bday.day)
        contacts.append(contact)

    return contacts
