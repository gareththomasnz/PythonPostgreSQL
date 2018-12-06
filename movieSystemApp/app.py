from movieSystemApp.user import User



# user.add_movie("The Matrix", "Sci-Fi")
# user.add_movie("2001 A Space Odessey", "Sci-Fi")

user = User.load_from_file('Simon.txt')

# user.save_to_file()

print(user.name)
print(user.movies)