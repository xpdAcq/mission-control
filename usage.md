# How to use mission-control

## Everyone
1. Make a GitHub account.
1. Install [ZenHub](https://www.zenhub.com/). ZenHub adds various agile software development tools to GitHub via a Chrome/Firefox extension. Please feel free to read the ZenHub documentation on how to use their software in the general sense 
1. Ask to join xpdAcq as a developer or as a user. Via GitHub or email (the email must contain your github handle (eg. CJ-Wright))

## Workflow
1. Submit a feature request by creating an issue on this repo.
1. The Dev team will review the feature request. If the feature request is accepted it will be turned into a ZenHub Epic. (Epics are like issues but they can be connected to issues across repos, so they allow us to track development across the stack)
1. Once the Dev team turns the issue into an Epic the Dev team will start to write issues across the stack specifying software which needs to be written to add the feature as requested.
1. These issues will be attached to the Epic (or Epics, a single issue could solve problems across multiple feature requests).
1. Epics are then collated into a release. The release definition will go into this repo under `releases` and a milestone will be created to track the release.
1. The Dev team will then distribute the work amongst the team and start issuing PRs which close the issues.
1. Progress on a given feature can be tracked by examining how many issues for a given feature are still open.
1. Once all the issues against a Epic are closed that feature request is satisfied in the master branch. (If you need the functionality ASAP you can then install the master branch)
1. Once all the epics associated with a release are closed then we will package and release the code.
