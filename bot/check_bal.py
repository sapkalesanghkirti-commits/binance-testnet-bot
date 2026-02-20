from client import get_client   # if no bot folder use: from client import get_client

client = get_client()

balance = client.futures_account_balance()

print("\nFUTURES BALANCE:\n")

for asset in balance:
    if asset["asset"] == "USDT":
        print("Asset:", asset["asset"])
        print("Total Balance:", asset["balance"])
        print("Available Balance:", asset["availableBalance"])