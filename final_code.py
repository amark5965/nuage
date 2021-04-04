from itertools import zip_longest
import threading

list1 = ["","","","","","","",""]

def reverse_char(char):
    if char.isalpha():
        if char.isupper():
            return chr(ord('A')+ord('Z')-ord(char))
        else:
            return chr(ord('a')+ord('z')-ord(char))
    return char


def list_object(line_number, line):
    list1[line_number] = line

def process_line(line_number, line):
    a = map(reverse_char,line)
    line = ''.join(list(a))
    # print(line)
    list_object(line_number,line)


def write_to_file(list1,file_name):
    line = "".join(list1)
    with open(file_name,'+a') as f:
        f.write(line)

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

if __name__ ==  '__main__':
    with open('output.txt','+w')as f:
        pass
    with open("input.txt") as f:
        for lines in grouper(f, 8, ''):
            assert len(lines) == 8
            processes = []
            list1 = ["","","","","","","",""]
            for i in range(8):
                process = threading.Thread(target=process_line,args=(i,lines[i]))
                processes.append(process)
                process.start()
            for proc in processes:
                proc.join()
            write_to_file(list1,"output.txt")