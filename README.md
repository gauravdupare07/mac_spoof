# MACSpoof

MACSpoof is a Python-based **MAC Address Spoofing Tool** developed to learn and demonstrate Linux networking concepts and cybersecurity fundamentals.

The project evolved step-by-step from a basic MAC changer (v1) to a more advanced, Red Team–style tool (v3), with added automation and usability features in each version.

---

## 📌 Versions Overview

- **v1.0** – Manual MAC address spoofing
- **v2.0** – Random MAC generation & improved CLI
- **v3.0** – Auto interface detection, MAC restore, and Red Team–oriented workflow

---

## ✨ Features by Version

### 🔹 Version 1.0
- Manually change MAC address
- Simple CLI interface
- Clean banner and readable output
- Lightweight and beginner-friendly
- Tested on Kali Linux

---

### 🔹 Version 2.0
- All v1 features
- Random MAC address generation
- Improved help menu and CLI options
- Better output formatting
- Modular and cleaner code structure

---

### 🔹 Version 3.0
- All v2 features
- Auto-detect active network interface (`eth0`, `wlan0`, etc.)
- Restore original MAC address
- Random MAC with locally administered bit
- Improved automation and usability
- Red Team–style workflow

---

## 🛠 Requirements

- Python 3.x
- Linux-based operating system
- Root / sudo privileges
- `ifconfig` and `ip` networking utilities

---

## 🚀 Usage

### ▶ Version 1 (Manual MAC)
```bash
sudo python3 mac_spoof.py -i eth0 -m 00:11:22:33:44:55
```
▶ Version 2 (Random MAC)
```bash
sudo python3 mac_spoof-v2.py -i eth0 -r
```
▶ Version 3 (Auto Interface + Random MAC)
```bash
sudo python3 mac_spoof-v3.py -a -r
```
▶ Version 3 (Restore Original MAC)
```bash
sudo python3 mac_spoof-v3.py -a --restore
```
---

🧾 Command-Line Options (v3)
- Option	Description
- -i, --interface	Specify network interface
- -a, --auto	Auto-detect active interface
- -m, --mac	Manually set MAC address
- -r, --random	Generate random MAC address
- --restore	Restore original MAC address
- -h, --help	Show help menu

---

📌 Example Output
- [+] Interface : eth0
- [+] Current MAC : xx:xx:xx:xx:xx:xx
- [+] Generated Random MAC : xx:xx:xx:xx:xx:xx
- [✔] MAC successfully changed

---

⚠ Disclaimer
- This tool is created strictly for educational purposes.
- Use it only on systems or networks you own or have explicit permission to test.
- The author is not responsible for any misuse of this tool.

---

👤 Author
- Created by Giga_Byte_Flow
- 📈 Future Improvements
- Vendor-based MAC spoofing
- macOS compatibility
- Stealth / silent mode
- Logging and report generation
- Packaging as a Kali Linux tool

---

⭐ If you find this project useful, feel free to star the repository and share feedback.
