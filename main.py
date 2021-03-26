from dearpygui.core import *
from dearpygui.simple import *
from window_management import *

from colors import *

def apply_centering():
    items = list(get_data("item_center_list"))
    if items:
        for item in items:
            container_width = get_item_rect_size(get_item_parent(item))[0]
            item_width, item_height = get_item_rect_size(item)
            set_item_height(f'{item}_container', int(item_height))
            pos = int((container_width / 2) - (item_width / 2))
            set_item_width(f'{item}_dummy', pos)
def center_item(name: str):
    with child(f'{name}_container', autosize_x=True, no_scrollbar=True, border=False):
        add_dummy(name=f'{name}_dummy')
        add_same_line(name=f'{name}_sameline')
        move_item(name, parent=f'{name}_container')
    items = list(get_data('item_center_list'))
    items.append(name)
    add_data('item_center_list', items)
    y_space = get_style_item_spacing()[1]
    set_item_style_var(f'{name}_container', mvGuiStyleVar_ItemSpacing, [0, y_space])

set_main_window_size(1200,800)
set_main_window_title("xWallet")
set_main_window_resizable(False)
set_global_font_scale(1.30)
add_additional_font("Roboto-Regular.ttf")


center_items = []
add_data('item_center_list', center_items)

with window("xWallet",width=1190, height=790, no_resize=True , no_move=False, no_close=True, no_collapse=True):

    set_window_pos("xWallet", 0, 0)

    with child("menu_chil", width=300, height=740):
        add_spacing(count=10)
        add_drawing("logo", width=107, height=19)
        center_item("logo")
        add_spacing(count=20)
        with group("usd_balance"):                      #g1
            add_text("Account balance")
            add_text("  $ ")
            add_same_line()
            add_text(name="balance", default_value="0.0000")
            add_same_line()
            add_text(" USD")                                            #ge1
        center_item("usd_balance")
        add_spacing(count=10)
        with group("buttons"):
            add_button("Stocks", callback=show_home)
            add_button("Portofolio", callback=show_dashboard)
            add_button("Wallet recovery")
            with popup("Wallet recovery", "Recovery", modal=True, mousebutton=mvMouseButton_Left, width=300, height=300):
                add_input_text("wallet_seed", label="Mnemonic")
                add_listbox("recover_network_combo", label="Network", items=["bitcoin", "litecoin", "dash", "dogecoin"], num_items=4)
                add_text("recover_status", default_value=" ")
                add_button("Recover", callback=lambda: [create_custom_wallet_with_seed(), check_for_wallets()])
                add_same_line()
                add_button("Close", callback=lambda: [close_popup("Recovery"), set_value("recover_status", " "), set_value("wallet_seed", "")])


        center_item("buttons")
        add_spacing(count=80)
        add_drawing("gear", width=30, height=30)
        add_same_line()
        add_button("Settings", callback=show_settings)
        add_drawing("help", width=30, height=30)
        add_same_line()
        add_button("Help")
        
        with popup("Help", "Help links", modal=True, mousebutton=mvMouseButton_Left, width=300, height=300):
            add_text("GitHub: https://github.com/revollucian")
            add_button("close_help", callback=lambda: close_popup("Help links"), label="Close")


    add_same_line()
    add_text("     ")
    add_same_line()

    add_group("test")
    add_group("ui_group")
    end()
    end()

    #theme

    set_theme_dark()
    set_styles()
    show_dashboard_ui()
    check_for_wallets()
    show_style_editor()

set_render_callback(apply_centering)
start_dearpygui(primary_window='xWallet')
