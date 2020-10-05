def solution(string, markers):
    s_list = string.split("\n")
    no_comment = ""
    comment = False
    for s, i in zip(s_list, range(0, len(s_list))):
        for j in range(0, len(s)):
            if s[j] in markers:
                no_comment += s[0:j].strip()
                if i != len(s_list)-1:
                    no_comment += "\n"
                comment = True
                break
        if comment:
            comment = False
        else:
            no_comment += s.strip()
            if i != len(s_list)-1:
                no_comment += "\n"
    return no_comment


print(solution("apples, pears # and bananas\ngrapes\nbananas !apples",
               ["#", "!"]))
