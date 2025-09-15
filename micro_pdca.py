#!/usr/bin/env python3
from github import Github
import os, re

TOKEN = os.getenv('GITHUB_TOKEN')
REPO  = os.getenv('REPO')

g = Github(TOKEN)
repo = g.get_repo(REPO)

# ۱. شناسایی آخرین micro-sprint
issues = repo.get_issues(state='all', labels=['micro-sprint'])
nums   = [int(re.search(r'micro-sprint-(\d+)', i.title).group(1))
          for i in issues if re.search(r'micro-sprint-(\d+)', i.title)]
next_n = max(nums)+1 if nums else 1

# ۲. اگر Sprint قبلی Open هست، آن را ببند
open_prev = [i for i in repo.get_issues(state='open', labels=['micro-sprint'])]
for i in open_prev:
    i.create_comment("⏱️ Closing this sprint before new one.")
    i.edit(state='closed')

# ۳. ایجاد Issue جدید
title = f"micro-sprint-{next_n}: افزودن تست edge case زاویه بوم {30}°"
body  = (
    f"**معیار پذیرش**:\n"
    f"- `compute_tipping_moment(30)` مقدار مرجع صحیح را بازگرداند\n"
    f"- تست واحد نوشته شده و از CI عبور کند\n\n"
    f"⏱️ این sprint از {os.popen('date').read().strip()} آغاز می‌شود."
)
new_issue = repo.create_issue(
    title=title,
    body=body,
    labels=['micro-sprint', '30min']
)

print(f"Created {new_issue.html_url}")
