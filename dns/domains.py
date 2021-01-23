"""
All domains hosted by madefor.cc.

If you want to add your own, this is where you should do it!
"""

from typing import Dict, TypedDict


class DomainOptional(TypedDict, total=False):
    """Optional options for a domain."""

    # Whether to proxy through cloudflare or not. Defaults to false.
    cloudflare: bool


class Domain(DomainOptional):
    """Required options for a domain."""

    # The CNAME record which should be created.
    cname: str


domains: Dict[str, Domain] = {
    # Please make sure to keep this sorted!

    "impulses-cc-programs": { "cname": "emeraldimpulse7.github.io" },
    "cash": { "cname": "mcjack123.github.io" },
    "craftos-pc": { "cname": "admiring-shannon-be238c.netlify.app" },
    "metis": { "cname": "squiddev-cc.github.io" },
    "plethora": { "cname": "squiddev-cc.github.io" },
    "potatos": { "cname": "osmarks.tk" },
    "skydocs": { "cname": "skythecodemaster.github.io" },
    "www": { "cname": "madefor.cc" },
}
