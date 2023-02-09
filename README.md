# Shell GPT

Shell GPT is an OpenAI ChatGPT shell interface that provides an interactive experience to the user from the command line.

## Features

* Command line prompt
* Session context
* Token counter
* Load prepared prompt from file during session
* Saves session to log file

## Installation

1. Clone the repository: `git clone <url>`
2. Change directory: `cd <dir>`
3. Install requirements: `pip install -r requirements`
4. Add you OpenAI api key to `.bashrc`:
    ```
    export OPENAI_API_KEY=<your-api-key-here>
    ```
5. Create a bash function in `.bashrc`
    ```
    <alias>() {
        python3 <dir>/src/main.py $*
    }
    ```
6. Reload `.bashrc`
    ```
    source ~/.bashrc
    ```

## Usage

### Direct prompt from cmd line

To get a response from Shell GPT, use the alias you created in the `.bashrc` file and type your query. For example:

`<alias> Please be informed that today is Wednesday, weather is cold and sunny and I'm about to finish development of Shell GPT. Please generate me a haiku of the day.`


### Load prompt from file

You can also load a prompt from a file:

`<alias> file <filepath>`

To end the session, type `thx`, `bye`, `quit` or `exit`. 

**Enjoy the interactive experience of Shell GPT and never leave your console again ! :)**


## Examples

```
dusan:shell-gpt$ <alias> Please be informed that today is Wednesday, weather is cold and sunny and I'm about to finish development of Shell GPT. Please generate me a haiku of the day.
> '
 -- logging to: chat-sessions/beinformedthattodayisWednesday.log

2023-02-09 13:26:00.821708 Prompt:
 Please be informed that today is Wednesday, weather is cold and sunny and Im about to finish development of Shell GPT. Please generate me a haiku of the day.


2023-02-09 13:26:08.923322 Answer:

The sun is cold and bright
A chill in the winter air
A new shell is born

 [0]:
```

```
dusan:shell-gpt$ <alias> file generate-cat-haiku.prompt
 -- logging to: chat-sessions/nerate-cat-haiku.prompt.log

2023-02-09 13:34:11.447691 Prompt:
 Please genrate haiku about black cat on a cold winter day



2023-02-09 13:34:15.987140 Answer:
 The server had an error while processing your request. Sorry about that!

 [0]: !ls
README.md
chat-sessions
generate-cat-haiku.prompt
generate-readme.prompt
requirements.txt
src

 [0]: file generate-cat-haiku.prompt

2023-02-09 13:34:38.209456 Prompt:
 Please genrate haiku about black cat on a cold winter day



2023-02-09 13:34:43.731249 Answer:

2023-02-09 13:34:41.377769 Answer:
Black cat on snow-covered ground
Cozy and content in its fur
A winter's peace found.

 [0]:
```

```
dusan:shell-gpt$ <alias> please generate git ignore file with the default python files, please also include 'chat-sessions' folde
 -- logging to: chat-sessions/generategitignorefilewiththede.log

2023-02-09 13:50:20.291205 Prompt:
 please generate git ignore file with the default python files, please also include chat-sessions folde


2023-02-09 13:51:17.703056 Answer:

# Created by https://www.gitignore.io/api/python

### Python ###
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# PEP 582; used by e.g. github.com/David-OConnor/pyflow
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# Chat-sessions folder
chat-sessions/

 [0]: what should be the name of the file ?

2023-02-09 13:51:30.679974 Prompt:
 what should be the name of the file ?


2023-02-09 13:51:39.060333 Answer:

2023-02-09 13:52:07.711390 Answer:
The file should be named ".gitignore".

 [0]:
```