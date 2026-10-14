# Git & GitHub Practice Exercises

Do these in order. Each one uses a new branch and a Pull Request.
Rule: never commit directly to `main`.

## Exercise 1: Your first PR
1. `git switch -c feature/add-author`
2. Add your name to the bottom of README.md.
3. `git add .` then `git commit -m "Add author to README"`
4. `git push -u origin feature/add-author`
5. On GitHub, click **Compare & pull request**, then **Create pull request**.
6. Watch the **Tests** check run on the PR, then merge it.
7. `git switch main && git pull && git branch -d feature/add-author`

## Exercise 2: Add a feature
Add a `clear` command that deletes all completed tasks.
1. Branch: `git switch -c feature/clear-done`
2. Add `clear_done(tasks)` to `todo/core.py`.
3. Add a `clear` sub-command in `todo/cli.py`.
4. Add a test in `tests/test_core.py`.
5. Run tests, commit in small steps (one commit for logic, one for CLI, one for tests).
6. Push, open PR, merge.

## Exercise 3: Fix a bug
`add_task` accepts a title of any length. Make it reject titles over 100 characters.
1. Branch: `git switch -c fix/title-length`
2. Write the failing test first, commit it.
3. Fix the code, commit it.
4. PR and merge. Look at `git log --oneline` to see your story.

## Exercise 4: Create a merge conflict on purpose
1. `git switch -c branch-a` and change the first line of README.md to "Version A". Commit.
2. `git switch main`, then `git switch -c branch-b` and change the same line to "Version B". Commit.
3. `git merge branch-a` (you are on branch-b).
4. Git reports a conflict. Open README.md in VS Code, click **Accept Both** or edit by hand, delete the `<<<<<<<` markers.
5. `git add README.md` then `git commit`.

## Exercise 5: Undo mistakes
- Edit a file, then discard it: `git restore <file>`
- Stage a file by mistake, unstage it: `git restore --staged <file>`
- Fix the last commit message: `git commit --amend -m "new message"` (only before pushing)
- Undo the last commit but keep your changes: `git reset --soft HEAD~1`
- Safely undo a pushed commit: `git revert <commit-hash>`

## Exercise 6: Issues
1. On GitHub, open the **Issues** tab and create "Add due dates to tasks".
2. Make a branch, implement it, and put `Closes #1` in the PR description.
3. Merge the PR and watch the issue close automatically.

## Exercise 7: Fork and contribute (optional)
Ask a friend to fork your repo, change something, and open a PR to you.
Review it, comment on a line, and merge it.
