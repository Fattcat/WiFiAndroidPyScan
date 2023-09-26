import subprocess

# Spustit příkaz pro získání informací o Wi-Fi sítích
wifi_info = subprocess.check_output(['termux-wifi-scaninfo']).decode('utf-8')

# Rozdělit výstup na řádky
wifi_info_lines = wifi_info.split('\n')

# Procházet řádky a získat SSID, MAC adresu a kanál
for line in wifi_info_lines:
    if 'SSID' in line:
        ssid = line.split(': ')[1]
    elif 'BSSID' in line:
        mac = line.split(': ')[1]
    elif 'Channel' in line:
        channel = line.split(': ')[1]
        # Vypsat informace o síti
        print('--------------------------------')
        print(f'SSID: {ssid}')
        print(f'MAC adresa: {mac}')
        print(f'Kanál: {channel}')
