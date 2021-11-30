-- CREATE TABLE users
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `customer_name` varchar(45) NOT NULL,
  `phone_number` varchar(45) NOT NULL,
  `money` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `phone_number_UNIQUE` (`phone_number`),
  KEY `money_index` (`money`),
  KEY `name_index_bt` (`customer_name`),
  KEY `phone_num_bt` (`phone_number`),
  FULLTEXT KEY `name_index` (`customer_name`),
  FULLTEXT KEY `phone_num_index` (`phone_number`)
);

--CREATE TABLE call_history
CREATE TABLE `call_history` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `call_id` int NOT NULL,
  `receive_id` int NOT NULL,
  `duration` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_index` (`id`) USING BTREE,
  KEY `date_index` (`date`),
  KEY `dura_index` (`duration`),
  KEY `call_id_bt_index` (`call_id`),
  KEY `re_id_bt_index` (`receive_id`),
  FULLTEXT KEY `call_id_index` (`call_id`),
  FULLTEXT KEY `re_id_index` (`receive_id`)
);



-- Query 1
SELECT * FROM users 
WHERE phone_number LIKE '09%'
LIMIT 10000;

-- Query 2
SELECT * FROM users
WHERE MATCH (`customer_name`)
AGAINST("Thành")
LIMIT 10000;

-- Quey 3
SELECT * FROM users
WHERE MATCH (`customer_name`)
AGAINST("Ank")
LIMIT 10000;

-- Query 4
SELECT customer_name, COUNT(*) FROM users 
GROUP BY customer_name limit 10000;


-- Query 5
SELECT Distinct(phone_number) FROM users AS u
JOIN call_history AS ch ON ch.call_id = u.id 
WHERE ch.date BETWEEN '2020-01-01' AND '2020-12-30';


-- UPDATE
UPDATE users
SET phone_number = CONCAT(0 , phone_number)
WHERE id = 10;


-- DELETE
DELETE FROM users 
WHERE phone_number LIKE "12025%";
