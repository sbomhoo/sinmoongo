# sinmoongo
selenium을 이용한 국민신문고 크롤링  /  크롬 드라이버 사용 / selenium chromdriver

https://www.epeople.go.kr/jsp/user/pp/UPpProposOpenList.paid?flag=A&pageNo=1&mode=&petiNo=&s_date=20180201&e_date=20190131&ancCode=&sortType=&sortTemp=&snsTokenMessage=%255B%25EA%25B5%25AD%25EB%25AF%25BC%25EC%25A0%259C%25EC%2595%2588%255D%2B%25EA%25B3%25B5%25EA%25B0%259C%25EC%25A0%259C%25EC%2595%2588&reg_d_s=2018-02-01&reg_d_e=2019-01-31&divCode=&s_anc_c=6260000&status=&keyfield=petiTitle&keyword=

<코드 설명>  
- 국민신문고 사이트의 신문 내용을 크롤링해오는 코드
- 자바스크립트를 크롤링하기 위해 selenium을 이용 (chromedriver.exe 다운받을 것!)
- 크롤링 할 날짜와 최대 페이지 수를 사용자로부터 입력 받음
- 크롤링 결과를 엑셀로 저장함

<주의점>  
- 2016년이전과 2017년 이후 신문고 글쓰기 내용이 다르다.
- 2016년 이전 : 개요 / 현황 및 문제점 / 개선방안 / 기대효과  => sinmoongo4_before2016.py  사용
- 2017년 이후 : 현황 및 문제점 / 개선방안 / 기대효과 => sinmoongo4.py  사용



<크롤링 해오는 것>  
- 2016년 이전 : 날짜 / 제목 / 개요 / 현황 및 문제점 / 개선방안 / 기대효과 / 
- 2017년 이후 : 날짜 / 제목 / 현황 및 문제점 / 개선방안 / 기대효과

