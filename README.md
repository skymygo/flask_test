# flask_test

실행법.

1.api_info.json, db_info.json에 올바른 정보를 입력하십시오.
2.api.py를 실행하십시오.

기능.

1. 통계정보 가져오기.

   1-1. 환자
   
      o. 전체 환자 수  (/statistic/person/total)
      
      o. 성별 환자 수  (/statistic/person/gender) 
      
      o. 인종별 환자 수 (/statistic/person/race)
      
      o. 민족별 환자 수 (/statistic/person/ethnicity)
      
      o. 사망 환자 수  (/statistic/person/death)
      
   1-2. 방문
   
      o. 방문 유형별 방문 수 (/statistic/visit/occurrence)
      
      o. 성별 방문 수      (/statistic/visit/gender)
      
      o. 인종별 방문 수    (/statistic/visit/race)
      
      o. 민족별 방문 수    (/statistic/visit/ethnicity)
      
      o. 방문시 연령대별 방문 수  (/statistic/visit/ages)


   
2. 테이블 별 concept_id들의 정보 조회 

   2-1 조회기능(/concept_info/<table>>/<column>)
   
      table과 column에 적절한 값을 입력하여 조회한다
      
      ex) condition_occurrence Table의 condition(_concept_id) Column의 정보를 알고싶다면, /concept_info/condition_occurrence/condition 를 입력한다.
   
   
   2-2 검색 기능
   
      Path Parameter로 keyword를 입력하여 검색한다.
      
      ex) 위의 예시에서 asthma를 검색하고 싶으면 /concept_info/condition_occurrence/condition?keyword=asthma 를 입력한다.
   
   
   2-3 페이징 기능
   
      Path Paramater로 page를 입력하여 검색한다
      
      ex) 위의 예시에서 2 page를 검색하고 싶으면 /concept_info/condition_occurrence/condition?keyword=asthma&page=2 를 입력한다
   
   
   
3. 테이블 row 조회

   3-1 조회 기능(get_row/<table>)
   
      table에 적절한 값을 입력하여 조회한다
      
      ex) person Table을 조회하려면 /get_row/person 을 입력한다.
      

   3-2 검색 기능
   
      Path Parameter로 column과 keyword를 입력하여 조회한다
      

   3-3 페이징 기능
   
      Path Parameter로 page를 입력하여 검색한다
      
      ex) 위의 예시에서 4 page를 검색하고 싶으면 /get_row/person?page=4 를 입력한다.
      
   
   3-4 현재 안되는 경우
   
      visit_occurrence : discharge_to_concept_id의 값이 모두 null 이어서 검색 결과가 없음
      
      condition_occurrence : condition_status_concept_id의 값이 모두 null 이어서 검색 결과가 없음
      
      death : death_type_concept_id의 값인 32815가 concept에 없어서 검색 결과가 없음.
     
