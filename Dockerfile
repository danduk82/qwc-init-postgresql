FROM python:3.11

# Install dependencies

COPY requirements.txt /app/requirements.txt
COPY pgstuff /app/pgstuff
COPY tests /app/tests

WORKDIR /app

# install requirements
RUN pip install -r requirements.txt

# Install pgstuff local module
RUN pip install -e pgstuff

# Run tests
RUN python -m unittest discover -s tests


