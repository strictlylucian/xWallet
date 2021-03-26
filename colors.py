from dearpygui.core import *
from dearpygui.simple import *

class Status:
    lightmode = False

class Light:
    COL_WINDOWBG = [222, 222, 222, 240]
    COL_FRAMEBG = [255, 255, 255, 255]
    COL_BUTTON = [255, 255, 255, 102]
    COL_TEXT = [0, 0, 0, 255]
    COL_CHILDBG = [255, 255, 255, 255]
    COL_TITLEBG = [255, 255, 255, 255]
    COL_BUTTON_HOVERED = [223, 223, 223, 255]
    COL_TABUNFOCUSED = [213, 213, 213, 255]
    COL_DOCKING = [174, 174, 174, 179]
    COL_PLOTLINES = [255, 255, 255, 255]
    COL_NAVHIGHLIGHT = [255, 255, 255, 255]
    COL_POPUPBG = [255, 255, 255, 240]
    COL_BORDERSHADOW = [255, 255, 255, 106]
    COL_TITLEBGCOLLAPSED = [235, 235, 235, 130]
    COL_MENUBARBG = [255, 255, 255, 255]
    COL_TAB_UNFOCUSED = [198, 198, 198, 248]
    COL_BUTTON_ACTIVE = [163, 163, 163, 255]
    COL_BORDER = [192, 190, 190, 128]

class Dark:
    COL_WINDOWBG = [25, 25, 25, 240]
    COL_FRAMEBG = [33, 30, 30, 255]
    COL_BUTTON = [57, 56, 56, 102]
    COL_TEXT = [255, 255, 255, 255]
    COL_CHILDBG = [11, 11, 11, 255]
    COL_TITLEBG = [71, 71, 71, 255]
    COL_BUTTON_HOVERED = [78, 78, 78, 255]
    COL_TABUNFOCUSED = [213, 213, 213, 255]
    COL_DOCKING = [174, 174, 174, 179]
    COL_PLOTLINES = [255, 255, 255, 255]
    COL_NAVHIGHLIGHT = [255, 255, 255, 255]
    COL_POPUPBG = [21, 21, 21, 240]
    COL_BORDERSHADOW = [83, 80, 80, 106]
    COL_TITLEBGCOLLAPSED = [235, 235, 235, 130]
    COL_MENUBARBG = [255, 255, 255, 255]
    COL_TAB_UNFOCUSED = [198, 198, 198, 248]
    COL_BUTTON_ACTIVE = [0, 0, 0, 255]
    COL_BORDER = [0, 0, 0, 128]
    COL_SEPARATOR = [255, 255, 255, 102]

def set_styles():
    set_style_window_padding(18.00, 8.00)
    set_style_frame_padding(14.00, 7.00)
    set_style_item_spacing(8.00, 4.00)
    set_style_item_inner_spacing(4.00, 4.00)
    set_style_touch_extra_padding(0.00, 0.00)
    set_style_indent_spacing(21.00)
    set_style_scrollbar_size(14.00)
    set_style_grab_min_size(10.00)
    set_style_window_border_size(1.00)
    set_style_child_border_size(1.00)
    set_style_popup_border_size(1.00)
    set_style_frame_border_size(1.00)
    set_style_tab_border_size(0.00)
    set_style_window_rounding(12.00)
    set_style_child_rounding(12.00)
    set_style_frame_rounding(12.00)
    set_style_popup_rounding(2.00)
    set_style_scrollbar_rounding(12.00)
    set_style_grab_rounding(0.00)
    set_style_tab_rounding(4.00)
    set_style_window_title_align(0.00, 0.50)
    set_style_window_menu_button_position(mvDir_Left)
    set_style_color_button_position(mvDir_Right)
    set_style_button_text_align(0.50, 0.50)
    set_style_selectable_text_align(0.00, 0.00)
    set_style_display_safe_area_padding(3.00, 3.00)
    set_style_global_alpha(1.00)
    set_style_antialiased_lines(True)
    set_style_antialiased_fill(True)
    set_style_curve_tessellation_tolerance(1.25)
    set_style_circle_segment_max_error(1.60)


def set_theme_light():
    Status.lightmode = True
    clear_drawing("logo")
    clear_drawing("gear")
    clear_drawing("help")
    draw_image("logo", "logo-light.jpg", [0, 0], [107, 19])
    draw_image("gear", "gear-light.jpg", [0, 0], [30, 30])
    draw_image("help", "help-light.jpg", [0, 0], [30, 30])
    set_theme_item(mvGuiCol_WindowBg, Light.COL_WINDOWBG[0], Light.COL_WINDOWBG[1], Light.COL_WINDOWBG[2], Light.COL_WINDOWBG[3])
    set_theme_item(mvGuiCol_FrameBg, Light.COL_FRAMEBG[0], Light.COL_FRAMEBG[1], Light.COL_FRAMEBG[2], Light.COL_FRAMEBG[3])
    set_theme_item(mvGuiCol_Button, Light.COL_BUTTON[0], Light.COL_BUTTON[1], Light.COL_BUTTON[2], Light.COL_BUTTON[3])
    set_theme_item(mvGuiCol_Text, Light.COL_TEXT[0], Light.COL_TEXT[1], Light.COL_TEXT[2], Light.COL_TEXT[3])
    set_theme_item(mvGuiCol_ChildBg, Light.COL_CHILDBG[0], Light.COL_CHILDBG[1], Light.COL_CHILDBG[2], Light.COL_CHILDBG[3])
    set_theme_item(mvGuiCol_TitleBg, Light.COL_TITLEBG[0], Light.COL_TITLEBG[1], Light.COL_TITLEBG[2], Light.COL_TITLEBG[3])
    set_theme_item(mvGuiCol_ButtonHovered, Light.COL_BUTTON_HOVERED[0], Light.COL_BUTTON_HOVERED[1], Light.COL_BUTTON_HOVERED[2], Light.COL_BUTTON_HOVERED[3])
    set_theme_item(mvGuiCol_TabUnfocusedActive, Light.COL_TABUNFOCUSED[0], Light.COL_TABUNFOCUSED[1], Light.COL_TABUNFOCUSED[2], Light.COL_TABUNFOCUSED[3])
    set_theme_item(mvGuiCol_DockingPreview, Light.COL_DOCKING[0], Light.COL_DOCKING[1], Light.COL_DOCKING[2], Light.COL_DOCKING[3])
    set_theme_item(mvGuiCol_PlotLines, Light.COL_PLOTLINES[0], Light.COL_PLOTLINES[1], Light.COL_PLOTLINES[2], Light.COL_PLOTLINES[3])
    set_theme_item(mvGuiCol_NavHighlight, Light.COL_NAVHIGHLIGHT[0], Light.COL_NAVHIGHLIGHT[1], Light.COL_NAVHIGHLIGHT[2], Light.COL_NAVHIGHLIGHT[3])
    set_theme_item(mvGuiCol_PopupBg, Light.COL_POPUPBG[0], Light.COL_POPUPBG[1], Light.COL_POPUPBG[2], Light.COL_POPUPBG[3])
    set_theme_item(mvGuiCol_BorderShadow, Light.COL_BORDERSHADOW[0], Light.COL_BORDERSHADOW[1], Light.COL_BORDERSHADOW[2], Light.COL_BORDERSHADOW[3])
    set_theme_item(mvGuiCol_TitleBgCollapsed, Light.COL_TITLEBGCOLLAPSED[0], Light.COL_TITLEBGCOLLAPSED[1], Light.COL_TITLEBGCOLLAPSED[2], Light.COL_TITLEBGCOLLAPSED[3])
    set_theme_item(mvGuiCol_MenuBarBg, Light.COL_MENUBARBG[0], Light.COL_MENUBARBG[1], Light.COL_MENUBARBG[2], Light.COL_MENUBARBG[3])
    set_theme_item(mvGuiCol_TabUnfocused, Light.COL_TAB_UNFOCUSED[0], Light.COL_TAB_UNFOCUSED[1], Light.COL_TAB_UNFOCUSED[2], Light.COL_TAB_UNFOCUSED[3])
    set_theme_item(mvGuiCol_ButtonActive, Light.COL_BUTTON_ACTIVE[0], Light.COL_BUTTON_ACTIVE[1], Light.COL_BUTTON_ACTIVE[2], Light.COL_BUTTON_ACTIVE[3])
    set_theme_item(mvGuiCol_Border, Light.COL_BORDER[0], Light.COL_BORDER[1], Light.COL_BORDER[2], Light.COL_BORDER[3])

def set_theme_dark():
    Status.lightmode = False
    clear_drawing("logo")
    clear_drawing("gear")
    clear_drawing("help")
    draw_image("logo", "logo-dark.png", [0, 0], [107, 19])
    draw_image("gear", "gear-dark.png", [0, 0], [30, 30])
    draw_image("help", "help-dark.png", [0, 0], [30, 30])
    set_theme_item(mvGuiCol_TitleBgActive, 14, 14, 14, 255)
    set_theme_item(mvGuiCol_WindowBg, Dark.COL_WINDOWBG[0], Dark.COL_WINDOWBG[1], Dark.COL_WINDOWBG[2], Dark.COL_WINDOWBG[3])
    set_theme_item(mvGuiCol_FrameBg, Dark.COL_FRAMEBG[0], Dark.COL_FRAMEBG[1], Dark.COL_FRAMEBG[2], Dark.COL_FRAMEBG[3])
    set_theme_item(mvGuiCol_Button, Dark.COL_BUTTON[0], Dark.COL_BUTTON[1], Dark.COL_BUTTON[2], Dark.COL_BUTTON[3])
    set_theme_item(mvGuiCol_Text, Dark.COL_TEXT[0], Dark.COL_TEXT[1], Dark.COL_TEXT[2], Dark.COL_TEXT[3])
    set_theme_item(mvGuiCol_ChildBg, Dark.COL_CHILDBG[0], Dark.COL_CHILDBG[1], Dark.COL_CHILDBG[2], Dark.COL_CHILDBG[3])
    set_theme_item(mvGuiCol_TitleBg, Dark.COL_TITLEBG[0], Dark.COL_TITLEBG[1], Dark.COL_TITLEBG[2], Dark.COL_TITLEBG[3])
    set_theme_item(mvGuiCol_ButtonHovered, Dark.COL_BUTTON_HOVERED[0], Dark.COL_BUTTON_HOVERED[1], Dark.COL_BUTTON_HOVERED[2], Dark.COL_BUTTON_HOVERED[3])
    set_theme_item(mvGuiCol_TabUnfocusedActive, Dark.COL_TABUNFOCUSED[0], Dark.COL_TABUNFOCUSED[1], Dark.COL_TABUNFOCUSED[2], Dark.COL_TABUNFOCUSED[3])
    set_theme_item(mvGuiCol_DockingPreview, Dark.COL_DOCKING[0], Dark.COL_DOCKING[1], Dark.COL_DOCKING[2], Dark.COL_DOCKING[3])
    set_theme_item(mvGuiCol_PlotLines, Dark.COL_PLOTLINES[0], Dark.COL_PLOTLINES[1], Dark.COL_PLOTLINES[2], Dark.COL_PLOTLINES[3])
    set_theme_item(mvGuiCol_NavHighlight, Dark.COL_NAVHIGHLIGHT[0], Dark.COL_NAVHIGHLIGHT[1], Dark.COL_NAVHIGHLIGHT[2], Dark.COL_NAVHIGHLIGHT[3])
    set_theme_item(mvGuiCol_PopupBg, Dark.COL_POPUPBG[0], Dark.COL_POPUPBG[1], Dark.COL_POPUPBG[2], Dark.COL_POPUPBG[3])
    set_theme_item(mvGuiCol_BorderShadow, Dark.COL_BORDERSHADOW[0], Dark.COL_BORDERSHADOW[1], Dark.COL_BORDERSHADOW[2], Dark.COL_BORDERSHADOW[3])
    set_theme_item(mvGuiCol_TitleBgCollapsed, Dark.COL_TITLEBGCOLLAPSED[0], Dark.COL_TITLEBGCOLLAPSED[1], Dark.COL_TITLEBGCOLLAPSED[2], Dark.COL_TITLEBGCOLLAPSED[3])
    set_theme_item(mvGuiCol_MenuBarBg, Dark.COL_MENUBARBG[0], Dark.COL_MENUBARBG[1], Dark.COL_MENUBARBG[2], Dark.COL_MENUBARBG[3])
    set_theme_item(mvGuiCol_TabUnfocused, Dark.COL_TAB_UNFOCUSED[0], Dark.COL_TAB_UNFOCUSED[1], Dark.COL_TAB_UNFOCUSED[2], Dark.COL_TAB_UNFOCUSED[3])
    set_theme_item(mvGuiCol_ButtonActive, Dark.COL_BUTTON_ACTIVE[0], Dark.COL_BUTTON_ACTIVE[1], Dark.COL_BUTTON_ACTIVE[2], Dark.COL_BUTTON_ACTIVE[3])
    set_theme_item(mvGuiCol_Border, Dark.COL_BORDER[0], Dark.COL_BORDER[1], Dark.COL_BORDER[2], Dark.COL_BORDER[3])
    #set_theme_item(mvGuiCol_Separator, Dark.COL_SEPARATOR[0], Dark.COL_SEPARATOR[1], Dark.COL_SEPARATOR[2], Dark.COL_SEPARATOR[3])
