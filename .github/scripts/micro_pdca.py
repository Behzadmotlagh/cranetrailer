name: Micro-PDCA Cycle

on:
  schedule:
    # هر ۳۰ دقیقه یک‌بار
    - cron: '*/30 * * * *'
  workflow_dispatch:

jobs:
  micro_pdca:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v3
        with:
          token: ${{ secrets.GH_BOT_TOKEN }}

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: pip install PyGithub

      - name: Run micro-PDCA script
        env:
          GITHUB_TOKEN: ${{ secrets.GH_BOT_TOKEN }}
          REPO: ${{ github.repository }}
        run: python3 .github/scripts/micro_pdca.py

      - name: Post status to issue (optional)
        if: success()
        run: echo "✅ micro-PDCA cycle completed at $(date)"
```
