from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
import json
from dataclasses import is_dataclass, fields

def to_dict(obj):
    response = {}

    if is_dataclass(obj):
        for field in fields(obj):
            response[field.name] = to_dict(getattr(obj, field.name))

    # isinstance(obj, Union[]) did not work due to something with Subscriptable generics
    elif type(obj) in [str, int, bool]:
        return obj

    elif type(obj) == list:
        return [to_dict(item) for item in obj]

    else:
        return None

    return response


# CamelCase is necessary for dataclasses_json to work
@dataclass_json
@dataclass
class TakerPays:
    currency: str
    issuer: str
    value: str

@dataclass_json
@dataclass
class Offers:
    Account: str
    BookDirectory: str
    BookNode: str
    Flags: int
    LedgerEntryType: str
    OwnerNode: str
    PreviousTxnID: str
    PreviousTxnLgrSeq: int
    Sequence: int
    TakerGets: str
    TakerPays: TakerPays
    index: str
    owner_funds: str = None
    quality: str = None
    taker_gets_funded: str = None
    taker_pays_funded: TakerPays = None
            

@dataclass_json
@dataclass
class Warnings:
    id: int
    message: str

@dataclass_json
@dataclass
class Result:
    ledger_hash: str
    ledger_index: int
    offers: List[Offers]
    validated: bool
    warnings: List[Warnings]

@dataclass_json
@dataclass
class Response:
    id: int
    result: Result
    status: str = None
    type: str = None
    
    def to_dict(self):
        return to_dict(self)

    def pretty_print(self):
        print(json.dumps(to_dict(self), sort_keys=True, indent=4))