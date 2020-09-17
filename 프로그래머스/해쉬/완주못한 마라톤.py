def solution(participant, completion):
    participant.sort()
    completion.sort()
    for _ in range(len(completion)):
        if participant[_] != completion[_]:
            return participant[_]
        else:
            pass
    return participant[-1]
