phone = {1: (0, 0), 2: (0, 1), 3: (0, 2),
         4: (1, 0), 5: (1, 1), 6: (1, 2),
         7: (2, 0), 8: (2, 1), 9: (2, 2),
         '*': (3, 0), 0: (3, 1), '#': (3, 2)
         }


def solution(numbers, hand):
    answer = ''
    tmp_l = '*'
    tmp_r = '#'
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            tmp_l = num
        elif num in [3, 6, 9]:
            answer += 'R'
            tmp_r = num
        else:
            dis_l = abs(phone[tmp_l][0] - phone[num][0]) + \
                abs(phone[tmp_l][1] - phone[num][1])
            dis_r = abs(phone[tmp_r][0] - phone[num][0]) + \
                abs(phone[tmp_r][1] - phone[num][1])
            if dis_r > dis_l:
                answer += 'L'
                tmp_l = num
            elif dis_r < dis_l:
                answer += 'R'
                tmp_r = num
            else:
                answer += hand[0].upper()
                if hand == 'left':
                    tmp_l = num
                else:
                    tmp_r = num
    return answer
