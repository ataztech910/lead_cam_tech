FROM python:3



COPY . .

RUN mkdir -p /usr/src/app/any-dashboard-app
COPY any-dashboard-app /usr/src/app/any-dashboard-app
RUN pip install --upgrade pip
RUN pip install -r /usr/src/app/any-dashboard-app/requirements.txt --cache-dir /usr/src/app/pip_cache
EXPOSE 8000

RUN chmod +x /usr/src/app/any-dashboard-app/start.sh
# ENTRYPOINT ["/usr/src/app/any-dashboard-app/start.sh"]
WORKDIR /usr/src/app/any-dashboard-app/
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]