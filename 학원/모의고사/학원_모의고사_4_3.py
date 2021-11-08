def solution(subway_times,current_time):

    answer = 1000000

    current_time = current_time.split(':')

    total_current = int(current_time[0])*60 + int(current_time[1])

    for i in subway_times:

        time_list = i.split(':')

        total_subway = int(time_list[0])*60 + int(time_list[1])

        if total_current > total_subway:

            continue

        else:

            gap = total_subway - total_current

            if gap < answer:

                answer = gap

    return answer


subway_times = ["05:31","11:59","13:30","23:32"]

subway_times_1 = ["14:31","15:31"]

current_time = "12:00"

current_time_1 = "15:31"


print(solution(subway_times,current_time))




