import tkinter as tk 
import sqlite3 

root = tk.Tk() 

# create table
'''
c.execute("""
        CREATE TABLE addresses(
            first_name text, 
            last_name text,
            address text, 
            city text, 
            state text, 
            zip_code integer 
    )
""")

'''

def submit():
    # create a database and connect to it 
    conn = sqlite3.connect('address_book.db') 
    # create a cursor c 
    c = conn.cursor() 

    # save the records into the table addresses 
    if f_name.get():
        c.execute("INSERT INTO addresses VALUES(:first_name, :last_name, :address, :city, :state, :zip_code)", 
                {
                    'first_name' : f_name.get(), 
                    'last_name' : l_name.get(), 
                    'address' : address.get(), 
                    'city' : city.get(), 
                    'state' : state.get(), 
                    'zip_code' : zip_code.get() 
                }
        )
    else:
        print('Please Enter at least one record') 
    
    # commmit the changes 
    conn.commit() 
    # close the connection 
    conn.close() 

    # Clear The Text Boxes
    f_name.delete(0, tk.END)
    l_name.delete(0, tk.END)
    address.delete(0, tk.END)
    city.delete(0, tk.END)
    state.delete(0, tk.END)
    zip_code.delete(0, tk.END)

def query():
    conn = sqlite3.connect('address_book.db') 
    c = conn.cursor() 

    q = "SELECT *, oid FROM addresses" 
    c.execute(q) 
    records = c.fetchall() 
    record_list = ''
    for record in records:
        record_list += record[0] + " " + record[1] + "\t" + str(record[6]) + "\n " 
    label = tk.Label(root, padx=20, pady=8, text=record_list) 
    label.grid(row=8, columnspan=2) 

    conn.commit() 
    conn.close() 

def delete():
    conn = sqlite3.connect('address_book.db') 
    c = conn.cursor() 

    c.execute('DELETE FROM addresses WHERE oid = ' + delete_box.get())
    delete_box.delete(0, tk.END) 

    conn.commit() 
    conn.close() 

def update():
    conn = sqlite3.connect('address_book.db') 
    c = conn.cursor() 

    c.execute('''UPDATE addresses SET 
              first_name = :first_name, 
              last_name = :last_name, 
              address = :address, 
              city = :city, 
              state = :state, 
              zip_code = :zip_code 
              WHERE oid = :oid''', 
              {
                  'first_name' : f_name_edited.get(), 
                  'last_name' : l_name_edited.get(), 
                  'address' : address_edited.get(), 
                  'city' : city_edited.get(), 
                  'state' : state_edited.get(), 
                  'zip_code' : zip_code_edited.get(), 
                  'oid' : delete_box.get() 
              }
        )

    conn.commit() 
    conn.close() 
    editor.destroy() 
    root.deiconify() 
def edit():
    if not delete_box.get():
        print('Plese enter the ID') 
        return 
    
    conn = sqlite3.connect('address_book.db') 
    c = conn.cursor() 

    c.execute('SELECT *, oid FROM addresses WHERE oid = ' + delete_box.get()) 
    user = c.fetchall() 
    print(user) 

    conn.commit() 
    conn.close() 

    # create a new editor 
    global editor 
    editor= tk.Toplevel() 
    editor.title('Edit the Record') 

    global f_name_edited 
    global l_name_edited 
    global address_edited 
    global city_edited 
    global state_edited 
    global zip_code_edited

    # cration of Entry Field 
    f_name_edited = tk.Entry(editor, width=30) 
    f_name_edited.grid(row=0, column=1, padx=30) 
    l_name_edited = tk.Entry(editor, width=30) 
    l_name_edited.grid(row=1, column=1, padx=30) 
    address_edited = tk.Entry(editor, width=30) 
    address_edited.grid(row=2, column=1, padx=30) 
    city_edited = tk.Entry(editor, width=30) 
    city_edited.grid(row=3, column=1, padx=30) 
    state_edited = tk.Entry(editor, width=30) 
    state_edited.grid(row=4, column=1, padx=30) 
    zip_code_edited = tk.Entry(editor, width=30) 
    zip_code_edited.grid(row=5, column=1, padx=30) 

    # cration of Labels 
    f_name_label = tk.Label(editor, text="First Name") 
    f_name_label.grid(row=0, column=0, padx=20, pady=10) 
    l_name_label = tk.Label(editor, text='Last Name') 
    l_name_label.grid(row=1, column=0, padx=20, pady=10) 
    address_label = tk.Label(editor, text="Address") 
    address_label.grid(row=2, column=0, padx=20, pady=10) 
    city_label = tk.Label(editor, text="City") 
    city_label.grid(row=3, column=0, padx=20, pady=10) 
    state_label = tk.Label(editor, text="State")
    state_label.grid(row=4, column=0, padx=20, pady=10) 
    zip_code_label = tk.Label(editor, text="Zip Code") 
    zip_code_label.grid(row=5, column=0, padx=20, pady=10) 
    for entry in user: 
        f_name_edited.insert(0, entry[0]) 
        l_name_edited.insert(0, entry[1]) 
        address_edited.insert(0, entry[2]) 
        city_edited.insert(0, entry[3]) 
        state_edited.insert(0, entry[4]) 
        zip_code_edited.insert(0, entry[5]) 

    submit_button = tk.Button(editor, text="Save", padx=20, pady=5, bg='purple', command=update) 
    submit_button.grid(row=6, column=0, columnspan=2) 



# cration of Entry Field 
f_name = tk.Entry(root, width=30) 
f_name.grid(row=0, column=1, padx=30) 
l_name = tk.Entry(root, width=30) 
l_name.grid(row=1, column=1, padx=30) 
address = tk.Entry(root, width=30) 
address.grid(row=2, column=1, padx=30) 
city = tk.Entry(root, width=30) 
city.grid(row=3, column=1, padx=30) 
state = tk.Entry(root, width=30) 
state.grid(row=4, column=1, padx=30) 
zip_code = tk.Entry(root, width=30) 
zip_code.grid(row=5, column=1, padx=30) 
delete_box = tk.Entry(root, width=30) 
delete_box.grid(row=9, column=1) 



# cration of Labels 
f_name_label = tk.Label(root, text="First Name") 
f_name_label.grid(row=0, column=0, padx=20, pady=10) 
l_name_label = tk.Label(root, text='Last Name') 
l_name_label.grid(row=1, column=0, padx=20, pady=10) 
address_label = tk.Label(root, text="Address") 
address_label.grid(row=2, column=0, padx=20, pady=10) 
city_label = tk.Label(root, text="City") 
city_label.grid(row=3, column=0, padx=20, pady=10) 
state_label = tk.Label(root, text="State")
state_label.grid(row=4, column=0, padx=20, pady=10) 
zip_code_label = tk.Label(root, text="Zip Code") 
zip_code_label.grid(row=5, column=0, padx=20, pady=10) 
submit_button = tk.Button(root, text="Submit to Database", padx=20, pady=5, bg='purple', command=submit) 
submit_button.grid(row=6, column=0, columnspan=2, ipadx=100) 
query_button = tk.Button(root, text="Show Records", padx=20, pady=5, bg='purple', command=query) 
query_button.grid(row=7, column=0, columnspan=2, ipadx=122) 
select_id = tk.Label(root, text='Select ID') 
select_id.grid(row=9, column=0, padx=20, pady=10) 
delete_button = tk.Button(root, text='Delete Record', bg='purple', command=delete) 
delete_button.grid(row=10, column=0, columnspan=2, ipadx=130)
edit_button = tk.Button(root, text='Edit Record', bg='purple', command=edit) 
edit_button.grid(row=11, column=0, columnspan=2, ipadx=140)

root.mainloop() 
