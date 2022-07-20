# skeletor

## A Project Template for Data Science Campus Projects

### 1. Guides for Private AND Public Repositories

#### 1.1 Introduction

This repository is intended to provide you with the documents you need to
include to get a repository started and give guidance as to what the contents
should be. The minimum content contained in the README.md for your project
should be (in the most suitable order for the content):

- description of what the project is
- instruction on how to install the tool (if applicable)
- detailed instructions on basic use
- a demo of the code

With the inclusion of all documents included here, your repository should meet
all of the recommended [community standards on github.com](https://help.github.com/en/categories/building-a-strong-community).

Once you have copied this directory you should replace the content of this file
with the description of your work.

Whilst no mandatory recommendation is made as to how to
structure the directories or manage the project itself - as this will vary based
on the needs and the abilities of those doing the development work - guidelines
are provided below on how to conduct your project in an Agile manner.

If your project is complex enough to warrant a documentation website please add
a branch called `gh_pages` and place your documentation (in html format) there.
Once you do this your html files will be rendered at
https://datasciencecampus.github.io/projectName

#### 1.2. Cloning this Repo

There are two ways to use this template:

##### 1.2.1. Using GitHub (simple method)

At the top of the main page of this repo is a green [Use this template](https://github.com/datasciencecampus/skeletor/generate) button, which
will clone this repository into a new repository of your choice. The Issue Templates are 
also cloned. Unfortunately, Issue Labels, and Project Boards are not cloned automatically,
and you will have to manually add these (guidelines below).

##### 1.2.2. Using Git

Create your new repository with a suitable projectName.

Clone this template to the new repository using

``` sh
git clone git@github.com:datasciencecampus/skeletor projectName
```

which will then create a new directory with your project's name and place all of
the files into it. However, the remote address will remain as the skeletor repo
until you do

``` sh
git remote set-url origin git@github.com:datasciencecampus/projectName
```

##### 2.3. Adding additional Labels

The [generic GitHub labels are limited in their use](https://medium.com/@dave_lunny/sane-github-labels-c5d2e6004b63),
this repository has additional [labels](https://github.com/datasciencecampus/skeletor/blob/develop/packages/custom-labels.json):

- Low
- Medium
- High
- Critical
- Legal!
- Data!
- Engagement!
- Resource!
- Tech!

The first four define the priority of the task. The last five are to highlight any blockers.

To setup these labels do the following:

```
npm i -g git-labelmaker
cd projectName
git-labelmaker
```

Then go to 'Add labels from package' and then type:

```
packages/custom-labels.json
```

The 'Project' labels encompass the majority of Discovery tasks. However, add more labels if you need (either manually or to the JSON file).

### 2. Guides for Private Repositories ONLY

#### 2.1. Using GitHub for Project Management (Agile)

Note: All updates for a project must be included on the relevant
[project on the portfolio board](https://github.com/orgs/datasciencecampus/projects/21).
These guidelines relate to the `project repository` that you created using the above guidelines.

##### 2.1.1. Projects (Phase)

This repository shows three projects in the [Project panel](https://github.com/datasciencecampus/skeletor/projects):
Discovery, Delivery and Dissemination. These projects are setup based on the Campus' project life-cycle and each use a kanban board. Issues (tasks) should be assigned to the relevant stage of the project life-cycle.

To setup click `New Project` and then select 'Automated Kanban with Review' template style for each. This will add the following columns to the Kanban: `To do`, `In Progress`, `Review in Progess`, `Reviewer approved`, `Done`. Add a new column called `Blocked` and move this between `To do` and `In Progress`.

##### 2.1.2. Milestones (Roadmap)

[GitHub Milestones](https://github.com/datasciencecampus/skeletor/milestones) can be used to reflect the project life-cycle phase roadmap. By assigning a task to a Project and a Milestone, progress on individual sprints as well as stages of the project life-cycle can be viewed by the project manager and delivery manager. 

##### 2.1.3. Sprints (Labels)

The sprint number, start and end date should be created as a label (e.g. `Sprint 1 25/11 - 8/12`) and assigned to a task.

##### 2.1.4. Issues (Tasks)

This GitHub template comes with four [Issue templates](https://github.com/datasciencecampus/skeletor/issues/new/choose):
`Bug report`, `Feature request`, `Use query` and `Task`. 

The [Task issue template](https://github.com/datasciencecampus/skeletor/issues/new?assignees=&labels=&template=task.md&title=)
should be used to create tasks during the project. Issues (tasks) can be created and assigned ad-hoc, or during stand-ups.

Each Task should have:

* An assigned owner(s), who is/are responsible for completing the task
* Labels to for the sprint, priority and blocker (if applicable)
* Linked to a Project
* Linked to a Milestone

##### 2.1.5. Wiki

The wiki should be used to hold all non-confidential information and links to confidential documents (which should be saved to SharePoint under Projects > projectName). 

[The wiki of skeletor](https://github.com/datasciencecampus/test-clone/wiki) has been setup with a distinct structure to record Sprint Goals, Retrospectives, Show and Tells, Meeting Notes, Technical Information, Project Documentation. To use this template the easier way is:

* In your created repository, create a blank wiki page.
* As GitHub wiki pages are just repositories, clone the Wiki pages locally using `git clone https://github.com/datasciencecampus/projectName/wiki`
* Clone the skeletor repository's wiki pages using `git clone https://github.com/datasciencecampus/skeletor/wiki`
* Copy the markdown files from the local skeletor folder to your new repository folder
* Use `git add .`, `git commit -m 'added wiki pages from skeletor`, `git push` to push the changes back up

##### 2.1.6. Benefits

- This will aid delivery and project managers to see the progress of projects in the project life-cycle
- a comprehensive use of an 'issue' in GitHub will allow delivery and project managers to filter tasks to assign additional resource
- use of the projects board for each stage of the life-cycle will allow users to quickly see what stage a project is in
- it facilitates agile working in sprints

### 3. Guides for Public Repositories ONLY

Make a clean, fresh repository! This will make sure no git history is opened to the public. Copy your code into this repository and update the **CONTRIBUTING.md** file. Your **README.md** might also need more information too. And check you are using the relevant **LICENSE.md** file too.

### 4. Contents

* **CODE_OF_CONDUCT.md**: a statement from the [Contributor
  Covenant](https://contributor-covenant.org) regarding what is and isn't
  acceptable behaviour for contributors
* **CONTRIBUTING.md**: guidelines for how contributions should be made to the work,
  this should be updated when the work is made public
* **README.md**: this document, every repository should have one and it acts as
  the main landing page for your repository
* **LICENSE**: the UK public sector usually operate under two different
  licensing schemes. The most common for code is the MIT license which is
  included in this repo. Alternatively there is an Open Government license and
  a description of what OpenGov enforces can be found
  [here](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).
* **.github**: this directory allows the user to specify templates for
  contribution types, included in this repository are a bug fix submission
  template, a feature request template and a pull request template. Each of them
  includes a series of tickboxes which you can use to help you decide whether or
  not the submission is suitable.
* **.gitignore**: this file allows you to specify which directories, files and
  globbed file types are to be ignored as part of the diffs being managed by
  git. This allows you to have your data in the same directory structure as your
  code without it needing to be pushed and pulled along with it. If you have
  data which you do need to manage I would highly advise the use of `git-annex`
  ahead of including data files in your repository (unless they are small).
