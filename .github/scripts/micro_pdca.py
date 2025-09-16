#!/usr/bin/env python3
from github import Github
import os, re

TOKEN = os.getenv('GITHUB_TOKEN')
REPO  = os.getenv('REPO')

g = Github(TOKEN)
repo = g.get_repo(REPO)

# پیدا کردن شماره بعدی micro-sprint
issues = repo.get_issues(state='all', labels=['micro-sprint'])
nums = [
    int(re.search(r'micro-sprint-(\d+)', i.title).group(1))
    for i in issues if re.search(r'micro-sprint-(\d+)', i.title)
]
next_n = max(nums)+1 if nums else 1

# بستن اسپرینت قبلی
for i in repo.get_issues(state='open', labels=['micro-sprint']):
    i.create_comment("⏱️ Closing this sprint before new one.")
    i.edit(state='closed')

# ایجاد Issue جدید
degree = 30
title = f"micro-sprint-{next_n}: افزودن تست edge case زاویه بوم {degree}°"
body = (
    "**معیار پذیرش**:\n"
    f"- `compute_tipping_moment({degree})` مقدار مرجع صحیح را بازگرداند\n"
    "- تست واحد نوشته شده و از CI عبور کند\n\n"
    f"⏱️ این sprint از {os.popen('date').read().strip()} آغاز می‌شود."
)
new_issue = repo.create_issue(
    title=title,
    body=body,
    labels=['micro-sprint','30min']
)

print(f"Created {new_issue.html_url}")
