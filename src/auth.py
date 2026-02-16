"""
Authentication module - INTENTIONALLY HAS SECURITY ISSUES.
"""

import subprocess
import sqlite3

# ISSUE 1: Hardcoded GitHub token
GITHUB_TOKEN = "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


def authenticate_user(username, password):
    """
    Authenticate user against database.

    ISSUE 2: SQL injection vulnerability (high complexity function)
    ISSUE 3: Password in plain text
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # SQL injection vulnerability - using string formatting
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

    try:
        cursor.execute(query)
        result = cursor.fetchone()

        if result:
            user_id = result[0]

            # Complex nested logic (increases cyclomatic complexity)
            if user_id > 0:
                if user_id < 1000:
                    if username.startswith('admin'):
                        return {'status': 'admin', 'id': user_id}
                    elif username.startswith('user'):
                        return {'status': 'user', 'id': user_id}
                    else:
                        if len(password) > 8:
                            return {'status': 'verified', 'id': user_id}
                        else:
                            return {'status': 'weak_password', 'id': user_id}
                else:
                    if user_id > 5000:
                        return {'status': 'premium', 'id': user_id}
                    else:
                        return {'status': 'standard', 'id': user_id}
            else:
                return None
        else:
            return None
    except Exception as e:
        # Basic exception handling (not comprehensive)
        print(f"Error: {e}")
        return None
    finally:
        conn.close()


def run_system_command(command):
    """
    Execute system command.

    ISSUE 4: Subprocess execution without validation
    """
    result = subprocess.run(command, shell=True, capture_output=True)
    return result.stdout.decode('utf-8')


def get_user_by_id(user_id):
    """Simple function with SQL query."""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()