from dearpygui.core import *
from dearpygui.simple import *
from bitcoinlib.wallets import *
from bitcoinlib.mnemonic import *

from colors import set_theme_light, set_theme_dark
from fade import *
from finance import *
from wallet import *

import threading
import time
import numpy as np
import yfinance as yf
import pyperclip

def check_for_wallets():
    list_of_wallets = collect_wallets()
    if list_of_wallets is None:
        with child("not_found", parent="graph_child_1", width=280, height=80, horizontal_scrollbar=True):
            add_text("No wallets found")
            center_item("No wallets found")
            add_button("+", height=40, width=40, callback=double_whammy)
            center_item("+")
            end()
    else:
        if does_item_exist("dash"):
            configure_item("currency_combo_1", items=list_of_wallets)
            for i in list_of_wallets:
                n = Wallet(i)
                network = n.network_list()[0]
                address = n.addresslist()[0]
                balance = n.balance()
                if does_item_exist(f"wallet_{i}"):
                    delete_item(f"wallet_{i}")
                with child(f"wallet_{i}", parent="graph_child_1", width=400, height=95, no_scrollbar=True):
                    add_text(f"Wallet name: {i}")
                    add_text(f"Network: {network}")
                    #add_text(f"Address: {address}")
                    add_text(f"Balance: {balance}")
                    add_same_line()
                    add_button(f"Details_{i}", callback=show_details, callback_data=i, label="Details")
                    add_same_line()
                    add_button(f"Delete_{i}", callback=delete_wallet, callback_data=i, label="Delete")

def go_back(sender, data):
    if does_item_exist(data):
        fade_out("test")
        delete_item(data)
        show_dashboard_ui()
        check_for_wallets()
        fade_in("test")

def show_WIF():
    n = get_value("Show WIF")
    if n is False:
        configure_item("WIF", show=False)
    else:
        configure_item("WIF", show=True)

def show_details(sender, data):
    if does_item_exist("dash") is True:
        fade_out("test")
        delete_item("dash")
        show_details_ui(data)
        fade_in("test")
        pass
    if does_item_exist("home") is True:
        fade_out("test")
        delete_item("home")
        show_details_ui(data)
        fade_in("test")
        pass

def add_wallet():
    # 000, 100, 010, 001, 110, 101, 001, 111
    list_of_wallets = collect_wallets()
    if len(list_of_wallets) >= 3:
        set_value("status_label", "You have too many wallets")
    else:
        fade_out("test")
        delete_item("dash")
        add_wallet_ui()
        fade_in("test")

def set_theme(sender, data):
    d = get_value("Themes")
    if (d == 0):
        set_theme_dark()
    if (d == 1):
        set_theme_light()


def show_settings_ui():
    with group("settings", parent="ui_group"):
        with child("settings_group", width=800, height=750):
            add_button("Back", callback=go_back, callback_data="settings")
            add_listbox("Themes", items=["Dark", "Light"], label="Theme", callback=set_theme)

def copy_to_clipboard(sender, data):
    pyperclip.copy(data[0])
    set_value(data[1], "Copied!")


def add_wallet_ui():
    with group("create_wallet", parent="ui_group"):
        with child("create_wallet_child", width=800, height=750):
            add_button("Back", callback=go_back, callback_data="create_wallet")
            add_spacing(count=5)
            add_text("Create a new wallet")
            add_separator()
            add_spacing(count=10)
            add_listbox("network_combo", label="Network", items=["bitcoin", "litecoin", "dash", "dogecoin"], num_items=4)
            add_input_text("Status", label="Mnemonic", tip="Copy this somewhere! Its important if you ever lose or delete your wallet.")
            add_button("Create wallet", callback=create_custom_wallet)
            add_same_line()
            add_button("Copy mnemonic to clipboard", callback=copy_to_clipboard, callback_data=lambda: [get_value("Status"), "Status"])

def show_home():
    if does_item_exist("home") is True:
        pass
    if does_item_exist("details") is True:
        fade_out("test")
        delete_item("details")
        show_home_ui()
        fade_in("test")
        pass
    if does_item_exist("create_wallet") is True:
        fade_out("test")
        delete_item("create_wallet")
        show_home_ui()
        fade_in("test")
        pass
    if does_item_exist("settings"):
        fade_out("test")
        delete_item("settings")
        show_home_ui()
        fade_in("test")
    else:
        fade_out("test")
        delete_item("dash")
        show_home_ui()
        fade_in("test")
        pass

def show_settings():
    if does_item_exist("settings") is True:
        pass
    if does_item_exist("details") is True:
        fade_out("test")
        delete_item("details")
        show_settings_ui()
        fade_in("test")
        pass
    if does_item_exist("create_wallet") is True:
        fade_out("test")
        delete_item("create_wallet")
        show_settings_ui()
        fade_in("test")
        pass
    if does_item_exist("home"):
        fade_out("test")
        delete_item("home")
        show_settings_ui()
        fade_in("test")
        pass
    else:
        fade_out("test")
        delete_item("dash")
        show_settings_ui()
        fade_in("test")
        pass

def show_dashboard():

    if does_item_exist("dash") is True:
        pass
    if does_item_exist("details") is True:
        fade_out("test")
        delete_item("details")
        show_dashboard_ui()
        check_for_wallets()
        fade_in("test")
        pass
    if does_item_exist("create_wallet") is True:
        fade_out("test")
        delete_item("create_wallet")
        show_dashboard_ui()
        check_for_wallets()
        fade_in("test")
        pass
    if does_item_exist("settings"):
        fade_out("test")
        delete_item("settings")
        show_dashboard_ui()
        check_for_wallets()
        fade_in("test")

    if does_item_exist("dash") is False:
        fade_out("test")
        delete_item("home")
        show_dashboard_ui()
        check_for_wallets()
        fade_in("test")
        pass

def show_details_ui(data):
    information = Wallet(data)
    payment_address = information.keys_addresses()[0].address
    last_transaction = information.transaction_last(payment_address)
    balance = information.balance()
    network = information.network_list()[0]
    wif = information.wif()
    if len(last_transaction) == 0:
        last_transaction = "No recent transaction"
    with group("details", parent="ui_group"):
        with child("details_child", width=800, height=750):
            add_button("Back", callback=go_back, callback_data="details")
            add_spacing(count=5)
            add_text("Details")
            add_separator()
            add_spacing(count=10)
            add_checkbox("Show WIF", callback=show_WIF)
            add_spacing(count=5)
            add_text(f"Network: {network}")
            add_spacing(count=5)
            add_text(f"Payment address: {payment_address}")
            add_spacing(count=5)
            add_text(f"Last transaction: {last_transaction}")
            add_spacing(count=5)
            add_text(f"Current balance: {balance}")
            add_spacing(count=5)
            add_text("WIF", show=False, default_value=f"WIF: {wif}" )

def plot_home_candles():
    data_TSLA = get_series_values("TSLA")
    data_RIOT = get_series_values("RIOT")
    data_GME = get_series_values("GME")
    add_line_series("TSLA", "TSLA", data_TSLA[0], data_TSLA[3] , weight=1)
    add_candle_series("TSLA", "TSLA", data_TSLA[0], data_TSLA[1], data_TSLA[3], data_TSLA[4], data_TSLA[2])
    add_line_series("RIOT", "RIOT", data_RIOT[0], data_RIOT[3] , weight=1)
    add_candle_series("RIOT", "RIOT", data_RIOT[0], data_RIOT[1], data_RIOT[3], data_RIOT[4], data_RIOT[2])
    add_line_series("GME", "GME", data_GME[0], data_GME[3] , weight=1)
    add_line_series("GME", "GME", data_GME[0], data_GME[4] , weight=1)
    add_candle_series("GME", "GME", data_GME[0], data_GME[1], data_GME[3], data_GME[4], data_GME[2])

def show_home_ui():
    with group("home", parent="ui_group"):
        with child("home_child", width=800, height=740):
            add_text("Home")
            add_separator()
            add_plot("TSLA", height=180, xaxis_time=True, label="", yaxis_no_tick_labels=True)
            add_plot("RIOT", height=180, xaxis_time=True, label="", yaxis_no_tick_labels=True)
            add_plot("GME", height=180, xaxis_time=True, label="", yaxis_no_tick_labels=True)
    plot_home_candles()

def show_dashboard_ui():
    with group("dash", parent="ui_group"):
        with child("graph_child_1", width=430, height=400, no_scrollbar=True):
            add_text("Your wallets")
            add_same_line()
            add_dummy(width=130)
            add_same_line()
            add_button("Refresh wallets", height=40)
            add_same_line()
            add_button("+", height=40, width=40, callback=double_whammy)
            add_label_text("status_label", label="")
            add_separator()                                                                           # end child 1
        add_same_line()
        add_text("")
        add_same_line()
        with child("graph_child_2", width=350, height=400):
            add_spacing(count=5)
            #plot graph
            add_dummy(width=110)
            add_same_line()
            add_text("Market data")
            add_separator()
            add_plot("Plot", height=165, xaxis_time=True, label="", yaxis_no_tick_labels=True)
            add_plot("PlotDOGE", height=165, xaxis_time=True, label="", yaxis_no_tick_labels=True)
            btc_plot_callback(0, 0)
            doge_plot_callback(0, 0)                                                                  # end child 2
        add_spacing(count=3)
        with child("calculator_child", width=798, height=325, no_scrollbar=True):
            add_spacing(count=5)
            add_dummy(width=330)
            add_same_line()
            add_text("Withdraw")
            add_separator()
            add_spacing(count=3)
            add_dummy(width=150)
            add_same_line()
            with group("exchange_combos"):
                with group("combo1"):                                                         # start group 1
                    add_spacing(count=17)
                    add_listbox("currency_combo_1", label="", width=200, num_items=3)
                    add_input_text("input_combo1", label="", width=200)
            #add_same_line()
            #add_drawing("exchange_logo", width=127, height=231)
            #draw_image("exchange_logo", "exchange.jpg", [0, 0], [127, 231])
                add_same_line()
                with group("combo2"):
                    add_spacing(count=17)
                    add_input_text("input_combo2", label="Address", width=200)
                    add_button("Send", width=90, callback=send_transaction, callback_data= lambda: get_value('currency_combo_1'))
                    add_same_line()
                    add_text("Estimated fee: ")
            add_label_text("status_transaction", label="")                                                                        # end group 1


def delete_wallet(sender, data):
    wallet_delete_if_exists(data)
    delete_item(f"wallet_{data}")
    check_for_wallets()

def double_whammy():
    add_wallet()
    check_for_wallets()


def refresh_wallets():
    scan_wallets()
    check_for_wallets()


def btc_plot_callback(sender, data):
    data = get_series_values("BTC-USD")
    add_line_series("Plot", "BTC-USD", data[0], data[3] , weight=0.75)
    add_candle_series("Plot", "BTC-USD", data[0], data[1], data[3], data[4], data[2])

def doge_plot_callback(sender, data):
    data = get_series_values("DOGE-USD")
    add_line_series("PlotDOGE", "DOGE-USD", data[0], data[3] , weight=0.75)
    add_candle_series("PlotDOGE", "DOGE-USD", data[0], data[1], data[3], data[4], data[2])
