Asynchronous Python API applications - Playground
=================================================

# Table of Content (ToC)
- [Asynchronous Python API applications - Playground](#asynchronous-python-api-applications-playground)
- [Table of Content (ToC)](#table-of-content-toc)
- [Overview](#overview)
- [Useage](#useage)
- [Installation](#installation)
  * [Python](#python)
  * [The Uvicorn playground application](#the-uvicorn-playground-application)

<small><i><a href='https://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

# Overview
[That project](https://github.com/cloud-helpers/uvicorn-playground) aims
at understanding, by practicing, how the asynchronous part of Python API
applications work.

To the best of our knowledge, the only asynchronous framework to power Python
applications is [Uvicorn](https://www.uvicorn.org/), which is also
the underlying framework used by [FastAPI](https://fastapi.tiangolo.com/),
itself a nice framework to operate Python-based API applications.

The starting point of this project is
[a discussion  on StackOverflow](https://stackoverflow.com/questions/67750367/fastapi-python-code-execution-speed-impacted-by-deployment-with-uvicorn-vs-gunic)
about the respective performances of asynchronous versus synchronous calls.

It is indeed not enough that FastAPI (and Uvicorn) are asynchronous frameworks,
the developers have to explicitly make their code asynchronous, by using
the `await` Python command (and specifying the API endpoint callback functions
with the `async` prefix). But not all Python payloads may be made
asynchronous-ready.

This project is an attempt to explore what asynchronous means for API
endpoints functions.

# Useage

* Launch the server
  + If Uvicorn and FastAPI are already installed in your `pip` environment:
```bash
$ uvicorn uvicorn-delay:app --port 8001 --reload
INFO:     Uvicorn running on http://127.0.0.1:8001 (Press CTRL+C to quit)
INFO:     Started reloader process [21835] using statreload
INFO:     Started server process [21870]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
  + With pipenv:
```bash
$ pipenv run uvicorn uvicorn-delay:app --port 8001 --reload
...
INFO:     Application startup complete.
```

* From another terminal window/tab, query the API with a client, for instance
  cURL:
```bash
$ curl localhost:8001/delay/0.0/0.0 && echo
```
```javascript
{"delays":[0.0,0.0],"total_time_taken_ms":5702,"times_avarage_ms":42.69,"times":[146,70,47,42,44,40,31,30,30,69,71,40,40,40,41,40,41,39,40,40,40,40,39,40,40,49,40,40,40,39,40,39,40,39,39,39,39,39,39,44,58,58,43,41,39,38,38,39,39,38,40,39,39,41,39,39,39,51,54,70,43,40,39,39,39,39,38,38,39,39,39,38,38,39,39,38,39,55,63,43,39,38,39,39,39,39,42,41,40,38,39,39,38,38,38,39,39,38,38,38]}
```

# Installation

## Python
* If not already done so, install PyEnv. For instance
  + Prepare the environment (here, with the Bash as default Shell):
```bash
$ git clone https://github.com/pyenv/pyenv.git $HOME/.pyenv
$ cat >> ~/.profile << _EOF

# Python
eval "$(pyenv init --path)"

_EOF
$ cat >> ~/.bashrc << _EOF

# Python
export PATH="\${HOME}/.pyenv/bin:\${PATH}"
. ~/.profile
if command -v pyenv 1>/dev/null 2>&1
then
        eval "\$(pyenv init -)"
fi
if command -v pipenv 1>/dev/null 2>&1
then
        eval "\$(pipenv --completion)"
#       echo
fi

_EOF
$ . ~/.bashrc
```
  + If PyEnv was already cloned a long time ago, think to update
    the repository from time to time:
```bash
$ pushd ~/.pyenv && git upll && popd
```
  + Install a specific version of Python (_e.g._, as of August 2021, 3.9.6
    is the latest stable version):
```bash
$ pyenv install 3.9.6 && pyenv global 3.9.6
```

* If not already done so, install `pip` and `pipenv`:
```bash
$ pip install -U pip
$ pip install -U pipenv
```

## The Uvicorn playground application
* Clone this repository and change directory to it:
```bash
$ mkdir -p ~/dev/showcase && \
  git clone https://github.com/cloud-helpers/uvicorn-playground.git ~/dev/showcase/uvicorn-playground
$ cd ~/dev/showcase/uvicorn-playground
```

* If not already done so, install a few Python required modules
  + Either with `pipenv` (so as to insulate that project from anything else):
```bash
$ pipenv install
```
  + Or with `pip` directly (which may mess with your Python installation):
```bash
$ pip install -r requirements.txt
```

