FROM python:3.9-slim
ENV APP_HOME /tweetapp
COPY . /streamlit_app
COPY requirements.txt /tweetapp/requirements.txt
WORKDIR $APP_HOME
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --bind 0.0.0.0:$PORT --workers=5 threads 10 --timeout 0 streamlit_app:streamlit_app 
