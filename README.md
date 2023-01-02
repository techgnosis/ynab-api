This repo has the shell and Python files I use to learn the YNAB (You Need A Budget) API. The repo relies on containerized Python environments powered by Colima. 



### .envrc
You will see `.envrc` in the `.gitignore` file. `.envrc` is a file used by a tool called `direnv` to automatically create environment variables when you enter a specific folder. It makes it effortless to maintain different environments by storing each environment's specific information in environment variables. The real `.envrc` is not checked in as it contains sensitive information, however the file looks like this:

```
export ACCESS_TOKEN=""
export BUDGET_ID=""

# this is referring to a money account, not a YNAB account
export ACCOUNT_ID=""

export CATEGORY_ID=""
```

### Why Colima?
Before containers, Python projects usually relied on Python virtual environments. This is because Python installs its dependencies into the Python runtime filesystem which makes it difficult to use the same Python install for different Python projects. Virtual environments allowed you to create many different Python installs, one for each project. In my opinion this functionality is not needed anymore since virtual environments is essentially what Docker gave us, but for all languages and runtimes instead of just Python.

Colima is a tool that replaces Docker Desktop for macOS since Docker Desktop is not free anymore for commercial use.