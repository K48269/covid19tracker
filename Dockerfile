FROM python:latest
COPY . .
RUN pip install Flask
RUN pip install bs4
RUN pip install requests
EXPOSE 5001
ENTRYPOINT [ "python3" ,"app.py"]
