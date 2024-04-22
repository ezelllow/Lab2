def display_main_menu():
    print("display_main_menu")
def calc_average():
    print("calc_average")
def get_user_input():
    ans=input("Enter some numbers separated by commas (e.g. 5, 67, 32)")
    x = ans.split(",")
    thislist = [float(x)]
    return thislist
def calc_average_temperature(thislist):
    total_num=len(thislist)
    total_sum=sum(thislist)
    avg_value=total_sum/total_num
    return avg_value
def calc_min_max_temperature(thislist):
    max_num=max(thislist)
    min_num=min(thislist)
    min_max_list=[min_num,max_num]
    return min_max_list
def sort_temperature(thislist):
    sorted_list=sorted(thislist)
    return sorted_list
def calc_median_temperature(thislist,sorted_list):
    n=len(sorted_list)
    if n % 2 == 1:
        median = sorted_list[n // 2]
    else:
        middle_right = n // 2
        middle_left = middle_right - 1
        median = (sorted_list[middle_left] + sorted_list[middle_right]) / 2
        return median