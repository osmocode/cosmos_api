FROM python:3.9

# Set work directories
WORKDIR /api

# Install dependencies
ADD requirements.txt /api/requirements.txt
RUN python3 -m pip install --upgrade pip
RUN pip3 install wheel
RUN pip3 install -r requirements.txt

# Copy Django project sources files
ADD apps/ /api/apps/
ADD cosmos/ /api/cosmos/
ADD manage.py /api/manage.py
