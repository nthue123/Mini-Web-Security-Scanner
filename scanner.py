import json
import requests

from urllib.parse import urljoin
from colorama import Fore, init

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

        self.report = {
            "target": self.target,
            "https": False,
            "security_headers": {},
            "server": None,
            "robots_txt": False,
            "directory_listing": False,
            "sensitive_paths": []
        }

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
            self.report["https"] = True

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
                self.report["security_headers"][header] = True

            else:
                print(Fore.RED + f"[MISSING] {header}")
                self.report["security_headers"][header] = False

    def check_server_info(self):
        print(Fore.YELLOW + "\n[+] Checking Server Information...")

        response = self.make_request(self.target)

        if not response:
            return

        server = response.headers.get("Server")

        if server:
            print(Fore.GREEN + f"[INFO] Server: {server}")
            self.report["server"] = server

        else:
            print(Fore.RED + "[INFO] Server header hidden")

    def check_robots(self):
        print(Fore.YELLOW + "\n[+] Checking robots.txt...")

        robots_url = urljoin(self.target, "/robots.txt")
        response = self.make_request(robots_url)

        if response and response.status_code == 200:
            print(Fore.GREEN + "[FOUND] robots.txt")

            self.report["robots_txt"] = True

            print(response.text[:300])

        else:
            print(Fore.RED + "[NOT FOUND] robots.txt")

    def check_directory_listing(self):
        print(Fore.YELLOW + "\n[+] Checking Directory Listing...")

        response = self.make_request(self.target)

        if not response:
            return

        indicators = [
            "Index of /",
            "Directory Listing For",
            "Parent Directory"
        ]

        for indicator in indicators:
            if indicator.lower() in response.text.lower():
                print(Fore.RED + "[WARNING] Directory listing enabled")

                self.report["directory_listing"] = True

                return

        print(Fore.GREEN + "[OK] Directory listing not detected")

    def check_common_paths(self):
        print(Fore.YELLOW + "\n[+] Checking Common Sensitive Paths...")

        for path in COMMON_PATHS:
            url = urljoin(self.target + "/", path)

            response = self.make_request(url)

            if response and response.status_code == 200:
                print(Fore.RED + f"[FOUND] {url}")

                self.report["sensitive_paths"].append(url)

            else:
                print(Fore.GREEN + f"[NOT FOUND] {path}")

    def save_report(self):
        with open("report.json", "w") as file:
            json.dump(self.report, file, indent=4)

        print(Fore.CYAN + "\n[+] JSON report saved: report.json")

    def run(self):
        banner()

        print(Fore.CYAN + f"\nTarget: {self.target}")

        self.check_https()
        self.check_headers()
        self.check_server_info()
        self.check_robots()
        self.check_directory_listing()
        self.check_common_paths()

        self.save_report()

        print(Fore.CYAN + "\nScan completed.")


if __name__ == "__main__":
    target = input("Enter target URL: ")

    scanner = WebScanner(target)
    scanner.run()