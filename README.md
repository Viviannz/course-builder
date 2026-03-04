# 📚 course-builder

A Claude skill that builds a fully personalized course on **any topic** — on demand.

Type `/course [topic]` and it generates a curriculum tailored to your level, language, and learning style. Resume where you left off. Add YouTube videos. Switch styles mid-lesson.

---

## ✨ Features

- **6 Learning Modes** — Structured Course, Sprint, Deep Dive, Project-Based, Socratic, Exam Prep
- **5 Teaching Styles** — Simple (ELI5), Academic, Conversational, Visual, Narrative
- **Progress tracking** — saved to JSON; works in both Claude Code and Cowork
- **Exercises with scoring** — per module, with feedback and reteaching on mistakes
- **Resume where you left off** — picks up your course from your last lesson
- **YouTube video integration** — add any YouTube URL mid-course; builds a lesson around it
- **Any language** — teach in English, Spanish, French, Portuguese, or whatever you name

---

## 🚀 Quick Start

### Claude Code (terminal)
```bash
# Install the skill
cp course-builder.skill ~/.claude/skills/

# Start a course
/course python for beginners

# Resume later
/course resume python
```

### Cowork (desktop app)
Install `course-builder.skill` via the Skills panel, then just type:
```
/course machine learning — I'm a software engineer, academic style, deep dive
```

---

## 🎛️ Commands

| Command | What it does |
|---------|-------------|
| `/course [topic]` | Start a new course |
| `/course save` | Save progress manually |
| `/course progress` | Show your progress dashboard |
| `/course mode [name]` | Switch learning mode |
| `/course style [name]` | Switch teaching style |
| `/course outline` | Show full course outline |
| `/course quiz` | Impromptu quiz on anything covered |
| `/course skip` | Skip current lesson/module |
| `/course slower` | More explanation, smaller steps |
| `/course faster` | Less detail, move quicker |

*(Legacy `/learn` commands work as aliases)*

---

## 📁 Progress Files

Progress is saved as JSON so you can resume from any device:

| Environment | Location |
|-------------|----------|
| **Cowork** | `outputs/course-builder-[topic].json` + `.learn/[topic].json` |
| **Claude Code** | `.learn/[topic].json` in your current directory |

---

## 📂 File Structure

```
course-builder/
├── SKILL.md                        # Main skill instructions
├── scripts/
│   └── progress.py                 # Progress save/load utility
└── references/
    └── modes-and-styles.md         # Detailed guidance for all modes & styles
```

---

## 💡 Example Prompts

```
/course stoicism — visual style, exam prep, philosophy exam in 3 weeks

/course python — I'm a marketer, total beginner, 30 mins/session, conversational

/course machine learning — software engineer background, academic, deep dive mode

/course public speaking — project-based, I want to practice a real talk

teach me about the stoic philosophers
```

---

## 🎬 YouTube Integration

Mid-course, just say:
```
Add this video: https://youtube.com/watch?v=...
```

The skill fetches the title, description, and transcript (where available), summarizes it, and offers to build a lesson around it — or treats it as supplementary material.

---

## 📊 Progress Dashboard

```
📊 Your Machine Learning Course — Progress Report

Mode: Deep Dive | Style: Academic | Level: Intermediate

Progress: ████████░░░░░░░░ 47% complete

✅ Module 1: Foundations — Completed
✅ Module 2: Supervised Learning — Completed (Score: 8/10)
▶️  Module 3: Neural Networks — In progress (Lesson 2/4)
⬜ Module 4: Unsupervised Learning — Not started

Average quiz score: 82%
Last active: 2026-03-04
```

---

## 🙏 Credits

Inspired by the original `/learn` Claude Code skill concept by [Alex Spalato](https://alexaspalato.gumroad.com/l/learn-anything). Built and extended using Anthropic's Claude + Cowork skill builder.

---

## 📄 License

MIT — free to use, modify, and share.
