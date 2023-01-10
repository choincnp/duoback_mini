# 기능명세서

---

## 1. 검색

- [ ] (FE) input에 입력된 text를 백엔드로 전달한다.
- [ ] (BE) 백엔드에서 bs4를 이용해 해당 페이지의 HTML 파일을 res로 전달한다.
      EndPoint : /search
      Method : GET
- [ ] (FE) 백엔드에서 전달해준 데이터를 파싱한다.

  - [ ] 제목
  - [ ] 썸네일
  - [ ] 재생시간
  - [ ] 조회수
  - [ ] url

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

## 2. 검색 결과

- [ ] 받은 결과물로 검색 결과를 렌더링한다.
  - [ ] 검색 결과 컴포넌트는 재사용이 가능한 컴포넌트로 구성한다.
  - [ ] 추가 버튼 구현
    - [ ] PlayList에 등록된다. (DB등록)

---

## 회원가입

- [ ] ID와 PW를 입력받고 Flask로 전달한다. (FE)
  - [ ] 유효성 검사
    - [ ] FE
      - [ ] 빈 문자열일 경우, 예외처리 한다.
      - [ ] ID와 PW가 4자리 미만일 경우, 예외처리 한다.
    - [ ] BE (백엔드에서 경우에 따라 에러 메시지 전달해주세요.)

---

## +a 추가 구현하고 싶은 사항

- [ ] DB 연동해서, playlist에 가장 많이 담긴 음악을 추천하는 페이지 구현.

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
