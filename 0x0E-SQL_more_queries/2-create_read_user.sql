-- Create database hbtn_0d_2
-- Create user user_0d_2
-- User should have SELECT priviledges
-- have pswd user_0d_2_pwd
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USE IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
GRANT USAGE ON *.* TO user_0d_2@localhost;
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
