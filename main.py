import os
import errno

import abcddb
import vcard

contacts = abcddb.load()

exportFolder = os.path.abspath("addressbook")
if not os.path.exists(exportFolder):
    try:
        os.makedirs(exportFolder)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise

for contact in contacts:
    filename = contact.company if contact.is_company else "{} {}".format(
        contact.forename, contact.surename)
    filename = filename.replace("/","_")
    f = open("{}/{}.vcf".format(exportFolder, filename), "w")
    f.write(vcard.create(contact))
    f.close()
