To get going:

```
git clone https://github.com/cjw296/ddns.git
cd ddns
python3 -m venv ve
./ve/bin/pip install -r requirements.txt
```

Sample crontab:

```
@hourly ve/bin/python cloudflare.conf
```

Sample cloudflare.conf contents:

```
zone_identifier={from domain's page on cloudflare}
record_name={the full A record you want to update}
auth_email={the email address of your account}
auth_token={token scoped for Zope.DNS, read and write, for the domain the record is in}
```
