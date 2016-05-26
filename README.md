To get going:

```
git clone https://github.com/cjw296/ddns.git
cd ddns
virtualenv ve
./ve/bin/pip install -r requirements.txt
```

Sample crontab:

```
@hourly ve/bin/python auth.txt https://some/url
```

Sample auth.txt contents:

```
username:password
```
