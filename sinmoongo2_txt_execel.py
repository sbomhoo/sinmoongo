# -*- coding: utf-8 -*-
import time
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

"""
<sinmoongo2_txt_execel>
다른 컴퓨터에서 전역변수 에러 떠서 만든 코드
승재 코드 보고 변형
크롤링 결과 -> txt -> csv 

"""
browser = 'C:/Users/User/Desktop/python study/sinmoongo_ws/chromedriver.exe'
RESULT_PATH ='C:/Users/User/Desktop/python study/sinmoongo_ws/result/'  #결과 저장할 경로
driver = webdriver.Chrome(browser)


def crawler(reg_d_s,reg_d_e,maxpage_no):
    f = open(RESULT_PATH + 'sinmoongo.txt', 'w', encoding='utf-8')
    pno=1
    s_date=reg_d_s.replace("-","")   
    e_date=reg_d_e.replace("-","")
    while pno <= int(maxpage_no):
        url = 'https://www.epeople.go.kr/jsp/user/pp/UPpProposOpenList.paid?flag=A&pageNo='+str(pno)+'&mode=&petiNo=&s_date='+str(s_date)+'&e_date='+str(e_date)+'&ancCode=&sortType=&sortTemp=&snsTokenMessage=%255B%25EA%25B5%25AD%25EB%25AF%25BC%25EC%25A0%259C%25EC%2595%2588%255D%2B%25EA%25B3%25B5%25EA%25B0%259C%25EC%25A0%259C%25EC%2595%2588&reg_d_s='+reg_d_s+'&reg_d_e='+reg_d_e+'&divCode=&s_anc_c=6260000&status=&keyfield=petiTitle&keyword='
        driver.get(url)
        time.sleep(3) #for selenium wait #파이썬에게 전달하는 데 시간 필요  2~3이 좋다.
        
        #게시글 번호 가져오기  
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        
        bno_list=[]
        bno_tags = soup.select('table > tbody > tr > td:nth-of-type(1)')  #nth-child : 모든 자식의 순서에서 찾음 nth-of-type: 해당하는 자식 태그 요소에서의 순서를 찾음
        for bno_tag in bno_tags:
            bno_list.append(bno_tag.text)
        print(bno_list)
        
        for bno in bno_list:
            try:
                driver.find_element_by_css_selector("#ancDetail_"+str(bno)).click()   #id가 bno인것을 클릭
                        
                html = driver.page_source
                bs = BeautifulSoup(html, 'html.parser')
                title=bs.select('table > thead > tr > th.tit')[0].text  #title.strip()
                date= bs.select('table > tbody > tr > td > ul > li.date > p > span')[0].text
                txt0=bs.select('#content > div.contestView > div > table > tbody > tr:nth-child(1) > td > div > p:nth-child(2)')[0].text  #현황 및 문제점
                txt1=bs.select('table > tbody > tr > td > div > p.txt')[1].text  #개선방안
                txt2=bs.select('table > tbody > tr > td > div > p.txt')[2].text  #기대효과 
                
                f.write(date.strip()+ "\t"+title.strip() + "\t"+txt0.replace('\n','').strip()+"\t"+txt1.replace('\n','').strip()+"\t"+txt2.replace('\n','').strip()+"\n")
                
                driver.execute_script("window.history.go(-1)")  #뒤로가기
                #sinmoongo_txt.write()    
            except:
                pass
        pno += 1
    f.close()  #메모장으로 만들기
    excel_make() #메모장을 엑셀화

    
def excel_make():    
    data = pd.read_csv(RESULT_PATH + 'sinmoongo.txt', sep='\t',header=None, error_bad_lines=False)
    data.columns = ['date','title','현황 및 문제점','개선방안','기대효과']
    print(data)    
    
    writer = pd.ExcelWriter(RESULT_PATH+"sinmoongo4.xlsx",
                            engine='xlsxwriter',
                            options={'strings_to_urls': False})    # 'UserWarning: Ignoring URL' 에러 방지 위함

    data.to_excel(writer,sheet_name='sheet1', encoding='utf-8')
    writer.save()



def main():
    info_main = input("="*50+"\n"+"2017년 이후 신문고 크롤러"+"\n"+"입력 형식에 맞게 입력해주세요."+"\n"+" 시작하시려면 Enter를 눌러주세요."+"\n"+"="*50)
    
    reg_d_s=input("검색 시작 날짜 입력(2019-01-01): ") 
    reg_d_e=input("검색 끝 날짜 입력(2019-01-31): ")
    maxpage_no=input("최대 출력할 페이지수 입력하시오: ") 
    
    crawler(reg_d_s,reg_d_e,maxpage_no)


main()