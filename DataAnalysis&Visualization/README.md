# Data Analysis & Visualization





## 1. 일정

- 데이터 수집 : ~ 2021. 07. 07
- 데이터 분석 & 시각화 : 2021. 07. 08 ~ 07. 19
- 발표 : 2021. 07. 20



## 2. 개요

- Data Analysis
  1. 서울특별시 모기예보제 실시 中
  2. 지역별 자료 구축 현황
     - 서울특별시 : DMS와 유문등 설치 및 채집 결과 공개
     - 인천광역시 & 부산광역시 : 유문등 설치 및 채집 결과 공개
     - 경기도 & 경상북도 & 전라북도 & 대전광역시 : 유문등 자료가 존재하나 조사 기간이 짧음
     - 강원도, 경상남도, 울산광역시 등은 자료 구축 X
     - 제주특별자치도는 유문등 데이터가 존재하나 주 단위로 별개의 파일로 되어있어 활용성이 낮다고 판단
       - http://hei.jeju.go.kr/contents/index.php?mid=0201&page=1
- Visualization
- Presentation





## 3. 주제 및 데이터



### 기후 데이터를 활용한 모기 발생 예보



#### 가설설정

- **H0** : 모기 성장 기간을 반영한 기후 데이터가 모기 개체수 증가량과 상관관계가 **있다.**

- **H1** : **없다.**



#### 데이터

##### 모기 데이터

1. <span style="color:red">**인천광역시 모기밀도 조사사업**</span>

   - 출처 : 인천광역시 보건환경연구원
     - https://www.incheon.go.kr/ecopia/search?siteSkn=ecopia&category=BOARD&kwd=%EB%AA%A8%EA%B8%B0&detailKwd=%EB%AA%A8%EA%B8%B0&srchFd=ALL&date=all&startDate=&endDate=&originalQuery=&previousQuery=&page=0&pageNum=1&detailSearch=false&anyWordFlag=0&sort=n&fields=&srchFd=ALL&total=156&spcFlag=true

   - **주 단위/유문등 장소별/ 모기 종류별** 채집 데이터
   - 조사 날짜 : 2013. 06 ~ 2021. 05(겨울 제외/연도마다 상이)

2. <span style="color:blue">**서울특별시 DMS(디지털 모기 측정기) 포집내역(2015~2020)(통합)**</span>
   - 출처 : 서울특별시 보건환경연구원
     - https://news.seoul.go.kr/welfare/archives/532165

   - **일자별** 포집 모기 개체수

   - 조사 날짜 : 2015 ~ 2020

   - 2-1. 서울특별시 DMS 설치 현황(2019)

     - 2019(연도마다 상이)

     - 설치된 50개소의 **지리적 특성 고려** 필요

3. <span style="color:red">**서울특별시 유문등 모기 개체수(2015~2020)(통합)**</span>
   - 출처 : 서울특별시 보건환경연구원
     - https://news.seoul.go.kr/welfare/archives/532165 (위와 동일)
   - **주 단위/서울특별시 전체/모기 종류별** 채집 데이터
   - 조사 날짜 : 2008 ~ 2020
   - 3-1. 서울특별시 유문등 설치 현황(2020)
     - 2020(연도마다 상이)
     - 설치된 58개소의 **지리적 특성** 고려 필요
   - 유문등 데이터 한계
     - **평균기온**과 **월합강수량**을 사용해야 함
     - 데이터 통합 어려움

4. <span style="color:green">**서울특별시 모기예보제 정보**</span>
   - 출처 : 서울특별시 보건환경연구원
     - https://news.seoul.go.kr/welfare/archives/532165 (위와 동일)

   - 일자별/서울특별시 전체/지역 특성별(수변부|주거지|공원) 모기지수
   - 모기예보제 관련 홍보 자료
     - https://news.seoul.go.kr/welfare/archives/532160

5. <span style="color:red">**부산광역시 유문등 모기 개체수(2002. 04~ 2021. 06)**</span>

   - **주 단위/부산광역시 전체/모기 종류별** 채집 데이터

6. 추가 필요 자료

   - 서울특별시 & 인천광역시 & 부산광역시 ~~유문등~~ 및 DMS 설치 위치 데이터

     - 2019, 2020, 2021

     - https://opengov.seoul.go.kr/sanction/17649043(비공개)




##### 기후 데이터

1. 시도별 날씨 데이터(서울, 부산, 인천)
2. CLM 온실가스(2015. 01~2021. 06)
   - 안면도 자료



##### 통합 데이터

1. <span style="color:purple">**daily_seoul**</span>
   - 서울특별시 DMS 포집내역 + 서울특별시 기후
2. <span style="color:purple">**trap_seoul**</span>
   - 서울특별시 유문등 채집 + 서울특별시 기후



##### 지리 데이터

1. 녹지(2015~2020)



##### 변수 설명

목표변수 : **모기 발생 개체수**

입력변수 : 

- temp : 평균기온(°C)

- - <span style="color:brown">**평균기온도 encoding?**</span>
- l_temp : 최저기온(°C)
  - <span style="color:brown">~~**encoding : 섭씨 10도 미만 → 0, 이상 → 1**~~</span>
- h_temp : 최고기온(°C)
  - <span style="color:brown">~~**encoding : 섭씨 33도 미만 → 1, 이상 → 0**~~</span>
- rain_per_day : 일강수량(mm)
- <span style="color:purple">**누적강수일**</span>
  - <span style="color:brown">**파생변수**</span>
- wind : 평균 풍속(m/s)
- dew : 평균 이슬점온도(°C)
- humidity : 평균 상대습도(%)
- steam_pressure : 평균 증기압(hPa)
- sunshine_time : 합계 일조시간(hr)
- sunshine : 합계 일사량(MJ/m2)
- ground_surface_temp : 평균 지면온도(°C)
- <span style="color:brown">**지역별 녹지 비율**</span>(보류)
  - 연도별 지정
- <span style="color:brown">~~**CO2 농도**~~</span>
  - 안면도 관측 자료가 우리나라 전체 이산화탄소 농도를 나타냄



<span style="color:blue">**각각 변수를 현재, 7일 전, 14일 전으로 추가 생성 후 분석**</span>



<span style="color:brown">**어떤 모델 사용하는 것이 좋을지?**</span>





## 4. 참고 자료



1. **2020년 국내 일본뇌염매개모기 발생 감시 현황**

   - 출처 : 질병관리청

   - 시각화 부분 참고
   - https://www.kdca.go.kr/board/board.es?mid=a20602010000&bid=0034&act=view&list_no=712903#
2. 2020년 국내 말라리아매개모기 감시 현황

   - 출처 : 질병관리청

   - 일본뇌염과 말라리아 비교
3. **부산광역시 2020년 일본뇌엽매개모기 밀도조사 보고**

   - 유문등 운영 방법
4. **모기 활동성 예측을 위한 기상 데이터에서 인접성 향상을 위한 연구**
   - p.18 : <span style="color:blue">**DMS 채집 결과와 날씨 데이터 정리 예시**</span>
5. <span style="color:purple">**★동네예보자료를 활용한 수도권 모기예측 지수 개발**</span>
   - 모기지수 개발 배경 및 개요
6. <span style="color:purple">**★황세영(2020)_머신러닝 기반 기후 데이터를 활용한 모기 개체수 예측**</span>
   - <span style="color:red">**분석방법 예시**</span>
7. **한국의 스마트 모기 모니터링 시스템의 도입 안산시 친환경 모기방제 방법 시행**
   - 전체적으로 참고하면 좋을 듯한 자료
   - 하지만...! 영어...
   - http://www.riss.kr/search/detail/DetailView.do?p_mat_type=be54d9b8bc7cdb09&control_no=b780daa5b8af0cdeffe0bdc3ef48d419&outLink=K
8. **수도권기상청, 날씨처럼 모기를 예측**
   - DMS와 유문등의 작동 원리
9. <span style="color:red">**★기상자료와 GIS 활용 수도권 모기 활동지수 개발**</span>



## 5. 분석 방향



