To get going:

```bash
git clone https://github.com/cjw296/ddns.git
cd ddns
uv sync
docker build -t ddns:dev .
```

Run it:

```
uv run client.py cloudflare.conf 
docker run -v $(pwd)/cloudflare.conf:/cloudflare.conf ddns:dev /cloudflare.conf -v
```

Sample cloudflare.conf contents:

```
zone_identifier={from domain's page on cloudflare}
record_name={the full A record you want to update}
auth_email={the email address of your account}
auth_token={token scoped for Zope.DNS, read and write, for the domain the record is in}
```
