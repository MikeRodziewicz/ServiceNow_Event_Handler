from dataclasses import dataclass


@dataclass
class NewIncident:
    sys_id: str
    number: str

    def __repr__(self) -> str:
        return f'this is {self.number}'

