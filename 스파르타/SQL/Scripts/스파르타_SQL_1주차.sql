SELECT * FROM orders
WHERE payment_method = 'kakaopay';

SELECT * FROM point_users
WHERE point >= 5000;

SELECT * FROM orders
WHERE course_title = '�۰��� ���չ�' AND payment_method = 'CARD';

-- QUIZ

SELECT * FROM point_users
WHERE point > 20000;

SELECT * FROM users
WHERE name ='Ȳ**';

SELECT * FROM orders
WHERE course_title = '������ ���չ�' AND payment_method ='CARD';

-- 

SELECT * FROM orders
WHERE course_title != '������ ���չ�';

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
-- %daum.net �� %�� ǥ���� daum.net���� �ڸ��� ������ ���� ��� ���� daum.net
-- �� ����ִ� ��� Ʃ���� ����϶�� �ǹ��̴�. ��, LIKE�� %�� �Բ����δ�.

SELECT * FROM users
WHERE email LIKE 'a%t';
/*a%t�� a�� �����ؼ� a�ڿ� ������ ���� ������� t�� ������ ��� Ʃ���� ������ִ� �ǹ��̴�*/

-- QUIZ_2
SELECT * FROM orders
WHERE payment_method != 'CARD';

SELECT * FROM point_users
WHERE point BETWEEN 20000 and 30000;
-- ���ڴ� ''�� ����Ͽ� ���������� ��ȯ���Ѽ� ǥ���ϸ� �ȵȴ�.

SELECT * FROM users
WHERE email LIKE 's%com';

SELECT * FROM users
WHERE email LIKE 's%com' and name LIKE '��%';

SELECT * FROM orders
WHERE payment_method = 'kakaopay' limit 5;
-- Ʃ���� ������ 5���� �����ؼ� ����϶�� �ǹ̷μ� �ſ� ū Ʃ���� ���� ���̺��� �ٷ궧 �ſ� �����ϴ�

SELECT payment_method FROM orders o;

SELECT DISTINCT payment_method FROM orders o;

-- select �� ���� ��µǴ� Ʃ�õ��� �ߺ��Ǵ� �� ���� ������ִ� ����� �ǹ��Ѵ�.

select count(*) from orders;

SELECT count(DISTINCT payment_method) FROM orders o ;

-- count�� �׻� () ��ȣ�� �Բ� ���Ǿ���ϸ� ��ȣ�ȿ��� Ʃ���� ǥ���ϴ� �Ӽ��� ���ǵȴ�

SELECT count(*) from orders
where payment_method = 'kakaopay';

-- sql���� ''�� ����Ͽ� ǥ������ ������ ��� �÷��Ӽ��� ǥ���ϴ� ������ ����.

-- QUIZ_3

SELECT email FROM users
WHERE name like '��%';

SELECT email FROM users u
WHERE email like '%gmail%'
AND created_at BETWEEN '2020-07-12' AND '2020-07-14';

SELECT count(*) FROM users
WHERE email LIKE '%gmail%'
AND created_at BETWEEN '2020-07-12' AND '2020-07-14';

-- ASSIGNMENT

SELECT * FROM orders o
WHERE email LIKE '%naver%'
AND course_title = '������ ���չ�'
AND payment_method = 'kakaopay';















