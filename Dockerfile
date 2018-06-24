FROM python:3.6.5-jessie

COPY . /home/ai-station
WORKDIR /home/ai-station

RUN apt-get update \
  && curl -sL https://deb.nodesource.com/setup_8.x | bash - \
  && cat docker-requirements/debian-requirements.txt | xargs apt-get install -y \
  && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip \
  && pip install -r docker-requirements/python-requirements.txt \
  && pip install .

RUN jupyter serverextension enable --sys-prefix jupyterlab_latex \
  && jupyter labextension install @jupyterlab/latex

RUN rm -rf /home/ai-station

WORKDIR /home

CMD ["/bin/bash"]
