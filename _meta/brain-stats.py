#!/usr/bin/env python3
"""
Brain Stats Logger
Logs current metrics (files, folders, memories, skills, lessons, words, commit hash)
to _meta/brain-stats.jsonl for historical growth tracking.
"""
import os
import json
import re
import subprocess
from datetime import datetime

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def capture_stats():
    files_count = 0
    folders_count = 0
    words_count = 0
    
    for root, dirs, files in os.walk(ROOT_DIR):
        dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', '__pycache__']]
        folders_count += len(dirs)
        for f in files:
            if f.endswith('.md'):
                files_count += 1
                fp = os.path.join(root, f)
                try:
                    with open(fp, 'r', encoding='utf-8', errors='ignore') as mf:
                        words_count += len(re.findall(r'\b\w+\b', mf.read()))
                except Exception:
                    pass

    # Count memories
    memories_count = 0
    mem_dir = os.path.join(ROOT_DIR, 'memory')
    if os.path.exists(mem_dir):
        memories_count = len([f for f in os.listdir(mem_dir) if f.endswith('.md') and f != 'MEMORY.md'])

    # Count skills
    skills_count = 0
    skills_dir = os.path.join(ROOT_DIR, 'skills')
    if os.path.exists(skills_dir):
        skills_count = len([f for f in os.listdir(os.path.join(skills_dir, 'rituals')) if f.endswith('.md')])

    # Count lessons
    lessons_count = 0
    lessons_file = os.path.join(ROOT_DIR, 'skills', 'lessons.md')
    if os.path.exists(lessons_file):
        try:
            with open(lessons_file, 'r', encoding='utf-8', errors='ignore') as lf:
                lessons_count = len(re.findall(r'^###\s+\d{4}-\d{2}-\d{2}', lf.read(), re.MULTILINE))
        except Exception:
            pass

    # Git commit hash
    git_commit = "N/A"
    try:
        res = subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True, cwd=ROOT_DIR)
        if res.returncode == 0:
            git_commit = res.stdout.strip()
    except Exception:
        pass

    entry = {
        "timestamp": datetime.now().isoformat(),
        "files": files_count,
        "folders": folders_count,
        "memories": memories_count,
        "skills": skills_count,
        "lessons": lessons_count,
        "words": words_count,
        "git_commit": git_commit
    }

    stats_path = os.path.join(ROOT_DIR, '_meta', 'brain-stats.jsonl')
    with open(stats_path, 'a', encoding='utf-8') as sf:
        sf.write(json.dumps(entry) + '\n')

    print("=== Brain Stats Captured ===")
    print(json.dumps(entry, indent=2))

if __name__ == '__main__':
    capture_stats()
