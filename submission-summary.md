# Submission Summary

## Submission Metadata
29. **Student Name:** Suleman Saddet
30. **Selected Issue Title & URL:** Add a beginner-plugin contribution guide example (#63) - https://github.com/AmalChUm/students-arcade/issues/63
31. **Difficulty Label & Task/Category Label:** `beginner`, `documentation` / `plugin-example`
32. **Parent Repository URL:** https://github.com/AmalChUm/students-arcade
33. **Fork URL:** https://github.com/sulemansaddet/students-arcade
34. **Local Clone Folder Name:** `students-arcade-contribution`
35. **Feature Branch URL:** https://github.com/sulemansaddet/students-arcade/tree/feature/issue-63-beginner-plugin-example
36. **Commit URLs:** https://github.com/sulemansaddet/students-arcade/commits/feature/issue-63-beginner-plugin-example/
37. **Verification Output:** Recorded in `evidence/02-verification.txt`
38. **Pull Request URL:** https://github.com/AmalChUm/students-arcade/pull/[YOUR_PR_NUMBER]
39. **Kanban Project URL:** https://github.com/users/sulemansaddet/projects/1
40. **Screenshot of Issue on Board:** `evidence/screenshots/board-issue.png`
41. **Screenshot Showing Issue Moving Through Statuses:** `evidence/screenshots/board-statuses.png`

---

## Required Documentation & Evidence Deliverables
42. `contribution-plan.md` - Included in root directory
43. `ai-log.md` - Included in root directory
44. `evidence/01-setup.txt` - Included in evidence/
45. `evidence/02-verification.txt` - Included in evidence/
46. `evidence/03-self-review.txt` - Included in evidence/


## 47–57. Reflection Questions

### 48. Why did you choose this issue?
I chose Issue #63 to establish a clean, verified, and minimal plugin example that helps onboard future student contributors while demonstrating proper software engineering practices (branching, PR linkage, and project board tracking) on an open-source codebase.

### 49. What did you learn by reading the existing repository before coding?
I learned how `main.py` uses dynamic importing to automatically discover and execute Python modules inside the `plugins/` directory based on a defined contract (`AUTHOR`, `APP_NAME`, `run()`), eliminating the need to modify the core entrypoint.

### 50. How does the plugin or documentation contribution fit the existing Students Arcade structure?
It resides cleanly in the `plugins/` folder (`plugins/beginner_guide_example.py`) alongside existing modules and strictly adheres to the standard launcher interface contract without introducing non-standard dependencies or altering central codebase logic.

### 51. What was the most important acceptance criterion?
The most critical acceptance criterion was ensuring `main.py` remained completely untouched while still discovering and executing the plugin successfully upon startup.

### 52. Which AI suggestion did you accept?
I accepted the AI's suggestion to use a minimal return-string structure inside `run()` to align with the beginner plugin specification.

### 53. Which AI suggestion did you revise or reject?
I rejected a suggestion to modify `main.py` to register the plugin, as modifying `main.py` was strictly prohibited by the lab constraints for beginner plugin issues.

### 54. What did you verify yourself instead of trusting the AI?
I manually executed `python main.py` inside Git Bash using my local Anaconda environment to confirm dynamic plugin discovery and verified that `git status` showed `main.py` as untracked/unmodified.

### 55. What evidence shows that your contribution works?
The log saved in `evidence/02-verification.txt` demonstrates `python main.py` running cleanly and outputting the string returned by `plugins/beginner_guide_example.py`.

### 56. What was the difference between your fork and the parent repository?
My fork contains the `feature/issue-63-beginner-plugin-example` branch with the newly added plugin, contribution plan, AI usage log, evidence directory, and submission summary markdown file.

### 57. What would you improve in a future pull request?
In a future pull request, I would implement unit tests using `unittest` or `pytest` to automatically test plugin discovery and return types without needing manual execution.