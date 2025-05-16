# ref. https://github.com/0msys/streamlit-template-devcontainer

FROM python:3.12-slim as base
# FROM python:3.12 as base
  # for 'gcc': No such file or directory
ARG USERNAME=pyuser
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN groupadd --gid $USER_GID $USERNAME \
  && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME
ENV PYTHONUSERBASE=/home/$USERNAME/.local
ENV PATH=$PYTHONUSERBASE/bin:$PATH
USER $USERNAME
WORKDIR /app
RUN pip install --user --upgrade pip setuptools

FROM base as dev
USER root
RUN apt-get update \
  && apt-get install -y sudo \
  && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
  && chmod 0440 /etc/sudoers.d/$USERNAME

FROM base
USER $USERNAME
RUN pip install fastapi ipywidgets jupyterlab marimo pygwalker streamlit
