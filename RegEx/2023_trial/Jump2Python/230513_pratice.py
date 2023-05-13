import re

# 주민등록번호 예시
def id_no_regex(data):
    result = []
    for line in data.split("\n"):
        temp1 = line.split(" ")
        temp2 = temp1[1].split("-")
        new_line = temp1[0] + " " + temp2[0] + "-" + "*******"
        result.append(new_line)
    return result

def id_regex(data):
    pat = re.compile("(\d{6})[-]\d{7}")
    return pat.sub("\g<1>-*******", data)


if __name__ == '__main__':
    id_data = """park 800905-1049118\nkim 700905-1059119"""

    print(id_no_regex(id_data))
    print(id_regex(id_data))
