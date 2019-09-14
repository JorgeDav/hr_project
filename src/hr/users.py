import subprocess, pwd, grp, json, os, sys
from .get_sys import get_system_users, get_system_groups

def check_users(users):
    sys_users=get_system_users()
    sys_groups=get_system_groups()
    user_names=[user['name'] for user in users]
    groups=[(group['groups']) for group in users]

    for group in groups:
        if group not in sys_groups:
            add_group(group, sys_groups)

    for user in users:
        if user['name'] not in sys_users:
            add_user(user)
        elif user['name'] in sys_users:
            update_user(user)

    for user in sys_users:
        if user not in user_names:
            del_user(user)

def add_user(user_info):
    print(f"Adding user '{user_info['name']}'")
    try:
        subprocess.run([
            'useradd', user_info['name'],
            '-G', ",".join(user_info['groups']),
            '-p', user_info['password']],
            check=True)
    except subprocess.CalledProcessError as err:
        print(f"failed to add user {user_info['name']}")
        sys.exit(1)

def del_user(user):
    print(f"Deleting user '{user}'")
    try:
        subprocess.run([
            'userdel', user,
            "-r"],check=True)
    except subprocess.CalledProcessError as err:
        print(f"Failed to delete user '{user}'")
        sys.exit(1)

def update_user(user_info):
    print(f"Updating the properties of the user {user_info['name']}")
    try:
        subprocess.run([
            'usermod',user_info['name'],
            '-G',','.join(user_info['groups']),
            '-p', user_info['password']],
            check=True)
    except subprocess.CalledProcessError :
        print("Failed to update the user info")
        sys.exit(1)

def add_group(groups,sys_groups):
    try:
        for group in groups:
            if group not in sys_groups:
                subprocess.run([
                    'groupadd',group],
                    check=True)
    except subprocess.CalledProcessError :
        sys.exit(1)


