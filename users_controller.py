from db import get_connection

def get_all_users():
  users = []
  with get_connection().cursor() as cur:
    cur.execute("SELECT id, email FROM users")
    data = cur.fetchall()
    for dato in data:
      users.append({
        "id": dato[0],
        "email": dato[1]
      })
    return users

def get_user_by_id(id):
  with get_connection().cursor() as cur:
    cur.execute("SELECT id, email, password FROM users WHERE id = %s", (id,))
    data = cur.fetchone()
    user = {
      "id": data[0],
      "email": data[1],
      "password": data[2]
    }
    return user

def get_user_by_email(email):
  with get_connection().cursor() as cur:
    cur.execute("SELECT id, name, password, role, permissions FROM users WHERE email = %s", (email,))
    data = cur.fetchone()
    user = {
      "id": data[0],
      "name": data[1],
      "password": data[2],
      "role": data[3],
      "permissions": data[4]
    }
    return user

def define_permissions_by_role(role):
  rector_permissions = "schedule"
  secretary_permissions = rector_permissions + ",add,reports,statistics"
  admin_permissions = secretary_permissions + ",admin"
  if role == '2':
    return rector_permissions
  return secretary_permissions

def create_user(id, role, name, lastname, doctype, document, phone, email, password, permissions):
  hashed_password = 