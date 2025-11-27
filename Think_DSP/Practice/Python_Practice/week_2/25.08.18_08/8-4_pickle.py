import pickle
# profile_file = open("profile.pickle", "wb")
# profile ={"이름" : "Kim", "나이" : "26", "취미":["축구, 음악, 당구"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()

profile_file =open('profile.pickle', 'rb')
profile = pickle.load(profile_file) # file에 잇는 정보 profile에 불러오기
print(profile)
profile_file.close()

