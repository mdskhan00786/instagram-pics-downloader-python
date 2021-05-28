import instaloader
ob = instaloader.Instaloader()
user = input("Enter username")
ob.download_profile(user,profile_pic=True)