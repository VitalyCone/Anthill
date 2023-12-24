import pandas as ps
import openpyxl
import datetime
from openpyxl.styles import Alignment, Font
from openpyxl.chart import LineChart, Reference
import matplotlib.pyplot as plt

def export_in_excel(data):

    """
    
    data формат:
    data = {
        'Номер тика': tiks,
        'Средние значения энергии всех муравьев': a,
        'Суммарные значения энергии муравьев': b,
        'Средние значения энергии пауков': c,
        'Суммарные значения энергии пауков': d,
        'Значения энергии муравейника': e
    },
    где tiks, a, b, c, d, e - массивы.   
    очень желательно никак не менять последовательность.

    заполнение массива tiks:
    for i in range(1, n+1):
        tiks.append(i)
    где n - кол-во тиков.
    
    """
    name = 'Данные за ' + str(datetime.datetime.today().strftime('%Y.%m.%d-%H_%M')) + '.xlsx'
    n = len(data['Номер тика'])
    not_last_not_filled_cell = None
    k = 0

    df = ps.DataFrame(data)

    df.to_excel('../../export/' + name, index=False)

    workbook = openpyxl.load_workbook( name)
    worksheet = workbook.active

    for cell in worksheet.iter_cols(min_row=1, max_row=1, min_col=1, max_col=len(data)+2):  # worksheet[1] обращается к первой строке
        if cell[0].value:
            cell[0].alignment = Alignment(wrapText=True,horizontal='center', vertical='center')
            cell[0].font = Font(bold=True)
            worksheet.column_dimensions[cell[0].column_letter].width+=5

        if cell[0].value == None:
            k+=1
        if cell[0].value == None and k==2:
            not_last_not_filled_cell = cell[0]
            k=0

    for line in range(2, n+2):
        for cell in worksheet[line]:
            cell.alignment = Alignment(horizontal='left')

    num = not_last_not_filled_cell.row+2

    # График первый
    chart = LineChart()
    chart.title = "График средней энергии пауков и муравьев"
    chart.x_axis.title = "Tic"
    chart.y_axis.title = "Energy"

    # Добавление данных на график
    ref_y_1 = Reference(worksheet, min_col=2, min_row=1, max_col=2, max_row=n+1)
    ref_y_2 = Reference(worksheet, min_col=4, min_row=1, max_col=4, max_row=n+1)
    ref_x = Reference(worksheet, min_col=1, min_row=2, max_row=n+1)
    chart.add_data(ref_y_1, titles_from_data=True)
    chart.add_data(ref_y_2, titles_from_data=True)
    chart.set_categories(ref_x)
    cell_name = not_last_not_filled_cell.column_letter + str(num)
    chart.width = 23
    chart.height = 10
    worksheet.add_chart(chart, cell_name)

    # График второй
    num+=20

    chart = LineChart()
    chart.title = "График суммарной энергии пауков и муравьев"
    chart.x_axis.title = "Tic"
    chart.y_axis.title = "Energy"

    # Добавление данных на график
    ref_y_1 = Reference(worksheet, min_col=3, min_row=1, max_col=3, max_row=n+1)
    ref_y_2 = Reference(worksheet, min_col=5, min_row=1, max_col=5, max_row=n+1)
    ref_x = Reference(worksheet, min_col=1, min_row=2, max_row=n+1)
    chart.add_data(ref_y_1, titles_from_data=True)
    chart.add_data(ref_y_2, titles_from_data=True)
    chart.set_categories(ref_x)
    cell_name = not_last_not_filled_cell.column_letter + str(num)
    chart.width = 23
    chart.height = 10
    worksheet.add_chart(chart, cell_name)

    # График третий
    num+=20

    chart = LineChart()
    chart.title = "График энергии муравейника"
    chart.x_axis.title = "Tic"
    chart.y_axis.title = "Energy"

    # Добавление данных на график
    ref_y_1 = Reference(worksheet, min_col=6, min_row=1, max_col=6, max_row=n+1)
    ref_x = Reference(worksheet, min_col=1, min_row=2, max_row=n+1)
    chart.add_data(ref_y_1, titles_from_data=True)
    chart.set_categories(ref_x)
    cell_name = not_last_not_filled_cell.column_letter + str(num)
    chart.width = 23
    chart.height = 10
    worksheet.add_chart(chart, cell_name)

    # Сохранение изменений
    workbook.save('../../export/' + name)


def data_in_game(data,y_name,x_name):
    plt.close()

    x_values = data.get(x_name)
    y_values = data.get(y_name)

    plt.plot(x_values, y_values, marker=',', linestyle='-')

    plt.xlabel(x_name,fontweight='bold')
    plt.ylabel(y_name,fontweight='bold')
    plt.title(y_name,fontweight='bold')

    plt.savefig('plot.png')
