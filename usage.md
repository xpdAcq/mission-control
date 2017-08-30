# Using Mission Control

## Everyone: How to use Mission Control
1. Make a GitHub account.
1. Install [ZenHub](https://www.zenhub.com/). ZenHub adds various agile software development tools to GitHub via a Chrome/Firefox extension. Please feel free to read the ZenHub documentation on how to use their software in the general sense 
1. Ask to join xpdAcq as a developer or as a user. Via GitHub or email (the email must contain your github handle (eg. CJ-Wright))

## Users: How to Use Mission Control
### Requesting Features
#### GitHub
1. Go to [Mission Control issues](https://github.com/xpdAcq/mission-control/issues).
1. Press the `New Issues` button.
1. Please start the title with __[Feature Request]__.
1. Follow the instructions in the issue template (it will show up in the `write` box).
1. Once finished click submit.
1. The dev team will read the issue and go from there.
#### xpd-users/xpd-dev Google Groups
1. Go to the [xpd-users](https://groups.google.com/forum/#!forum/xpd-users)/[xpd-dev](https://groups.google.com/forum/#!forum/xpd-dev) Google Group
1. Copy the template from the pinned discussion.
1. Please start the title with __[Feature Request]__.
1. Fill out the template in a new discussion.
1. Submit the discussion
1. The dev team will read the issue and go from there.
### Tracking Features
1. Go to [Mission Control issues](https://github.com/xpdAcq/mission-control/issues).
1. Find the feature request in the issues.
1. If the feature is currently being worked on it will be listed as a ZenHub `Epic`.
1. The Epic will have issues associated with it, and a progress bar which shows how many of those issues have been resolved. When all the issues have been closed the feature is ready.
### Tracking Releases
1. Go to [Mission Control releases folder](https://github.com/xpdAcq/mission-control/tree/master/releases)
1. Open the file for the requested release.
1. The release will have links to all the Epics being worked on for this release.
1. The release will also have a date for release and other information.
1. A milestone will also be created for the release those can be found [here](https://github.com/xpdAcq/mission-control/milestones) and will have a link back to the relevant release definition in the  `release` folder. 


## Dev Team: How to use Mission Control

### Workflow
1. Submit a feature request by creating an issue on this repo.
1. The Dev team will review the feature request. If the feature request is accepted it will be turned into a ZenHub Epic. (Epics are like issues but they can be connected to issues across repos, so they allow us to track development across the stack)
1. Once the Dev team turns the issue into an Epic the Dev team will start to write issues across the stack specifying software which needs to be written to add the feature as requested.
1. These issues will be attached to the Epic (or Epics, a single issue could solve problems across multiple feature requests).
1. Epics are then collated into a release. The release definition will go into this repo under `releases` and a milestone will be created to track the release.
1. The Dev team will then distribute the work amongst the team and start issuing PRs which close the issues.
1. Progress on a given feature can be tracked by examining how many issues for a given feature are still open.
1. Once all the issues against a Epic are closed that feature request is satisfied in the master branch. (If you need the functionality ASAP you can then install the master branch)
1. Once all the epics associated with a release are closed then we will package and release the code.
