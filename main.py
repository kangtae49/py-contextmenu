import ctypes
import sys
import winreg as reg

def run_as_admin():
    if not ctypes.windll.shell32.IsUserAnAdmin():
        try:
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, " ".join(sys.argv), None, 1
            )
        except Exception as e:
            print(f"{e}")
        sys.exit()

def add_context_menu_option_cmd():
    try:
        key_path = r"Directory\\shell\\OpenCMDHere"
        command_key_path = key_path + r"\\command"

        with reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path) as key:
            reg.SetValue(key, "", reg.REG_SZ, "Open Command Here")
            reg.SetValueEx(key, "Icon", 0, reg.REG_SZ, "C:\\Windows\\System32\\cmd.exe")

        with reg.CreateKey(reg.HKEY_CLASSES_ROOT, command_key_path) as command_key:
            reg.SetValue(command_key, "", reg.REG_SZ, "cmd.exe /s /k pushd \"%V\"")

        key_path = r"Directory\\Background\\shell\\OpenCMDHere"
        command_key_path = key_path + r"\\command"

        with reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path) as key:
            reg.SetValue(key, "", reg.REG_SZ, "Open Command Here")
            reg.SetValueEx(key, "Icon", 0, reg.REG_SZ, "C:\\Windows\\System32\\cmd.exe")

        with reg.CreateKey(reg.HKEY_CLASSES_ROOT, command_key_path) as command_key:
            reg.SetValue(command_key, "", reg.REG_SZ, "cmd.exe /s /k pushd \"%V\"")
    except Exception as e:
        print(f"{e}")



def add_context_menu_option_powershell():
    try:
        key_path = r"Directory\\shell\\OpenPowershellHere"
        command_key_path = key_path + r"\\command"

        with reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path) as key:
            reg.SetValue(key, "", reg.REG_SZ, "Open Powershell Here")
            reg.SetValueEx(key, "Icon", 0, reg.REG_SZ, "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe")

        with reg.CreateKey(reg.HKEY_CLASSES_ROOT, command_key_path) as command_key:
            reg.SetValue(command_key, "", reg.REG_SZ, "powershell.exe -noexit -command Set-Location -literalPath '%V'")

        key_path = r"Directory\\Background\\shell\\OpenPowershellHere"
        command_key_path = key_path + r"\\command"

        with reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path) as key:
            reg.SetValue(key, "", reg.REG_SZ, "Open Powershell Here")
            reg.SetValueEx(key, "Icon", 0, reg.REG_SZ, "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe")

        with reg.CreateKey(reg.HKEY_CLASSES_ROOT, command_key_path) as command_key:
            reg.SetValue(command_key, "", reg.REG_SZ, "powershell.exe -noexit -command Set-Location -literalPath '%V'")
    except Exception as e:
        print(f"{e}")

if __name__ == "__main__":
    run_as_admin()
    add_context_menu_option_cmd()
    add_context_menu_option_powershell()
    