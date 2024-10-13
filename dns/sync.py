"""Sync DNS records with our registrar"""

from dataclasses import dataclass
import os
import logging
import sys
from typing import List, NamedTuple, Set

import requests

import dns.log
from dns.domains import Domain, domains


@dataclass
class AddDomain:
    name: str
    info: Domain


@dataclass
class UpdateDomain:
    name: str
    id: str
    info: Domain


root = "madefor.cc"


class ApiClient:
    def __init__(self, session: requests.Session, *, api_key: str, api_secret: str) -> None:
        self._session = session
        self._secrets = {"apikey": api_key, "secretapikey": api_secret}

    def request(self, path: str, args: dict = {}) -> dict:
        with self._session.post(
            f"https://api.porkbun.com/api/json/v3/dns{path}",
            json={**args, **self._secrets},
            timeout=5,
        ) as response:
            if response.status_code not in (200, 201):
                raise RuntimeError(f"Failed in request to {path} with {response.status_code}")

            return response.json()


def make_zone(name: str, info: Domain) -> dict:
    return {
        "name": name,
        "type": "CNAME",
        "content": info["cname"],
    }


def sync(client: ApiClient) -> None:
    existing_domains = client.request(f"/retrieve/{root}", {})["records"]

    remove: List[str] = []
    add: List[AddDomain] = []
    update: List[UpdateDomain] = []
    known: Set[str] = set()

    for record in existing_domains:
        if record["type"] != "CNAME":
            continue

        domain_id: str = record["id"]
        name: str = record["name"][: -len(root) - 1]
        known.add(name)

        if name not in domains:
            logging.warning(f"Removing record for {name}")
            remove.append(domain_id)
        else:
            domain = domains[name]
            old: str = record["content"]
            new: str = domain["cname"]
            if old.lower() != new.lower():
                logging.info(f"Updating record for {name} ({old} → {new})")
                update.append(UpdateDomain(name=name, id=domain_id, info=domain))
            else:
                logging.info(f"Nothing to do for {name}")

    for name, domain in domains.items():
        if name not in known:
            logging.info(f"Adding record for {name} ({domain['cname']})")
            add.append(AddDomain(name=name, info=domain))

    logging.warning("Applying DNS changes.")

    for record in add:
        client.request(f"/create/{root}", make_zone(record.name, record.info))

    for record in update:
        client.request(
            f"/edit/{root}/{record.id}",
            make_zone(record.name, record.info),
        )

    for record in remove:
        client.request(f"/delete/{root}/{record}")

    logging.warning("Done.")


def main() -> None:
    api_key = os.getenv("PORKBUN_API_KEY")
    api_secret = os.getenv("PORKBUN_API_SECRET")
    if not api_key or not api_secret:
        sys.stderr.write("Need API key and secret")
        sys.exit(1)

    with requests.Session() as session:
        sync(ApiClient(session, api_key=api_key, api_secret=api_secret))


if __name__ == "__main__":
    dns.log.configure()
    main()
