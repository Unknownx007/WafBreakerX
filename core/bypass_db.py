# core/bypass_db.py

FIREWALL_INTEL = {
    "CLOUDFLARE": {
        "description": "Cloudflare Enterprise Edge Shield Protection Layer",
        "evasion_strategies": [
            "Perform direct infrastructure scans to isolate the backend origin IP address, bypassing the cloud proxy.",
            "Deploy specialized SQLMap tamper scripts: --tamper=charencode,modsecurity,space2comment",
            "Leverage HTTP Parameter Pollution (HPP) matrices to slip payloads past the edge pipeline parsing buffers.",
            "Rotate high-reputation residential proxy IPs and enforce random delay intervals (Jitter: 5-15s)."
        ]
    },
    "LITESPEED": {
        "description": "LiteSpeed Native Anti-DDoS & Web Application Firewall",
        "evasion_strategies": [
            "Mask automated scanner traces by injecting complex browser identity tokens (--random-agent).",
            "Deploy advanced encoding routines against input paths: --tamper=base64encode,between",
            "Abuse HTTP Keep-Alive pipelines to split or chunk payload chunks over continuous sessions."
        ]
    },
    "MODSECURITY": {
        "description": "OWASP Core Rule Set (CRS) ModSecurity Engine Instance",
        "evasion_strategies": [
            "Utilize inline comment interleaving methods to split trigger words: S/*!ELECT*/",
            "Swap standard spacing layout tokens out for alternative URL elements like %0a or %0d control characters.",
            "Obfuscate high-risk system parameters using hex or nested unicode notation structures."
        ]
    },
    "GENERIC_WAF": {
        "description": "An unidentified security wrapper or proxy firewall has intercepted the attack vector.",
        "evasion_strategies": [
            "Switch to low-and-slow execution profiles to avoid triggering localized rate-limiting rules.",
            "Enforce strict HTTP/2 protocol parameters to bypass legacy HTTP/1 request-validation filters.",
            "Test alternative domain pathways or mobile API sub-endpoints (e.g., ://target.com) which often lack heavy WAF rule configurations."
        ]
    }
}
