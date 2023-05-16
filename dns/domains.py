"""
All domains hosted by madefor.cc.

If you want to add your own, this is where you should do it!
"""

from typing import Dict, TypedDict, Optional


class Domain(TypedDict):
    """Required options for a domain."""

    # The CNAME record which should be created.
    cname: str
    source_url: Optional[str]


domains: Dict[str, Domain] = {
    # Please make sure to keep this sorted!

    "9551": Domain(cname="9551-dev.github.io", source_url="https://github.com/9551-Dev/9551-dev.github.io"),
    "advancedperipherals": Domain(cname="advancedperipherals.netlify.app", source_url="https://github.com/SirEndii/AdvancedPeripherals"),
    "basalt": Domain(cname="pyroxenium.github.io", source_url="https://github.com/Pyroxenium/Basalt"),
    "brag": Domain(cname="bragosmagos.github.io"),
    "c3d": Domain(cname="9551-dev.github.io", source_url="https://github.com/9551-Dev/C3D"),
    "cash": Domain(cname="mcjack123.github.io", source_url="https://github.com/MCJack123/cash"),
    "consult": Domain(cname="1Turtle.github.io", source_url="https://github.com/1Turtle/CONSULT"),
    "craftos-pc": Domain(cname="admiring-shannon-be238c.netlify.app", source_url="https://github.com/MCJack123/craftos2"),
    "freax": Domain(cname="freax.netlify.app"),
    "guih": Domain(cname="9551-dev.github.io", source_url="https://github.com/9551-Dev/GuiH"),
    "impulsive-cc": Domain(cname="emeraldimpulse7.github.io", source_url="https://github.com/EmeraldImpulse7/impulsive-cc"),
    "infernity": Domain(cname="infernostars.github.io"),
    "kristify": Domain(cname="kristify.github.io", source_url="https://github.com/Kristify/kristify"),
    "metis": Domain(cname="squiddev-cc.github.io", source_url="https://github.com/SquidDev-CC/metis"),
    "misc": Domain(cname="masongulu.github.io", source_url="https://github.com/MasonGulu/CC-MISC"),
    "monitorsize": Domain(cname="masongulu.github.io", source_url="https://github.com/MasonGulu/CC_Monitor_Size"),
    "music": Domain(cname="autoclave.squiddev.cc", source_url="https://github.com/SquidDev-CC/music.madefor.cc"),
    "pecdocs": Domain(cname="apethesis.github.io"),
    "phileos": Domain(cname="ryan-te.github.io", source_url="https://github.com/Ryan-Te/PhileOS-OC"),
    "phoenix": Domain(cname="phoenix-computercraft.netlify.app"),
    "plethora": Domain(cname="squiddev-cc.github.io", source_url="https://github.com/SquidDev-CC/plethora"),
    "poster": Domain(cname="masongulu.github.io", source_url="https://github.com/MasonGulu/2dj-site"),
    "potatos": Domain(cname="osmarks.net", source_url="https://git.osmarks.net/osmarks/potatOS"),
    "recrafted": Domain(cname="ocawesome101.github.io"),
    "scm": Domain(cname="mc-cc-scripts.github.io", source_url="https://github.com/mc-cc-scripts/script-manager"),
    "ships": Domain(cname="ships.knijn.one"),
    "skydocs": Domain(cname="skythecodemaster.github.io", source_url="https://github.com/SkyTheCodeMaster/SkyDocs"),
    "skygui": Domain(cname="skythecodemaster.github.io", source_url="https://github.com/SkyTheCodeMaster/cc-gui"),
    "thox": Domain(cname="thox.touhey.pro", source_url="https://forge.touhey.org/cc/thox.git/"),
    "unicornpkg": Domain(cname="unicornpkg.github.io", source_url="https://github.com/unicornpkg"),
    "uwuntucc": Domain(cname="sall0-0p.github.io", source_url="https://github.com/sall0-0p/Dragonstone"),
    "webify": Domain(cname="webify.knijn.one", source_url="https://github.com/knijn/webify"),
    "wolf-os": Domain(cname="cc-wolf-os.github.io", source_url="https://github.com/cc-wolf-os"),
    "www": Domain(cname="madefor.cc", source_url="https://github.com/SquidDev-CC/madefor.cc"),
    "youcube": Domain(cname="cc-youcube.github.io", source_url="https://github.com/CC-YouCube"),
}
