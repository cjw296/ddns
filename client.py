import logging
from argparse import ArgumentParser, FileType

import requests
from requests import Session


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('config', type=FileType())
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()
    return args


def parse_config(raw):
    config = {}
    for line in raw.splitlines():
        key, value = line.split('=', 1)
        config[key] = value.strip()
    return config


def lookup_ip():
    raw = requests.get('https://cloudflare.com/cdn-cgi/trace').text
    return parse_config(raw)['ip']


def main():
    args = parse_args()
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)

    config = parse_config(args.config.read())
    zone_identifier = config['zone_identifier']
    record_name = config['record_name']

    base = 'https://api.cloudflare.com/client/v4'

    session = Session()
    session.headers.update({
        'X-Auth-Email': config['auth_email'],
        'Authorization': 'Bearer '+config['auth_token'],
    })

    response = session.get(
        f'{base}/zones/{zone_identifier}/dns_records',
        params={'type': 'A', 'name': record_name}
    )
    response.raise_for_status()
    data = response.json()
    logging.debug(data)

    records_found = data['result_info']['total_count']
    if records_found != 1:
        raise ValueError(f'Found {records_found} records for {record_name}')

    record = data['result'][0]

    current_ip = lookup_ip()
    record_ip = record['content']

    if current_ip != record_ip:
        response = session.patch(
            f"{base}/zones/{zone_identifier}/dns_records/{record['id']}",
            json={'content': current_ip}
        )
        logging.debug(response.json())
        response.raise_for_status()


if __name__=='__main__':
    main()
