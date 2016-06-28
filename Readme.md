# Python template project

This project shows how to set up a python module, and should be used as starting point for most python projects developed in the IAL group.

# IAL Python Development Guidelines

Even though most projects start off as a bunch of experimental scripts, as soon as one notices there are pieces of code that could be reused across different scripts, it makes sense to write a python module. Here are some guidelines that help you to write readable and reusable code, which facilitates collaboration.

## Legend: 

* Guidelines written in normal font should be mandatory for all projects
* _Italics_ for the high quality ones (e.g. those that should be used from ilastik)

## Guidelines:

2. Put your module under GIT version control [https://www.atlassian.com/git/tutorials/](https://www.atlassian.com/git/tutorials/) and make it available via http://github.com
    * Commit early and commit often: use small atomic commits.
    * How to write git commit messages: basically complete the sentence "When I apply this commit, I ... to ...". [http://chris.beams.io/posts/git-commit/](http://chris.beams.io/posts/git-commit/)
    * For projects with more developers (and/or users), use the github issue system, and refer to issues in your commit messages (“fixes #42”). You can also use these issues as your roadmap of things to be done.
    * Workflow aka branching model: [https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow)
     In a nutshell: Have one master branch, develop features in short-lived feature-branches, create a pull request to merge them back into master once finished (using `git merge --no-ff` is one [option](http://stackoverflow.com/questions/18126297/when-to-use-the-no-ff-merge-option-in-git)), delete the feature branch after it is merged. Releases are tagged commits in your master branch.
3. Write tests (we mostly use nosetests):
    * Put them in a “tests” subfolder
    * Run the tests before every commit!
    * _For testing, import the module locally without the need to run setup.py beforehand [(http://docs.python-guide.org/en/latest/writing/* structure/#test-suite)](http://docs.python-guide.org/en/latest/writing/* structure/#test-suite)_
    * _Set up continuous integration (e.g. travis, circle CI) which runs your tests every time you push to github_
4. Write readable Python code:
    * Write class and method docstrings [(https://www.python.org/dev/peps/pep-0257/)](https://www.python.org/dev/peps/pep-0257/)
    * Reduce the warnings given from linting tools (e.g. in Pycharm, SublimeLinter-pylint or simply pylint on the command line)
    * Use Python’s logging module: [http://victorlin.me/posts/2012/08/26/good-logging-practice-in-python](http://victorlin.me/posts/2012/08/26/good-logging-practice-in-python)
    * General Python variable naming style: 
     * Classes uppercase and in `CamelCase`
     * Variable and method names all `lowercase_with_underscores`
     * Protected members start with an `_underscore`.
     * Files (especially those in modules) start lowercase, then all lowercase or camelCase, without spaces, dashes, underscores, whatsoever (otherwise the import statement looks ugly, it even forbids most special characters).
1. _Module Structure:_
    * _See [http://docs.python-guide.org/en/latest/writing/structure/](http://docs.python-guide.org/en/latest/writing/structure/)_
    * _Every folder that contains an `__init__.py` can be imported by Python_
    * _Write a `setup.py` installation script which allows others to simply use your module everywhere. ([https://docs.python.org/2/distutils/setupscript.html](https://docs.python.org/2/distutils/setupscript.html))_
