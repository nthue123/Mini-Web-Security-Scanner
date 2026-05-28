import requests
from urllib.parse import urljoin
from colorama import Fore, Style, init

init(autoreset=True)

COMMON_HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy"
]

COMMON_PATHS = [
    "admin",
    "backup",
    "test",
    "dashboard",
    ".git"
]


def banner():
    print(Fore.CYAN + "=" * 50)
    print(Fore.CYAN + " MINI WEB SECURITY SCANNER ")
    print(Fore.CYAN + "=" * 50)


class WebScanner:
    def __init__(self, target):
        self.target = target.rstrip("/")

    def make_request(self, url):
        try:
            response = requests.get(url, timeout=5)
            return response
        except requests.RequestException as e:
            print(Fore.RED + f"[ERROR] {url} -> {e}")
            return None

    def check_https(self):
        print(Fore.YELLOW + "\n[+] Checking HTTPS...")

        if self.target.startswith("https://"):
            print(Fore.GREEN + "[OK] HTTPS enabled")
        else:
            print(Fore.RED + "[WARNING] Website not using HTTPS")

    def check_headers(self):
        print(Fore.YELLOW + "\n[+] Checking Security Headers...")

        response = self.make_request(self.target)

        if not response:
            return

        headers = response.headers

        for header in COMMON_HEADERS:
            if header in headers:
                print(Fore.GREEN + f"[OK] {header}")
            else:
                print(Fore.RED + f"[MISSING] {header}")

    def check_server_info(self):
        print(Fore.YELLOW + "\n[+] Checking Server Information...")

        response = self.make_request(self.target)
    scanner.run()