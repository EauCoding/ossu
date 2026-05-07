# prompts the user for the name of a file
user_input = input("File name: ")

# outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
# .gif, .jpg, .jpeg, .png, .pdf, .txt, .zip
user_input = user_input.strip().lower()
count_dot = user_input.count(".")

if count_dot == 2:
    file_name1, file_name2, file_extension = user_input.split(sep=".")
elif count_dot == 1:
    file_name, file_extension = user_input.split(sep=".")
else:
    file_extension = user_input

match file_extension:
    case "gif" | "jpg" | "jpeg" | "png":
        print("image/" + ("jpeg" if file_extension == "jpeg" or file_extension == "jpg" else file_extension))
    case "pdf" | "zip":
        print("application/" + file_extension)
    case "txt":
        print("text/plain")
# If the file’s name ends with some other suffix or has no suffix at all,
# output application/octet-stream instead, which is a common default.
    case _:
        print("application/octet-stream")
