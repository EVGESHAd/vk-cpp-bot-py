# -*- coding: utf-8 -*-

"""
input messange:
	int chat_id
	int user_id
	int msg_id
	char msg_flags
	string msg
	string lp_msg

modules:
	int money_get(string id)
	money_add(string id, int money)
	
	int user_get(string id)
	user_set(string id, int acess_level)
	acess levels:
		0 ban
		1 user
		2 vip
		3 coder
		4 -
		5 admin
	
	int msg_count()
	int msg_countComplete()
	
output message:
	dict outMsg
	(vk.api-message.send)

other:
	string getStartTime()
"""
import os
import psutil

outMsg["message"] = "id чата (пользователь/чат): " + str(user_id) + "/" + str(chat_id) + "\n";
outMsg["message"] += "запущен на: " + os.uname()[3] + "\n";
outMsg["message"] += "Я сожрал оперативы: " + str(int(psutil.Process().memory_info().vms / (2**23))) + " Мб\n";
outMsg["message"] += "Сообщений: " + str(msg_countComplete()) + "/" + str(msg_count()) + "\n";
outMsg["message"] += "Запущен: " + getStartTime() + "\n";
