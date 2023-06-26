#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for n in range(0, list_length):
        x = 0
        try:
            x = my_list_1[n] / my_list_2[n]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            result.append(x)
    return result
