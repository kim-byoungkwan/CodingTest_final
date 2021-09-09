def solution(mid_scores,final_scores):
    answer = []
    answer.append(max(final-mid for mid,final in list(zip(mid_scores,final_scores))))
    
    answer.append(min(final-mid for mid,final in list(zip(mid_scores,final_scores))))    
    return answer


mid_scores = [20,50,40]
final_scores = [10,50,70]
ret = solution(mid_scores,final_scores)
print(ret)
