import json
import grp
import pwd
import spwd

from .get_sys import get_system_users

def load(path):
    with open(path, 'r') as f:
        return json.load(f)

def dump(path, sys_users=get_system_users()):
    users=[]
    for user in sys_users:
        password=spwd.getspnam(user).sp_pwdp
        group=_group_names(user)
        users.append({
            'name': user,
            'groups': group,
            'password': password,
            })
    with open(path,'w') as f:
        json.dump(users,f)

def _group_names(user):
    return [group.gr_name for group in grp.getgrall() if user in group.gr_mem]
