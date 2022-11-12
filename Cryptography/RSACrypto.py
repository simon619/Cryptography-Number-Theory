from tkinter import *
import tkinter.font as font
import tkinter.ttk as ttk

class RSACrypto:

    def __init__(self, public_key, private_key, p, q):
        self.e = public_key
        self.d = private_key
        self.p = p
        self.q = q
        self.n = self.p * self.q 
        self.phi = (self.p - 1) * (self.q - 1)
        self.alpha_dic = {}
        self.forbidder = [91, 92, 93, 40, 39, 41, 123, 125]

    def __build_dic_table__(self):
        i = 0
        pointer = 0
        while(i < 95):
            if i + 32 not in self.forbidder: 
                self.alpha_dic[chr(i + 32)] = pointer
                pointer += 1
            i += 1
    
    def __conversion__(self, st):
        main_string_list = [0] * len(st)
        main_string_list = [self.alpha_dic[st[i]] for i in range(len(st))]
        return main_string_list

    def __gcd__(self, x, y):
        if x == 0:
            return y
        else:
            return self.__gcd__(y % x, x)

    def __encrtption__(self, st):
        st_to_num_conv = self.__conversion__(st)
        en_string_list = [0] * len(st_to_num_conv)
        bool = self.__gcd__(self.e, self.phi)
        if bool != 1:
            print("Wrong p, q or publc key selection")
        else:
            en_string_list = [(st_to_num_conv[i] ** self.e) % self.n  for i in range(len(st_to_num_conv))]
            en_num, en_st = self.__list_to_string__(en_string_list)
            return en_num, en_st

    def __euler_extend__(self, phi1, phi2, e, d):
        if e == 1:
            return d
        else:
            div = phi1 // e
            a, b = e * div, d * div
            x, y = phi1 - a, phi2 - b
            if x < 0:
                x = x % self.phi
            if y < 0:
                y = y % self.phi
            return self.__euler_extend__(e, d, x, y)

    def __decryption__(self, st):
        st_to_num_conv = self.__conversion__(st)
        de_string_list = [0] * len(st_to_num_conv)
        self.d = self.__euler_extend__(self.phi, self.phi, self.e, 1)
        de_string_list = [(st_to_num_conv[i] ** self.d) % self.n for i in range(len(st_to_num_conv))]
        de_num, de_st = self.__list_to_string__(de_string_list)
        return de_num, de_st

    def __list_to_string__(self, list):
        num, st = '', ''
        for i in list:
            num += str(i)
            st += [j for j in self.alpha_dic if self.alpha_dic[j] == i][0]
        return num, st


if __name__ == "__main__":
    root = Tk()
    color = '#000000'
    root.configure(background=color)
    root.title("RSACypto")
    en = Entry(root, width=100)
    f = font.Font(weight="bold")
    rb = ttk.Style()
    rb.configure('Wild.TRadiobutton', background=color, foreground='#ffffff')
    en.grid(row=0, column=0, padx=10, pady=20, ipady=10, columnspan=3)
    en.insert(0,'')
    en_re = Entry(root, width=100)
    en_re.grid(row=1, column=0, padx=10, pady=10, ipady=10, columnspan=3)
    en_re.insert(0,'Here Will Be Your Result')
    want = StringVar()
    want.set('en')
    ttk.Radiobutton(root, text="Encryption", variable=want, value="en", style = 'Wild.TRadiobutton').grid(row=2, column=2, ipadx=20)
    ttk.Radiobutton(root, text="Decryption", variable=want, value="de", style = 'Wild.TRadiobutton').grid(row=3, column=2, ipadx=20)
    inst = RSACrypto(public_key=5, private_key=0, p=3, q=29)
    inst.__build_dic_table__()
    def click(wish):
        global inst
        try:
            what_you_want_encrypt = en.get()
            st = ''
            if wish == 'en':
                encypted_result_num, encypted_result_string = inst.__encrtption__(what_you_want_encrypt)
                st = f'[{what_you_want_encrypt}] Encrypted to String: [{encypted_result_string}] & Number:[{encypted_result_num}]'
            elif wish == 'de':
                decypted_result_num, decypted_result_string = inst.__decryption__(what_you_want_encrypt)
                st = f'[{what_you_want_encrypt}] Decrypted to String: [{decypted_result_string}] & Number: [{decypted_result_num}]'
            else:
                st = 'Pick A Choice'
            en_re.delete(0, END)
            en_re.insert(0, st)
        except:
            en_re.delete(0, END)
            en_re.insert(0, 'Wrong Input: Unsupported Character')

    def clear():
        en.delete(0,END)
        en_re.delete(0, END)
        en_re.insert(0,'Here Will Be Your Result')

    my_button1 = Button(root, text='Enter Your Message', padx=70, pady=20, bg="blue", fg='white', command=lambda: click(want.get()))
    my_button1.grid(row=4, column=0)
    my_button2 = Button(root, text='CLEAR', padx=52, pady=20, bg="red", fg='white', command=clear)
    my_button2.grid(row=4, column=1)
    quitbutton = Button(root, text="Exit", padx=52, pady=20, bg="red", fg='white', command=root.quit)
    quitbutton.grid(row=4, column=2)
    my_button1['font'] = f
    my_button2['font'] = f
    quitbutton['font'] = f
    root.mainloop()