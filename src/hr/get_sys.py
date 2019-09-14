import pwd, grp, os

def get_system_users():
    sys_users=[user.pw_name for user in pwd.getpwall() if user.pw_uid>1000 and (
        user.pw_name != 'cloud_user' and user.pw_name != 'centos' and user.pw_name != 'user')]
    return sys_users

def get_system_groups():
    sys_groups=[group.gr_name for group in grp.getgrall()]
    return sys_groups

