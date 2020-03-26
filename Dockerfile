FROM python:3.7.4

WORKDIR /app

ADD ./requirements.txt /app/
RUN pip --trusted-host pypi.org --trusted-host files.pythonhosted.org --trusted-host  pypi.python.org install --upgrade pip
RUN python -m pip --trusted-host pypi.org --trusted-host files.pythonhosted.org install -r requirements.txt

ADD . /app

# RUN export FLASK_APP=app.py
# CMD ["python", "app.py"]
#CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
