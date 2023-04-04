from __future__ import division, absolute_import, print_function
from airflow.plugins_manager import AirflowPlugin

import operators
import hooks


class MyPlugins(AirflowPlugin):
    name = "my_plugin"

    operators = [operators.MyOwnOperator]
    hooks = [hooks.MyOwnHook]
