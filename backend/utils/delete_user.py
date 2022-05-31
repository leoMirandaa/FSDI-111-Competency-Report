import requests
from pprint import pprint

URL= "http://127.0.0.1:5000/users"

def get_user(pk):
  url = "%s/%s" % (URL,  pk) # http://127.0.0.1:5000/users/1
  response = requests.get(url)
  if response.status_code == 200:
    pprint(response.json())
  else:
    print("something went wrong retrievibg the target user.")


def delete_user(pk):
    url = "%s/%s" % (URL,  pk) # http://127.0.0.1:5000/users/1
    response = requests.delete(url)
    if response.status_code == 204:
      print("User successfully deleted.")
    else:
      print("Something went wrong while trying to delete the target user.")

if __name__ == "__main__":
  print("DELETE A USER")
  print("-" * 50)
  user_id = input("Type in the target user's ID: ")
  print("Delete the user shown belows?")
  get_user(user_id)
  # print ("result.. ",get_user(user_id))

  option = input("[Y/n]: ")
  if option == "Y" or option == "y":
    delete_user(user_id)
  else:
    print("User not deleted")