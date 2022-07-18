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

    "basalt": { "cname": "pyroxenium.github.io" },
    "brag": { "cname": "bragosmagos.github.io" },
    "cash": { "cname": "mcjack123.github.io" },
    "ccsimplegui": { "cname": "masongulu.github.io" },
    "consult" : {"cname": "1Turtle.github.io"},
    "craftos-pc": { "cname": "admiring-shannon-be238c.netlify.app" },
    "freax": { "freax.netlify.app" },
    "gemstone": { "cname": "gemstone.znepb.me" },
    "guih": { "cname": "9551-dev.github.io" },
    "impulsive-cc": { "cname": "emeraldimpulse7.github.io" },
    "infernity": { "cname": "infernostars.github.io" },
    "metis": { "cname": "squiddev-cc.github.io" },
    "music": { "cname": "autoclave.squiddev.cc" },
    "pecdocs": { "cname": "apethesis.github.io" },
    "phileos" : {"cname": "ryan-te.github.io"},
    "phoenix": { "cname": "phoenix-computercraft.netlify.app" },
    "plethora": { "cname": "squiddev-cc.github.io" },
    "potatos": { "cname": "osmarks.net" },
    "recrafted": { "cname": "ocawesome101.github.io" },
    "skydocs": { "cname": "skythecodemaster.github.io" },
    "skygui": { "cname": "skythecodemaster.github.io" },
    "thox": { "cname": "thox.touhey.pro" },
    "wolf-os": { "cname": "cc-wolf-os.github.io" },
    "www": { "cname": "madefor.cc" },
}
