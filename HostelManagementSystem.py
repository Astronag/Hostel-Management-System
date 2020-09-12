from tkinter import *
import sqlite3

# Create the connection with the database.
conn = sqlite3.connect('HTLMgmt.db')
print('Connected\n')

# Create a cursor object.
cursor = conn.cursor()

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