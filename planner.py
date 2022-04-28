import streamlit as st
import pandas as pd 
#from planner_util import *
import random
import sqlite3
import json

import plotly.express as px 
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')


def run_plannerapp():
    
	f = open('user_creds/temp_login_2.json','r')
	log_details = json.load(f)
	username = list(log_details.keys())
	
	
	dbconnector = sqlite3.connect(f'user_record/aids/{username[0]}/planner.db',check_same_thread=False)
	c = dbconnector.cursor()

	def create_table():
		c.execute('CREATE TABLE IF NOT EXISTS taskstable(task TEXT,task_status TEXT,task_due_date DATE)')


	def add_data(task,task_status,task_due_date):
		c.execute('INSERT INTO taskstable(task,task_status,task_due_date) VALUES (?,?,?)',(task,task_status,task_due_date))
		dbconnector.commit()


	def view_all_data():
		c.execute('SELECT * FROM taskstable')
		data = c.fetchall()
		return data

	def view_all_task_names():
		c.execute('SELECT DISTINCT task FROM taskstable')
		data = c.fetchall()
		return data

	def get_task(task):
		c.execute('SELECT * FROM taskstable WHERE task="{}"'.format(task))
		data = c.fetchall()
		return data

	def get_task_by_status(task_status):
		c.execute('SELECT * FROM taskstable WHERE task_status="{}"'.format(task_status))
		data = c.fetchall()


	def edit_task_data(new_task,new_task_status,new_task_date,task,task_status,task_due_date):
		c.execute("UPDATE taskstable SET task =?,task_status=?,task_due_date=? WHERE task=? and task_status=? and task_due_date=? ",(new_task,new_task_status,new_task_date,task,task_status,task_due_date))
		dbconnector.commit()
		data = c.fetchall()
		return data

	def delete_data(task):
		c.execute('DELETE FROM taskstable WHERE task="{}"'.format(task))
		dbconnector.commit()

    
	quotes_ls = ["“It's not what you achieve, it's what you overcome. That's what defines your career”. —Carlton Fisk",
					"“Failure doesn't mean you are a failure it just means you haven't succeeded yet.” —Robert H. Schuller",
					"“Dreams are extremely important. You can't do it unless you imagine it.” —George Lucas",
					"""“The future depends on what you do today.” – Mahatma Gandhi""",
					"“A mind troubled by doubt cannot focus on the course to victory.” —Arthur Golden",
					"“If opportunity doesn’t knock, build a door.” -Milton Berle",
					"“The only way to do great work is to love what you do. If you haven't found it yet, keep looking. Don't settle.” -Steve Jobs ",
					"“Act as if what you do makes a difference. It does.” -William James",
					"“If it scares you, it might be a good thing to try.” -Seth Godin",
					"“There are no shortcuts to any place worth going.” -Beverly Sills"
				]
    
	st.header("A Place to Plan your Career and Academics")
	st.text(quotes_ls[random.randint(0,9)])
	menu = ["Create a Task","View My Tasks","Update a Task","Delete a Task"]
	choice = st.selectbox("What Would you like to do?",menu)
 
	
	create_table()

	if choice == "Create a Task":
		st.subheader("Add Item")
		col1,col2 = st.columns(2)
		
		with col1:
			task = st.text_area("Task To Do")

		with col2:
			task_status = st.selectbox("Status",["ToDo","Doing","Done"])
			task_due_date = st.date_input("Due Date")

		if st.button("Add Task"):
			add_data(task,task_status,task_due_date)
			st.success("Added :: {} ::To Task in DataBase".format(task))


	elif choice == "View My Tasks":
		
		result = view_all_data()
		clean_df = pd.DataFrame(result,columns=["Task","Status","Date"])
		st.dataframe(clean_df)

		with st.expander("Show My Task Status"):
			task_df = clean_df['Status'].value_counts().to_frame()
			task_df = task_df.reset_index()
			st.dataframe(task_df)

			p1 = px.pie(task_df,names='index',values='Status')
			st.plotly_chart(p1,use_container_width=True)


	elif choice == "Update a Task":
		st.subheader("Edit Items")
		with st.expander("Current Data"):
			result = view_all_data()
			clean_df = pd.DataFrame(result,columns=["Task","Status","Date"])
			st.dataframe(clean_df)

		list_of_tasks = [i[0] for i in view_all_task_names()]
		selected_task = st.selectbox("Task",list_of_tasks)
		task_result = get_task(selected_task)

		if task_result:
			task = task_result[0][0]
			task_status = task_result[0][1]
			task_due_date = task_result[0][2]

			col1,col2 = st.columns(2)
			
			with col1:
				new_task = st.text_area("Task To Do",task)

			with col2:
				new_task_status = st.selectbox("Status",["ToDo","Doing","Done"])
				new_task_due_date = st.date_input(task_due_date)

			if st.button("Update Task"):
				edit_task_data(new_task,new_task_status,new_task_due_date,task,task_status,task_due_date)
				st.success("Updated :: {} ::To {} in DataBase".format(task,new_task))

			with st.expander("View Updated Data"):
				result = view_all_data()
				clean_df = pd.DataFrame(result,columns=["Task","Status","Date"])
				st.dataframe(clean_df)


	elif choice == "Delete a Task":
		st.subheader("Delete")
		with st.expander("View Data"):
			result = view_all_data()
			clean_df = pd.DataFrame(result,columns=["Task","Status","Date"])
			st.dataframe(clean_df)

		unique_list = [i[0] for i in view_all_task_names()]
		delete_by_task_name =  st.selectbox("Select Task",unique_list)
		if st.button("Delete"):
			delete_data(delete_by_task_name)
			st.warning("Deleted: '{}' in DataBase".format(delete_by_task_name))

		with st.expander("Updated Data"):
			result = view_all_data()
			clean_df = pd.DataFrame(result,columns=["Task","Status","Date"])
			st.dataframe(clean_df)


