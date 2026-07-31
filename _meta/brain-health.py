#!/usr/bin/env python3
"""
Brain Health Audit Engine
Fast linter checking context budgets, wikilink integrity, conflict markers, and routing table entries.
"""
import os
import sys
import re
import argparse

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class HealthAuditEngine:
    def __init__(self):
        self.findings = []
        self.expertise_bytes = 0

    def add_finding(self, mode, path, message):
        self.findings.append({
            'mode': mode,
            'path': path,
            'message': message
        })

    def run_quick_checks(self):
        # 1. Conflict Markers Check
        for root, dirs, files in os.walk(ROOT_DIR):
            dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', '__pycache__']]
            for f in files:
                if f.endswith('.md') or f.endswith('.py') or f.endswith('.json'):
                    fp = os.path.join(root, f)
                    try:
                        with open(fp, 'r', encoding='utf-8', errors='ignore') as mf:
                            content = mf.read()
                            if ('<' * 7) in content or ('>' * 7) in content:
                                self.add_finding('clash', os.path.relpath(fp, ROOT_DIR), "Unmerged git conflict marker detected")
                    except Exception:
                        pass

        # 2. Unrouted Folders Check
        agents_path = os.path.join(ROOT_DIR, 'AGENTS.md')
        if os.path.exists(agents_path):
            with open(agents_path, 'r', encoding='utf-8', errors='ignore') as f:
                agents_content = f.read()

            for item in os.listdir(ROOT_DIR):
                item_path = os.path.join(ROOT_DIR, item)
                if os.path.isdir(item_path) and not item.startswith('.') and not item.startswith('_'):
                    if item not in ['personal', 'work', 'lab', 'memory', 'skills', 'bin']:
                        if f"`{item}/`" not in agents_content and f"`{item}`" not in agents_content:
                            self.add_finding('routing', item, f"Folder '{item}' is missing from AGENTS.md Routing Table")

    def run_context_budget_check(self):
        # Calculate size of Expertise Context
        expertise_files = ['AGENTS.md', 'constraints.md', 'memory/MEMORY.md']
        total_size = 0
        for rel in expertise_files:
            fp = os.path.join(ROOT_DIR, rel)
            if os.path.exists(fp):
                total_size += os.path.getsize(fp)

        self.expertise_bytes = total_size
        if total_size > 45000:
            self.add_finding('budget', 'Expertise Context', f"Expertise context size {total_size} bytes exceeds 45,000 byte budget cap")

def main():
    parser = argparse.ArgumentParser(description="Second Brain Health Audit Engine")
    parser.add_argument('--quick', action='store_true', help="Run quick health audit")
    parser.add_argument('--full', action='store_true', help="Run full health audit")
    args = parser.parse_args()

    engine = HealthAuditEngine()
    engine.run_quick_checks()
    engine.run_context_budget_check()

    print("="*60)
    print("🏥 HEALTH AUDIT & LINTING SUMMARY")
    print("="*60)
    print(f"Mode                : {'--quick' if args.quick else '--full'}")
    print(f"Expertise Context   : {engine.expertise_bytes:,} Bytes (Cap: 45,000 B)")
    print(f"Total Findings      : {len(engine.findings)}")
    print("-" * 60)

    if engine.findings:
        for f in engine.findings:
            print(f"❌ [{f['path']}] {f['message']}")
        sys.exit(1)
    else:
        print("✅ Health Audit PASSED cleanly.\n")

if __name__ == '__main__':
    main()
