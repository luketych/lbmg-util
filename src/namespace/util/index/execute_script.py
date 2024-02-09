import os
import subprocess
import sys

from namespace.mylogging import createLogger

from namespace.util import getProjectRootDir


file_name = os.path.join( getProjectRootDir(), "logs", os.path.basename(__file__).replace(".py", ".log") )
logger = createLogger(__file__, filename=file_name, level=10)


def execute_script(*args, timeout=60):
    # All arguments are stored in ARGS as a list
    ARGS = list(args)

    script_name = filename = os.path.basename(ARGS[2])

    # Execute the command with check=True
    try:
        print("Python version:", sys.version)
        print("Python executable:", sys.executable)
      
        logger.info("\033[96m" + f"Executing script {script_name} using task_wrapper.py" + "\033[0m")
        
        args = [sys.executable]
        args.extend(ARGS[1:])
        
        result = subprocess.run(args, check=True, timeout=timeout)
        
        if result.returncode != 0:
            logger.info("\033[91m" + f"Script '{script_name}' execution failed" + "\033[0m")
            logger.info(result)
            raise subprocess.CalledProcessError(returncode=result.returncode, cmd=result.args)
        
        script_name = ARGS[-1]
        
        # log the tail of the script_name
        logger.info(f"Script //{'/'.join( script_name.split('/')[-3:] )} executed successfully.")
        
        # print(result)
        
        
        return result
    except subprocess.TimeoutExpired as e:
        logger.error("\033[91m" + f"Script '{script_name}' execution timed out" + "\033[0m")
        # You can handle the timeout error here as needed
        raise
    except subprocess.CalledProcessError as e:
        logger.error("\033[91m" + f"Script '{script_name}' execution failed" + "\033[0m")
        logger.error("Error:", e)  # Print the error message from the exception

        raise e  # Re-raise thel exception to stop the script

    except Exception as e:
        logger.error("\033[91m" + f"Script '{script_name}' execution failed" + "\033[0m")
        logger.error("Unexpected error:", sys.exc_info()[0])
        raise