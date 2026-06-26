# waf_breaker.py
import os
import sys
import time
from core.fingerprinter import WafFingerprinter
from core.bypass_db import FIREWALL_INTEL

# Terminal ANSI Color Escape Constants (Crimson DedSec Theme)
C_RED   = "\033[31m"
C_BOLD  = "\033[1m"
C_CYAN  = "\033[96m"
C_GREEN = "\033[92m"
C_YEL   = "\033[93m"
C_WHITE = "\033[97m"
C_RESET = "\033[0m"

def print_dedsec_banner():
    os.system("clear")
    print(f"{C_RED}{C_BOLD}")
    print(r"    ,__                   __")
    print(r"    '~~****Nm_    _mZ*****~~")
    print(r"            _8@mm@K_")
    print(r"           W~@`  '@~W")
    print(r"          ][][    ][][")
    print(r"    gz    'W'W.  ,W`W`    es")
    print(r"  ,Wf    gZ****MA****Ns    VW.")
    print(r" gA`   ,Wf     ][     VW.   'Ms")
    print(r"Wf    ,@`      ][      '@.    VW")
    print(r"M.    W`  _mm_ ][ _mm_  'W    ,A")
    print(r"'W   ][  i@@@@i][i@@@@i  ][   W`")
    print(r" !b  @   !@@@@!][!@@@@!   @  d!")
    print(r"  VWmP    ~**~ ][ ~**~    YmWf")
    print(r"    ][         ][         ][")
    print(r"  ,mW[         ][         ]Wm.")
    print(r" ,A` @  ,gms.  ][  ,gms.  @ 'M.")
    print(r" W`  Yi W@@@W  ][  W@@@W iP  'W")
    print(r"d!   'W M@@@A  ][  M@@@A W`   !b")
    print(r"@.    !b'V*f`  ][  'V*f`d!    ,@")
    print(r"'Ms    VW.     ][     ,Wf    gA`")
    print(r"  VW.   'Ms.   ][   ,gA`   ,Wf")
    print(r"   'Ms    'V*mmWWmm*f`    gA`")
    print(f"{C_WHITE}☠️  [ W A F   B R E A K E R X   E N G I N E ]  ☠️")
    print(f"   [ PRODUCED BY DEVELOPER: Unknownx007 ]{C_RED}{C_BOLD}")
    print(f"================================================================================{C_RESET}")


def run_framework_pipeline():
    print_dedsec_banner()
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = input(f"{C_WHITE}[+] Enter Target URL Domain to Audit Defense Profiles: {C_RESET}").strip()
        
    if not target:
        print(f"{C_RED}[!] Error: No target endpoint address input found.{C_RESET}")
        return

    print(f"\n{C_YEL}[*] Initializing active reconnaissance and trigger probes against: {target}{C_RESET}")
    time.sleep(1.0)
    
    scanner = WafFingerprinter(target)
    waf_type, certitude = scanner.scan_perimeter_defenses()
    
    print(f"{C_RED}================================================================================{C_RESET}")
    print(f"{C_WHITE}[✦] TARGET PERIMETER DEFENSIVE AUDIT SUMMARY Matrix:{C_RESET}\n")
    
    if not waf_type:
        print(f"    {C_GREEN}[✅] STATUS : NO FIREWALL / WAF INJECTION LAYER DETECTED")
        print(f"    {C_WHITE}[*] TARGET PROFILE : Target application responses matched standard direct-to-host baseline paths.{C_RESET}")
    else:
        intel = FIREWALL_INTEL[waf_type]
        print(f"    {C_RED}[☠️] ACTIVE DEFENSE SHIELD DETECTED : {waf_type}")
        print(f"    {C_WHITE}└── Fingerprint Profile Match Confidence : {C_YEL}{certitude}{C_RESET}")
        print(f"    {C_WHITE}└── Infrastructure Platform Subsystem    : {intel['description']}{C_RESET}")
        
        print(f"\n{C_CYAN}[✦] EXPOSED EVASION PLAYBOOK REMEDIATION VECTORS:{C_RESET}\n")
        for idx, strategy in enumerate(intel["evasion_strategies"]):
            print(f"    {C_GREEN}[{idx + 1}]{C_RESET} {strategy}")
            
    print(f"\n{C_RED}================================================================================{C_RESET}")
    print(f"{C_GREEN}[✅] Firewall intelligence diagnostic check successfully complete.{C_RESET}\n")

if __name__ == "__main__":
    run_framework_pipeline()
