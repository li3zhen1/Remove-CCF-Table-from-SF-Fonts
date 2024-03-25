# Remove CCF Table from SF Fonts

Scripts for convert otf to ttf for specific font (like SF Pro). `RemoveCCFTable` removes CCF table in OpenType files, so that software like typst can export PDF with correctly subsetted glyphs and you don't get a bloated PDF file (which includes all the characters even if you don't use them).

The script also modify all the metadata in the font so your system won't confuse the font with the original one.

**You are responsible for the usage of this script and the produced font files.**

