FROM python:3.8
USER root
RUN mkdir /app
COPY . /app/
WORKDIR /app/
RUN apt update -y && apt install awscli -y
RUN pip3 install -r requirements.txt
ENV AIRFLOW_HOME="/app/airflow"
ENV AIRFLOW__CORE__DAGBAG_IMPORT_TIMEOUT=1000
ENV AIRFLOW__CORE__ENABLE_XCOM_PICKLING=True
RUN airflow db init
RUN airflow users create  -e digvijay.taunk@gmail.com -f Digvijay -l Taunk -u admin -p admin -r Admin
RUN chmod 777 start.sh
ENTRYPOINT [ "/bin/sh" ]
CMD ["start.sh"]