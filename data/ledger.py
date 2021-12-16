from xrpl.clients import JsonRpcClient
from xrpl.models.requests.account_info import AccountInfo

JSON_RPC_URL = "https://s2.ripple.com:51234/"
client = JsonRpcClient(JSON_RPC_URL)

acct_info = AccountInfo(
    account="rMPoP2EXVHW7ZYt93rzLD59oo1MdkkVnkx",
    ledger_index="validated",
    strict=True,
)
response = client.request(acct_info)
result = response.result
print("response.status: ", response.status)
import json
print(json.dumps(response.result, indent=4, sort_keys=True))