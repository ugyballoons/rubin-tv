from ast import For
from dataclasses import dataclass, field
from datetime import datetime
from typing import Tuple
from unicodedata import name

@dataclass
class Telescope:
    name: str
    slug: str
    # bucketname: str
    online: bool

@dataclass
class Channel:
    name: str
    prefix: str
    endpoint: str
    css_class: str

@dataclass
class Image:
    url: str
    name: str = field(init=False)
    date: datetime = field(init=False)
    seq: int = field(init=False)
    chans: list = field(init=False)

    def parse_filename(self, delimiter: str = "_") -> Tuple:
        name = self.url.split("/")[
            -1
        ]  # We know the name is the last part of the URL
        nList = name.split(delimiter)
        date = nList[2]
        seq = nList[4][:-4]  # Strip extension
        return (name, datetime.strptime(date, "%Y-%m-%d"), int(seq))

    def cleanDate(self) -> str:
        return self.date.strftime("%Y-%m-%d")

    def humanDate(self) -> str:
        return self.date.strftime("%a %d/%m/%Y")

    def __post_init__(self) -> None:
        self.name, self.date, self.seq = self.parse_filename()
        self.chans = []

# channels = {
#     "monitor": Channel(
#         name="AuxtelMonitor",
#         prefix="auxtel_monitor",
#         endpoint="monitorevents",
#     ),
#     "spec": Channel(
#         name="SpecExamine", prefix="summit_specexam", endpoint="specevents"
#     ),
#     "im": Channel(
#         name="ImExamine", prefix="summit_imexam", endpoint="imevents"
#     ),
#     "mount": Channel(
#         name="AuxtelTorques",
#         prefix="auxtel_mount_torques",
#         endpoint="mountevents",
#     ),
# }

# print(channels['monitor'])