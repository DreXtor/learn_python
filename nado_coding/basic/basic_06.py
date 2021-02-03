# # 파일 입출력

# score_file = open("score.txt", "w", encoding="utf8")      # w : 쓰기 모드
# print("수학 = 0", file=score_file)
# print("영어 = 50", file=score_file)
# score_file.close()

# # 덧붙여서 쓰기
# score_file = open("score.txt", "a", encoding="utf8")        # a : append
# score_file.write("과학 : 80")
# score_file.write("\n영어 : 90")
# score_file.close()

# # 파일 읽기
# # 전부 읽기
# score_file = open("score.txt", "r", encoding="utf8")        # a : append
# print(score_file.read())
# score_file.close()

# # 줄별로 읽기
# score_file = open("score.txt", "r", encoding="utf8")        # a : append
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# # 몇줄인지 모를때 있는만큼 읽기
# # 반복 방법 1
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)
# score_file.close()

# # 반복 방법 2
# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines()
# for line in lines:
#     print(line)
# score_file.close()

#####################################################################
# # pickle
# from os import close
# import pickle
# profile_file = open("profile.pickle", "wb")     # wb : write binariy
# profile = {"이름": "박명수", "나이": 30, "취미": ["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)  # profile에 있는 정보를 file에 저장
# profile_file.close()

# # 데이터 읽어오기
# profile_file = open("profile.pickle", "rb")     # wb : write binariy
# profile = pickle.load(profile_file)  # file 에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

#####################################################################
# with

import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf=8") as study_file:
    study_file.write("나는 파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf=8") as study_file:
    print(study_file.read())
