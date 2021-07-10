FROM python:3.9-slim-buster

ENV LANG=C.UTF-8 \
  LC_ALL=C.UTF-8 \
  PATH="${PATH}:/root/.poetry/bin"

RUN apt-get update && \
  apt-get install -y --no-install-recommends \
    curl \
    git \
    make \
    graphviz \
  && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml ./

# Allow installing dev dependencies to run tests
ARG INSTALL_DEV=true
RUN if [ "${INSTALL_DEV}x" = "truex" ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi

ENV PATH "/opt/poetry/venv/bin:${PATH}"
ENV VIRTUAL_ENV "/opt/poetry/venv"
RUN echo "export PATH=/opt/poetry/venv/bin:${PATH}" >> ~/.profile && \
    echo "export VIRTUAL_ENV=/opt/poetry/venv" >> ~/.profile

CMD mkdir -p /usr/src/pacu
WORKDIR /usr/src/pacu

COPY . .
CMD ["python", "-m", "pacu"]
