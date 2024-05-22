show databases;
create database airline;
use airline;
create table passengers(slno int(2),name varchar(20),email varchar(15),country char(10),dob date,address varchar(40),pincode int(6),mobile int(12),rdate date,dest varchar(10));
select * from passengers; 
show tables;
create table location(flight_type varchar(10),departure char(20),arrival char(20));
select * from location;
select * from passengers;
