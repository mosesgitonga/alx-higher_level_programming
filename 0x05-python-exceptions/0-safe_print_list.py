#/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for elem in my_list[:x]:
            if isinstance(elem, int):
                print("{:d}".format(elem), end = "")
                
                count += 1

                if count == x:
                    break
        print()
    except TypeError:
        pass
    return count
