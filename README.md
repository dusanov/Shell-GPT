# Shell GPT

Shell GPT is an OpenAI ChatGPT shell interface that provides an interactive experience to the user from the command line.

## Features

* Command line prompt
* Session (reset) context
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

2023-02-09 13:26:08.923322 Answer:

The sun is cold and bright
A chill in the winter air
A new shell is born

 [0]:
```

```
dusan:shell-gpt$ <alias> file generate-cat-haiku.prompt
 
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

2023-02-09 13:34:41.377769 Answer:
Black cat on snow-covered ground
Cozy and content in its fur
A winter's peace found.

 [0]:
```

```
dusan:shell-gpt$ <alias> please generate git ignore file with the default python files, please also include 'chat-sessions' folder
 
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

...

# Chat-sessions folder
chat-sessions/

 [0]: what should be the name of the file ?

2023-02-09 13:51:30.679974 Prompt:
 what should be the name of the file ?

2023-02-09 13:52:07.711390 Answer:
The file should be named ".gitignore".

 [0]:
```