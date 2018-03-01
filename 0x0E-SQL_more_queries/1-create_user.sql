-- This script creates a MySQL server user at user_0d_1
-- User will have all privileges on MySQL server
-- If user already exists, script won't fail
GRANT ALL ON *.* TO 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
