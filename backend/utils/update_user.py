import requests

URL= "http://127.0.0.1:5000/users"
USER_TEMPLATE = {
  "first_name": "John",
  "last_name": "Cena",
  "hobbies":"Play basketball"
}

def get_user(pk):
  url = "%s/%s" % (URL,  pk) # http://127.0.0.1:5000/users/1
  response = requests.get(url)
  my_response = response.json()
  return my_response


def update_user(pk, first_name, last_name, hobbies):
  url = "%s/%s" % (URL,  pk) # http://127.0.0.1:5000/users/1
  print("update URL: ",url)
  user_data = USER_TEMPLATE
  user_data["first_name"] = first_name
  user_data["last_name"] = last_name
  user_data["hobbies"] = hobbies

  print('data to send: ',user_data)

  response = requests.put(url, json=user_data)# http://127.0.0.1:5000/users/#id
  print("response.status... ", response.status_code)
  if response.status_code == 204:
    print("User successfully updated")
  else:
    print("Something went wrong while trying to update a user")


if __name__ == "__main__":
  target_id = input("Type in the user's ID: ")
  user = get_user(target_id)
  print('user to update:',user["user"])

  print("---------------")
  print("UPDATE DATA")
  print("---------------")
  fname  = input("First name: ")
  lname = input("last name: ")
  hobbies= input("Hobbies: ")
  print("---------------")
  update_user(target_id, fname, lname, hobbies)

