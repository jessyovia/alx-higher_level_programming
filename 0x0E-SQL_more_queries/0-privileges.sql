-- Lists all privileges of MySQL users user_0d_1 and user_0d_2 on localhost

-- For user_0d_1
SELECT * FROM information_schema.user_privileges
WHERE grantee LIKE 'user_0d_1@localhost';

-- For user_0d_2
SELECT * FROM information_schema.user_privileges
WHERE grantee LIKE 'user_0d_2@localhost';
