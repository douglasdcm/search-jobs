from subprocess import PIPE, STDOUT, run
from sqlalchemy import text
from src.helper.helper import data_pre_processing_portuguese, Connection


def populate_database_with_desired_jobs(positions):
    try:
        with Connection.get_database_connection().connect() as connection:
            for position in positions:
                descrition_processed = data_pre_processing_portuguese(position["description"])
                connection.execute(
                    text(
                        f"insert into positions (url, description) values ('{position['url']}'"
                        f", '{descrition_processed}')"
                    )
                )
                connection.commit()
    except Exception:
        raise

def exec_command(params, command, domain="python", sudo=False):
    try:
        cmd = []
        if sudo is True:
            cmd.extend(["sudo"])
        cmd.extend([domain, command])
        if isinstance(params, str):
            params = [params]
        cmd.extend(params)
        result = run(cmd, stdout=PIPE, stderr=STDOUT, encoding="utf-8")
        result.check_returncode()
        return result.stdout.strip()
    except Exception:
        raise


def populate_database_with_thecnical_jobs():
    description1 = "jira manager senior dashboards carrer"
    description2 = "jira developer python java postgres sql"
    description3 = "jira tester qa pytest postman jmeter"
    description4 = "ux figma design xd"
    positions = [
        {"url": "www.position1.com", "description": description1},
        {"url": "www.position2.com", "description": description2},
        {"url": "www.position3.com", "description": description3},
        {
            "url": (
                "www.very_loooooooooooooooooooooooooooooooooooooooooooo"
                "ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong_url.com"
            ),
            "description": description4,
        },
    ]
    populate_database_with_desired_jobs(positions)
