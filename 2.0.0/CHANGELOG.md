# Changelog

Astronomer Certified 2.0.0-3.dev
-----------------------------------------

## Bugfixes

- Bugfix: Return XCom Value in the XCom Endpoint API ([commit](https://github.com/astronomer/airflow/commit/c2c9c06b3))
- BugFix: Dag-level Callback Requests were not run ([commit](https://github.com/astronomer/airflow/commit/4412aba55))
- Increase the default ``min_file_process_interval`` to decrease CPU Usage ([commit](https://github.com/astronomer/airflow/commit/6de02157f))
- Stop creating duplicate Dag File Processors ([commit](https://github.com/astronomer/airflow/commit/4ced807ab))

Astronomer Certified 2.0.0-2, 2020-12-23
-----------------------------------------

## Bugfixes

- Allow PID file path to be relative when daemonizing a process (scheduler, kerberos, etc) (#13232) ([commit](https://github.com/astronomer/airflow/commit/ebfb6f207))
- Dispose connections when running tasks with `os.fork` & CeleryExecutor ([commit](https://github.com/astronomer/airflow/commit/3a7d34c7a))
- Bump datatables.net from 1.10.21 to 1.10.23 in /airflow/www ([commit](https://github.com/astronomer/airflow/commit/a46642b6d))
- Stop sending Callback Requests if no callbacks are defined on DAG (#13163) ([commit](https://github.com/astronomer/airflow/commit/0c54f684c))
- Filter DagRuns with Task Instances in removed State while Scheduling (#13165) ([commit](https://github.com/astronomer/airflow/commit/426ce80cc))

Astronomer Certified 2.0.0-1, 2020-12-17
-----------------------------------------

User-facing CHANGELOG for AC 2.0.0+astro.1 from Airflow 2.0.0:

## Bugfixes

- Fix race conditions in task callback invocations ([commit](https://github.com/astronomer/airflow/commit/b179f544c))
