import os
from fontTools import ttLib

system_font_path = "/Library/Fonts/"

list = os.listdir(system_font_path)

def rename_font(font, from_str = "SF", to_str="SF-TrueType"):
    for nr in font['name'].names:
        nr_str = nr.__str__() 
        if "SF" in nr_str :
            # print(nr_str)
            font['name'].setName(
                nr_str.replace(from_str, to_str),
                nr.nameID, nr.platformID, nr.platEncID, nr.langID
            )
    return font

def convert_to_ttf(font_name, from_str = "SF", to_str="SF-TrueType"):
    new_font_name = font_name[:-3].replace(from_str, to_str) + "ttf"
    command  = "otf2ttf " + system_font_path + font_name + " -o "+ "./"+new_font_name
    print(command)
    os.system(command)
    return new_font_name