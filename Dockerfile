FROM python:3.9
ENV APP_HOME /tweetapp
COPY . /streamlit_app
WORKDIR /streamlit_app
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --bind 0.0.0.0:$PORT --workers=5 threads 10 --timeout 0 streamlit_app:streamlit_app 
