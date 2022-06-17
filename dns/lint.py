import sys
import logging
from difflib import SequenceMatcher
from typing import List

from dns.domains import domains
import dns.log


def write_diff(prefix: str, domain_list: List[str], start: int, end: int):
    for i in range(start, end):
        print(f"{prefix}{domain_list[i]}\33[0m")


def main() -> None:
    valid = True

    domain_list = list(domains.keys())
    sorted_domain_list = sorted(domain_list)

    # Ensure the list is sorted.
    if domain_list != sorted_domain_list:
        logging.error("Domain list is not sorted")

        matcher = SequenceMatcher(None, domain_list, sorted_domain_list)
        for tag, alo, ahi, blo, bhi in matcher.get_opcodes():
            if tag == "insert":
                write_diff("\033[32m +", sorted_domain_list, blo, bhi)
            elif tag == "delete":
                write_diff("\033[31m -", domain_list, alo, ahi)
            elif tag == "equal":
                write_diff("  ", domain_list, alo, ahi)
            elif tag == "replace":
                write_diff("\033[31m *", domain_list, alo, ahi)
                write_diff("\033[32m *", sorted_domain_list, blo, bhi)

    # Ensure CNAMEs are valid(ish). We only need to catch the common case of people using URLs instead of domains.
    for domain, info in domains.items():
        cname = info["cname"]
        if "/" in info["cname"]:
            logging.error(
                "Invalid CNAME '%s' for '%s'. This should be a domain name, not a URL",
                cname,
                domain,
            )

            cname = cname.removeprefix("https://").removeprefix("http://")
            if "/" in cname and (idx := cname.index("/")) and idx > 0:
                cname = cname[0:idx]

            if "/" not in cname:
                logging.info("Maybe try '%s' instead?", cname)

    sys.exit(0 if valid else 1)


if __name__ == "__main__":
    dns.log.configure()
    main()
