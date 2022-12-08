FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /ProjectMicroservice
COPY requirements.txt /ProjectMicroservice/requirements.txt
RUN pip install -r requirements.txt
COPY . /ProjectMicroservice
#this above statement copy all the localfile from here into projectMicrosercive directory

CMD python manage.py runserver 0.0.0.0:8000
#this command connect to the localhost at port 8000