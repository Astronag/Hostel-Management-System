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

	# Function for refreshing the details of the student after the data has been modified.
	def refresh_stud():
		display_details()

	# Function for refreshing the details of the warden after the data has been modified.
	def refresh_wdn():
		display_warden_info()

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
			# Function to display the details of warden.
			def display_warden_info():
				# Style configuration for treeview.
				style = ttk.Style()
				# Gap between the rows.
				style.configure('mystyle.Treeview', rowheight=40)
				# Heading configuration.
				style.configure("mystyle.Treeview.Heading", font=('Times', 18, 'bold'), background='#800080', foreground='#FFFFFF')
				# Rows of data configuration.
				style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Times', 16), background='#F0F8FF')
				# To remove the border.
				style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])

				# StringVar for some entry boxes.
				usn = StringVar()
				stud_block = StringVar()
				block_type = StringVar()
				room_num = StringVar()
				fee_paid = StringVar()

				warden_record = cursor.execute('select name from warden where id=?', (uname,))
				warden_record = warden_record.fetchall()
				warden_name = warden_record[0]

				empty_label = Label(top2, bg='white', fg='white', width=60, height=5)
				empty_label.place(relx=0.04, rely=0.15, anchor=W)

				wrdn_name_label = Label(top2, text=warden_name[0].title(), font=('Helvetica', 27), bg='white', fg='gray1')
				wrdn_name_label.place(relx=0.04, rely=0.15, anchor=W)

				labelframe = LabelFrame(top2, bg='azure')
				labelframe.place(relx=0.299, rely=0.15, anchor=W, width=734, height=46)

				home_label_frame = LabelFrame(top2, bg='azure')
				home_label_frame.place(rely=0.21, width=1850, height=780)

				add_stud_btn = Button(home_label_frame, text='ADD STUDENT', font=('Helvetica', 20), bg='purple', fg='white', command=add_student)
				add_stud_btn.place(relx=0.35, rely=0.5, anchor=W)

				delete_stud_btn = Button(home_label_frame, text='DELETE STUDENT', font=('Helvetica', 20), bg='purple', fg='white', command=delete_student)
				delete_stud_btn.place(relx=0.5, rely=0.5, anchor=W)

				fee_btn = Button(labelframe, text='Fee details', font=('Helvetica', 20),  fg='white', bg='SpringGreen3', command=display_fee_details)
				fee_btn.place(rely=0.49, anchor=W)

				block_btn = Button(labelframe, text='Block details', font=('Helvetica', 20),  fg='white', bg='SpringGreen3', command=display_block_details)
				block_btn.place(relx=0.219, rely=0.49, anchor=W)

				room_btn = Button(labelframe, text='Room details', font=('Helvetica', 20),  fg='white', bg='SpringGreen3', command=display_room_details)
				room_btn.place(relx=0.465, rely=0.49, anchor=W)

				wrdn_btn = Button(labelframe, text='Warden details', font=('Helvetica', 20),  fg='white', bg='SpringGreen3', command=display_warden_details)
				wrdn_btn.place(relx=0.718, rely=0.49, anchor=W)

				home_icon = Image.open('/home/astronag/home.png')
				home_icon = home_icon.resize((45, 46), Image.ANTIALIAS)
				home_img = ImageTk.PhotoImage(home_icon)
				home_btn = Button(top2, image=home_img, bg='white', font=('Courier', 17), command=home_wrdn)
				home_btn.place(relx=0.88, rely=0.15, anchor=W)
				home_btn.image = home_img

				logout_icon = Image.open('/home/astronag/logout.png')
				logout_icon = logout_icon.resize((45, 45), Image.ANTIALIAS)
				logout_img = ImageTk.PhotoImage(logout_icon)
				logout_btn = Button(top2, image=logout_img, bg='lavender', font=('Courier', 17), command=logout_wrdn)
				logout_btn.place(relx=0.92, rely=0.15, anchor=W)
				logout_btn.image = logout_img
				logout_label = Label(top2, text="Logout", font=('Helvetica', 17), bg='white')
				logout_label.place(relx=0.95, rely=0.15, anchor=W)

				refresh_wdn_icon = Image.open('/home/astronag/refresh.ico')
				refresh_wdn_img = refresh_wdn_icon.resize((45, 46), Image.ANTIALIAS)
				refresh_wdn_img = ImageTk.PhotoImage(refresh_wdn_img)
				refresh_wdn_btn = Button(mid_frame_wrdn, bg='white', image=refresh_wdn_img, command=refresh_wdn)
				refresh_wdn_btn.place(relx=0.84, rely=0.45, anchor=W)
				refresh_wdn_btn.image = refresh_wdn_img

				def display_fee_details():

					def change_fee():

						new_fee = StringVar()

						def cancel_ch_fee():
							fee_top.destroy()

						def submit_ch_fee():
							if new_fee.get() != '':
								cursor.execute('update fee set totalfee=?', (new_fee.get(),))
								cursor.execute('update fee set feebalance=(totalfee-feepaid)')
								conn.commit()
								messagebox.showinfo('INFORMATION', 'Fee updated.')
								fee_top.destroy()
								display_fee_details()
							else:
								messagebox.showwarning('WARNING', 'Enter the new fee.')

						fee_top = Toplevel()
						fee_top.geometry('500x350+730+400')
						fee_top.resizable(False, False)
						fee_top.configure(bg='linen')

						change_fee_title = Label(fee_top, text='CHANGE FEE', font=('Times', 25, 'bold'), bg='linen', fg='DodgerBlue4')
						change_fee_title.pack()

						cur_fee_label = Label(fee_top, text='Current Fee', bg='linen', fg='brown4', font=('Courier', 17, 'bold'))
						cur_fee_label.place(relx=0.22, rely=0.3, anchor=W)

						cur_fee_record = cursor.execute('select distinct totalfee from fee')
						cur_fee_record = cur_fee_record.fetchall()
						cur_fee = Label(fee_top, text='₹ ' + str(cur_fee_record[0][0]), font=('Times', 17), bg='linen')
						cur_fee.place(relx=0.6, rely=0.3, anchor=W)

						new_fee_label = Label(fee_top, text='New Fee', bg='linen', fg='brown4', font=('Courier', 17, 'bold'))
						new_fee_label.place(relx=0.22, rely=0.55, anchor=W)

						new_fee_entry = Entry(fee_top, textvariable=new_fee, width=17)
						new_fee_entry.place(relx=0.6, rely=0.55, anchor=W)

						submit_ch_fee_btn = Button(fee_top, text='SUBMIT', font=('Courier', 11), bg='light steel blue', command=submit_ch_fee)
						submit_ch_fee_btn.place(relx=0.3, rely=0.85, anchor=W)

						cancel_ch_fee_btn = Button(fee_top, text='CANCEL', font=('Courier', 11), bg='light steel blue', command=cancel_ch_fee)
						cancel_ch_fee_btn.place(relx=0.55, rely=0.85, anchor=W)


					fee_frame = LabelFrame(top2, width=1850, height=780, bg='azure')
					fee_frame.place(rely=0.605, anchor=W)
					cols = ('USN', 'Name', 'Branch', 'Year', 'Room No.', 'Fee paid', 'Fee balance')
					listbox = ttk.Treeview(fee_frame, columns=cols, show='headings', style='mystyle.Treeview')
					for col in cols:
						listbox.heading(col, text=col)
					listbox.place(rely=0.5, anchor=W, width=1850, height=780)
					fee_list = cursor.execute('select s.usn, s.name, s.branch, s.year, r.roomnum, f.feepaid, f.feebalance '
					                          'from student s, fee f, room r where f.studusn=s.usn and '
					                          'r.studusn=s.usn order by feebalance desc')
					fee_list = fee_list.fetchall()
					for i in fee_list:
						listbox.insert('', 'end', values=(i[0], i[1], i[2], i[3], i[4], '₹ ' + str(i[5]), '₹ ' + str(i[6])))

					scroll = Scrollbar(listbox, orient='vertical', command=listbox.yview, width=15)
					scroll.pack(side=RIGHT, fill='y')

					listbox.configure(yscrollcommand=scroll.set)

					change_fee_btn = Button(fee_frame, text='CHANGE FEE', bg='salmon4', fg='white', font=('Courier', 15), command=change_fee)
					change_fee_btn.place(relx=0.45, rely=0.93, anchor=W)

				def display_block_details():
					block_frame = LabelFrame(top2, width=1850, height=780, bg='azure')
					block_frame.place(rely=0.605, anchor=W)
					cols = ('Block No.', 'Room No.', 'Room type', 'Vacancies', 'Block type', 'Warden')
					listbox = ttk.Treeview(block_frame, columns=cols, show='headings', style='mystyle.Treeview')

					for col in cols:
						listbox.heading(col, text=col)

					listbox.place(rely=0.5, anchor=W, width=1850, height=780)
					display = cursor.execute(
						'select distinct r.roomnum, r.roomtype, r.blocknum, r.blocktype, b.wardenname '
						'from room r, block b, warden w where b.blocknum=r.blocknum and b.type=r.blocktype order by r.blocknum')
					roomlist = display.fetchall()
					roomlist.sort(key=lambda e: e[0])
					
					for i in roomlist:
						vacancies = cursor.execute('select count(*) from room where roomnum=? and blocknum=?', (i[0], i[2]))
						vacancies = vacancies.fetchall()
						vacancies = vacancies[0]
						listbox.insert('', 'end', values=(i[2], i[0], i[1], 4-vacancies[0], i[3].title(), i[4].title()))

					scroll = Scrollbar(listbox, orient='vertical', command=listbox.yview, width=15)
					scroll.pack(side=RIGHT, fill='y')

					listbox.configure(yscrollcommand=scroll.set)

				def display_room_details():
					ch_usn = StringVar()
					ch_new_block = StringVar()
					ch_new_room = StringVar()

					def change_room():
						def ch_room_next():
							def cancel_ch():
								ch_room_info.destroy()

							def submit_ch():
								if ch_new_block.get() != '' and ch_new_room.get() != '':
									cursor.execute('update room set roomnum=?, blocknum=? where studusn=?', (ch_new_room.get(), ch_new_block.get(), ch_usn.get()))
									cursor.execute('update block set blocknum=? where studusn=?', (ch_new_block.get(), ch_usn.get()))
									conn.commit()
									messagebox.showinfo('INFORMATION', 'Successfully updated.')
									ch_room_info.destroy()
									display_room_details()
								else:
									messagebox.showwarning('WARNING', 'Some of the required fields are empty.')

							if ch_usn.get() != '':
								is_present = cursor.execute('select * from room where studusn=?', (ch_usn.get(),))
								is_present = is_present.fetchall()
								if len(is_present) != 0:
									ch_room.destroy()
									ch_room_info = Toplevel()
									ch_room_info.geometry('600x500+690+297')
									ch_room_info.configure(bg='linen')
									ch_room_info.resizable(False, False)

									ch_room_title = Label(ch_room_info, text='CHANGE ROOM', font=('Times', 25, 'bold'), bg='linen', fg='DodgerBlue4')
									ch_room_title.pack()

									ch_stud_name_label = Label(ch_room_info, text='Name', font=('Courier', 16, 'bold'), bg='linen', fg='brown4')
									ch_stud_name_label.place(relx=0.2, rely=0.2, anchor=W)

									ch_name_record = cursor.execute('select studname from room where studusn=?', (ch_usn.get(),))
									ch_name_record = ch_name_record.fetchall()
									ch_stud_name = Label(ch_room_info, text=ch_name_record[0][0].title(), font=('Times', 18), bg='linen')
									ch_stud_name.place(relx=0.57, rely=0.2, anchor=W)

									ch_stud_usn_label = Label(ch_room_info, text='USN', font=('Courier', 16, 'bold'), bg='linen', fg='brown4')
									ch_stud_usn_label.place(relx=0.2, rely=0.3, anchor=W)

									ch_usn_disp = Label(ch_room_info, text=ch_usn.get(), font=('Times', 18), bg='linen')
									ch_usn_disp.place(relx=0.57, rely=0.3, anchor=W)

									ch_cur_block = Label(ch_room_info, text='Current Block', font=('Courier', 16, 'bold'), bg='linen', fg='brown4')
									ch_cur_block.place(relx=0.2, rely=0.4, anchor=W)

									ch_cur_block_record = cursor.execute('select blocknum, blocktype, roomnum from room where studusn=?', (ch_usn.get(),))
									ch_cur_block_record = ch_cur_block_record.fetchall()

									ch_cur_block = Label(ch_room_info, text=ch_cur_block_record[0][1].title() + "' hostel " + ch_cur_block_record[0][0],
									                     font=('Times', 18), bg='linen')
									ch_cur_block.place(relx=0.57, rely=0.4, anchor=W)

									ch_cur_room_label = Label(ch_room_info, text='Current Room No.', font=('Courier', 16, 'bold'), bg='linen', fg='brown4')
									ch_cur_room_label.place(relx=0.2, rely=0.5, anchor=W)

									ch_cur_room = Label(ch_room_info, text=ch_cur_block_record[0][2], font=('Times', 18), bg='linen')
									ch_cur_room.place(relx=0.57 , rely=0.5, anchor=W)

									ch_new_block_label = Label(ch_room_info, text='New Block', font=('Courier', 16, 'bold'), bg='linen', fg='brown4')
									ch_new_block_label.place(relx=0.2, rely=0.6, anchor=W)

									ch_new_block_entry = Entry(ch_room_info, font=('Times', 14), textvariable=ch_new_block)
									ch_new_block_entry.place(relx=0.57, rely=0.6, anchor=W)

									ch_new_room_label = Label(ch_room_info, text='New Room No.', font=('Courier', 16, 'bold'), bg='linen', fg='brown4')
									ch_new_room_label.place(relx=0.2, rely=0.7, anchor=W)

									ch_new_room_entry = Entry(ch_room_info, textvariable=ch_new_room, font=('Times', 14))
									ch_new_room_entry.place(relx=0.57, rely=0.7, anchor=W)

									submit_ch_btn = Button(ch_room_info, text='SUBMIT', font=('Courier', 13), bg='light steel blue', command=submit_ch)
									submit_ch_btn.place(relx=0.35, rely=0.85, anchor=W)

									cancel_ch_btn = Button(ch_room_info, text='CANCEL', font=('Courier', 13), bg='light steel blue', command=cancel_ch)
									cancel_ch_btn.place(relx=0.53, rely=0.85, anchor=W)
								else:
									messagebox.showwarning('WARNING', 'Invalid USN.')
							else:
								messagebox.showwarning('WARNING', 'Enter USN.')

						ch_room = Toplevel()
						ch_room.geometry('700x250+640+400')
						ch_room.resizable(False, False)
						ch_room.configure(bg='linen')

						ch_usn.set('')

						ch_title = Label(ch_room, text='CHANGE ROOM', font=('Times', 25, 'bold'), bg='linen', fg='DodgerBlue4')
						ch_title.pack()

						ch_usn_label = Label(ch_room, text='USN', bg='linen', fg='brown4', font=('Courier', 17, 'bold'))
						ch_usn_label.place(relx=0.3, rely=0.5, anchor=W)

						ch_usn_entry = Entry(ch_room, font=('Times', 14), textvariable=ch_usn, width=20)
						ch_usn_entry.place(relx=0.4, rely=0.5, anchor=W)

						ch_next_btn = Button(ch_room, text='NEXT', font=('Courier', 17), bg='purple', fg='white', command=ch_room_next)
						ch_next_btn.place(relx=0.8, rely=0.8, anchor=W)

					room_frame = LabelFrame(top2, width=1850, height=780, bg='azure')
					room_frame.place(rely=0.605, anchor=W)
					cols = ('Room No.', 'Room type', 'Block No.', 'Block type', 'Students')
					listbox = ttk.Treeview(room_frame, columns=cols, show='headings', style='mystyle.Treeview')

					for col in cols:
						listbox.heading(col, text=col)
					listbox.place(rely=0.5, anchor=W, width=1850, height=780)
					roomlist = cursor.execute('select roomnum, roomtype, blocknum, blocktype from room group by roomnum order by blocknum')
					roomlist = roomlist.fetchall()
					
					for i in roomlist:
						roommates = cursor.execute('select studname from room where roomnum=?', (i[0],))
						roommates = roommates.fetchall()
						names = ''
						for j in roommates:
							names += j[0] + ', '
						names = names[:len(names)-2]
						listbox.insert('', 'end', values=(i[0], i[1], i[2], i[3].title(), names))

					scroll = Scrollbar(listbox, orient='vertical', command=listbox.yview, width=15)
					scroll.pack(side=RIGHT, fill='y')

					listbox.configure(yscrollcommand=scroll.set)

					change_room_btn = Button(room_frame, text='CHANGE ROOM', bg='salmon4', fg='white', font=('Courier', 15), command=change_room)
					change_room_btn.place(relx=0.45, rely=0.93, anchor=W)

				def delete_warden():
					def delete_warden_btn():
						if del_wrdn_id.get() != '':
							is_present = cursor.execute('select * from warden where id=?', (del_wrdn_id.get(),))
							is_present = is_present.fetchall()
							if len(is_present) != 0:
								cursor.execute('delete from warden where id=?', (del_wrdn_id.get(),))
								a = cursor.execute(
									'select id, name from warden where blocknum=(select w.blocknum from warden w where w.id=?)'
									' and type=(select ww.type from warden ww where ww.id=?)', (del_wrdn_id.get(), del_wrdn_id.get()))
								a = a.fetchall()

								if len(a) != 0:
									a = [item for item in a if item[0] != del_wrdn_id.get()]
									a = [item for item in a[0]]
									cursor.execute('update block set wardenid=?, wardenname=? where wardenid=?',
									               (a[0], a[1], del_wrdn_id.get()))

								conn.commit()
								messagebox.showinfo('INFORMATION', 'Successfully deleted.')
								del_wrdn.destroy()
								display_warden_details()
							else:
								messagebox.showwarning('WARNING', 'Invalid ID')
						else:
							messagebox.showwarning('WARNING', 'Enter ID')

					del_wrdn = Toplevel()
					del_wrdn.configure(bg='linen')
					del_wrdn.geometry('700x250+640+400')
					del_wrdn.resizable(False, False)

					del_wrdn_id = StringVar()

					delete_title = Label(del_wrdn, text='DELETE WARDEN', font=('Times', 25, 'bold'), bg='linen', fg='DodgerBlue4')
					delete_title.pack()

					del_wrdn_id_label = Label(del_wrdn, text='ID', font=('Courier', 17, 'bold'), fg='brown4', bg='linen')
					del_wrdn_id_label.place(relx=0.3, rely=0.5, anchor=W)

					del_wrdn_entry = Entry(del_wrdn, font=('Times', 14), textvariable=del_wrdn_id)
					del_wrdn_entry.place(relx=0.4, rely=0.5, anchor=W)

					next_btn = Button(del_wrdn, text='DELETE', font=('Courier', 17), fg='white', bg='purple', command=delete_warden_btn)
					next_btn.place(relx=0.8, rely=0.8, anchor=W)

				def add_warden():
					def cancel_wrdn_add():
						new_wrdn.destroy()

					def submit_wrdn_add():
						if new_wrdn_name.get() != '' and new_wrdn_gmail.get() != '' and new_wrdn_ph.get() != '' and \
								new_wrdn_post.get() != '' and new_wrdn_block_type.get() != '' and new_wrdn_pwd.get() != '' \
								and new_wrdn_confirm_pwd.get() != '':
							if len(new_wrdn_ph.get()) == 10:
								if new_wrdn_pwd.get() == new_wrdn_confirm_pwd.get():
									is_present = cursor.execute('select * from warden where gmail=?',
									                            (new_wrdn_gmail.get(),))
									is_present = is_present.fetchall()
									btype = new_wrdn_block_type.get()[:4].lower()
									# is_already = cursor.execute('select * from warden where blocknum=? and type=?',
									#                             (new_wrdn_block.get(), btype))
									# is_already = is_already.fetchall()
									if len(is_present) == 0:
										wdn_id = cursor.execute('select id from warden')
										wdn_id = wdn_id.fetchall()
										id_list = []
										for i in wdn_id:
											id_list.append(i[0])
										id_list = [int(j[4:]) for j in id_list]
										cursor.execute('insert into warden values(?, ?, ?, ?, ?, ?, ?, ?)',
										               (new_wrdn_name.get(), 'wrdn' + str(max(id_list) + 1),
										                new_wrdn_ph.get(), new_wrdn_gmail.get(),
										                new_wrdn_pwd.get(), new_wrdn_post.get(),
										                new_wrdn_block.get(), btype))
										conn.commit()
										messagebox.showinfo('INFORMATION',
										                    'Successfully added.\n\nYour ID is ' + 'wrdn' + str(
											                    max(id_list) + 1))
										new_wrdn.destroy()
									else:
										messagebox.showwarning('WARNING', 'Warden already exists.')
								else:
									messagebox.showwarning('WARNING', 'Passwords should be the same.')
							else:
								messagebox.showwarning('WARNING', 'Invalid Phone No.')
						else:
							messagebox.showwarning('WARNING', 'Some of the required fields are empty.')

					new_wrdn_name = StringVar()
					new_wrdn_gmail = StringVar()
					new_wrdn_ph = StringVar()
					new_wrdn_post = StringVar()
					new_wrdn_block = StringVar()
					new_wrdn_block_type = StringVar()
					new_wrdn_pwd = StringVar()
					new_wrdn_confirm_pwd = StringVar()

					new_wrdn = Toplevel()
					new_wrdn.geometry('900x450+550+300')
					new_wrdn.resizable(False, False)
					new_wrdn.configure(bg='linen')

					new_title = Label(new_wrdn, text='WARDEN DETAILS', fg='DodgerBlue4', bg='linen',
					                  font=('Times', 30, 'bold'))
					new_title.pack()

					new_wrdn_name_label = Label(new_wrdn, text='Name', font=('Courier', 17, 'bold'), fg='brown4',
					                            bg='linen')
					new_wrdn_name_label.place(relx=0.04, rely=0.25, anchor=W)

					new_wrdn_name_entry = Entry(new_wrdn, textvariable=new_wrdn_name, font=('Times', 14))
					new_wrdn_name_entry.place(relx=0.14, rely=0.25, anchor=W)

					new_wrdn_gmail_label = Label(new_wrdn, text='Gmail', font=('Courier', 17, 'bold'), fg='brown4',
					                             bg='linen')
					new_wrdn_gmail_label.place(relx=0.04, rely=0.4, anchor=W)

					new_wrdn_gmail_entry = Entry(new_wrdn, textvariable=new_wrdn_gmail, font=('Times', 14))
					new_wrdn_gmail_entry.place(relx=0.14, rely=0.4, anchor=W)

					new_wrdn_ph_label = Label(new_wrdn, text='Phone', font=('Courier', 17, 'bold'), fg='brown4',
					                          bg='linen')
					new_wrdn_ph_label.place(relx=0.04, rely=0.55, anchor=W)

					new_wrdn_ph_entry = Entry(new_wrdn, textvariable=new_wrdn_ph, font=('Times', 14))
					new_wrdn_ph_entry.place(relx=0.14, rely=0.55, anchor=W)

					new_wrdn_post_label = Label(new_wrdn, text='Post', font=('Courier', 17, 'bold'), fg='brown4',
					                            bg='linen')
					new_wrdn_post_label.place(relx=0.04, rely=0.7, anchor=W)

					new_wrdn_post_entry = Entry(new_wrdn, textvariable=new_wrdn_post, font=('Times', 14))
					new_wrdn_post_entry.place(relx=0.14, rely=0.7, anchor=W)

					new_wrdn_block_label = Label(new_wrdn, text='Block No.', font=('Courier', 17, 'bold'), fg='brown4',
					                             bg='linen')
					new_wrdn_block_label.place(relx=0.47, rely=0.25, anchor=W)

					new_wrdn_block_entry = Entry(new_wrdn, textvariable=new_wrdn_block, font=('Times', 14))
					new_wrdn_block_entry.place(relx=0.75, rely=0.25, anchor=W)

					new_wrdn_btype_label = Label(new_wrdn, text='Block type', font=('Courier', 17, 'bold'), fg='brown4',
					                             bg='linen')
					new_wrdn_btype_label.place(relx=0.47, rely=0.4, anchor=W)

					new_wrdn_block_type_options = ["Boys' hostel", "Girls' hostel"]
					new_wrdn_btype_drop_down = OptionMenu(new_wrdn, new_wrdn_block_type, *new_wrdn_block_type_options)
					new_wrdn_block_type.set("Boys' hostel")
					new_wrdn_btype_drop_down.place(relx=0.75, rely=0.4, anchor=W)

					new_wrdn_pwd_label = Label(new_wrdn, text='Password', font=('Courier', 17, 'bold'), fg='brown4',
					                           bg='linen')
					new_wrdn_pwd_label.place(relx=0.47, rely=0.55, anchor=W)

					new_wrdn_pwd_entry = Entry(new_wrdn, textvariable=new_wrdn_pwd, font=('Times', 14), show='*')
					new_wrdn_pwd_entry.place(relx=0.75, rely=0.55, anchor=W)

					new_wrdn_cnfrm_pwd_label = Label(new_wrdn, text='Confirm password', font=('Courier', 17, 'bold'),
					                                 fg='brown4', bg='linen')
					new_wrdn_cnfrm_pwd_label.place(relx=0.47, rely=0.7, anchor=W)

					new_wrdn_cnfrm_pwd_entry = Entry(new_wrdn, textvariable=new_wrdn_confirm_pwd, font=('Times', 14),
					                                 show='*')
					new_wrdn_cnfrm_pwd_entry.place(relx=0.75, rely=0.7, anchor=W)

					submit_new_btn = Button(new_wrdn, text='SUBMIT', font=('Courier', 14), bg='light steel blue',
					                        command=submit_wrdn_add)
					submit_new_btn.place(relx=0.35, rely=0.9, anchor=W)

					cancel_new_btn = Button(new_wrdn, text='CANCEL', font=('Courier', 14), bg='light steel blue',
					                        command=cancel_wrdn_add)
					cancel_new_btn.place(relx=0.53, rely=0.9, anchor=W)

				def display_warden_details():
					wrdn_frame = LabelFrame(top2, width=1850, height=780, bg='azure')
					wrdn_frame.place(rely=0.605, anchor=W)
					cols = ('ID', 'Name', 'Gmail', 'Phone', 'Block No.', 'Block type')
					listbox = ttk.Treeview(wrdn_frame, columns=cols, show='headings', style='mystyle.Treeview')
					for col in cols:
						listbox.heading(col, text=col)
					listbox.place(rely=0.5, anchor=W, width=1850, height=780)
					wrdnlist = cursor.execute('select id, name, gmail, phone, blocknum, type from warden')
					wrdnlist = wrdnlist.fetchall()
					for i in wrdnlist:
						listbox.insert('', 'end', values=(i[0], i[1].title(), i[2], str(i[3]), str(i[4]), i[5].title() + "'"))

					scroll = Scrollbar(listbox, orient='vertical', command=listbox.yview, width=15)
					scroll.pack(side=RIGHT, fill='y')

					listbox.configure(yscrollcommand=scroll.set)

					add_warden_btn = Button(wrdn_frame, text='ADD WARDEN', font=('Courier', 15), bg='salmon4', fg='white', command=add_warden)
					add_warden_btn.place(relx=0.4, rely=0.93, anchor=W)

					delete_warden_btn = Button(wrdn_frame, text='DELETE WARDEN', font=('Courier', 15), bg='salmon4', fg='white', command=delete_warden)
					delete_warden_btn.place(relx=0.49, rely=0.93, anchor=W)

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