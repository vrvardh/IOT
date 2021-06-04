#!/usr/bin/env python

from flask import Flask, make_response, jsonify
from DB_Connect_Util import get_entire_table,get_latest_row,get_current_activity,get_run_count_today,get_run_count_yesterday,get_walk_count_today,get_walk_count_yesterday
from SensorAPI import getSensorValues
from FCM_PushNotification import timer
from threading import Thread

webapp = Flask(__name__)


@webapp.route('/history', methods=["GET"])
def history():
  table = get_entire_table()
  json_table = jsonify(table)
  resp = make_response(json_table, 200)
  return resp


@webapp.route("/latest_reading", methods=["GET"])
def latest_data():
  row = get_latest_row()
  json_row = jsonify(row)
  resp = make_response(json_row, 200)
  return resp

@webapp.route("/current_activity", methods=["GET"])
def current_activity():
  row = get_current_activity()
  json_row = jsonify(row)
  resp = make_response(json_row, 200)
  return resp

@webapp.route("/yesterdays_walk_count", methods=["GET"])
def yest_walk_data():
  row = get_walk_count_yesterday()
  json_row = jsonify(row)
  resp = make_response(json_row, 200)
  return resp

@webapp.route("/todays_walk_count", methods=["GET"])
def today_walk_data():
  row = get_walk_count_today()
  json_row = jsonify(row)
  resp = make_response(json_row, 200)
  return resp

@webapp.route("/yesterdays_run_count", methods=["GET"])
def yest_run_data():
  row = get_run_count_yesterday()
  json_row = jsonify(row)
  resp = make_response(json_row, 200)
  return resp

@webapp.route("/todays_run_count", methods=["GET"])
def today_run_data():
  row = get_run_count_today()
  json_row = jsonify(row)
  resp = make_response(json_row, 200)
  return resp


if __name__ == "__main__":
  t = Thread(target=getSensorValues)
  t.start()
  t1 = Thread(target=timer)
  t1.start()
  webapp.run('0.0.0.0', port=80)
