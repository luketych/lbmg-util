import os

from namespace.mylogging import createLogger
from namespace.util import getProjectRootDir, getPyprojectRootDir

from .execute_script import execute_script

file_name = os.path.join( getProjectRootDir(), "logs", os.path.basename(__file__).replace(".py", ".log") )
logger = createLogger(__file__, filename=file_name, level=10)


PROJECT_ROOT_DIR = getProjectRootDir()
THIS_DIR = os.path.dirname(os.path.realpath(__file__))
TASK_WRAPPER_DIR = os.path.join(PROJECT_ROOT_DIR, "src", "task_wrappers")


def execute_scripts(scripts_to_execute):
    try:
        for script_path in scripts_to_execute:
            _, extension = os.path.splitext(script_path)
            if extension == ".py":
                execute_script("python", os.path.join(TASK_WRAPPER_DIR, "task_wrapper.py"), script_path)
            elif extension == ".sh":
                execute_script("sh", os.path.join(TASK_WRAPPER_DIR, "task-wrapper.sh"), script_path)
            else:
                logger.info(f"Skipping execution of unsupported script: {script_path}")
    except Exception as e:
        logger.error(f"Script execution stopped due to exception: {e}")