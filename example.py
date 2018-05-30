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
#outMsg["message"] += "запущен на: " + os.uname()[3] + "\n";
for idx, cpu in enumerate(psutil.cpu_percent(interval=1, percpu=True)):
	outMsg["message"] += 'CPU '+str(idx+1)+': '+str(cpu)+'%\n'
mem = psutil.virtual_memory()
MB = 2**20
outMsg["message"] += 'Оперативы всего: '+str(int(mem.total / MB))+'MB\nИспользовано оперативы: '+str(int((mem.total - mem.available) / MB))+'MB\nСвободно оперативы: '+str(int(mem.available / MB))+'MB\nСожрано ботом: '+str(int(psutil.Process().memory_info().vms / MB / 8))+'MB\n'
outMsg["message"] += "Сообщений: " + str(msg_countComplete()) + "/" + str(msg_count()) + "\n";
outMsg["message"] += "Запущен: " + getStartTime() + "\n";
