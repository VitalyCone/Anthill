import pandas as ps
import openpyxl
import datetime
from openpyxl.styles import Alignment, Font
from openpyxl.chart import LineChart, Reference


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
    n = len(data['Number of tic'])
    not_last_not_filled_cell = None
    k = 0

    data_1 = {
        'Number of tic': data.get('Number of tic')[0:n-1],
        'Average energy of ant':
            data.get('Average energy of ant')[0:n-1],
        'Accumulated energy of ants':
            data.get('Accumulated energy of ants')[0:n-1],
        'Average energy of spider':
            data.get('Average energy of spider')[0:n-1],
        'Accumulated energy of spiders':
            data.get('Accumulated energy of spiders')[0:n-1],
        'Energy of anthill':
            data.get('Energy of anthill')[0:n-1],
        'Number of messages':
            data.get('Number of messages')[0:n-1],
        'Number of ants':
            data.get('Number of ants')[0:n-1],
        'Number of spiders':
            data.get('Number of spiders')[0:n-1],
        'Number of apples':
            data.get('Number of apples')[0:n-1]
    }

    df = ps.DataFrame(data_1)

    df.to_excel('export/' + name, index=False)

    workbook = openpyxl.load_workbook('export/' + name)
    worksheet = workbook.active

    for cell in worksheet.iter_cols(min_row=1, max_row=1, min_col=1,
                                    max_col=len(data) + 2):  # worksheet[1] обращается к первой строке
        if cell[0].value:
            cell[0].alignment = Alignment(wrapText=True, horizontal='center', vertical='center')
            cell[0].font = Font(bold=True)
            worksheet.column_dimensions[cell[0].column_letter].width += 5

        if cell[0].value is None:
            k += 1
        if cell[0].value is None and k == 2:
            not_last_not_filled_cell = cell[0]
            k = 0

    for line in range(2, n + 2):
        for cell in worksheet[line]:
            cell.alignment = Alignment(horizontal='left')

    num = not_last_not_filled_cell.row + 2

    # График первый
    chart = LineChart()
    chart.title = "Average energy of ant and spiders graph"
    chart.x_axis.title = "Tic"
    chart.y_axis.title = "Energy"

    # Добавление данных на график
    ref_y_1 = Reference(worksheet, min_col=2, min_row=1, max_col=2, max_row=n + 1)
    ref_y_2 = Reference(worksheet, min_col=4, min_row=1, max_col=4, max_row=n + 1)
    ref_x = Reference(worksheet, min_col=1, min_row=2, max_row=n + 1)
    chart.add_data(ref_y_1, titles_from_data=True)
    chart.add_data(ref_y_2, titles_from_data=True)
    chart.set_categories(ref_x)
    cell_name = not_last_not_filled_cell.column_letter + str(num)
    chart.width = 23
    chart.height = 10
    worksheet.add_chart(chart, cell_name)

    # График второй
    num += 20

    chart = LineChart()
    chart.title = "Accumulated energy of ants and spiders graph"
    chart.x_axis.title = "Tic"
    chart.y_axis.title = "Energy"

    # Добавление данных на график
    ref_y_1 = Reference(worksheet, min_col=3, min_row=1, max_col=3, max_row=n + 1)
    ref_y_2 = Reference(worksheet, min_col=5, min_row=1, max_col=5, max_row=n + 1)
    ref_x = Reference(worksheet, min_col=1, min_row=2, max_row=n + 1)
    chart.add_data(ref_y_1, titles_from_data=True)
    chart.add_data(ref_y_2, titles_from_data=True)
    chart.set_categories(ref_x)
    cell_name = not_last_not_filled_cell.column_letter + str(num)
    chart.width = 23
    chart.height = 10
    worksheet.add_chart(chart, cell_name)

    # График третий
    num += 20

    chart = LineChart()
    chart.title = "Graph of energy of anthill"
    chart.x_axis.title = "Tic"
    chart.y_axis.title = "Energy"

    # Добавление данных на график
    ref_y_1 = Reference(worksheet, min_col=6, min_row=1, max_col=6, max_row=n + 1)
    ref_x = Reference(worksheet, min_col=1, min_row=2, max_row=n + 1)
    chart.add_data(ref_y_1, titles_from_data=True)
    chart.set_categories(ref_x)
    cell_name = not_last_not_filled_cell.column_letter + str(num)
    chart.width = 23
    chart.height = 10
    worksheet.add_chart(chart, cell_name)


    # График четвертый
    num += 20

    chart = LineChart()
    chart.title = "Graph of number of messages"
    chart.x_axis.title = "Tic"
    chart.y_axis.title = "Messages"

    # Добавление данных на график
    ref_y_1 = Reference(worksheet, min_col=7, min_row=1, max_col=7, max_row=n + 1)
    ref_x = Reference(worksheet, min_col=1, min_row=2, max_row=n + 1)
    chart.add_data(ref_y_1, titles_from_data=True)
    chart.set_categories(ref_x)
    cell_name = not_last_not_filled_cell.column_letter + str(num)
    chart.width = 23
    chart.height = 10
    worksheet.add_chart(chart, cell_name)

    # График кол-ва муравьев
    num += 20

    chart = LineChart()
    chart.title = "Graph of number ants"
    chart.x_axis.title = "Tic"
    chart.y_axis.title = "Number of ants"

    # Добавление данных на график
    ref_y_1 = Reference(worksheet, min_col=8, min_row=1, max_col=8, max_row=n + 1)
    ref_x = Reference(worksheet, min_col=1, min_row=2, max_row=n + 1)
    chart.add_data(ref_y_1, titles_from_data=True)
    chart.set_categories(ref_x)
    cell_name = not_last_not_filled_cell.column_letter + str(num)
    chart.width = 23
    chart.height = 10
    worksheet.add_chart(chart, cell_name)

    # График кол-ва пауков
    num += 20

    chart = LineChart()
    chart.title = "Graph of number spiders"
    chart.x_axis.title = "Tic"
    chart.y_axis.title = "Number of spiders"

    # Добавление данных на график
    ref_y_1 = Reference(worksheet, min_col=9, min_row=1, max_col=9, max_row=n + 1)
    ref_x = Reference(worksheet, min_col=1, min_row=2, max_row=n + 1)
    chart.add_data(ref_y_1, titles_from_data=True)
    chart.set_categories(ref_x)
    cell_name = not_last_not_filled_cell.column_letter + str(num)
    chart.width = 23
    chart.height = 10
    worksheet.add_chart(chart, cell_name)

    # График кол-ва яблок
    num += 20

    chart = LineChart()
    chart.title = "Graph of number apples"
    chart.x_axis.title = "Tic"
    chart.y_axis.title = "Number of apples"

    # Добавление данных на график
    ref_y_1 = Reference(worksheet, min_col=10, min_row=1, max_col=10, max_row=n + 1)
    ref_x = Reference(worksheet, min_col=1, min_row=2, max_row=n + 1)
    chart.add_data(ref_y_1, titles_from_data=True)
    chart.set_categories(ref_x)
    cell_name = not_last_not_filled_cell.column_letter + str(num)
    chart.width = 23
    chart.height = 10
    worksheet.add_chart(chart, cell_name)

    # Сохранение изменений
    workbook.save('export/' + name)

