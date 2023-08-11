url = input().strip()
username_pos = url.find("username")
pwd_pos = url.find("pwd")
profile_pos = url.find("profile")
role_pos = url.find("role")
key_pos = url.find("key")
username = url[username_pos + 9 : pwd_pos - 1]
pwd = url[pwd_pos + 4 : profile_pos - 1]
profile = url[profile_pos + 8 : role_pos - 1]
role = url[role_pos + 5 : key_pos - 1]
key = url[key_pos + 4 :]
print("username:", username)
print("pwd:", pwd)
print("profile:", profile)
print("role:", role)
print("key:", key)
