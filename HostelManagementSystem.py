from tkinter import *
import sqlite3

# Create the connection with the database.
conn = sqlite3.connect('HTLMgmt.db')
print('Connected\n')

# Create a cursor object.
cursor = conn.cursor()

# Function for login
def login(uname, pword):

	# Function to set username and password fields to null.
	def setnull():
		messagebox.showwarning('WARNING', 'Invalid Username/Password !!!')
		user.set('')
		pwod.set('')

	# Function for student logout.
	def logout():
		top1.destroy()
		user.set('')
		pwod.set('')

	# Function to display student details.
	def display_details():

		# Retrieve details of the student from the database.
		cursor.execute('select name from student where usn=?', (uname,))
		display_name = cursor.fetchall()
		display_name = display_name[0]

		# Label to display name of the student.
		welcome = Label(top1, text=display_name[0].title(), font=('Helvetica', 27), bg='white', fg='gray1')
		welcome.place(relx=0.04, rely=0.15, anchor=W)

		# USN label.
		usn_label = Label(top1, text='USN: ', font=('Courier', 20, 'bold'), bg='azure', fg='brown4')
		usn_label.place(relx=0.04, rely=0.29, anchor=W)
		# Label to display USN of the student.
		usn = Label(top1, text=uname, font=('Times New Roman', 20), bg='azure')
		usn.place(relx=0.11, rely=0.29, anchor=W)

		# Student course label.
		stud_course_label = Label(top1, text='Course: ', font=('Courier', 20, 'bold'), bg='azure', fg='brown4')
		stud_course_label.place(relx=0.04, rely=0.36, anchor=W)
		# Retrieve course of the student from the database.
		course = cursor.execute('select course from student where usn=?', (uname,))
		stud_course_record = course.fetchall()
		# Label to display course of the student.
		stud_course = Label(top1, text=stud_course_record[0], font=('Times New Roman', 20), bg='azure')
		stud_course.place(relx=0.11, rely=0.36, anchor=W)

		# Student branch label.
		stud_branch_label = Label(top1, text='Branch: ', font=('Courier', 20, 'bold'), bg='azure', fg='brown4')
		stud_branch_label.place(relx=0.04, rely=0.43, anchor=W)
		# Retrieve branch of the student from the database.
		branch = cursor.execute('select branch from student where usn=?', (uname,))
		stud_branch_record = branch.fetchall()
		# Label to display course of the student.
		stud_branch = Label(top1, text=stud_branch_record[0],font=('Times New Roman', 20), bg='azure')
		stud_branch.place(relx=0.11, rely=0.43, anchor=W)

		# Year label.
		stud_year_label = Label(top1, text='Year: ', font=('Courier', 20, 'bold'), bg='azure', fg='brown4')
		stud_year_label.place(relx=0.04, rely=0.50, anchor=W)
		# Retrieve year of study of the student from the database.
		year = cursor.execute('select year from student where usn=?', (uname,))
		stud_year_record = year.fetchall()
		# Label to display year of study of the student.
		stud_year = Label(top1, text=stud_year_record[0], font=('Times New Roman', 20), bg='azure')
		stud_year.place(relx=0.11, rely=0.50, anchor=W)

		# Gmail label
		stud_gmail_label = Label(top1, text='Gmail: ', font=('Courier', 20, 'bold'), bg='azure', fg='brown4')
		stud_gmail_label.place(relx=0.04, rely=0.57, anchor=W)
		# Retrieve Gmail of the student from the database.
		gmail = cursor.execute('select gmail from student where usn=?', (uname,))
		stud_gmail_record = gmail.fetchall()
		# Label to display Gmail of the student.
		stud_gmail = Label(top1, text=stud_gmail_record[0], font=('Times New Roman', 20), bg='azure')
		stud_gmail.place(relx=0.11, rely=0.57, anchor=W)

		# Phone label.
		stud_phone_label = Label(top1, text='Phone: ', font=('Courier', 20, 'bold'), bg='azure', fg='brown4')
		stud_phone_label.place(relx=0.04, rely=0.64, anchor=W)
		# Retrieve the phone no. of the student from the database.
		phone = cursor.execute('select phone from student where usn=?', (uname,))
		stud_phone_record = phone.fetchall()
		# Label to display the phone no. of the student.
		stud_phone = Label(top1, text=stud_phone_record[0], font=('Times New Roman', 20), bg='azure')
		stud_phone.place(relx=0.11, rely=0.64, anchor=W)

		# This try block is for the situation when the student has just registered and has not been added by the warden.
		try:
			# Student block number label.
			stud_block_label = Label(top1, text='Block:', font=('Courier', 20, 'bold'), bg='azure', fg='brown4')
			stud_block_label.place(relx=0.04, rely=0.71, anchor=W)
			# Retrieve the block number of the student from the database.
			stud_block_record = cursor.execute('select blocknum from block where studusn=?', (uname,))
			stud_block_record = stud_block_record.fetchall()
			# Label to display the block number of the student.
			stud_block = Label(top1, text=stud_block_record[0], font=('Times New Roman', 20), bg='azure')
			stud_block.place(relx=0.11, rely=0.71, anchor=W)

			# Room number label.
			stud_room_label = Label(top1, text='Room No.: ', font=('Courier', 20, 'bold'), bg='azure', fg='brown4')
			stud_room_label.place(relx=0.04, rely=0.78, anchor=W)
			# Retrieve the room number of the student from the database.
			stud_room_record = cursor.execute('select roomnum from room where studusn=?', (uname,))
			stud_room_record = stud_room_record.fetchall()
			# Label to display the room number of the student.
			stud_room = Label(top1, text=stud_room_record[0], font=('Times New Roman', 20), bg='azure')
			stud_room.place(relx=0.125, rely=0.78, anchor=W)

			# Warden phone no. label.
			warden_ph = Label(top1, text='Contact: ', font=('Courier', 20, 'bold'), bg='azure', fg='brown4')
			warden_ph.place(relx=0.7, rely=0.29, anchor=W)
			# Retrieve the warden details from the datbase.
			one = cursor.execute('select w.name, w.phone, w.gmail, w.post, w.type, w.blocknum from warden w where'
			                     ' w.blocknum=(select b.blocknum from block b where b.studusn=?) and'
			                     ' w.type=(select bl.type from block bl where bl.studusn=?)',
			                     (uname, uname))
			one = one.fetchall()

			# Display details of the warden.
			y = 0.335
			num = 1
			j = 0
			for i in one:
				p = one[j]
				w = str(num) + '. ' + p[3].title() + ', ' + p[4].title() + "' hostel " + str(p[5]) + '\n' + i[0].title() + ' \n ' + str(i[1]) + '\n' + i[2]
				w_name = Label(top1, text=w, font=('Times New Roman', 20), bg='azure')
				w_name.place(relx=0.78, rely=y, anchor=W)
				y += 0.15
				j += 1
				num += 1

			# Roommates label.
			stud_roommates = Label(top1, text='Roomies: ', font=('Courier', 20, 'bold'), bg='azure', fg='brown4')
			stud_roommates.place(relx=0.35, rely=0.29, anchor=W)
			rmates = stud_room_record[0]
			# Retrieve roommates details from the database.
			stud_rmates = cursor.execute('select studusn, studname from room where roomnum=?', (rmates[0],))
			stud_rmates = stud_rmates.fetchall()
			# Display details of roommates.
			y = 0.29
			for roommates in stud_rmates:
				roomies = Label(top1, text=roommates[1] + ' (' + roommates[0] + ')', font=('Times New Roman', 20), bg='azure')
				roomies.place(relx=0.43, rely=y, anchor=W)
				y += 0.05

			# Fee paid label.
			stud_fee_paid_label = Label(top1, text='Fee paid: ', font=('Courier', 20, 'bold'), bg='azure', fg='brown4')
			stud_fee_paid_label.place(relx=0.35, rely=0.57, anchor=W)
			# Retrieve the fee paid details of the student from the database.
			fee_paid_record = cursor.execute('select feepaid from fee where studusn=?', (uname,))
			fee_paid_record = fee_paid_record.fetchall()
			fee_paid_record = fee_paid_record[0]
			# Label to display fee paid by the student.
			fee_paid = Label(top1, text='₹ ' + str(fee_paid_record[0]), font=('Times', 20), bg='azure')
			fee_paid.place(relx=0.43, rely=0.57, anchor=W)

			# Fee balance label.
			stud_fee_balance_label = Label(top1, text='Balance fee: ', font=('Courier', 20, 'bold'), bg='azure', fg='brown4')
			stud_fee_balance_label.place(relx=0.35, rely=0.78, anchor=W)
			# Retrieve balance fee details from the database.
			fee_balance_record = cursor.execute('select feebalance from fee where studusn=?', (uname,))
			fee_balance_record = fee_balance_record.fetchall()
			fee_balance_record = fee_balance_record[0]
			# Label to display balance fee of the student.
			fee_balance = Label(top1, text='₹ ' + str(fee_balance_record[0]), font=('Times', 20), bg='azure')
			fee_balance.place(relx=0.46, rely=0.78, anchor=W)

		except:
			pass

	if uname != '' and pword != '':
		# Check the credentials with the data in the database.
		cursor.execute('select username from login where username=?', (uname, ))
		name = cursor.fetchall()
		# print(name)
		cursor.execute('select password from "login" where "username"=?', (uname,))
		pwd = cursor.fetchall()
		# print(pwd)
		if len(name) != 0 and len(pwd) != 0:
			entry_name = name[0]
			entry_pwd = pwd[0]
			if entry_name[0] == uname and entry_pwd[0] == pword:
				# Login if the student credentials are matched.
				top1 = Toplevel()
				top1.configure(bg='azure')
				top1.resizable(False, False)
				top1.geometry('1850x990')

				# Label frame to display the heading of student login
				stud_frame = LabelFrame(top1, bg='azure')
				stud_frame.place(width=1850, height=100)

				# Label frame to display the refresh and logout buttons.
				mid_frame = LabelFrame(top1, bg='white')
				mid_frame.place(rely=0.105, width=1850, height=90)

				# Label frame to display the student details.
				info_frame = LabelFrame(top1, bg='azure')
				info_frame.place(rely=0.2, width=1850, height=800)

				# Student title.
				title = Label(top1, text='STUDENT PROFILE', font=('Times New Roman', 55, 'bold'), fg='DodgerBlue4', bg='azure')
				title.pack()

				# Student icon.
				stud_icon = Image.open('/home/astronag/student.png')
				stud_icon = stud_icon.resize((50, 50), Image.ANTIALIAS)
				stud_image = ImageTk.PhotoImage(stud_icon)
				stud_img_label = Label(top1, image=stud_image, bg='white')
				img_label.image = stud_image
				stud_img_label.place(relx=0.008, rely=0.15, anchor=W)

				# Logout button for student.
				logout_icon_stud = Image.open('/home/astronag/logout.png')
				logout_icon_stud = logout_icon_stud.resize((45, 45), Image.ANTIALIAS)
				logout_img_stud = ImageTk.PhotoImage(logout_icon_stud)
				logout_btn_stud = Button(top1, image=logout_img_stud, bg='lavender', command=logout)
				logout_btn_stud.place(relx=0.92, rely=0.15, anchor=W)
				logout_btn_stud.image = logout_img_stud
				logout_stud_label = Label(top1, text='Logout', font=('Helvetica', 17), bg='white')
				logout_stud_label.place(relx=0.95, rely=0.15, anchor=W)

				# Edit button for student.
				edit_img = Image.open("/home/astronag/edit.png")
				edit_img = edit_img.resize((30, 30), Image.ANTIALIAS)
				edit_img_1 = ImageTk.PhotoImage(edit_img)
				edit_btn = Button(top1, image=edit_img_1, height=30, width=30, bg='lavender', command=edit)
				edit_btn.place(relx=0.04, rely=0.23, anchor=W)
				edit_btn.image = edit_img_1
				edit_label = Label(top1, text='Edit', font=('Helvetica', 14), bg='azure')
				edit_label.place(relx=0.06, rely=0.23, anchor=W)

				# Refresh button for student.
				refresh_stud_icon = Image.open('/home/astronag/refresh.ico')
				refresh_stud_img = refresh_stud_icon.resize((30, 30), Image.ANTIALIAS)
				refresh_stud_img = ImageTk.PhotoImage(refresh_stud_img)
				refresh_stud_btn = Button(top1, bg='lavender', image=refresh_stud_img, height=30, width=30, command=refresh_stud)
				refresh_stud_btn.place(relx=0.013, rely=0.23, anchor=W)
				refresh_stud_btn.image = refresh_stud_img

				# Display the details of the student.
				display_details()
			else:
				# Set the username and password fields to null if the credentials are not matched.
				setnull()
		else:
			# Display the details of warden.
			wrdn_name = cursor.execute('select name from warden where id=?', (uname, ))
			wrdn_name = wrdn_name.fetchall()
			wrdn_pwd = cursor.execute('select password from warden where id=?', (uname, ))
			wrdn_pwd = wrdn_pwd.fetchall()
			if len(wrdn_name) != 0 and len(wrdn_pwd) != 0:
				wrdn_id, wrdn_pass = wrdn_name[0], wrdn_pwd[0]
				if wrdn_pass[0] == pword:
					top2 = Toplevel()
					top2.configure(bg='azure')
					top2.resizable(False, False)
					top2.geometry('1850x990')

					title_frame = LabelFrame(top2, bg='azure')
					title_frame.place(width=1850, height=100)

					mid_frame_wrdn = LabelFrame(top2, bg='white')
					mid_frame_wrdn.place(rely=0.105, width=1850, height=100)

					title = Label(top2, text='WARDEN PROFILE', font=('Times New Roman', 55, 'bold'), fg='DodgerBlue4', bg='azure')
					title.pack()
					wrdn_icon = Image.open('/home/astronag/warden.png')
					wrdn_icon = wrdn_icon.resize((50, 50), Image.ANTIALIAS)
					wrdn_img = ImageTk.PhotoImage(wrdn_icon)
					wrdn_img_btn = Button(top2, image=wrdn_img, bg='white', command=show_wrdn_info)
					wrdn_img_btn.image = wrdn_img
					wrdn_img_btn.place(relx=0.008, rely=0.15, anchor=W)
					display_warden_info()
				else:
					setnull()
			else:
				setnull()
	else:
		setnull()


	def edit():

		# Toplevel window to edit details of the student.
		edit_top = Toplevel()
		edit_top.geometry('1500x900')
		edit_top.resizable(False, False)
		edit_top.config(bg='mint cream')

		# Label frame for the top portion of the window.
		edit_title_frame = LabelFrame(edit_top, bg='mint cream')
		edit_title_frame.place(relx=0, rely=0, anchor=W, width=1500, height=170)

		# Edit information title.
		edit_title = Label(edit_top, text='EDIT INFORMATION', bg='mint cream', font=('Times New Roman', 45, 'bold'), fg='DodgerBlue4')
		edit_title.pack()

		# Label frame for the middle of the window.
		frame = LabelFrame(edit_top, bg='white')
		frame.place(relx=0, rely=0.43, anchor=W, width=1500, height=600)

		# Label frame for the rest of the window.
		down_frame = LabelFrame(edit_top, bg='mint cream')
		down_frame.place(relx=0, rely=0.883, anchor=W, width=1500, height=210)

		# Function to cancel the edit of the student.
		def cancel_edit():
			edit_top.destroy()

		# Function that checks for all the valid inputs and updates the database with the new values given.
		def submit_edit():

			# TRIGGER TO UPDATE STUDENT INFO
			# cursor.execute('create trigger update_stud_room_info after update on student begin update room set studname=New.name where studusn=New.usn; end;')
			# cursor.execute('create trigger update_stud_block_info after update on student begin update block set studname=New.name where studusn=New.usn; end;')
			# cursor.execute('create trigger update_stud_fee_info after update on student begin update fee set studname=New.name where studusn=New.usn; end;')

			# Check whether none of the fields are left empty.
			if stud_name.get() != '' and gmail.get() != '' and gender.get() != '' and phone.get() != '' and parent_name.get() != '' \
					and parent_gmail.get() != '' and parent_phone.get() != '' and address_entry.get("1.0", 'end-1c') != '' and dob.get() != '':

				# Check whether both passwords match.
				if login_password.get() == confirm_password.get():

					# Check whether the Phone No. is valid i.e., 10 digits.
					if len(parent_phone.get()) == 10 and len(phone.get()) == 10 and parent_phone.get() != phone.get():

						# If the password is not changed then update the modified fields.
						if login_password.get() == '':
							cursor.execute('update student set name=?, gmail=?, course=?, branch=?, phone=?,year=?, '
							               'gender=?, parentname=?, parentphone=?,parentgmail=?, dob=?, address=? where usn=?',
							               (stud_name.get(), gmail.get(), option.get(), option1.get(),
							                phone.get(), option_year.get(), gender.get(), parent_name.get(),
							                parent_phone.get(), parent_gmail.get(), dob.get(), address_entry.get("1.0",
							                                                                                     'end-1c'), uname))
							conn.commit()
							messagebox.showinfo('INFORMATION', 'Successfully updated')
							edit_top.destroy()
							# display_details()

						else:
							# If the password is changed then update the modified fields.
							cursor.execute('update student set name=?, gmail=?, course=?, branch=?, phone=?,year=?, '
							               'gender=?, parentname=?, parentphone=?,parentgmail=?, dob=?, address=? where usn=?',
							               (stud_name.get(), gmail.get(), option.get(), option1.get(),
							                phone.get(), option_year.get(), gender.get(), parent_name.get(),
							                parent_phone.get(), parent_gmail.get(), dob.get(), address_entry.get("1.0",
							                                                                                     'end-1c'),
							                uname))
							cursor.execute('update login set password=? where username=?', (login_password.get(), uname))
							conn.commit()
							messagebox.showinfo('INFORMATION', 'Successfully updated')
							edit_top.destroy()
							# display_details()

					else:
						# Issue a warning if the Phone No. is invalid.
						messagebox.showwarning('WARNING', 'Invalid Phone No. !!!')

				else:
					# Issue a warning if the passwords does not match.
					messagebox.showwarning('WARNING', 'Passwords should be the same !!!')

			else:
				# Issue a warning if any of the fields are left empty.
				messagebox.showwarning('WARNING', 'Some of the required field(s) are left empty !!!')

		# Text variables for the input during edit.
		stud_name = StringVar()
		option = StringVar()
		option1 = StringVar()
		option_year = StringVar()
		gmail = StringVar()
		gender = StringVar()
		dob = StringVar()
		phone = StringVar()
		parent_name = StringVar()
		parent_phone = StringVar()
		parent_gmail = StringVar()
		login_password = StringVar()
		confirm_password = StringVar()
		inst = StringVar()

		instruct = Label(edit_top, text='', font=('Courier', 13), bg='azure', fg='OrangeRed3', textvariable=inst)
		instruct.place(relx=0.37, rely=0.83, anchor=W)

		# Retrieve the student USN from the database.
		values = cursor.execute('select * from student where usn=?', (uname,))
		values = values.fetchall()
		values = values[0]
		# print(values)

		# Name label in edit window.
		name_label = Label(edit_top, text='Name', font=('Courier', 16), bg='white')
		name_label.place(relx=0.1, rely=0.15, anchor=W)

		# Entry box for name edit. It is set with the previous value given.
		name_entry = Entry(edit_top, textvariable=stud_name, font=('Times', 14))
		stud_name.set(values[0])
		name_entry.place(relx=0.18, rely=0.15, anchor=W, width=250)

		# USN label in edit window.
		usn_label = Label(edit_top, text='USN', font=('Courier', 16), bg='white')
		usn_label.place(relx=0.1, rely=0.22, anchor=W)

		# Label displaying the USN of the student which cannot be edited.
		usn_entry = Label(edit_top, text=values[1], bg='white', font=('Times', 18, 'bold'))
		usn_entry.place(relx=0.18, rely=0.22, anchor=W)

		# Course label in edit window.
		course_label = Label(edit_top, text='Course', font=('Courier', 16), bg='white')
		course_label.place(relx=0.1, rely=0.29, anchor=W)
		OPTIONS = ["UG"]

		# Dropdown list for course in edit window.
		course_drop_down = OptionMenu(edit_top, option, *OPTIONS)
		option.set(values[3])
		course_drop_down.place(relx=0.18, rely=0.29, anchor=W)

		# Branch label in edit window.
		branch_label = Label(edit_top, text='Branch', font=('Courier', 16), bg='white')
		branch_label.place(relx=0.1, rely=0.36, anchor=W)
		BRANCH_OPTIOINS = ['CSE', 'ECE', 'EEE', 'ME', 'CV', 'AE', 'ISE']

		# Dropdown list for branch in edit window.
		branch_drop_down = OptionMenu(edit_top, option1, *BRANCH_OPTIOINS)
		option1.set(values[4])
		branch_drop_down.place(relx=0.18, rely=0.36, anchor=W)

		# Year label in edit windwow.
		year_label = Label(edit_top, text='Year', font=('Courier', 16), bg='white')
		year_label.place(relx=0.1, rely=0.43, anchor=W)
		YEAR_OPTIONS = ['1st', '2nd', '3rd', '4th']

		# Dropdown list for year  in edit window.
		year_drop_down = OptionMenu(edit_top, option_year, *YEAR_OPTIONS)
		option_year.set(values[6])
		year_drop_down.place(relx=0.18, rely=0.43, anchor=W)

		# Gmail label in edit window.
		gmail_label = Label(edit_top, text='Gmail', font=('Courier', 16), bg='white')
		gmail_label.place(relx=0.1, rely=0.5, anchor=W)

		# Gmail entry box with the previous value given.
		gmail_entry = Entry(edit_top, textvariable=gmail, font=('Times', 14))
		gmail.set(values[2])
		gmail_entry.place(relx=0.18, rely=0.5, anchor=W, width=250)

		# Gnder label in edit window.
		gender_label = Label(edit_top, text='Gender', font=('Courier', 16), bg='white')
		gender_label.place(relx=0.1, rely=0.57, anchor=W)

		# Male radio button in edit window.
		male_rbtn = Radiobutton(edit_top, text='Male', font=('Courier', 14), variable=gender, value='male', bg='white')
		male_rbtn.place(relx=0.18, rely=0.57, anchor=W)

		# Female radio button in edit window.
		female_rbtn = Radiobutton(edit_top, text='Female', font=('Courier', 14), variable=gender, value='female', bg='white')
		female_rbtn.place(relx=0.239, rely=0.57, anchor=W)

		# Others radio button in edit window.
		other_rbtn = Radiobutton(edit_top, text='Other', font=('Courier', 14), variable=gender, value='other', bg='white')
		other_rbtn.place(relx=0.313, rely=0.57, anchor=W)
		gender.set(values[7])

		# DOB label in edit window.
		dob_label = Label(edit_top, text='DOB', font=('Courier', 16), bg='white')
		dob_label.place(relx=0.1, rely=0.64, anchor=W)

		# DOB entry in edit window
		dob_entry = Entry(edit_top, textvariable=dob, font=('Times', 14))
		dob_entry.place(relx=0.18, rely=0.64, anchor=W, width=250)
		dob.set(values[11])

		# Phone label in edit window.
		phone_label = Label(edit_top, text='Phone', font=('Courier', 16), bg='white')
		phone_label.place(relx=0.66, rely=0.15, anchor=W)

		# Phone entry box in entry window.
		phone_entry = Entry(edit_top, textvariable=phone, font=('Times', 14))
		phone_entry.place(relx=0.81, rely=0.15, anchor=W, width=250)
		phone.set(values[5])

		# Parent name label in edit window.
		parent_name_label = Label(edit_top, text='Parent name', font=('Courier', 16), bg='white')
		parent_name_label.place(relx=0.66, rely=0.22, anchor=W)

		# Parent entry box in edit window.
		parent_name_entry = Entry(edit_top, textvariable=parent_name, font=('Times', 14))
		parent_name_entry.place(relx=0.81, rely=0.22, anchor=W, width=250)
		parent_name.set(values[8])

		# Parent phone label in edit window.
		parent_phone_label = Label(edit_top, text="Parent's phone", font=('Courier', 16), bg='white')
		parent_phone_label.place(relx=0.66, rely=0.29, anchor=W)

		# Parent phone entry box in edit window.
		parent_phone_entry = Entry(edit_top, textvariable=parent_phone, font=('Times', 14))
		parent_phone_entry.place(relx=0.81, rely=0.29, anchor=W, width=250)
		parent_phone.set(values[9])

		# Parent Gmail label in edit window.
		parent_gmail_label = Label(edit_top, text="Parent's Gmail", font=('Courier', 16), bg='white')
		parent_gmail_label.place(relx=0.66, rely=0.36, anchor=W)

		# Parent Gmail entry box in edit window.
		parent_gmail_entry = Entry(edit_top, textvariable=parent_gmail, font=('Times', 14))
		parent_gmail_entry.place(relx=0.81, rely=0.36, anchor=W, width=250)
		parent_gmail.set(values[10])

		# Address label in edit window.
		address_label = Label(edit_top, text='Address', font=('Courier', 16), bg='white')
		address_label.place(relx=0.66, rely=0.43, anchor=W)

		# Address entry box in edit window.
		address_entry = Text(edit_top, width=27, height=6, font=('Times', 14))
		address_entry.place(relx=0.81, rely=0.465, anchor=W)
		address_entry.insert("1.0", values[12])

		# Password label in edit window.
		password_label = Label(edit_top, text='New Password', font=('Courier', 16), bg='white')
		password_label.place(relx=0.66, rely=0.57, anchor=W)

		# Password entry box in edit window.
		password_entry = Entry(edit_top, show='*', textvariable=login_password, font=('Times', 14))
		password_entry.place(relx=0.81, rely=0.57, anchor=W, width=250)

		# Confirm password label in edit window.
		confirm_password_label = Label(edit_top, text='Confirm password', font=('Courier', 16), bg='white')
		confirm_password_label.place(relx=0.66, rely=0.64, anchor=W)

		# Confirm password entry box in edit window.
		confirm_password_entry = Entry(edit_top, show='*', textvariable=confirm_password, font=('Times', 14))
		confirm_password_entry.place(relx=0.81, rely=0.64, anchor=W, width=250)

		# Submit button in edit window.
		submit_edit_btn = Button(edit_top, text='SUBMIT', bg='lavender', command=submit_edit)
		submit_edit_btn.place(relx=0.42, rely=0.9, anchor=W)

		# Cancel button in edit window.
		cancel_edit_btn = Button(edit_top, text='CANCEL', bg='lavender', command=cancel_edit)
		cancel_edit_btn.place(relx=0.53, rely=0.9, anchor=W)
		

def cancel():
	top.destroy()
	root.destroy()
	sys.exit()


def register_new():
	stud_usn = StringVar()
	option = StringVar()
	option1 = StringVar()
	option_year = StringVar()
	gmail = StringVar()
	gender = StringVar()
	dob = StringVar()
	phone = StringVar()
	parent_name = StringVar()
	parent_phone = StringVar()
	parent_gmail = StringVar()
	login_password = StringVar()
	confirm_password = StringVar()
	inst = StringVar()

	def get_name():
		name_label = Label(new_user, text='Name', font=('Courier', 16), bg='azure')
		name_label.place(relx=0.1, rely=0.15, anchor=W)
		name_entry = Entry(new_user, textvariable=stud_name, font=('Times', 14))
		name_entry.place(relx=0.16, rely=0.15, anchor=W, width=250)

	def get_USN():
		usn_label = Label(new_user, text='USN', font=('Courier', 16), bg='azure')
		usn_label .place(relx=0.1, rely=0.22, anchor=W)
		usn_entry = Entry(new_user, textvariable=stud_usn, font=('Times', 14))
		usn_entry.place(relx=0.16, rely=0.22, anchor=W, width=250)

	def get_course():
		course_label = Label(new_user, text='Course', font=('Courier', 16), bg='azure')
		course_label.place(relx=0.1, rely=0.29, anchor=W)
		OPTIONS = ["UG"]
		course_drop_down = OptionMenu(new_user, option, *OPTIONS)
		course_drop_down.place(relx=0.16, rely=0.29, anchor=W)

		branch_label = Label(new_user, text='Branch', font=('Courier', 16), bg='azure')
		branch_label.place(relx=0.1, rely=0.36, anchor=W)
		BRANCH_OPTIOINS = ['CSE', 'ECE', 'EEE', 'ME', 'CV', 'AE', 'ISE']
		branch_drop_down = OptionMenu(new_user, option1, *BRANCH_OPTIOINS)
		branch_drop_down.place(relx=0.16, rely=0.36, anchor=W)

	def get_study_year():
		year_label = Label(new_user, text='Year', font=('Courier', 16), bg='azure')
		year_label.place(relx=0.1, rely=0.43, anchor=W)
		YEAR_OPTIONS = ['1st', '2nd', '3rd', '4th']
		year_drop_down = OptionMenu(new_user, option_year, *YEAR_OPTIONS)
		year_drop_down.place(relx=0.16, rely=0.43, anchor=W)

	def get_gmail():
		gmail_label = Label(new_user, text='Gmail', font=('Courier', 16), bg='azure')
		gmail_label.place(relx=0.1, rely=0.5, anchor=W)
		gmail_entry = Entry(new_user, textvariable=gmail, font=('Times', 14))
		gmail_entry.place(relx=0.16, rely=0.5, anchor=W, width=250)

	def get_gender():
		gender_label = Label(new_user, text='Gender', font=('Courier', 16), bg='azure')
		gender_label.place(relx=0.1, rely=0.57, anchor=W)
		male_rbtn = Radiobutton(new_user, text='Male', font=('Courier', 14), variable=gender, value='male', bg='azure')
		male_rbtn.place(relx=0.16, rely=0.57, anchor=W)
		female_rbtn = Radiobutton(new_user, text='Female', font=('Courier', 14), variable=gender, value='female', bg='azure')
		female_rbtn.place(relx=0.209, rely=0.57, anchor=W)
		other_rbtn = Radiobutton(new_user, text='Other', font=('Courier', 14), variable=gender, value='other', bg='azure')
		other_rbtn.place(relx=0.27, rely=0.57, anchor=W)

	def get_dob():
		dob_label = Label(new_user, text='DOB', font=('Courier', 16), bg='azure')
		dob_label.place(relx=0.1, rely=0.64, anchor=W)
		dob_entry = Entry(new_user, textvariable=dob, font=('Times', 14))
		dob_entry.place(relx=0.16, rely=0.64, anchor=W, width=250)

	def get_phone():
		phone_label = Label(new_user, text='Phone', font=('Courier', 16), bg='azure')
		phone_label.place(relx=0.68, rely=0.15, anchor=W)
		phone_entry = Entry(new_user, textvariable=phone, font=('Times', 14))
		phone_entry.place(relx=0.81, rely=0.15, anchor=W, width=250)

	def get_parent_name():
		parent_name_label = Label(new_user, text='Parent name', font=('Courier', 16), bg='azure')
		parent_name_label.place(relx=0.68, rely=0.22, anchor=W)
		parent_name_entry = Entry(new_user, textvariable=parent_name, font=('Times', 14))
		parent_name_entry.place(relx=0.81, rely=0.22, anchor=W, width=250)

	def get_parent_phone():
		parent_phone_label = Label(new_user, text="Parent's phone", font=('Courier', 16), bg='azure')
		parent_phone_label.place(relx=0.68, rely=0.29, anchor=W)
		parent_phone_entry = Entry(new_user, textvariable=parent_phone, font=('Times', 14))
		parent_phone_entry.place(relx=0.81, rely=0.29, anchor=W, width=250)

	def get_parent_gmail():
		parent_gmail_label = Label(new_user, text="Parent's Gmail", font=('Courier', 16), bg='azure')
		parent_gmail_label.place(relx=0.68, rely=0.36, anchor=W)
		parent_gmail_entry = Entry(new_user, textvariable=parent_gmail, font=('Times', 14))
		parent_gmail_entry.place(relx=0.81, rely=0.36, anchor=W, width=250)

	def get_password():
		password_label = Label(new_user, text='Password', font=('Courier', 16), bg='azure')
		password_label.place(relx=0.68, rely=0.57, anchor=W)
		password_entry = Entry(new_user, show='*', textvariable=login_password, font=('Times', 14))
		password_entry.place(relx=0.81, rely=0.57, anchor=W, width=250)

		confirm_password_label = Label(new_user, text='Confirm password', font=('Courier', 16), bg='azure')
		confirm_password_label.place(relx=0.68, rely=0.64, anchor=W)
		confirm_password_entry = Entry(new_user, show='*', textvariable=confirm_password, font=('Times', 14))
		confirm_password_entry.place(relx=0.81, rely=0.64, anchor=W, width=250)

	def register_cancel():
		new_user.destroy()

	def register_submit():
		if stud_name.get() != '' and stud_usn.get() != '' and option.get != '' and option1.get() != '' and \
				option_year.get() != '' and gmail.get() != '' and gender.get() != '' and phone.get() != '' and \
				parent_name.get() != '' and parent_gmail.get() != '' and parent_phone.get() != '' and \
				address_entry.get("1.0", 'end-1c') != '' and login_password.get() != '' and \
				confirm_password.get() != '' and dob.get() != '':
			if login_password.get() == confirm_password.get():
				if len(parent_phone.get()) == 10 and len(phone.get()) == 10 and parent_phone.get() != phone.get():
					cursor.execute('select * from student where usn=?', (stud_usn.get(), ))
					is_already = cursor.fetchall()
					if len(is_already) == 0:
						cursor.execute('insert into student values(?,?,?,?,?,?,?,?,?,?,?,?,?)', (stud_name.get(), stud_usn.get(), gmail.get(), option.get(), option1.get(), phone.get(), option_year.get(), gender.get(), parent_name.get(), parent_phone.get(), parent_gmail.get(), dob.get(), address_entry.get("1.0", 'end-1c')))
						cursor.execute('insert into login values(?,?)', (stud_usn.get(), login_password.get()))
						conn.commit()
						messagebox.showinfo('INFORMATION', 'Successfully Registered')
						new_user.destroy()
						# cursor.execute('create trigger room_insert after insert on student begin insert into fee(studusn, studname) values(New.usn, New.name); end;')
					else:
						inst.set(f'Student with USN {stud_usn.get()} has already registered !!!')
				else:
					messagebox.showwarning('WARNING', 'Invalid Phone No. !!!')
			else:
				messagebox.showwarning('WARNING', 'Passwords should be the same !!!')
		else:
			messagebox.showwarning('WARNING', 'Some of the required field(s) are left empty !!!')

	stud_name = StringVar()
	new_user = Toplevel(root)
	new_user.resizable(False, False)
	new_user.geometry('1850x990')
	new_user.title('Register')
	new_user.configure(background='azure')
	register_frame = LabelFrame(new_user, bg='azure')
	register_frame.place(width=1850, height=90)
	info_frame = LabelFrame(new_user, bg='azure')
	info_frame.place(rely=0.093, width=1850, height=900)
	head = Label(new_user, text='STUDENT INFORMATION', font=('Times New Roman', 35, 'bold'), bg='azure', fg='DodgerBlue4')
	head.place(relx=0.5, rely=0.04, anchor=CENTER)
	get_name()
	get_USN()
	get_course()
	get_study_year()
	get_gmail()
	get_gender()
	get_dob()
	get_phone()
	get_parent_name()
	get_parent_phone()
	get_parent_gmail()

	address_label = Label(new_user, text='Address', font=('Courier', 16), bg='azure')
	address_label.place(relx=0.68, rely=0.43, anchor=W)
	address_entry = Text(new_user, width=27, height=6, font=('Times', 14))
	address_entry.place(relx=0.81, rely=0.465, anchor=W)

	get_password()

	note = Label(new_user, text='Note:', bg='azure', fg='red', font=('Courier', 15))
	note.place(relx=0.1, rely=0.73, anchor=W)
	must_note = Label(new_user, text='1. Every field is required. None should be left blank.', bg='azure', font=('Courier', 11))
	must_note.place(relx=0.13, rely=0.76, anchor=W)
	usn_note = Label(new_user, text='2. USN will be your USERNAME.', bg='azure', font=('Courier', 11))
	usn_note.place(relx=0.13, rely=0.78, anchor=W)
	dob_note = Label(new_user, text='3. DOB should be given in DD-MMM-YYYY format.', bg='azure', font=('Courier', 11))
	dob_note.place(relx=0.13, rely=0.8, anchor=W)
	submit = Button(new_user, text='SUBMIT',  command=lambda: register_submit(), bg='light steel blue')
	submit.place(relx=0.43, rely=0.9, anchor=W)
	# instruct = Label(new_user, text='', font=('Courier', 13), bg='azure', fg='OrangeRed3', textvariable=inst)
	# instruct.place(relx=0.37, rely=0.83, anchor=W)
	cancel_register = Button(new_user, text='CANCEL', command=lambda: register_cancel(), bg='light steel blue')
	cancel_register.place(relx=0.51, rely=0.9, anchor=W)


if __name__ == '__main__':
	root = Tk()
	root.resizable(False, False)
	top = Toplevel()
	top.resizable(False, False)
	top.geometry('1850x990')
	top.title('LOGIN')
	top.configure(background='light cyan')

	user = StringVar()
	pwod = StringVar()
	inv = StringVar()
	img = Image.open('hostel.jpg')
	img = img.crop((100, 0, 1090, 720))
	image = ImageTk.PhotoImage(img)
	img_label = Label(top, image=image)
	img_label.image = image
	img_label.place(relx=0.56, rely=0.5, anchor=CENTER)
	heading = Label(top, text='HOSTEL MANAGEMENT SYSTEM', font=('Times New Roman', 55, 'bold'), fg='DodgerBlue4', bg='light cyan')
	heading.place(relx=0.49, rely=0.05, anchor=CENTER)
	label_one = Label(top, text='Username', font=('Helvetica', 15), bg='light cyan')
	entry_one = Entry(top, textvariable=user, font=('Times', 14))
	username = entry_one.get()
	label_two = Label(top, text='Password', font=('Helvetica', 15), bg='light cyan')
	entry_two = Entry(top, show='*', textvariable=pwod, font=('Times', 14))
	password = entry_two.get()
	login_btn = Button(top, text='LOGIN', command=lambda: login(entry_one.get(), entry_two.get()), bg='light steel blue')
	cancel_btn = Button(top, text='CANCEL', command=lambda: cancel(), bg='light steel blue')
	register = Label(top, text='New user?', font=('Helvetica', 13), bg='light cyan')
	reg_btn = Button(top, text='Register', command=lambda: register_new(), bg='lavender')
	label_one.place(relx=0.14, rely=0.337, anchor=NE)
	entry_one.place(relx=0.2, rely=0.35, anchor=CENTER)
	label_two.place(relx=0.1135, rely=0.41, anchor=CENTER)
	entry_two.place(relx=0.2, rely=0.41, anchor=CENTER)
	login_btn.place(relx=0.173, rely=0.5, anchor=CENTER)
	cancel_btn.place(relx=0.225, rely=0.5, anchor=CENTER)
	register.place(relx=0.9, rely=.15, anchor=CENTER)
	reg_btn.place(relx=0.95, rely=.15, anchor=CENTER)
	root.title('Hostel Management System')
	root.configure(background='alice blue')
	root.geometry('855x654')
	root.withdraw()
	root.mainloop()
	conn.close()