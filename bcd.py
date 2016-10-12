def dec2bin(d_num):
    assert d_num >= 0, "cannot convert negative number to binary"
    if d_num == 0:
        return '0'
    b_num = ""
    while d_num > 0:
        b_num = str(d_num%2) + b_num
        d_num = d_num//2
    return b_num
def bin24digit(bin_num):
    res_list = ["0", "0", "0", "0"]
    for i in range(len(bin_num)):
        res_list[len(res_list) - i - 1] = bin_num[len(bin_num) - i - 1]
    return "".join(res_list)

n = "010001100111"
m = "001001000101"
n_len = len(n)
m_len = len(m)
if n_len != m_len:
    o = ""
    if n_len > m_len:
        for i in range(m_len):
            o += "0"
        o += m
        m = o
    if n_len < m_len:
        for i in range(n_len):
            o += "0"
        o += n
        n = o

r = 0
ans = []
final = []
for h in range(len(n)/4):
    ans = []
    for i in range(4):
        x = int(n[len(n) - i - 1 - 4*h])
        y = int(m[len(m) - i - 1 - 4*h])
        part_ans = dec2bin(x + y + r)

        for j in range(len(part_ans)):
            if j==0:
                ans.append(part_ans[len(part_ans) - j - 1])
                r = 0
            if j == 1:
                r = int(part_ans[len(part_ans) - j - 1])
            if i == 3:
                if r == 1:
                    ans.append(str(r))
                    r = 0
    final.append("".join(ans[::-1]))
print final
r = 0
final_answer = []
for item in final:
    if int(item, 2) >= 10:
        n = item
        m = "0110"
        ans = []
        for i in range(4):
            x = int(n[len(n) - i - 1])
            y = int(m[len(m) - i - 1])
            print "r: %d/ x: %d/ y: %d" %(r,x,y)
            part_ans = dec2bin(x + y + r)

            for j in range(len(part_ans)):
                if j==0:
                    ans.append(part_ans[len(part_ans) - j - 1])
                    r = 0

                if j == 1:
                    r = int(part_ans[len(part_ans) - j - 1])

                if len(n) == 5 and i == 3:
                    r = int(n[0])

        final_answer.append("".join(ans[::-1]))
    else:
        if r == 1:
            ans = []
            n = item
            m = "0000"
            for i in range(4):
                x = int(n[len(n) - i - 1])
                y = int(m[len(m) - i - 1])
                print "r: %d/ x: %d/ y: %d" %(r,x,y)
                part_ans = dec2bin(x + y + r)

                for j in range(len(part_ans)):
                    if j==0:
                        ans.append(part_ans[len(part_ans) - j - 1])
                        r = 0

                    if j == 1:
                        r = int(part_ans[len(part_ans) - j - 1])

                    if len(n) == 5 and i == 3:
                        r = int(n[0])

            final_answer.append("".join(ans[::-1]))
        else:
            final_answer.append(item)
answer = "".join(final_answer[::-1])
print answer
print "ENd Carry: %d" % r
ans = ""
ans += str(r)
for i in range(len(answer)/4):
    ans += str(int(answer[i*4:(i+1)*4], 2))
print ans






