def validate_entry(data):
  if(data["first_name"].isdigit() or not data["first_name"]):
    print("**first name should not be digit")
    return False

  if(data["last_name"].isdigit() or data["last_name"] == ''):
    print("**last name should not be digit")
    return False

  if(data["hobbies"].isdigit() or not data["hobbies"]):
    print("**hobbies should not be digit")
    return False

  return True

