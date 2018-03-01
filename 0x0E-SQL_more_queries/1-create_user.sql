-- This script creates a MySQL server user at user_0d_1
-- User will have all privileges on MySQL server
-- If user already exists, script won't fail
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
