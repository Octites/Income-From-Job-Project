job = input('What is your job? ')
per_hour = float(input('How much money do you make per hour? '))
hours_w = int(input('How many hours have you worked this week? '))
a_p_w = (per_hour*hours_w)
a_p_m = (per_hour*hours_w*4)
a_p_y = (per_hour*hours_w*52)

print(f'With a job as a {job}, you make {a_p_w} in one week, {a_p_m} in one month, and you make {a_p_y} in one year.')
