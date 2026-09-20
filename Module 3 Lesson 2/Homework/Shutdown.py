def shutdown(argument):
  if argument == "Yes" or argument == "yes":
    print("shutting down")
  elif argument == "no" or argument == "No":
    print("abort shut down")
  else:
    print("sorry.")

shutdown("No")