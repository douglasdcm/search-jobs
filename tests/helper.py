from subprocess import PIPE, STDOUT, run


def exec_command(params, entry_point):
    try:
        cmd = ["python", entry_point]
        cmd.extend(params)
        return run(cmd,
                   stdout=PIPE,
                   stderr=STDOUT,
                   encoding="utf-8").stdout.strip()
    except Exception:
        raise
