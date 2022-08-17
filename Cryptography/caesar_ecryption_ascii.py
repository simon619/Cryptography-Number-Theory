class CeaEnAs:

    def __init__(self, key):
        self.key = key
        self.alpha_dic = {}
        self.forbidden = [91, 92, 93, 40, 39, 41, 123, 125, 34]

    def __build_dic_table__(self):
        i = 0
        pointer = 0
        while(i < 95):
            if i + 32 not in self.forbidden: 
                self.alpha_dic[chr(i + 32)] = pointer
                pointer += 1
            i += 1
    
    def __conversion__(self, st):
        main_string_list = [0] * len(st)
        main_string_list = [self.alpha_dic[st[i]] for i in range(len(st))]
        return main_string_list

    def __encryption__(self, st):
        st_to_num_conv = self.__conversion__(st)
        en_string_list = [0] * len(st_to_num_conv)
        en_string_list = [(st_to_num_conv[i] + self.key) % len(self.alpha_dic) for i in range(len(st_to_num_conv))]
        return en_string_list

    def __decyption__(self, st):
        st_to_num_conv = self.__conversion__(st)
        de_string_list = [0] * len(st_to_num_conv)
        de_string_list = [(st_to_num_conv[i] - self.key) % len(self.alpha_dic) for i in range(len(st_to_num_conv))]
        return de_string_list
    
    def __list_to_string__(self, list):
        num, st = '', ''
        for i in list:
            num += str(i)
            st += [j for j in self.alpha_dic if self.alpha_dic[j] == i][0]
        return num, st


if __name__ == "__main__":
    inst = CeaEnAs(3)
    inst.__build_dic_table__()
    what_you_want_encrypt = str(input("What Your Want to Encrypt: "))
    en_list = inst.__encryption__(what_you_want_encrypt)
    encypted_result_num, encypted_result_string = inst.__list_to_string__(en_list)
    de_list = inst.__decyption__(encypted_result_string)
    dencypted_result_num, dencypted_result_string = inst.__list_to_string__(de_list)
    print(f'[{what_you_want_encrypt}] encrypted to String: [{encypted_result_string}] & Number:[{encypted_result_num}],\n[{encypted_result_string}] decrypted to String: [{dencypted_result_string}] & Number: [{dencypted_result_num}]')


