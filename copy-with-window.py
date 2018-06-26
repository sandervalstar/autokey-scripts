import subprocess
try:
#keyboard.send_keys(clipboard.get_clipboard())
    #result = subprocess.run(['xdotool', 'getwindowfocus', 'getwindowname'], stdout=subprocess.PIPE)
    #active_window = result.stdout.decode('utf-8')
    #active_window = os.popen("xdotool getwindowfocus getwindowname").read()
    active_window="bla"
    if "sander@sander-desktop" not in active_window:
        keyboard.send_keys('<ctrl>+c')
except Exception as e:
    dialog.info_dialog("Error", 
          "error: " + str(error))