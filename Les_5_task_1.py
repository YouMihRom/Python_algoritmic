#Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно
# вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

number_co = int(input("введите количество компаний: "))
companies_name = []
profit_year = []
i = 0
while i < number_co:
    companies_name.append(input(f"Введите наименование {i + 1}й компании: "))
    profit_year.append(sum([float(_) for _ in input('Введите через пробел прибыль в каждом квартале: ').split()]))
    i += 1

profit_mean = sum(profit_year) / len(profit_year)
company_profit_lower_mean = []
company_profit_higher_mean = []
for i in profit_year:
    if i <= profit_mean:
        company_profit_lower_mean.append(companies_name[profit_year.index(i)])
    else:
        company_profit_higher_mean.append(companies_name[profit_year.index(i)])

print(f'Компании, чья прибыль равна или выше средней: {company_profit_higher_mean}')
print(f'Компании, чья прибыль ниже средней: {company_profit_lower_mean}')
