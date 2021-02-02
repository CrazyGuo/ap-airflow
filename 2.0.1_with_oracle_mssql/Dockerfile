#Airflow IMAGE
FROM astronomerinc/ap-airflow:2.0.0-1-buster
MAINTAINER Matthew Guo <guohuanhuan_cool@126.com>

ENV AIRFLOW_USER_HOME=/usr/local/airflow

#Configure oracle
ENV ORACLE_HOME=${AIRFLOW_USER_HOME}/oracle/instantclient
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ORACLE_HOME
ENV OCI_HOME=${AIRFLOW_USER_HOME}/oracle/instantclient
ENV OCI_LIB_DIR=${AIRFLOW_USER_HOME}/oracle/instantclient
ENV OCI_INCLUDE_DIR=${AIRFLOW_USER_HOME}/oracle/instantclient/sdk/include

USER root
# INSTALL TOOLS For Oracle
RUN apt-get update \
    && mkdir -p ${AIRFLOW_USER_HOME}/oracle \
    && apt-get -y install libaio-dev \
    && pip install -U pip setuptools wheel \
    && pip install 'cx_Oracle==8.1.0' \
    && pip install 'pymssql==2.1.5' \
    && apt-get clean

RUN chown -R astro: /usr/local/airflow

# Set Oracle Client
COPY instantclient ${AIRFLOW_USER_HOME}/oracle/instantclient
COPY script/entrypoint.sh ${AIRFLOW_USER_HOME}/entrypoint.sh
COPY config/airflow.cfg ${AIRFLOW_USER_HOME}/airflow.cfg
COPY oracle_task.py ${AIRFLOW_USER_HOME}/
COPY mssql_task.py ${AIRFLOW_USER_HOME}/

EXPOSE 8080 5555 8793

USER astro
WORKDIR ${AIRFLOW_USER_HOME}
ENTRYPOINT ["/usr/local/airflow/entrypoint.sh"]