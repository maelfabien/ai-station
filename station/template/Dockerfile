FROM fmikaelian/ai-station

COPY . /home/{{ project_name }}
WORKDIR /home/{{ project_name }}

RUN ais install

CMD ais flask --prod
