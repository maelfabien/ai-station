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

The `ai-station` docker image contains:

- A minimal ubuntu OS with some productivity packages (git, make, tree, htop, etc...).
- Cuda and tensorflow dependencies for GPU computing.
- An enhanced shell based on zsh + oh-my-zsh, with a powerline theme and useful plugins.
- A python 3 environment with some productivity packages (pipreqs, pytest, autopep8, etc...).
- The great Jupyter Lab IDE, for data exploration and model prototyping.
- The ![latex](https://latex.codecogs.com/gif.latex?%24%7B%5Clatex%7D%7B%5CLaTeX%5Cxspace%7D%24) template used for NIPS research papers (directly editable in Jupyter Lab).
- The `ais` command line interface, a swiss knife for building your next machine learning project.

### 👩🏻‍💻‍ Installation

Requirements:

- [Docker CE](https://docs.docker.com/install/)

Get the docker image:

```bash
docker pull fmikaelian/ai-station
```

Start the container in the directory that will contain your development projects:

```bash
docker run -it \
  -v $(pwd):/home \
  -p 8888:8888 \
  -p 6006:6006 \
  -p 5000:5000 \
  -p 80:80 \
  --name ai-station \
  fmikaelian/ai-station
```

If you are willing to use `ai-station` with **GPU ⚡️**, please read my [medium blog post](https://medium.com/@fmikaelian/how-to-setup-a-custom-docker-gpu-development-environment-in-8-minutes-c7f0b41c02a6) for installation instructions.

### 🏃‍ Getting started

You can now generate a base template for your machine project ([see this example](station/template)) with the `ais` CLI:

```bash
ais init --name NAME --author AUTHOR
```

There are many other useful shortcuts for classic data science tasks:

| ⌨️ Command                              | ⚡️ Action                                                                                                  |
|:---------------------------------------|:----------------------------------------------------------------------------------------------------------|
| `ais init --name NAME --author AUTHOR` | Generate a base template for your machine project.                                                        |
| `ais install`                          | Install OS dependencies + your project as a python package.                                               |
| `ais pipeline --step`                  | Execute one of your machine learning steps located in `/project/pipeline` (eg. `--train` or `--predict`). |
| `ais tests`                            | Performs unit-tests, pep8 checks and coverage reports for your tests located in `/tests`.                 |
| `ais flask --config`                   | Start a flask server to serve your demo web app with defined server config (eg. `--dev` or `--prod`).     |
| `ais lab`                              | Start jupyter lab.                                                                                        |
| `ais tb`                               | Start a tensorboard server to display your logs located in `/logs`.                                       |

To generate a list of all available commands, type `ais --help`. To see individual commands options, type `ais [COMMAND] --help`.

If you exited the container and want to restart it:

```bash
docker start ai-station && docker exec -it ai-station bash
```

### 🐜 Contributions

Contributions are welcomed! Be sure to review the contributing guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

### 📃 License

Copyright (c) 2018 fmikaelian. Licensed under the [MIT License](LICENSE)

### 💸 Donations

Support my indie work by sending me magic money:

|                                   currency                                    | address                                    |
|:-----------------------------------------------------------------------------:|--------------------------------------------|
| <a ><img src="https://cdn.coinranking.com/rk4RKHOuW/eth.svg" width="30" ></a> | 0x2B2c793230D5433D00c2d1D1e7c4b1C647e74908 |
