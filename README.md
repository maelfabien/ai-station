<p align="center">
  <img alt="logo" src="docs/img/logo.png" height="160" />
  <h3 align="center">ai-station</h3>
    <p align="center">A minimalist development environment for machine learning hackers.</p>
    <p align="center">
    <img src="https://travis-ci.org/fmikaelian/ai-station.svg?branch=master" height="18">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" height="18">
  </p>
</p>

---

### 💡 The concept

Data scientists waste too much time setting up their development environment and adapting their code to the machine learning workflow. `ai-station` allow them focus on what they are good at (eg. data exploration, model building and evaluation) by making it easier and faster to build prototypes and deploy them in production.

### 🔮 What's inside?

The `ai-station` Docker image contains:

- A minimal debian OS with some productivity packages (git, make, tree, htop, etc...).
- A ready-to-use python 3.6 environment.
- The great Jupyter Lab IDE, for data exploration and model prototyping.
- The ![latex](https://latex.codecogs.com/gif.latex?%24%7B%5Clatex%7D%7B%5CLaTeX%5Cxspace%7D%24) template used for NIPS research papers (directly editable in Jupyter Lab).
- The `ais` command line interface, a swiss knife for building your next machine learning project.

### 🏃‍ Getting started

Installation requirements:

- [Docker CE](https://docs.docker.com/install/)

To install:

```bash
docker pull fmikaelian/ai-station
docker run -it -p 8888:8888 -p 6006:6006 -p 5000:5000 ai-station
```

You can generate a machine learning project structure with the `ais` command:

```bash
ais init --name NAME --author AUTHOR
```

There are many other useful shortcuts for classic data science tasks:

| ⌨️ Command                              | ⚡️ Action                                                      |
|:---------------------------------------|:--------------------------------------------------------------|
| `ais init --name NAME --author AUTHOR` | Generate a template for an machine project                    |
| `ais install`                          | Install OS and python dependencies for your project           |
| `ais pipeline [--step]`                | Execute your project steps under `/project/pipeline`          |
| `ais tests`                            | Manage your tests under `/tests`                              |
| `ais lab`                              | Start jupyter lab                                             |
| `ais flask`                            | Start a flask server to serve your AI web app                 |
| `ais tb`                               | Start a tensorboard server with your project under in `/logs` |

To generate a list of all available commands, type `ais --help`. To see individual commands options, type `ais [COMMAND] --help`.

### 🐜 Contributions

Contributions and feedback are welcomed!

### 📃 License

Copyright (c) 2018 fmikaelian. Licensed under the [MIT License](LICENSE)

### 💸 Donations

Support my indie work by sending me magic money:

|                                   currency                                    | address                                    |
|:-----------------------------------------------------------------------------:|--------------------------------------------|
| <a ><img src="https://cdn.coinranking.com/rk4RKHOuW/eth.svg" width="30" ></a> | 0x2B2c793230D5433D00c2d1D1e7c4b1C647e74908 |
