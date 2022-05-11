from os import listdir, path


def find_all_files(mypath_):
    for file in listdir(mypath_):
        if file.endswith(".txt"):
            make_raw_list(path.join(mypath_, file))
            #  print(path.join(mypath_, file))


def make_raw_list(path_):
    with open(path_, "r") as m:
        m_content = m.read()
        split_cont = m_content.split("\n")
        tmp_work_list = []
        for i in split_cont:
            func_stripped_line = i.strip()
            i_list = func_stripped_line.split("\n")
            tmp_work_list.append(i_list)
    out_list = []
    for i2 in tmp_work_list:
        out_list += i2
    return search_for_log_entries(out_list)


def search_for_log_entries(in_list):
    log_entries = []
    for k, v in enumerate(in_list):
        if v.__contains__('"text": "') and not v.__contains__("lightsleep"):
            if v.__contains__("QSY"):  # Start of code
                #print(f"Start of code: {v[v.find('QSY') + 3:-3]}")
                log_entries.append(v[v.find('QSY') + 3:-3])
            elif v.__contains__("SRN") and v.__contains__("P"):  # Moisture sample
                #print(f"Moisture sample: {v[v.find('SRN') + 3:-3]}")
                log_entries.append(v[v.find('SRN') + 3:-3])
            elif v.__contains__("SQW"):  # Watering
                #print(f"Watering: {v}")
                index_1 = v.find("SQW")
                print(f"WATERRRRR: {v}!!!")
    for foo in log_entries:
        if (foo.__contains__("SRN") and foo.__contains__("QSY")) or (foo.__contains__("\\n")):
            pass
        else:
            if foo.__contains__("P"):
                p = foo.split("P")
                for key, value in enumerate(p):
                    if key == 0:
                        print(f"{value}%")
                    elif key == 1:
                        print(f"{value}˚C")
            else:
                print(f"{((1 / int(foo)) * 1000) * 1000}µHz")


if __name__ == '__main__':
    mypath = "/Users/mattiasbehndig/Library/Thonny/user_logs"
    find_all_files(mypath)
    print((90 % 35))
