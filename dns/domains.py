"""
All domains hosted by madefor.cc.

If you want to add your own, this is where you should do it!
"""

from typing import Dict, TypedDict

class Domain(TypedDict):
    """Required options for a domain."""

    # The CNAME record which should be created.
    cname: str


domains: Dict[str, Domain] = {
    # Please make sure to keep this sorted!

    "9551": { "cname": "9551-dev.github.io" },
    "advancedperipherals": { "cname": "advancedperipherals.netlify.app" },
    "basalt": { "cname": "pyroxenium.github.io" },
    "brag": { "cname": "bragosmagos.github.io" },
    "c3d": { "cname": "9551-dev.github.io" },
    "cash": { "cname": "mcjack123.github.io" },
    "ccloner": { "cname": "hzfishy.github.io" },
    "charmap": {"cname": "masongulu.github.io"},
    "consult" : {"cname": "1Turtle.github.io"},
    "craftos-pc": { "cname": "admiring-shannon-be238c.netlify.app" },
    "datapacks": { "cname": "cc-tweaked.github.io" },
    "epoch": { "cname": "haeleon.github.io" },
    "guih": { "cname": "9551-dev.github.io" },
    "impulsive-cc": { "cname": "emeraldimpulse7.github.io" },
    "infernity": { "cname": "infernostars.github.io" },
    "kristify": { "cname": "kristify.github.io"},
    "metis": { "cname": "squiddev-cc.github.io" },
    "mg": { "cname": "minecraftedgaming.github.io" },
    "misc": { "cname": "masongulu.github.io" },
    "monitorsize": { "cname": "masongulu.github.io" },
    "music": { "cname": "so-desperate.squiddev.cc" },
    "pecdocs": { "cname": "apethesis.github.io" },
    "phileos" : {"cname": "ryan-te.github.io"},
    "phoenix": { "cname": "phoenix-computercraft.netlify.app" },
    "plethora": { "cname": "squiddev-cc.github.io" },
    "poster": { "cname": "masongulu.github.io" },
    "potatos": { "cname": "osmarks.net" },
    "recrafted": { "cname": "ocawesome101.github.io" },
    "sanjuuni": { "cname": "mcjack123.github.io" },
    "scm": { "cname": "mc-cc-scripts.github.io" },
    "ships": {"cname":"ships.knijn.one"},
    "siredvin": {"cname": "docs-redir.siredvin.site"},
    "skydocs": { "cname": "skythecodemaster.github.io" },
    "skygui": { "cname": "skythecodemaster.github.io" },
    "thox": { "cname": "thox.touhey.pro" },
    "turtlematic": {"cname": "docs-redir.siredvin.site"},
    "unicornpkg": { "cname": "unicornpkg.github.io" },
    "upw": {"cname": "docs-redir.siredvin.site"},
    "uwuntucc": { "cname": "sall0-0p.github.io" },
    "webify": { "cname": "webify.knijn.one" },
    "wolf-os": { "cname": "cc-wolf-os.github.io" },
    "www": { "cname": "madefor.cc" },
    "youcube": { "cname": "cc-youcube.github.io" },
}
