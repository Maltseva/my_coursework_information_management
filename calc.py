#!/usr/bin/python
# -*- coding: utf-8 -*-
#import ipaddress


class CALC():
    def __init__(self):
        self.hex2dec = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10,
                   'a': 10, 'B': 11, 'b': 11, 'C': 12, 'c': 12, 'D': 13, 'd': 13, 'E': 14, 'e': 14, 'F': 15, 'f': 15}
        self.dec2hex = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A',
                   11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        print('Калькулятор для операций с числами в системе счисления с основанем 16')
        print('Введите два числа в hex-системе и знак необходимой операции("+", "-", "*", "/")')
        self.inp_dict = {}

        #self.oper = '*'
        #dict_nums = self.change_to_blocks(inp_dict['znak_1'], inp_dict['num_1'], inp_dict['znak_2'], inp_dict['num_2'])
        #result = self.calculation(dict_nums, self.oper)

    def run(self):
        dict_nums = self.change_to_blocks(self.inp_dict['znak_1'], self.inp_dict['num_1'], self.inp_dict['znak_2'], self.inp_dict['num_2'])
        result = self.calculation(dict_nums, self.oper)
        return result['znak'], result['short']

    def set_oper(self, oper):
        self.oper = oper

    def set_num_1(self, inp_1):
        #todo validate
        if len(inp_1) == 0:
            return

        if inp_1[0] == '-':
            znak_1 = '-'
            num_1 = inp_1[1:]
        elif inp_1[0] == '+':
            znak_1 = '+'
            num_1 = inp_1[1:]
        else:
            znak_1 = '+'
            num_1 = inp_1
        self.inp_dict['num_1'] = num_1
        self.inp_dict['znak_1'] = znak_1

    def set_num_2(self, inp_2):
        #todo validate
        if len(inp_2) == 0:
            return
        if inp_2[0] == '-':
            znak_2 = '-'
            num_2 = inp_2[1:]
        elif inp_2[0] == '+':
            znak_2 = '+'
            num_2 = inp_2[1:]
        else:
            znak_2 = '+'
            num_2 = inp_2
        self.inp_dict['num_2'] = num_2
        self.inp_dict['znak_2'] = znak_2

    def change_to_blocks(self, znak_1, num_1, znak_2, num_2):
        dict_nums = {'first': {'short': num_1, 'znak' : znak_1},
                     'twice': {'short': num_2, 'znak': znak_2}  }
        ideal = '00000000000000000000000000000000'
        list_num = []
        for num_x in num_1, num_2:

            if len(num_x) < len(ideal):
                diff_len = (len(ideal) - len(num_x))
                app_zero = '0' * diff_len
                num_x = app_zero + num_x
                list_num.append(num_x)
        i = 0
        for key, value in dict_nums.items():
            dict_nums[key]['long'] = list_num[i]
            staff_list = []
            for symbol_n in list_num[i]:
                staff_list.append(symbol_n)
            dict_nums[key]['to_hex_symbol'] = staff_list
            i += 1
        return dict_nums

    def summation_num(self, list_num_1, list_num_2):

        result = {}
        summary = []
        next_range = 0
        for i in range(len(list_num_1)-1, -1, -1):
            sym = self.hex2dec[list_num_1[i]] + self.hex2dec[list_num_2[i]] + next_range
            if sym > 15:
                next_range = 1
                sym -= 16
            else:
                next_range = 0
            summary.insert(0, sym)
        for i in range(0, len(summary)):
            summary[i] = (self.dec2hex[summary[i]]).lower()
        result['to_hex_symbol'] = summary

        short_list = []
        short_str = ''
        for i in range(0, len(summary)):
            if summary[i] == '0': continue
            if summary[i] != '0':
                short_list = summary[i:]
                for symb in short_list:
                    short_str = short_str + symb
                break
        result['short'] = short_str
        s_str = ''
        for symb in summary:
            s_str = s_str + symb
        result['long'] = s_str

        return result

    def subtraction_num(self, list_num_1, list_num_2):
        result = {}
        substracty = []
        next_range = 0
        for i in range(len(list_num_1)-1, -1, -1):
            sym = self.hex2dec[list_num_1[i]] - self.hex2dec[list_num_2[i]] - next_range
            if sym < 0:
                next_range = 1
                sym += 16
            else:
                next_range = 0
            substracty.insert(0, sym)
        #print(substracty)
        for i in range(0, len(substracty)):
            substracty[i] = (self.dec2hex[substracty[i]]).lower()
        #print(summary)
        result['to_hex_symbol'] = substracty

        short_list = []
        short_str = ''
        for i in range(0, len(substracty)):
            if substracty[i] == '0': continue
            if substracty[i] != '0':
                short_list = substracty[i:]
                for symb in short_list:
                    short_str = short_str + symb
                break
        result['short'] = short_str
        s_str = ''
        for symb in substracty:
            s_str = s_str + symb
        result['long'] = s_str


        return result

    def multiplication_num(self, d_first, d_twice):
        if d_first['znak'] == d_twice['znak']:
            znak = '+'
        else:
            znak = '-'
        result = {}
        multy = []
        list_num_1 = d_first['to_hex_symbol']
        list_num_2 = d_twice['to_hex_symbol']

        count_razr = 0

        to_summation = []
        for i_2 in range(len(list_num_2)-1, -1, -1):
            next_range = 0
            staff_multy = []
            for i_1 in range(len(list_num_1)-1, -1, -1):
                mul = self.hex2dec[list_num_1[i_1]] * self.hex2dec[list_num_2[i_2]] + next_range
                if mul > 15:
                    next_range = mul//16
                    mul = int(mul % 16)
                else:
                    next_range = 0
                staff_multy.insert(0, mul)

            for i in range(0, count_razr):
                staff_multy.append(0)
                staff_multy.remove(0)
            count_razr += 1
            to_hex = []
            for i in range(0, len(staff_multy)):
                staff_multy[i] = (self.dec2hex[staff_multy[i]]).lower()
            to_summation.append(staff_multy)
        #print(to_summation)

        multy = to_summation[0]
        staff_dict = {}
        for i in range(1, len(to_summation)-1):
            staff_dict = self.summation_num(multy, to_summation[i])
            multy = staff_dict['to_hex_symbol']

        result = staff_dict
        result['znak'] = znak
        # print(result.keys())
        # print(result.values())
        return result

    def division_num(self, d_first, d_twice):
        result = {}
        if d_first['znak'] == d_twice['znak']:
            znak = '+'
        else:
            znak = '-'
        delimoe_list = []
        delitel_list = []
        for sym in d_first['short']:
            delimoe_list.append(self.hex2dec[sym])
        #print(delimoe_list)

        for sym in d_twice['short']:
            delitel_list.append(self.hex2dec[sym])
        #print(delitel_list)

        num_1 = 0
        razr = 0
        for i in range(len(delimoe_list)-1, -1, -1):
            # print(i)
            num_1 += delimoe_list[i]*(16**razr)
            razr+=1
        #print(num_1, 'delimoe')
        num_2 = 0
        razr = 0
        for i in range(len(delitel_list)-1, -1, -1):
            #print(i)
            num_2 += delitel_list[i]*(16**razr)
            razr+=1
        #print(num_2, 'delitel')

        chastnoe = num_1 // num_2
        #print(chastnoe, 'chastnoe')

        hex_chastn = (hex(chastnoe))[2:]
        #print(hex_chastn, 'hex_chastn', type(hex_chastn))
        result = (self.change_to_blocks(znak, hex_chastn, '+', '0'))['first']
        #print(*result)

        return result

    def calculation(self, dict_nums, oper):
        result = {}

        if (oper == '+'):
            if  (dict_nums['first']['long'] == '00000000000000000000000000000000'):
                result = dict_nums['twice']
            elif dict_nums['twice']['long'] == '00000000000000000000000000000000':
                result = dict_nums['first']

            elif (dict_nums['first']['znak'] == dict_nums['twice']['znak']) :
                result = self.summation_num(dict_nums['first']['to_hex_symbol'], dict_nums['twice']['to_hex_symbol'])
                result['znak'] = dict_nums['first']['znak']
                #print(result['short'])
            elif (dict_nums['first']['znak'] != dict_nums['twice']['znak']): #разные знаки
                if dict_nums['first']['short'] == dict_nums['twice']['short']: #равны по модулю
                    result = (self.change_to_blocks('0', '+', '0', '+'))['first'] #результат 0
                elif (int(dict_nums['first']['short'], 16)) > (int(dict_nums['twice']['short'], 16)):
                    first_num = dict_nums['first']['to_hex_symbol']
                    twice_num = dict_nums['twice']['to_hex_symbol']
                    result = self.subtraction_num(first_num, twice_num) #вычитание из большего меньшего
                    result['znak'] = dict_nums['first']['znak'] # знак большего
                elif (int(dict_nums['first']['short'], 16)) < (int(dict_nums['twice']['short'], 16)):
                    twice_num = dict_nums['first']['to_hex_symbol']
                    first_num = dict_nums['twice']['to_hex_symbol']
                    result = self.subtraction_num(first_num, twice_num) #вычитание из большего меньшего
                    result['znak'] = dict_nums['twice']['znak'] # знак большего

        elif  (oper == '-'):
            if  (dict_nums['first']['long'] == '00000000000000000000000000000000'):
                result = dict_nums['twice']
            elif dict_nums['twice']['long'] == '00000000000000000000000000000000':
                result = dict_nums['first']

            elif (dict_nums['first']['znak'] != dict_nums['twice']['znak']) :
                result = self.summation_num(dict_nums['first']['to_hex_symbol'], dict_nums['twice']['to_hex_symbol'])
                if (int(dict_nums['first']['short'], 16)) > (int(dict_nums['twice']['short'], 16)):
                    result['znak'] = dict_nums['first']['znak']
                elif (int(dict_nums['first']['short'], 16)) < (int(dict_nums['twice']['short'], 16)):
                    result['znak'] = dict_nums['twice']['znak']
                #print(result['short'])
            elif (dict_nums['first']['znak'] == dict_nums['twice']['znak']):
                if dict_nums['first']['short'] == dict_nums['twice']['short']: #равны по модулю
                    result = (self.change_to_blocks('0', '+', '0', '+'))['first'] #результат 0
                elif (int(dict_nums['first']['short'], 16)) > (int(dict_nums['twice']['short'], 16)):
                    first_num = dict_nums['first']['to_hex_symbol']
                    twice_num = dict_nums['twice']['to_hex_symbol']
                    result = self.subtraction_num(first_num, twice_num) #вычитание из большего меньшего
                    result['znak'] = dict_nums['first']['znak'] # знак большего
                elif (int(dict_nums['first']['short'], 16)) < (int(dict_nums['twice']['short'], 16)):
                    twice_num = dict_nums['first']['to_hex_symbol']
                    first_num = dict_nums['twice']['to_hex_symbol']
                    result = self.subtraction_num(first_num, twice_num) #вычитание из большего меньшего
                    if dict_nums['twice']['znak'] == '+':
                        result['znak'] = '-'
                    elif dict_nums['twice']['znak'] == '-':
                        result['znak'] = '+'
                    #result['znak'] = dict_nums['twice']['znak'] # знак большего

        elif (oper == '*'):
            if ( (dict_nums['first']['long'] == '00000000000000000000000000000000')
                    or dict_nums['twice']['long'] == '00000000000000000000000000000000'):
                result = (self.change_to_blocks('0', '+', '0', '+'))['first'] #результат 0
            else:
                result = self.multiplication_num(dict_nums['first'], dict_nums['twice'])
                #print(result['short'])

        elif (oper == '/'):
            if dict_nums['twice']['long'] == '00000000000000000000000000000000':
                print ('Операция не будет выполнена, деление на 0')
            elif dict_nums['first']['long'] == '00000000000000000000000000000000':
                result = (self.change_to_blocks('0', '+', '0', '+'))['first']
            else:
                result = self.division_num(dict_nums['first'], dict_nums['twice'])

        return result

if __name__ == "__main__":
    calc = CALC()


