# Contribution plan
Issue: Add a beginner-plugin contribution guide example #63
Issue URL: https://github.com/AmalChUm/students-arcade/issues/63
Selected difficulty: beginner
Proposed branch: feature/issue-63-beginner-plugin-example
Expected files: plugins/beginner_guide_example.py, contribution-plan.md, ai-log.md

## My interpretation of the task
Add a clear, minimal Python plugin module inside plugins/ that conforms to the required launcher contract (AUTHOR, APP_NAME, run()) to serve as a practical, working example for new contributors.

## Acceptance criteria
- [ ] Placed in plugins/ with a unique descriptive filename.
- [ ] Defines AUTHOR, APP_NAME, and run().
- [ ] Uses only standard Python libraries.
- [ ] python main.py discovers and executes the module cleanly.
- [ ] Output is readable and verified.

## Possible risks or questions
- Ensure main.py is strictly untouched.
- Verify that importing the plugin triggers no unintended side effects or immediate output.