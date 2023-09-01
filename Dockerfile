FROM python:3.11

# Install dependencies
COPY requirements.txt /app/requirements.txt
COPY setup.py /app/setup.py
COPY pgstuff /app/pgstuff
COPY tests /app/tests

WORKDIR /app

# Install requirements
RUN pip install -r requirements.txt

# Install pgstuff local module
RUN pip install -e .

# Copy ansible playbooks
COPY inventory /app/inventory

# Run tests
RUN pytest

