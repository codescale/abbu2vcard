# ABBU to vCards

If you have exported a "Contacts Archive" from your apple addressbook you end up with a ABBU file.

But actually you can't use the same application (Apple Addressbook) to import your contacts from this archive.

## Install

You can download the binary from the release page or buid it yourself.

## Use

First you have to get the database file out of your "Contacts Archive". 

- Right click and select `Show Package Contents`
- Open folder `Sources`

There may be multiple folders inside, each containing a `AddressBook-v22.abcddb` file. Those are the database files we're looking for.

- Copy the `AddressBook-v22.abcddb` file into the same folder as `abbu2vcard`
- Open the `Terminal` and run `abbu2vcard`

All the contacts from the database should now be exported in to an `addressbook` folder.

## Build

```sh
pip3 install vobject
pip3 install pyinstaller
pyinstaller main.py --onefile --name abbu2vcard
```