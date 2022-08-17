class CeaserEn:

    def __init__(self, key):
        self.alpha_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.alpha_dic = {}
        self.key = key

    def __encryption__(self):
        for i in range(len(self.alpha_list)):
            self.alpha_dic[self.alpha_list[i]] = i 

    def __string_encryption__(self, st):
        temp = [0] * len(st)
        for i in range(len(st)):
            temp[i] = (self.alpha_dic[st[i]] + self.key) % len(self.alpha_list)
        return temp
    
    def __string_decryption__(self, st):
        for i in range(len(st)):
            st[i] = (st[i]- self.key) % len(self.alpha_list)
        return st

    def __list_to_string__(self, list):
        num, st = '', ''
        for i in list:
            num += str(i)
            st += [j for j in self.alpha_dic if self.alpha_dic[j] == i][0]
        return num, st

if __name__ == "__main__":
    inst = CeaserEn(3)
    inst.__encryption__()
    st = str(input('What You Want to Encrypt and Remember, This Only Supports Capital Letters: '))
    encypted = inst.__string_encryption__("SIMON")
    encypted_result_num, encypted_result_string = inst.__list_to_string__(encypted) 
    decrypted = inst.__string_decryption__(encypted)
    decrypted_result_num, decrypted_result_string = inst.__list_to_string__(decrypted)
    print(f'Encryption: {encypted_result_num} and {encypted_result_string},\nDecryption: {decrypted_result_num} and {decrypted_result_string}')
    
     