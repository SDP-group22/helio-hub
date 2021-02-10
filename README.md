# Helio-app
An Android application for controlling Helio blinds

### Things not to do
- Do not directly edit the main branch, only use GitHub pull requests
- Do not merge any branches directly into the main branch without using a GitHub pull request
- Do not push the main branch to GitHub (there should be no reason to if previous steps are followed)
- Do not merge pull requests without a reviewer approving it

### Workflow guide
1. Choose a card from the [kanban board](https://github.com/SDP-group22/Helio-app/projects/1), assign yourself to it, and drag it to the In progress column.
2. Switch to the main branch with `git checkout main` then `git pull` from console or use Android studio to do the same, to make sure your main branch is up to date.
3. On console, `git checkout main` then `git checkout -b short_descriptive_name` to create a new branch to work on your task. Or, in Studio, in the Git tab, right click on main and select New Branch from Selected and call it short_descriptive_name. Name examples: homepage_mockup, readme_workflow_guide.
4. Complete your task, adding files and committing whenever you want
5. If main has been updated on GitHub since you started, `git fetch`, then either merge `git merge origin/main` or rebase (right click on remote/origin/main and click Rebase current onto selected), and fix any merge errors if you need to.
6. Push your changes with `git push`.
7. Create a pull request on GitHub, add any descriptions or explanations as necessary, and mention the team with @SDP-group22/app to request a review. Link the pull request to the issue it is for.
8. Move the card to Review on the kanban board.
9. If the reviewer requested changes, make them and push again, it will update the pull request. Then re-request a review and move to Review column.
10. Once the reviewer has accepted your changes, merge the pull request on GitHub and delete the branch.

### Review guide
1. Assign yourself as the reviewer for the card.
2. `git fetch` and checkout the branch that the work was done on, and test it.
3. Go to files changed and review the changes, making comments and requesting changes if necessary. Consider if the goal has been achieved, code style, clarity, comments, etc.
4. When you approve a review, move the issue card to Reviewer approved.
5. If you request changes, move the issue to In progress and add the rework label.

### connecting to `helio-hub` (server side)
In order to do anything interesting within the app, we have to communicate with the Hub.
You can run the Hub on your own device in the following way:
1. clone `https://github.com/SDP-group22/helio-hub`
2. follow the instructions in the `README` over there to launch the Hub
3. the app can now communicate with the Hub by sending requests to `10.0.2.2:4310` (`10.0.2.2` is `localhost` in Android)
