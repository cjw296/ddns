git clone https://github.com/cjw296/ddns.git
cd ddns
virtualenv ve
./ve/bin/pip install -r requirements.txt

@hourly ve/bin/python auth.ini https://some/url

auth.ini contents:
username:password
