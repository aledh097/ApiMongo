#!/usr/bin/python
# -*- coding: utf-8 -*-

from bottle import route, run, template, get, post, request, response, redirect, default_app, static_file, TEMPLATE_PATH, error, redirect
from pymongo import MongoClient
from bson.json_util import dumps

@route('/')
def redirect_to_login():
	redirect('/login')

@route('/login', method=["GET"])
def login():
	return template('login.tpl')

@route('/resultado', method='POST')
def resultado():
	user  = request.forms.get("user")
	passwd = request.forms.get("passwd")
	database = request.forms.get("database")
	ip_host = request.forms.get("ip_host")
	mongoserver_uri = "mongodb://%s:%s@%s:27017/%s" % (user,passwd,ip_host,database)
	conection = MongoClient(host=mongoserver_uri)
	db = conection[database]
	nombre_coleccion='productos'
	collection = db[nombre_coleccion]
	resultado = collection.find()
	resultado_dumps=dumps(resultado)
	return template('resultado.tpl', resultado_dumps=resultado_dumps, coleccion=nombre_coleccion)

#@error(500)

#def error500(error):
#	return template('500.tpl')

run(host='127.0.0.1', port=8080, debug=True)

