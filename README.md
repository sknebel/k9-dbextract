# k9-dbextract
Simple Python script to extract password &amp; connection details from K9 Mail configuration files

## how to use
Copy the the K9 Mail configuration database from your phone (using adb or a file manager, requires a rooted phone) to your computer or extract it from a backup. It's located unter /data/data/com.fsck.k9/databases/preferences_storage. Run `k9-dbextract.py` in the same folder. 

It then outputs all configured profiles and their connection information:

  $ python3 k9-dbextract.py
  profile-name : imap://username:password@mail.example.com:port
