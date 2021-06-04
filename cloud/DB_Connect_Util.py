#!/usr/bin/env python

import datetime
import pymysql
import pickle

select_all = '''select * from fitness_dataset; '''
add_row = ''' insert into fitness_dataset(date, timestamp, activity, acceleration_x, acceleration_y, acceleration_z, gyro_x, gyro_y, gyro_z) values ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s"); '''
select_last_row = ''' select id, date, timestamp, activity, acceleration_x, acceleration_y, acceleration_z, gyro_x, gyro_y, gyro_z from fitness_dataset order by id desc limit 1; '''
select_current_activity = ''' select activity from fitness_dataset order by id desc limit 1; '''
run_count_yesterday = ''' select activity from fitness_dataset where activity=1 and date= CURDATE() - INTERVAL 1 DAY ; '''
run_count_today = ''' select activity from fitness_dataset where activity=1 and date= CURDATE() ; '''
walk_count_yesterday = ''' select activity from fitness_dataset where activity=0 and date= CURDATE() - INTERVAL 1 DAY ; '''
walk_count_today = ''' select activity from fitness_dataset where activity=0 and date= CURDATE() ; '''

def update_db(accel_gyro):
    conn = pymysql.connect(host="localhost", user="root", password='Pass@123', database="FitnessTracker")
    sample= accel_gyro
    model = pickle.load(open('/home/vrvardh/cloud/FitnessTracker.pkl' , 'rb'))
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    timestamp = datetime.datetime.now().strftime("%H-%M-%S")
    acceleration_x, acceleration_y, acceleration_z, gyro_x, gyro_y, gyro_z = sample.split(',')
    prediction = str(model.predict([sample.split(',')]))
    predictionstr = prediction[1:-1]
    activity = predictionstr.rstrip('.')
    with conn.cursor() as cursor:
        cursor.execute(add_row % (date, timestamp, activity, acceleration_x, acceleration_y, acceleration_z, gyro_x, gyro_y, gyro_z))
    conn.commit()

def get_entire_table():
    conn = pymysql.connect(host="localhost", user="root", password='Pass@123', database="FitnessTracker")
    with conn.cursor() as cursor:
        cursor.execute(select_all)
        table = cursor.fetchall()
        print(table)
        return table


def get_latest_row():
    conn = pymysql.connect(host="localhost", user="root", password='Pass@123', database="FitnessTracker")
    with conn.cursor() as cursor:
        cursor.execute(select_last_row)
        row = cursor.fetchone()
        return row

def get_current_activity():
    conn = pymysql.connect(host="localhost", user="root", password='Pass@123', database="FitnessTracker")
    with conn.cursor() as cursor:
        cursor.execute(select_current_activity)
        row = cursor.fetchone()
        return row[0]

def get_run_count_today():
    conn = pymysql.connect(host="localhost", user="root", password='Pass@123', database="FitnessTracker")
    with conn.cursor() as cursor:
        cursor.execute(run_count_today)
        rows_affected=cursor.rowcount
        print(rows_affected)
        return rows_affected

def get_run_count_yesterday():
    conn = pymysql.connect(host="localhost", user="root", password='Pass@123', database="FitnessTracker")
    with conn.cursor() as cursor:
        cursor.execute(run_count_yesterday)
        rows_affected=cursor.rowcount
        print(rows_affected)
        return rows_affected

def get_walk_count_today():
    conn = pymysql.connect(host="localhost", user="root", password='Pass@123', database="FitnessTracker")
    with conn.cursor() as cursor:
        cursor.execute(walk_count_today)
        rows_affected=cursor.rowcount
        print(rows_affected)
        return rows_affected

def get_walk_count_yesterday():
    conn = pymysql.connect(host="localhost", user="root", password='Pass@123', database="FitnessTracker")
    with conn.cursor() as cursor:
        cursor.execute(walk_count_yesterday)
        rows_affected=cursor.rowcount
        print(rows_affected)
        return rows_affected
