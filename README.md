# python

python 공부 기록합니다

## 2021.01.17

### web_scrapper

`stackoverflow`사이트의 `job list scrapper`를 만들었습니다.

지난번 배웠던 `indeed job scrapper`를 많이 참고하였습니다.

data soup의 범위를 타이트하게 잡아서 `job_link`를 좀더 간결하게 가져오지못해 아쉽습니다.

선생님 코드와 비교해보며 공부하였습니다.



## 2021.01.18

### django에 대한 기본 지식

`django` : python으로 웹사이트를 만드는데 사용하는 `웹 프레임워크`

`argument`의 종류

`*args` (position argument) : 위치에 있는 단일(?)값을 넣을수 있다

`**kwargs` (keyword argument) : 키워드(어떤 값?string?) 을 넣을수 있냐?(서치)

`객체지향 프로그래밍`은 코드를 정리하는 하나의 방법이라고 이해했다.

`하나의 블루프린트(청사진.설계도)`로 `여러개의 instance`를 만들어 사용할수있다.

`class`는 `무언가(instance)`를 구성할 기본형태를 만든다.

`method` is `function(def)` inside of  `class`!

`method`를 호출할때 `instance`를 초기 `argument`(_self_)로 사용한다

`class` 안에는 기본적으로 들어있는 `method` 가 있다. #ex) __init__

`dictionary` 는 `get`을 갖는다. `{dic_name}.get`

`how to extend of class`

`extend class`란? 기존의 class를 확장하여 필요한것을 추가한 class응 만드는 것.

`class extend_’class_name’(‘upper class’)` 로 표현하여 'upper class'를 상속시킨다.

`method`의 `extend`도 `super().’class_name’(**kwargs)` 로 표현하여 `upper class`에 있는 `method`를 유지하면서 `extend` 할 수 있다


### `GitHub`알게 된 것

`local`의 링크와 `GitHub_reposit`링크가 안맞으면 커맨드(iterm)를 통해 올리고 내릴수없었다.

그래서 `git clone (reposit_URL)`을 사용하여 복제해주니 다시 연결이 가능해졌다.

GitHub에서 `GitHub_Desktop`을 제공해주던데 무엇인지 알아봐야겠다.



## 2021.01.19

###visual studio code 단축키

`cmd + d` : 같은 코드를 선택하여 한번에 수정할수있다.

`option + click` : 클릭하는 곳에 한번에 입력할수있다.

`option + up/down` : 선택한 코드를 위/아래로 이동시킬수 있다.

`option + shift + up/down` : 선택한 코드를 위/아래로 복사하여 이동시킬수있다.

`cmd + /` 해당 줄 전체를 주석처리해준다.

`option + shift + i` : 선택된 영역에 커서가 생겨서 한번에 수정할수있다.

`option + shift + drag ` : 드래그한 모든 영역에 커서가 생겨서 한번에 수정할수있다.

`cmd + up/down` : 맨 위로, 맨 아래로

`cmd + b` : 사이드바 숨기기


