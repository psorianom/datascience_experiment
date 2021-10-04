FROM continuumio/miniconda3

WORKDIR usr/src/datascience
ADD environment.yml environment.yml
RUN apt update
RUN apt install python3-pip
RUN conda env create -f environment.yml
ENV PATH /opt/conda/envs/datascience_experiment/bin:$PATH
RUN /bin/bash -c "source activate datascience_experiment"
COPY . .
RUN streamlit run ./src/app.py

