create database if not exists FitnessTracker;
use FitnessTracker;

drop table if exists fitness_dataset;
create table fitness_dataset(
   id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
   date varchar(255),
   timestamp varchar(255),
   activity varchar(255),
   acceleration_x varchar(255),
   acceleration_y varchar(255),
   acceleration_z varchar(255),
   gyro_x varchar(255),
   gyro_y varchar(255),
   gyro_z  varchar(255)
);

create user 'root'@'localhost' identified by 'Pass@123';
