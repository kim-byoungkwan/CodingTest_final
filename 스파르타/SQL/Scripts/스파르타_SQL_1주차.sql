SELECT * FROM orders
WHERE payment_method = 'kakaopay';

SELECT * FROM point_users
WHERE point >= 5000;

SELECT * FROM orders
WHERE course_title = '앱개발 종합반' AND payment_method = 'CARD';

-- QUIZ

SELECT * FROM point_users
WHERE point > 20000;

SELECT * FROM users
WHERE name ='황**';

SELECT * FROM orders
WHERE course_title = '웹개발 종합반' AND payment_method ='CARD';

-- 

SELECT * FROM orders
WHERE course_title != '웹개발 종합반';

SELECT * FROM orders
WHERE created_at BETWEEN '2020-07-13' and '2020-07-14';

SELECT * FROM orders
WHERE created_at BETWEEN '2020-07-13' and '2020-07-15';

SELECT week,comment FROM checkins
WHERE week in (1,3);

SELECT comment,week FROM checkins
WHERE week in (1,3);

SELECT comment,week FROM checkins
WHERE week in (1,2,3);

SELECT * FROM users
WHERE email LIKE '%daum.net';
-- %daum.net 는 %가 표현된 daum.net앞의 자리에 무엇이 오든 상관 없이 daum.net
-- 가 들어있는 모든 튜플을 출력하라는 의미이다. 즉, LIKE는 %와 함께쓰인다.

SELECT * FROM users
WHERE email LIKE 'a%t';
/*a%t는 a로 시작해서 a뒤에 무엇이 오든 상관없이 t로 끝나는 모든 튜플을 출력해주는 의미이다*/

-- QUIZ_2
SELECT * FROM orders
WHERE payment_method != 'CARD';

SELECT * FROM point_users
WHERE point BETWEEN 20000 and 30000;
-- 숫자는 ''를 사용하여 문자형으로 변환시켜서 표현하면 안된다.

SELECT * FROM users
WHERE email LIKE 's%com';

SELECT * FROM users
WHERE email LIKE 's%com' and name LIKE '이%';

SELECT * FROM orders
WHERE payment_method = 'kakaopay' limit 5;
-- 튜플의 개수를 5개로 제한해서 출력하라는 의미로서 매우 큰 튜플을 가진 테이블을 다룰때 매우 유용하다

SELECT payment_method FROM orders o;

SELECT DISTINCT payment_method FROM orders o;

-- select 에 의해 출력되는 튜플들을 중복되는 것 없이 출력해주는 기능을 의미한다.

select count(*) from orders;

SELECT count(DISTINCT payment_method) FROM orders o ;

-- count는 항상 () 괄호와 함께 사용되어야하며 괄호안에는 튜플을 표현하는 속성이 정의된다

SELECT count(*) from orders
where payment_method = 'kakaopay';

-- sql에선 ''를 사용하여 표현하지 않으면 모두 컬럼속성을 표현하는 것으로 본다.

-- QUIZ_3

SELECT email FROM users
WHERE name like '남%';

SELECT email FROM users u
WHERE email like '%gmail%'
AND created_at BETWEEN '2020-07-12' AND '2020-07-14';

SELECT count(*) FROM users
WHERE email LIKE '%gmail%'
AND created_at BETWEEN '2020-07-12' AND '2020-07-14';

-- ASSIGNMENT

SELECT * FROM orders o
WHERE email LIKE '%naver%'
AND course_title = '웹개발 종합반'
AND payment_method = 'kakaopay';















