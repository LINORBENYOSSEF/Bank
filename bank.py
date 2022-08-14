from tkinter import *
from datetime import *
#import matplotlib.pyplot as plt


# Account is the class that handles the account's database and the GUI
class Account:
    accountNumbering = 1000
    Database = {}
    Transactions = {}


    # adds an account to the database
    @staticmethod
    def add_account(name, balance, credit, window):
        if credit is not "":
            Account.Database[Account.accountNumbering] = name, [float(balance)], float(credit), ()
        else:
            Account.Database[Account.accountNumbering] = name, [float(balance)], 1500.0, ()
        Account.add_transaction(str(Account.accountNumbering), "Account Created", balance)
        Account.accountNumbering += 1
        if Account.accountNumbering - 1 == 1000:
            EntryWindowT1.display_account(window, Account.accountNumbering - 1)
        return Account.accountNumbering - 1


    # get a client's name
    @staticmethod
    def get_client_name(account_id):
        return Account.Database[int(account_id)][0]


    # get a client's current cash
    @staticmethod
    def get_current_cash(account_id):
        return Account.Database[int(account_id)][1][0]


    # set a client's current cash
    @staticmethod
    def set_current_cash(account_id, new_balance):
        Account.Database[int(account_id)][1][0] = new_balance


    # get a client's credit frame
    @staticmethod
    def get_credit_frame(account_id):
        return Account.Database[int(account_id)][2]


    # Method that returns if x is a number
    @staticmethod
    def is_number(x):
        try:
            float(x)
            return True
        except ValueError:
            return False


    # Method that adds all transactions to a transaction database
    @staticmethod
    def add_transaction(acc_num, action_type, amount, to="-"):
        date_now = datetime.now().strftime("%Y/%m/%d")
        time_now = datetime.now().strftime("%H:%M")
        if acc_num in Account.Transactions.keys():
            Account.Transactions[acc_num].append([action_type, amount, to, date_now, time_now])
        else:
            Account.Transactions[acc_num] = [[action_type, amount, to, date_now, time_now]]




# The mutual attributes to all pages who are his children
class SystemGui(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        master.resizable(0, 0)


        task1_btn = Button(master, text="Task #1", width=20)
        task2_btn = Button(master, text="Task #2", width=20)
        self.task1_btn = task1_btn
        self.task2_btn = task2_btn




# This class is the window of account creation
class CreateAccountWindow:
    def __init__(self, window):
        self.master = Tk()
        self.master.title(string="Add Account")
        self.master.resizable(0, 0)


        # initialization of all widgets in the window
        self.header_lbl = Label(self.master, text="Create Account", font=("David", 16), width=22)
        self.name_lbl = Label(self.master, text="*Name: ", fg="red")
        self.f_depo_lbl = Label(self.master, text="*First Deposit: ", fg="red")
        self.credit_frame_lbl = Label(self.master, text="Credit Frame: ")
        self.mandatory_lbl = Label(self.master, text="* is mandatory", fg="red")


        self.create_acc_btn = Button(self.master, text="Create Account", command=self.create_account)
        self.cancel_btn = Button(self.master, text="Cancel", command=self.master.destroy)


        self.name_field = Entry(self.master)
        self.f_depo_field = Entry(self.master)
        self.credit_frame_field = Entry(self.master)


        self.window = window


        # inserting all widgets to the window
        self.header_lbl.grid(row=0, columnspan=2)
        self.name_lbl.grid(row=1, sticky=E)
        self.f_depo_lbl.grid(row=2, sticky=E)
        self.credit_frame_lbl.grid(row=3, sticky=E)
        self.mandatory_lbl.grid(row=5, columnspan=2)


        self.create_acc_btn.grid(row=4, pady=(10, 0))
        self.cancel_btn.grid(row=4, column=1, pady=(10, 0), padx=(0, 10), sticky=E)


        self.name_field.grid(row=1, column=1, sticky=W, padx=(0, 10))
        self.f_depo_field.grid(row=2, column=1, sticky=W)
        self.credit_frame_field.grid(row=3, column=1, sticky=W)


    def clear_name_field(self):
        if self.name_field is "Mandatory Field":
            self.name_field.delete(0, END)


    # This method will check that all the entries are valid and then sends them to the database add account method
    def create_account(self):
        if self.name_field.get() is not "" and self.f_depo_field.get() is not "":
            if Account.is_number(self.f_depo_field.get()):
                if Account.is_number(self.credit_frame_field.get() or self.credit_frame_field is ""):
                    if Account.is_number(self.credit_frame_field.get()):
                        if float(self.f_depo_field.get()) > 0 and float(self.credit_frame_field.get()) > 0:
                            Account.add_account(self.name_field.get(), self.f_depo_field.get(),
                                                self.credit_frame_field.get(), self.window)
                            self.master.destroy()
                        elif float(self.credit_frame_field.get()) <= 0 and float(self.f_depo_field.get()) <= 0:
                            self.credit_frame_field.delete(0, END)
                            self.f_depo_field.delete(0, END)
                            self.f_depo_field.insert(0, "Input Positive Number")
                            self.credit_frame_field.insert(0, "Input Positive Number")
                        elif float(self.f_depo_field.get()) <= 0:
                            self.f_depo_field.delete(0, END)
                            self.f_depo_field.insert(0, "Input Positive Number")
                        else:
                            self.credit_frame_field.delete(0, END)
                            self.credit_frame_field.insert(0, "Input Positive Number")
                    elif float(self.f_depo_field.get()) > 0:
                        Account.add_account(self.name_field.get(), self.f_depo_field.get(),
                                            self.credit_frame_field.get(), self.window)
                        self.master.destroy()
                    else:
                        self.f_depo_field.delete(0, END)
                        self.f_depo_field.insert(0, "Input Positive Number")
                else:
                    self.credit_frame_field.delete(0, END)
                    self.credit_frame_field.insert(0, "Enter A Number")
            else:
                self.f_depo_field.delete(0, END)
                self.f_depo_field.insert(0, "Enter A Number")
        else:
            if self.name_field.get() is "":
                self.name_field.insert(0, "Mandatory Field")
            if self.f_depo_field.get() is "":
                self.f_depo_field.insert(0, "Mandatory Field")




# This class is the window of the transaction data
class TransactionsWindow:
    def __init__(self, acc_num):
        self.master = Tk()
        string = "Transactions\nAccount: " + str(acc_num)
        self.master.title(string="Transactions")
        self.master.resizable(0, 0)


        # Initializing all the needed widgets
        self.transactions_lbl = Label(self.master, text=string, font=("Times", 18))


        self.data_frame = Frame(self.master)


        self.close_btn = Button(self.master, text="Exit", command=self.master.destroy)


        self.acc_num = acc_num


        # Inserting all the widgets to the window
        self.transactions_lbl.grid(row=0, columnspan=4)


        self.data_frame.grid(row=1, sticky=NSEW)


        self.close_btn.grid(row=2, columnspan=4)


        self.make_data_frame(self.data_frame)


    # This method inserts the labels of each transaction's detail in it's proper place at the transaction window
    def make_data_frame(self, window):
        type_lbl = Label(window, text="Type")
        amount_lbl = Label(window, text="Amount")
        to_lbl = Label(window, text="To")
        date_lbl = Label(window, text="Date")
        time_lbl = Label(window, text="Time")
        type_lbl.grid(row=0)
        amount_lbl.grid(row=0, column=1)
        to_lbl.grid(row=0, column=2)
        date_lbl.grid(row=0, column=3)
        time_lbl.grid(row=0, column=4)
        for row, value_via_key in enumerate(Account.Transactions[str(self.acc_num)]):
            for column, value_via_list in enumerate(Account.Transactions[str(self.acc_num)][row]):
                lbl = Label(window, text=value_via_list)
                lbl.grid(row=row+1, column=column)




# This class is the main window of the 2nd question - the word generator + the distribution of letters
class EntryWindowT2(SystemGui):
    def __init__(self):
        self.master = Tk()
        self.master.title(string="Question#2")
        SystemGui.__init__(self, self.master)
        self.last_char = ""
        self.last_state = True
        self.word = ""
        self.lbl_text = ""
        self.state = IntVar(value=1)
        self.lbl_list = EntryWindowT2.read_from_file("words.txt")


        # initialization of the widgets in this window
        self.header_lbl = Label(self.master, text="Word Generator", font=("Times", 18), width=23)
        self.word_lbl = Label(self.master, font=("Times", 14), width=15)
        self.letter_lbl = Label(self.master, text="Letter: ")


        self.include_radiobtn = Radiobutton(self.master, text="Include", variable=self.state, value=1,
                                            command=self.include)
        self.exclude_radiobtn = Radiobutton(self.master, text="Exclude", variable=self.state, value=0,
                                            command=self.exclude)


        self.reset_btn = Button(self.master, text="Reset", command=self.reset)
        self.next_btn = Button(self.master, text="Next word", command=self.next_word)
        self.distribution_btn = Button(self.master, text="A-J\nDistribution", command=self.distribute)


        self.letter_field = Entry(self.master, width=2)


        # insertion of all the widgets into the window
        self.header_lbl.grid(row=0, columnspan=3)
        self.word_lbl.grid(row=1, columnspan=3)
        self.letter_lbl.grid(row=2, sticky=W)


        self.include_radiobtn.grid(row=3, sticky=W)
        self.exclude_radiobtn.grid(row=4, sticky=W)
        self.include_radiobtn.select()


        self.reset_btn.grid(row=2, columnspan=3)
        self.next_btn.grid(row=2, column=2, sticky=E, padx=(0, 5))
        self.distribution_btn.grid(row=3, column=2, sticky=E, padx=(0, 3), rowspan=2)
        self.task1_btn.grid(row=3, columnspan=3, rowspan=2, padx=(0, 5))


        self.letter_field.grid(row=2, padx=(1, 4))


        self.task1_btn.configure(command=self.task1btn)


    # This method calculates the occurrence of each letter between 'a' to 'j' in the list of given words
    @staticmethod
    def get_distribute(tlist):
        count_arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for word in tlist:
            for letter in word:
                if letter.lower() == "a":
                    count_arr[0] += 1
                elif letter.lower() == "b":
                    count_arr[1] += 1
                elif letter.lower() == "c":
                    count_arr[2] += 1
                elif letter.lower() == "d":
                    count_arr[3] += 1
                elif letter.lower() == "e":
                    count_arr[4] += 1
                elif letter.lower() == "f":
                    count_arr[5] += 1
                elif letter.lower() == "g":
                    count_arr[6] += 1
                elif letter.lower() == "h":
                    count_arr[7] += 1
                elif letter.lower() == "i":
                    count_arr[8] += 1
                elif letter.lower() == "j":
                    count_arr[9] += 1
        return count_arr


    # This method shows the graphical graph.
    def distribute(self):
        letter_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        number_array = EntryWindowT2.get_distribute(self.lbl_list)
        plt.bar(letter_array, number_array)
        plt.xlabel("Alphabet")
        plt.ylabel("Appearances")
        plt.title("Distribution of first 10th letters in the ABC")
        plt.show()


    # This method sets the radio button state to 1
    def include(self):
        self.state.set(1)


    # This method sets the radio button state to 0
    def exclude(self):
        self.state.set(0)


    # This method resets the generator so the list will start from the beginning
    def reset(self):
        self.word = EntryWindowT2.generate_next_word(self.lbl_list, self.letter_field.get().lower(), self.state.get())
        self.lbl_text = next(self.word)
        self.word_lbl.configure(text=self.lbl_text, fg='black')


    #     # This method shows the next word according to the data given in the window
    def next_word(self):
        try:
            if len(self.letter_field.get().strip(' ')) == 1 and self.letter_field.get() is \
                    not " " and self.letter_field.get().isalpha():
                if self.last_char is self.letter_field.get() and self.last_state is self.state.get():
                    self.lbl_text = next(self.word)
                    self.word_lbl.configure(text=self.lbl_text, fg='black')
                else:
                    self.last_char = self.letter_field.get()
                    self.last_state = self.state.get()
                    self.word = EntryWindowT2.generate_next_word(self.lbl_list, self.letter_field.get().lower(),
                                                                 self.state.get())
                    self.lbl_text = next(self.word)
                    self.word_lbl.configure(text=self.lbl_text, fg='black')
            else:
                self.lbl_text = "*Please enter 1 letter"
                self.word_lbl.configure(text=self.lbl_text, fg='red')
        except StopIteration:
            self.word_lbl.configure(text="No more words", fg='red')


    # This method terminates the word generator window and opens the bank window
    def task1btn(self):
        tk = Tk()
        EntryWindowT1(tk)
        self.master.destroy()


    # A generator method that returns the next word according to the rules
    @staticmethod
    def generate_next_word(word_list, char, include):
        if include:
            for word in word_list:
                if char in word:
                    yield word
        else:
            for word in word_list:
                if char not in word:
                    yield word


    # A method that gets a file path and reads it's lines into a list, with a comma (,) separator
    @staticmethod
    def read_from_file(path):
        text_file = open(path, "r")
        lines = text_file.readlines()
        text_file.close()


        helper = []
        for line in lines:
            helper.append(line.split("," or "."))
        flat_list = [item for sublist in helper for item in sublist]
        for index, word in enumerate(flat_list):
            flat_list[index] = word.strip('\n')
            flat_list[index] = flat_list[index].lower()
        return flat_list




# This class is the main window of the first question - the bank.
class EntryWindowT1(SystemGui):
    def __init__(self, master):
        SystemGui.__init__(self, master)
        master.title(string="Question#1")
        self.current_acc = -1
        self.flag = False


        self.data_frame = Frame(master)


        # initialization of the widgets needed in the window
        self.bank_lbl = Label(master, text="Bank", font=("Times", 18), width=20)
        self.frame_exceed_lbl = Label(master, text="*Can't Exceed Credit Frame!", fg="red")
        self.no_acc_lbl = Label(master, text="*No Accounts found", fg="red")
        self.amount_lbl = Label(master, text="Amount: ")
        self.acc_num_lbl = Label(master, text="Transfer to Account Number: ")


        self.acc_num_lbl_frame = Label(self.data_frame, text="Account Number: ")
        self.name_lbl = Label(self.data_frame, text="Name: ")
        self.balance_lbl = Label(self.data_frame, text="Balance: ")
        self.credit_frame_lbl = Label(self.data_frame, text="Credit Frame: ")


        self.amount_field = Entry(master, width=13)
        self.acc_num_field = Entry(master, width=15)


        self.acc_num_field_frame = Entry(self.data_frame, state=DISABLED)
        self.name_field = Entry(self.data_frame, state=DISABLED)
        self.balance_field = Entry(self.data_frame, state=DISABLED)
        self.credit_frame_field = Entry(self.data_frame, state=DISABLED)


        # insertion of the widgets into the window
        self.right_btn = Button(master, text=">", command=self.next_account)
        self.withdraw_btn = Button(master, text="Withdraw", command=self.withdrawal)
        self.deposit_btn = Button(master, text="Deposit", command=self.deposit)
        self.transfer_btn = Button(master, text="Transfer", command=self.transfer)
        self.transactions_btn = Button(master, text="Transactions", command=self.transactions_window_with_parameter)
        self.create_acc_btn = Button(master, text="Create Account", command=self.create_account_window_with_parameter)


        self.data_frame.grid(row=1, rowspan=2, column=1, columnspan=2, sticky=NSEW)


        self.bank_lbl.grid(row=0, columnspan=4)
        self.amount_lbl.grid(row=4, sticky=E)
        self.acc_num_lbl.grid(row=4, column=2, sticky=E)


        self.acc_num_lbl_frame.grid(row=0, sticky=E)
        self.name_lbl.grid(row=1, sticky=E)
        self.balance_lbl.grid(row=2, sticky=E)
        self.credit_frame_lbl.grid(row=3, sticky=E)


        self.amount_field.grid(row=4, column=1, sticky=W)
        self.acc_num_field.grid(row=4, column=3, sticky=W, padx=(0, 10), pady=(5, 5))


        self.acc_num_field_frame.grid(row=0, column=1, sticky=W)
        self.name_field.grid(row=1, column=1, sticky=W)
        self.balance_field.grid(row=2, column=1, sticky=W)
        self.credit_frame_field.grid(row=3, column=1, sticky=W)


        self.right_btn.grid(row=1, rowspan=2, column=3)
        self.withdraw_btn.grid(row=3, sticky=W, padx=(20, 0), pady=(5, 0))
        self.deposit_btn.grid(row=3, column=1, pady=(5, 0))
        self.transfer_btn.grid(row=3, column=3, columnspan=2, pady=(5, 0))
        self.transactions_btn.grid(row=5, column=1, sticky=E)
        self.create_acc_btn.grid(row=5, column=2, columnspan=2)


        self.task2_btn.grid(row=10, column=1, columnspan=2, pady=(10, 5))
        self.display_account()
        self.task2_btn.configure(command=self.task2btn)


    # A generator method that returns the next account number in the account database
    @staticmethod
    def generate_next_account():
        for k, v in Account.Database.items():
            yield k


    # This method get an account number and shows it's details in the proper fields
    def display_account(self, acc_num=None):
        if acc_num is not None:
            self.acc_num_field_frame.configure(state=NORMAL)
            self.name_field.configure(state=NORMAL)
            self.balance_field.configure(state=NORMAL)
            self.credit_frame_field.configure(state=NORMAL)
            self.acc_num_field_frame.delete(0, END)
            self.name_field.delete(0, END)
            self.balance_field.delete(0, END)
            self.credit_frame_field.delete(0, END)
            self.acc_num_field_frame.insert(0, str(acc_num))
            self.name_field.insert(0, Account.get_client_name(acc_num))
            self.balance_field.insert(0, str(float(Account.get_current_cash(acc_num))))
            self.credit_frame_field.insert(0, str(float(Account.get_credit_frame(acc_num))))
            self.acc_num_field_frame.configure(state=DISABLED)
            self.name_field.configure(state=DISABLED)
            self.balance_field.configure(state=DISABLED)
            self.credit_frame_field.configure(state=DISABLED)


    # This method runs the generator to browse between the account numbers once,
    # and after that, will restart with a simpler code ( at the except code - this was intended!)
    def next_account(self):
        self.amount_field.delete(0, END)
        self.acc_num_field.delete(0, END)
        self.no_acc_lbl.grid_forget()
        if self.acc_num_field_frame.get() is "":
            return
        try:
            if self.flag is False:
                next(self.current_acc)
                self.display_account(next(self.current_acc))
                self.flag = True
            else:
                self.display_account(next(self.current_acc))
        except StopIteration:
            if self.acc_num_field_frame.get() is "":
                return
            if int(self.acc_num_field_frame.get()) + 1 in Account.Database.keys():
                self.display_account(str(int(self.acc_num_field_frame.get())+1))
            else:
                self.display_account(1000)


    # This method deposit money to the current account that is shown in the window
    def deposit(self):
        self.no_acc_lbl.grid_forget()
        if self.acc_num_field_frame.get() is "":
            self.no_acc_lbl.grid(row=3, column=2)
            self.amount_field.delete(0, END)
            return
        if not Account.is_number(self.amount_field.get()) or self.amount_field.get() is "":
            self.amount_field.delete(0, END)
            self.amount_field.insert(0, "Input Number")
        elif int(self.amount_field.get()) > 0:
            self.frame_exceed_lbl.grid_forget()
            equal = float(self.amount_field.get()) + float(self.balance_field.get())
            Account.set_current_cash(self.acc_num_field_frame.get(), equal)
            self.display_account(self.acc_num_field_frame.get())
            Account.add_transaction(self.acc_num_field_frame.get(), "Deposit", self.amount_field.get())
        else:
            self.amount_field.delete(0, END)
            self.amount_field.insert(0, "Enter positive number")


    # This method withdraws money from the current account that is shown in the window,
    # if the account would not exceed it's credit frame
    def withdrawal(self, isbtn=True):
        self.no_acc_lbl.grid_forget()
        if self.acc_num_field_frame.get() is "":
            self.no_acc_lbl.grid(row=3, column=2)
            self.amount_field.delete(0, END)
            return
        self.frame_exceed_lbl.grid_forget()
        if not Account.is_number(self.amount_field.get()) or self.amount_field.get() is "":
            self.amount_field.delete(0, END)
            self.amount_field.insert(0, "Input Number")
        elif int(self.amount_field.get()) > 0:
            equal = float(self.balance_field.get()) - float(self.amount_field.get())
            if float(self.balance_field.get()) < 0:
                if abs(float(self.balance_field.get())) + float(self.amount_field.get()) \
                        > float(self.credit_frame_field.get()):
                    self.frame_exceed_lbl.grid(row=3, column=2)
                    return False
                else:
                    Account.set_current_cash(self.acc_num_field_frame.get(), equal)
                    self.display_account(self.acc_num_field_frame.get())
                    if isbtn:
                        Account.add_transaction(self.acc_num_field_frame.get(), "Withdrawal",
                                                self.amount_field.get())
                    return True
            else:
                if float(self.amount_field.get()) - float(self.balance_field.get()) > \
                        float(self.credit_frame_field.get()):
                    self.frame_exceed_lbl.grid(row=3, column=2)
                    return False
                else:
                    Account.set_current_cash(self.acc_num_field_frame.get(), equal)
                    self.display_account(self.acc_num_field_frame.get())
                    if isbtn:
                        Account.add_transaction(self.acc_num_field_frame.get(),"Withdrawal", self.amount_field.get())
                    return True
        else:
            self.amount_field.delete(0, END)
            self.amount_field.insert(0, "Enter positive number")


    # This method will transfer money from the current account that is shown in the window,
    # to another account that is present in the database, if the current account would not exceed it's credit frame.
    def transfer(self):
        self.no_acc_lbl.grid_forget()
        if Account.is_number(self.amount_field.get()) and Account.is_number(self.acc_num_field.get()):
            if float(self.acc_num_field.get()) in Account.Database.keys():
                if not (self.acc_num_field_frame.get() == self.acc_num_field.get()) and self.withdrawal(False):
                    self.frame_exceed_lbl.grid_forget()
                    equal = float(self.amount_field.get()) + float(Account.get_current_cash(self.acc_num_field.get())
                                                                   )
                    Account.set_current_cash(self.acc_num_field.get(), equal)
                    Account.add_transaction(self.acc_num_field_frame.get(),
                                               "Transfer To", self.amount_field.get(), self.acc_num_field.get())
                    Account.add_transaction(self.acc_num_field.get(), "Transfer From", self.amount_field.get())
            else:
                    self.acc_num_field.delete(0, END)
                    self.acc_num_field.insert(0, "Invalid Account")
        elif Account.is_number(self.acc_num_field.get()) and not Account.is_number(self.amount_field.get()):
                self.amount_field.delete(0, END)
                self.amount_field.insert(0, "Input Number")
        elif Account.is_number(self.amount_field.get()) and not Account.is_number(self.acc_num_field.get()):
                self.acc_num_field.delete(0, END)
                self.acc_num_field.insert(0, "Input Number")
        else:
                self.acc_num_field.delete(0, END)
                self.amount_field.delete(0, END)
                self.acc_num_field.insert(0, "Input Number")
                self.amount_field.insert(0, "Input Number")


    # This method calls the create account method with the needed parameters
    def create_account_window_with_parameter(self):
        self.no_acc_lbl.grid_forget()
        CreateAccountWindow(self)
        self.current_acc = EntryWindowT1.generate_next_account()


    # This method calls the transaction method with the needed parameters
    def transactions_window_with_parameter(self):
        self.no_acc_lbl.grid_forget()
        if Account.is_number(self.acc_num_field_frame.get()):
            TransactionsWindow(int(self.acc_num_field_frame.get()))
        else:
            self.no_acc_lbl.grid(row=3, column=2)


    # This method terminates the bank window and opens the word generator window
    def task2btn(self):
        EntryWindowT2()
        self.master.destroy()




# The main program
if __name__ == "__main__":
    root = Tk()
    EntryWindowT1(root)
    root.mainloop()