"""
Sync DNS records to CloudFlare

This expects your CloudFlare token to be located in
~/.cloudflare/cloudflare.cfg. That said, it is unlikely anyone but me will be
running this :).
"""

import sys
import logging
from typing import Set, NamedTuple, List

from CloudFlare import CloudFlare

from dns.domains import Domain, domains
import dns.log


class AddDomain(NamedTuple):
    name: str
    info: Domain


class UpdateDomain(NamedTuple):
    name: str
    id: str
    info: Domain


root = "madefor.cc"


def make_zone(name: str, info: Domain) -> dict:
    return {
        "name": name,
        "type": "CNAME",
        "content": info["cname"],
        "proxied": info.get("cloudflare", False),
    }


def main() -> None:
    cloudflare = CloudFlare()
    zones = cloudflare.zones.get(params={"name": root, "per_page": 1})
    if not zones:
        sys.stdout.write("Cannot find domain")
        sys.exit(1)

    zone_id: str = zones[0]["id"]
    existing_domains = cloudflare.zones.dns_records.get(zone_id)

    remove: List[str] = []
    add: List[AddDomain] = []
    update: List[UpdateDomain] = []
    known: Set[str] = set()

    for record in existing_domains:
        if record["type"] != "CNAME":
            continue

        domain_id: str = record["id"]
        name: str = record["name"][:-len(root) - 1]
        known.add(name)

        if name not in domains:
            logging.warning(f"Removing record for {name}")
            remove.append(domain_id)
        else:
            domain = domains[name]
            old, new = record["content"], domain["cname"]
            if old != new or record["proxied"] != domain.get("cloudflare", False):
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
        cloudflare.zones.dns_records.post(zone_id, data=make_zone(record.name, record.info))

    for record in update:
        cloudflare.zones.dns_records.put(zone_id, record.id, data=make_zone(record.name, record.info))

    for record in remove:
        cloudflare.zones.dns_records.delete(zone_id, record)

    logging.warning("Done.")


if __name__ == "__main__":
    dns.log.configure()
    main()
