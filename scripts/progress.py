#!/usr/bin/env python3
"""
Progress tracker for the learn-anything skill.
Handles saving, loading, and displaying course progress.
"""

import json
import os
import sys
import re
from datetime import datetime
from pathlib import Path


def slugify(text: str) -> str:
    """Convert topic name to a safe filename slug."""
    slug = text.lower().strip()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'[\s]+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    return slug[:50]


def get_progress_path(topic: str, env: str = "cowork") -> Path:
    """
    Get the progress file path for a given topic and environment.
    env: 'cowork' or 'codex' (Claude Code)
    """
    slug = slugify(topic)
    if env == "cowork":
        # Outputs folder for Cowork
        outputs_dir = Path("/sessions/zen-jolly-dijkstra/mnt/outputs")
        outputs_dir.mkdir(parents=True, exist_ok=True)
        return outputs_dir / f"learn-progress-{slug}.json"
    else:
        # .learn folder for Claude Code
        learn_dir = Path(".learn")
        learn_dir.mkdir(exist_ok=True)
        return learn_dir / f"{slug}.json"


def load_progress(topic: str, env: str = "cowork") -> dict | None:
    """Load progress for a topic. Returns None if no progress file exists."""
    path = get_progress_path(topic, env)
    if path.exists():
        with open(path) as f:
            return json.load(f)
    return None


def save_progress(progress: dict, env: str = "cowork") -> str:
    """Save progress to the appropriate file. Returns the path."""
    topic = progress.get("topic", "unknown")
    path = get_progress_path(topic, env)
    progress["last_active"] = datetime.utcnow().isoformat()
    with open(path, "w") as f:
        json.dump(progress, f, indent=2)
    return str(path)


def create_progress(topic: str, level: str, mode: str, style: str,
                    language: str = "English", session_minutes: int = 30,
                    course_outline: dict = None) -> dict:
    """Create a new progress object."""
    return {
        "topic": topic,
        "topic_slug": slugify(topic),
        "language": language,
        "level": level,
        "learning_mode": mode,
        "teaching_style": style,
        "session_minutes": session_minutes,
        "course_outline": course_outline or {},
        "current_module": 1,
        "current_lesson": 1,
        "completed_modules": [],
        "completed_lessons": [],
        "exercise_scores": [],
        "youtube_resources": [],
        "created_at": datetime.utcnow().isoformat(),
        "last_active": datetime.utcnow().isoformat(),
        "notes": []
    }


def display_progress_dashboard(progress: dict) -> str:
    """Generate a text dashboard from a progress object."""
    outline = progress.get("course_outline", {})
    modules = outline.get("modules", [])
    total = len(modules)
    completed = len(progress.get("completed_modules", []))
    pct = int((completed / total * 100)) if total > 0 else 0
    bar_filled = int(pct / 5)
    bar = "█" * bar_filled + "░" * (20 - bar_filled)

    scores = progress.get("exercise_scores", [])
    avg_score = (sum(s.get("pct", 0) for s in scores) / len(scores)) if scores else None

    lines = [
        f"📊 Your {progress['topic']} Course — Progress Report",
        "",
        f"**Mode:** {progress['learning_mode']} | **Style:** {progress['teaching_style']} | **Level:** {progress['level']}",
        "",
        f"Progress: {bar} {pct}% complete",
        "",
    ]

    current_mod = progress.get("current_module", 1)
    current_les = progress.get("current_lesson", 1)

    for i, mod in enumerate(modules, 1):
        mod_name = mod.get("name", f"Module {i}")
        if i in progress.get("completed_modules", []):
            mod_scores = [s for s in scores if s.get("module") == i]
            score_str = ""
            if mod_scores:
                s = mod_scores[-1]
                score_str = f" (Score: {s.get('correct', 0)}/{s.get('total', 0)})"
            lines.append(f"✅ Module {i}: {mod_name} — Completed{score_str}")
        elif i == current_mod:
            lines.append(f"▶️  Module {i}: {mod_name} — In progress (Lesson {current_les}/{len(mod.get('lessons', []))})")
        else:
            lines.append(f"⬜ Module {i}: {mod_name} — Not started")

    if avg_score is not None:
        lines.append(f"\n**Average quiz score:** {avg_score:.0f}%")

    yt = progress.get("youtube_resources", [])
    if yt:
        lines.append(f"📹 YouTube resources added: {len(yt)}")

    last = progress.get("last_active", "")
    if last:
        lines.append(f"**Last active:** {last[:10]}")

    return "\n".join(lines)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "help"

    if cmd == "load":
        topic = sys.argv[2]
        env = sys.argv[3] if len(sys.argv) > 3 else "cowork"
        prog = load_progress(topic, env)
        if prog:
            print(json.dumps(prog, indent=2))
        else:
            print("null")

    elif cmd == "dashboard":
        topic = sys.argv[2]
        env = sys.argv[3] if len(sys.argv) > 3 else "cowork"
        prog = load_progress(topic, env)
        if prog:
            print(display_progress_dashboard(prog))
        else:
            print(f"No progress found for '{topic}'")

    elif cmd == "slugify":
        print(slugify(sys.argv[2]))

    else:
        print("Usage: progress.py [load|dashboard|slugify] <topic> [env]")
