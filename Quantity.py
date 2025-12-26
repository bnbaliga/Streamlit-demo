from dataclasses import dataclass
from typing import Dict

from Unit import Unit

@dataclass
class Quantity:
    std_unit: str
    units: Dict[str, Unit]