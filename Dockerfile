FROM python:3.9
# set work directory
WORKDIR /usr/src/app/
# copy project
COPY . /usr/src/app/
# install dependencies
RUN pip install -r /usr/src/app/requirements.txt
# run app
CMD ["python", "app.py"]
