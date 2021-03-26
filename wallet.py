from dearpygui.core import *
from dearpygui.simple import *
from bitcoinlib.wallets import *
from bitcoinlib.mnemonic import *
from bitcoinlib.keys import *
from bitcoinlib.services.services import *


def get_estimated_fee(sender, data):

    pass

def send_transaction(sender, data):
    config = get_item_configuration('currency_combo_1')['items']
    wallet = Wallet(config[data])
    amount = get_value('input_combo1')
    address = get_value('input_combo2')
    transaction = wallet.send_to(address, amount)
    set_value("status_label", f"Transaction ID: {transaction}")

def collect_wallets():
    wal = []
    if wallet_exists("xWallet"):
        wal.append("xWallet")
    if wallet_exists("xWallet2"):
        wal.append("xWallet2")
    if wallet_exists("xWallet3"):
        wal.append("xWallet3")
    return wal

def scan_wallets():
    wallets = collect_wallets()
    for i in wallets:
        w  = Wallet(i)
        w.scan()

def create_custom_wallet(sender, data):
    wallet_1 = wallet_exists("xWallet")
    wallet_2 = wallet_exists("xWallet2")
    wallet_3 = wallet_exists("xWallet3")
    list_of_wallets = collect_wallets()
    passphrase = Mnemonic().generate()
    n = get_item_configuration("network_combo")["items"]
    s = get_value("network_combo")
    selected_network = n[s]
    if list_of_wallets == 3:
        set_value("Status", "You have too many wallets")
    if selected_network == "":
        set_value("Status", "No network selected")
    else:
        if wallet_1 is False and wallet_2 is False and wallet_3 is False: # 000
            Wallet.create("xWallet", keys=passphrase, network=selected_network)
            set_value("Status", f"{passphrase}")
            pass
        if wallet_1 is False and wallet_2 is False and wallet_3 is True: # 001
            Wallet.create("xWallet", keys=passphrase, network=selected_network)
            set_value("Status", f"{passphrase}")
            pass
        if wallet_1 is False and wallet_2 is True and wallet_3 is False: # 010
            Wallet.create("xWallet", keys=passphrase, network=selected_network)
            set_value("Status", f"{passphrase}")
            pass
        if wallet_1 is False and wallet_2 is True and wallet_3 is True: # 011
            Wallet.create("xWallet", keys=passphrase, network=selected_network)
            set_value("Status", f"{passphrase}")
            pass
        if wallet_1 is True and wallet_2 is False and wallet_3 is False: # 100
            Wallet.create("xWallet2", keys=passphrase, network=selected_network)
            set_value("Status", f"{passphrase}")
            pass
        if wallet_1 is True and wallet_2 is False and wallet_3 is True: # 101
            Wallet.create("xWallet2", keys=passphrase, network=selected_network)
            set_value("Status", f"{passphrase}")
            pass
        if wallet_1 is True and wallet_2 is True and wallet_3 is False: # 110
            Wallet.create("xWallet3", keys=passphrase, network=selected_network)
            set_value("Status", f"{passphrase}")
            pass
        if wallet_1 is True and wallet_2 is True and wallet_3 is True: # 111
            pass



def create_custom_wallet_with_seed():
    wallet_1 = wallet_exists("xWallet")
    wallet_2 = wallet_exists("xWallet2")
    wallet_3 = wallet_exists("xWallet3")

    list_of_wallets = collect_wallets()
    seed = Mnemonic().to_seed(get_value("wallet_seed"))
    key = HDKey().from_seed(seed)

    n = get_item_configuration("recover_network_combo")["items"]
    s = get_value("recover_network_combo")

    selected_network = n[s]

    if list_of_wallets == 3:
        set_value("recover_status", "Too many wallets")
    if selected_network == "":
        set_value("Status", "No network selected")
    else:
        if wallet_1 is False and wallet_2 is False and wallet_3 is False: # 000
            Wallet.create("xWallet", keys=key, network=selected_network)
            set_value("recover_status", "Recovered succesfully")
            pass
        if wallet_1 is False and wallet_2 is False and wallet_3 is True: # 001
            Wallet.create("xWallet", keys=key, network=selected_network)
            set_value("recover_status", "Recovered succesfully")
            pass
        if wallet_1 is False and wallet_2 is True and wallet_3 is False: # 010
            Wallet.create("xWallet", keys=key, network=selected_network)
            set_value("recover_status", "Recovered succesfully")
            pass
        if wallet_1 is False and wallet_2 is True and wallet_3 is True: # 011
            Wallet.create("xWallet", keys=key, network=selected_network)
            set_value("recover_status", "Recovered succesfully")
            pass
        if wallet_1 is True and wallet_2 is False and wallet_3 is False: # 100
            Wallet.create("xWallet2", keys=key, network=selected_network)
            set_value("recover_status", "Recovered succesfully")
            pass
        if wallet_1 is True and wallet_2 is False and wallet_3 is True: # 101
            Wallet.create("xWallet2", keys=key, network=selected_network)
            set_value("recover_status", "Recovered succesfully")
            pass
        if wallet_1 is True and wallet_2 is True and wallet_3 is False: # 110
            Wallet.create("xWallet3", keys=key, network=selected_network)
            set_value("recover_status", "Recovered succesfully")
            pass
        if wallet_1 is True and wallet_2 is True and wallet_3 is True: # 111
            pass
