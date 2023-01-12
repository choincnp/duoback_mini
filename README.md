# 붉은 영상 재생기
---
![](https://github.com/choincnp/duoback_mini/issues/23#issue-1530632222)
> 2023.1.9 ~ 2023.1.12
## Stack
* HTML
* CSS
* Python
* VanillaJS
* JQuery
---
## TEAMMATES
| 곽승민 | 김대현 | 조영준 | 한승현 |
|---|---|---|---|
| FE | FE | BE | BE |

---

## HOME
![](https://github.com/choincnp/duoback_mini/issues/24#issue-1530632858)
### you have to sign in without having any ID/PW


---
# 기능명세서
---

## 검색 API 구현

- [x] (FE) input에 입력된 text를 백엔드로 전달한다.
- [x] (BE) 백엔드에서 bs4를 이용해 해당 페이지의 HTML 파일을 res로 전달한다.
      EndPoint : /search
      Method : GET
- [x] (FE) 백엔드에서 전달해준 데이터를 파싱한다.

  - [x] 제목
  - [x] 썸네일
  - [x] 재생시간
  - [x] 조회수
  - [x] url

  ```ts
  interface dataType = {
    channelUrl: string;
    duration: string;
    id: string;
    owner: string;
    thumbnail: string;
    title: string;
  }

  let data:dataType;
  ```

## Player

- [x] 선택된 music을 Player에 마운트한다
- [ ] 현재 진행중인 곡이 끝나면 다음 곡으로 넘어간다
- [ ] 컨트롤러 구현(이전곡 / 다음곡 / 일시정지)

## 검색 결과 렌더링

- [x] 받은 결과물로 검색 결과를 렌더링한다
  - [x] 검색 결과 컴포넌트는 재사용이 가능한 컴포넌트로 구성한다
  - [x] 추가 버튼 구현
    - [x] PlayList에 등록된다. (DB등록)

## 로그인

- [x] ID와 PW를 입력받고 Flask로 전달한다.
  - [x] 유효성 검사를 진행한다(BE)
    - [x] 빈 문자열일 경우, 예외처리 한다.
    - [x] ID와 PW가 4자리 미만일 경우, 예외처리 한다.
    - [x] DB에 존재하지 않는 ID인 경우, 예외처리 한다. (해당 경우는, signIn으로 redirect)
    - [x] PW가 불일치 하는 경우, 예외처리 한다. (ID 존재 여부 따진 이후에 진행)
    - [x] 문제가 없다면 프론트로 해당 user의 playList를 return

## 회원가입

- [x] ID와 PW를 입력받고 Flask로 전달한다(FE)
  - [x] 유효성 검사를 진행한다(BE)
    - [x] BE (백엔드에서 경우에 따라 에러 메시지 전달한다)- [ ]
    - [x] 빈 문자열일 경우, 예외처리 한다.
    - [x] ID와 PW가 4자리 미만일 경우, 예외처리 한다.
    - [x] DB에 존재하는 ID일 경우 예외처리 한다.

---

## 유의미한 커밋 로그 남기기.

```jsx
feat: input의 value가 빈 문자열일 경우, 예외처리 한다
feat: 중복된 할 일이 있을 경우, 예외처리 한다
feat: 유효성 검사에 문제가 없다면 DB에 저장한다
refactor: 유효성 검사 함수 모듈화
docs: 기능 명세서 추가
feat: playList 추가 버튼 구현
```

1. 기능 단위로 구현 및 commit한다.
2. [commit-convention](https://github.com/pengooseDev/Interactive-Study/blob/main/docs/convention/commit.md)을 지킨다.
3. 기능명세서는 한 번에 추가하지 않는다. 필요할 때마다 수정한다.
