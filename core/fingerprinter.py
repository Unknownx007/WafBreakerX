import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning

# FIXED: Standard urllib3 exceptions method suppresses TLS warnings smoothly
urllib3.disable_warnings(InsecureRequestWarning)

class WafFingerprinter:
    def __init__(self, target_url: str):
        if not target_url.startswith("http://") and not target_url.startswith("https://"):
            self.target_url = f"https://{target_url}"
        else:
            self.target_url = target_url
            
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

    def scan_perimeter_defenses(self) -> tuple:
        """Inspects network responses and actively triggers security controls to identify the firewall model."""
        detected_waf = None
        confidence = "LOW"
        
        # Phase A: Passive Response Header Tracking
        try:
            res = requests.get(self.target_url, headers=self.headers, timeout=6, verify=False)
            server_header = res.headers.get("Server", "").lower()
            
            if "cloudflare" in server_header or "cf-ray" in res.headers:
                return "CLOUDFLARE", "HIGH"
            elif "litespeed" in server_header:
                return "LITESPEED", "MEDIUM"
        except Exception:
            pass

        # Phase B: Active Fuzz Trigger Check (Safe parameter injection attempt)
        try:
            trigger_url = f"{self.target_url.rstrip('/')}/?id=' UNION SELECT NULL,NULL,NULL--"
            fuzz_res = requests.get(trigger_url, headers=self.headers, timeout=6, verify=False)
            
            # Analyze blocking behavior configurations
            if fuzz_res.status_code in body_clean == fuzz_res.text.lower():
                if "cloudflare" in body_clean:
                    return "CLOUDFLARE", "HIGH"
                elif "modsecurity" in body_clean or "owasp" in body_clean:
                    return "MODSECURITY", "HIGH"
                elif "litespeed" in body_clean:
                    return "LITESPEED", "HIGH"
                else:
                    return "GENERIC_WAF", "MEDIUM"
        except Exception:
            pass

        return detected_waf, confidence
