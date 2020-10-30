def solution(m, musicinfos):
    mel = ''
    df = [0, "(None)"]
    for mm in list(m):
        if mm.isalpha():
            mel += ' '
        mel += mm
    mel += ' '
    for music in musicinfos:
        st, end, name, sheet = music.split(',')
        st, end = list(map(int, st.split(':'))), list(map(int, end.split(':')))
        time = end[0]*60 + end[1] - st[0]*60 - st[1]
        sheet = full_sheet(time, sheet)
        if sheet.find(mel) != -1:
            if time > df[0]:
                df = [time, name, sheet]
    return df[1]


def full_sheet(time, sheet):
    cnt = 0
    ret = ''
    fin = False
    while not fin:
        for s in list(sheet):
            if s.isalpha():
                ret += ' '
                cnt += 1
                if cnt > time:
                    fin = True
                    break
            ret += s
    return ret
