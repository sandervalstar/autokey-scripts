AutoKey
Install AutoKey and add your preferred shortcuts for the scripts


Mnemonics
create a file:
.config/gtk-3.0/settings.ini

containing:
[Settings]
gtk-enable-mnemonics = 0


Firefox
Unset ui.key.menuAccessKey in Firefox


stty
Add the following line to your .bashrc 
[ $- == *i* ]] && stty intr \^\\
this makes ctrl+\ the interrupt command instead of ctrl+c.

