
from fontTools.ttLib import TTFont, tables
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.ttLib.tables import _n_a_m_e, _g_l_y_f

sf_pro_path = "/Library/Fonts/SF-Pro.ttf"
font = TTFont(sf_pro_path)



# generate a single instance of the font
single_instance: TTFont = instantiateVariableFont(font, axisLimits={
    'wdth': 100.0,
    'opsz': 17.0,
    'wght': 360.0
})

for nr in single_instance['name'].names:
    nr_str = nr.__str__() 
    if "SF" in nr_str :
        print(nr_str)
        single_instance['name'].setName(
            nr_str.replace("SF", "ATL"),
            nr.nameID, nr.platformID, nr.platEncID, nr.langID
        )
        

single_instance.save("SF-Instanced Pro Text.ttf")