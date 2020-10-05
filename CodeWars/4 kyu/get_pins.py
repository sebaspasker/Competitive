def all_options_index(prestring, options, index):
    # TODO
    return ""


def all_options(options):
    return all_options_index("", options, 0)


def get_pins(observed):
    observed_list = list(observed)
    options = []
    for i in range(0, len(observed_list)):
        i_options = []
        i_options.append(int(observed_list[i]))
        if int(observed_list[i]) % 3 == 0 and int(observed_list[i]) != 0:
            i_options.append(int(observed_list[i]) - 1)
        if int(observed_list[i]) % 3 == 1:
            i_options.append(int(observed_list[i]) + 1)
        if int(observed_list[i]) % 3 == 2:
            i_options.append(int(observed_list[i]) + 1)
            i_options.append(int(observed_list[i]) - 1)
        if int(observed_list[i]) < 7 and int(observed_list[i]) != 0:
            i_options.append(int(observed_list[i]) + 3)
        if int(observed_list[i]) > 3 and int(observed_list[i]) != 0:
            i_options.append(int(observed_list[i]) - 3)
        if int(observed_list[i]) == 0:
            i_options.append(8)
        if int(observed_list[i]) == 8:
            i_options.append(0)
        options.append(i_options.copy())
    return all_options(options)


get_pins('8')
get_pins('11')
get_pins('369')
