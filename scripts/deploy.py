from brownie import network, config, accounts, Contract, MortToken


def main():
    token = deploy(False)


def get_account(local=True):
    if local == True:
        return accounts[0]
    else:
        return accounts.load("development-bs-738")


def deploy(local=True):
    account = get_account(local)
    token = MortToken.deploy(1000000, {"from": account}, publish_source=True)
    print(f"Deployed at {token.address}")
    return token
