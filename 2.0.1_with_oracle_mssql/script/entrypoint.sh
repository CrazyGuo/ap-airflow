#!/usr/bin/env bash

# User-provided configuration must always be respected.
#
# Therefore, this script must only derives Airflow AIRFLOW__ variables from other variables
# when the user did not provide their own configuration.

export ORACLE_HOME="/usr/local/airflow/oracle/instantclient"
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ORACLE_HOME

export OCI_HOME="/usr/local/airflow/oracle/instantclient"
export OCI_LIB_DIR="/usr/local/airflow/oracle/instantclient"
export OCI_INCLUDE_DIR="/usr/local/airflow/oracle/instantclient/sdk/include"

case "$1" in
  webserver)
    airflow db init
    exec airflow webserver
    ;;
  scheduler)
    exec airflow "$@"
    ;;
  worker)
    exec airflow celery "$@"
    ;;
  flower)
    sleep 10
    exec airflow celery "$@"
    ;;
  version)
    exec airflow "$@"
    ;;
  *)
    # The command is something like bash, not an airflow subcommand. Just run it in the right environment.
    exec "$@"
    ;;
esac
