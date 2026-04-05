# INSTRUCTIONS.md

## Submission
Student: Usama Bin Muslehuddin
Version: v3
Push date: Friday April 3, 2026
Review date: Saturday April 4, 2026
Focus: Final app wiring and deployment-ready configuration.

## App Files In This Version
- `app.py`
- `requirements.txt`
- `Dockerfile`
- `.github/workflows/ci.yml`

## Shared Repository
Use this repository:
`https://github.com/Mohammed-Ashhad/Systems_Deploy_And_Implement_Project_SmartSpend_AI-.git`

## Push Order For This Date
1. Usama Bin Muslehuddin - v3
2. Ghaidaa Alomari - v3
3. Mohd Ashhad Gull - v3

Your turn: push first.
After your push: Ghaidaa Alomari should pull latest `main`, then continue with v3.

## Safe Push Workflow
Do not run Git commands inside this extracted `v3` folder. Use it only as a source folder for copying files into the shared repository clone.

If you do not already have the shared repository on your computer:
`git clone https://github.com/Mohammed-Ashhad/Systems_Deploy_And_Implement_Project_SmartSpend_AI-.git`

Move into the shared repository folder:
`cd Systems_Deploy_And_Implement_Project_SmartSpend_AI-`

Set your Git username for this repository:
`git config user.name "YOUR NAME"`

Set your GitHub email for this repository:
`git config user.email "YOUR_EMAIL@example.com"`

Pull the latest shared history before copying files:
`git pull origin main`

Copy only the app files listed above from this `v3` folder into the matching paths inside the shared repository.

Check the files before staging:
`git status`

Stage only the app files for this version. Do not stage `INSTRUCTIONS.md`.
`git add -- .github/workflows/ci.yml app.py Dockerfile requirements.txt`

Create the commit for this submission:
`git commit -m "Usama Bin Muslehuddin - v3 submission"`

Push the submission:
`git push origin main`

If Git rejects the push, stop, run `git pull origin main`, re-check `git status`, and only then retry the push.
Never run `git init` in this version folder. Never use `git push --force`.

## Review Day
Review date: Saturday April 4, 2026
Review the other two member submissions for `v3` inside the shared repository after everyone has pushed.

## Ready-to-Copy Review Comments
### Review Ghaidaa Alomari (Member 2)
GOOD:
- Final transaction routes connect dashboard data, delete flow, and AI report display.
- Qatar timezone conversion is a useful final detail for report timestamps.
SUGGESTIONS:
- Expand tests beyond smoke checks to cover model behavior and edge cases.
- Add validation around malformed ids or missing form fields.
ISSUES: Issues to fix before the final presentation:
- Current tests are lightweight and do not fully exercise the Mongo-backed transaction logic.

### Review Mohd Ashhad Gull (Member 3)
GOOD:
- The final dashboard layout is more complete and includes empty states, stats, and action areas.
- The AI route adds richer prompt context with category and monthly spending breakdowns.
SUGGESTIONS:
- Move AI configuration details into environment-driven settings for easier maintenance.
- Add deeper AI tests around prompt building and fallback behavior.
ISSUES: Issues to fix before the final presentation:
- The AI flow now exists end to end, but it still depends on correct external API configuration at runtime.

## Review Checklist
### Checklist For Reviewing Ghaidaa Alomari (Member 2)
- Check `models/transaction.py` for final CRUD logic.
- Check `routes/transactions.py` for timezone formatting and final route flow.
- Check `tests/test_transactions.py` for useful transaction-layer coverage.

### Checklist For Reviewing Mohd Ashhad Gull (Member 3)
- Check `routes/ai_analysis.py` for final AI flow and error handling.
- Check `templates/dashboard.html` and `static/styles.css` for the final UI state.
- Check `tests/test_ai.py` for AI-related review coverage.

## Note
This final version keeps the deployment files and finishes the shared app wiring.
