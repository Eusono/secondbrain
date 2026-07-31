#!/usr/bin/env python3
"""
SkillSpector — AI Skill Security Scanner
Inspired by NVIDIA SkillSpector (github.com/nvidia/skillspector).
Scans custom skills and rituals in skills/ for prompt injection, hardcoded credentials,
dangerous shell execution, and data exfiltration threats.
"""
import os
import sys
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DANGEROUS_PATTERNS = [
    (r'rm\s+-rf\s+/', "Critical: Destructive root directory removal attempt"),
    (r'curl\s+.*\s*\|\s*bash', "High: Remote script pipe to bash execution"),
    (r'wget\s+.*\s*\|\s*bash', "High: Remote script pipe to bash execution"),
    (r'(?i)(api[_-]?key|secret[_-]?key|password|token)\s*[:=]\s*[\'"][A-Za-z0-9_\-]{16,}[\'"]', "Critical: Hardcoded secret/token detected"),
    (r'(?i)ignore\s+previous\s+instructions', "Medium: Potential prompt injection keyword"),
    (r'(?i)exfiltrate|send_to_remote', "High: Unsanctioned data transfer pattern"),
]

def scan_skills():
    skills_dir = os.path.join(ROOT_DIR, 'skills')
    results = []
    
    if not os.path.exists(skills_dir):
        print("No skills directory found.")
        return results

    for root, dirs, files in os.walk(skills_dir):
        for f in files:
            if f.endswith('.md') or f.endswith('.sh') or f.endswith('.py'):
                filepath = os.path.join(root, f)
                rel_path = os.path.relpath(filepath, ROOT_DIR)
                
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as sf:
                        content = sf.read()
                        
                    findings = []
                    for pattern, risk in DANGEROUS_PATTERNS:
                        if re.search(pattern, content):
                            findings.append(risk)
                            
                    status = "SAFE" if not findings else "HIGH RISK"
                    results.append({
                        'skill': f,
                        'path': rel_path,
                        'status': status,
                        'findings': findings
                    })
                except Exception as e:
                    pass

    return results

def main():
    print("="*60)
    print("🛡️  SKILLSPECTOR — AI AGENT SKILL SECURITY SCANNER")
    print("="*60)
    
    results = scan_skills()
    critical_count = sum(1 for r in results if r['status'] != "SAFE")
    
    print(f"Total Skills Scanned : {len(results)}")
    print(f"Safe Skills          : {len(results) - critical_count} ✅")
    print(f"Critical/High Risk   : {critical_count} ❌")
    print("-" * 60)
    
    for r in results:
        icon = "✅" if r['status'] == "SAFE" else "❌"
        print(f"• [{r['skill']}] ({r['path']}) → {icon} {r['status']}")
        for f in r['findings']:
            print(f"   ⚠️  {f}")
            
    print("="*60)
    if critical_count > 0:
        sys.exit(1)

if __name__ == '__main__':
    main()
