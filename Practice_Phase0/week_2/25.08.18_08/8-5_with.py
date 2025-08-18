# import pickle
#
# with open("profile.pickle", "rb") as profile_file:
#      print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf-8" ) as study_file:
#     study_file.write("파이썬의 본질을 이해하고 싶어요.")

with open("study.txt", "r", encoding="utf-8") as study_file:
    print(study_file.read())
