# Quiz) 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙 1 : http:// 부분은 제외 => naver.com
# 규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성

# 예 ) 생성된 비밀번호 :nav51!

def my_code():
    URL = "http://naver.com"                            # URL
    rule_2 = URL.find(".")                              # "."의 위치값

    URL_name = (URL[7:rule_2])                          # 도메인 이름 출력

    pw_01 = URL_name[:3]                                # 앞에 3자리
    pw_02 = len(URL_name)                               # 문자열의 길이
    pw_03 = URL_name.count("e")                         # "e"의 갯수

    print(f"{pw_01}{pw_02}{pw_03}!")      # 출력

# 샘 코드처럼 password 라는 변수를 만들어 한번에 return 해주는것이 깔끔한듯
# replace와 format의 활용이 부족했던것 같다


def sam_code():
    url = "http://naver.com"
    my_str = url.replace("http://", "")                # 규칙 1
    # 규칙 2 : my_str[0:5] -> (0,1,2,3,4)
    my_str = my_str[:my_str.index(".")]
    password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
    print("{0}의 비밀번호는 {1} 입니다.".format(url, password))


my_code()
sam_code()
