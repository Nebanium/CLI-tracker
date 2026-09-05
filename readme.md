# CLI Tracker

A command-line tool for tracking deadlines and progress across multiple 
tracks — architecture coursework, dev milestones, and project tasks — 
with add/edit/delete, mark-done, a built-in countdown timer, and CSV export.

## Features
- Add entries with title, category, and due date
- Mark entries done, delete entries, or clear all
- Set a duration and run a live countdown timer for a task
- Export all entries to CSV for use in spreadsheets
- Data persists between runs via JSON

## How to run
```bash
python tracker.py
```
Follow the on-screen menu to add, view, edit, or export entries.

## What I learned
Refactored this from a set of loose functions sharing a global list into 
a proper `Tracker` class — the shift from passing `entries` around 
everywhere to having methods share state through `self` was the main 
concept that clicked doing this project.

## Tech
Python 3, standard library only (`json`, `os`, `csv`, `time`) — no 
external dependencies.