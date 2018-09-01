FROM python:3.6.5-jessie

COPY . /home/ai-station
WORKDIR /home/ai-station

RUN apt-get update \
  && curl -sL https://deb.nodesource.com/setup_8.x | bash - \
  && cat docker-requirements/requirements-os.txt | xargs apt-get install -y \
  && curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh \
  && curl -L git.io/antigen > ~/antigen.zsh \
  && cat docker-requirements/requirements-shell.txt > ~/.zshrc \
  && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip \
  && pip install -r docker-requirements/requirements-python.txt \
  && pip install .

RUN jupyter serverextension enable --sys-prefix jupyterlab_latex \
  && jupyter labextension install @jupyterlab/latex

ENV LC_ALL=C.UTF-8 LANG=C.UTF-8

WORKDIR /home

RUN rm -rf /home/ai-station

CMD ["zsh"]
