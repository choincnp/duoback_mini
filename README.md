# duoback_mini

---

## 기능명세서

##### FE

- [x] #1 input으로 유저에게 검색어를 받는다.
- [ ] #6 데이터를 받아와 playList에 추가한다.
- [ ] #7 List에 추가하면 해당 유저 데이터베이스에 저장된다.(로컬 써도 OK);
- [ ] #8 List 요소를 누르면 기존 Video가 언마운트 되고, 새로운 Video가 Mount된다.

##### BE

- [ ] #2 프론트에서 넘어온 query를 받아 BS4로 검색 결과를 가져온다.
  - [ ] #3 검색 결과에서 원하는 정보를 파싱한다
    - [ ] #4 [정규표현식](https://regexr.com/) 사용한다.
- [ ] #5 파싱한 데이터를 프론트로 넘겨준다. (프론트에서 필요한 정보 알아서 쓰기)
