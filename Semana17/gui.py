import actions_transactions,actions_categories,data_handle,file_handle
import PySimpleGUI as sg


def record_expense_window():
    record_transaction_buttons=[[sg.Button('Record',font=('Heebo Light',11),pad=(10,10))]]
    record_transaction_fields=[[sg.Text('Type(*)',font=('Heebo Light',11))],[sg.Input(default_text='Expense',font=('Heebo Light',11),key='-INPUT_TYPE-',disabled=True)],[sg.Text('Category(*)',font=('Heebo Light',11))],[sg.Input(key='-INPUT_CATEGORY-',font=('Heebo Light',11))],[sg.Text('Description(*)',font=('Heebo Light',11))],[sg.Input(key='-INPUT_DESCRIPTION-',font=('Heebo Light',11))],[sg.Text('Date(*)',font=('Heebo Light',11))],[sg.Input(key='-DATE-',disabled=True,font=('Heebo Light',11))],[sg.CalendarButton('Select a date',format='%Y-%m-%d',target='-DATE-',key='-CALENDAR-',font=('Heebo Light',11))],[sg.Text('Amount(*)',font=('Heebo Light',11))],[sg.Input(key='-INPUT_AMOUNT-',default_text=0,font=('Heebo Light',11),enable_events=True)]]
    record_transaction_layout=[[sg.Frame('Data form',record_transaction_fields)],[sg.Frame('Buttons',record_transaction_buttons,size=(250,70))]]
    record_expense_wdw=sg.Window('Record an Expense',record_transaction_layout)
    return record_expense_wdw


def record_income_window():
    record_transaction_buttons=[[sg.Button('Record',font=('Heebo Light',11),pad=(10,10))]]
    record_transaction_fields=[[sg.Text('Type(*)',font=('Heebo Light',11))],[sg.Input(default_text='Income',font=('Heebo Light',11),key='-INPUT_TYPE-',disabled=True)],[sg.Text('Category(*)',font=('Heebo Light',11))],[sg.Input(key='-INPUT_CATEGORY-',font=('Heebo Light',11))],[sg.Text('Description(*)',font=('Heebo Light',11))],[sg.Input(key='-INPUT_DESCRIPTION-',font=('Heebo Light',11))],[sg.Text('Date(*)',font=('Heebo Light',11))],[sg.Input(key='-DATE-',disabled=True,font=('Heebo Light',11))],[sg.CalendarButton('Select a date',format='%Y-%m-%d',target='-DATE-',key='-CALENDAR-',font=('Heebo Light',11))],[sg.Text('Amount(*)',font=('Heebo Light',11))],[sg.Input(key='-INPUT_AMOUNT-',default_text=0,font=('Heebo Light',11),enable_events=True)]]
    record_transaction_layout=[[sg.Frame('Data form',record_transaction_fields)],[sg.Frame('Buttons',record_transaction_buttons,size=(250,70))]]
    record_income_wdw=sg.Window('Record an Income',record_transaction_layout)
    return record_income_wdw


def record_category_window():
    record_category_buttons=[[sg.Button('Record',font=('Heebo Light',11))]]
    record_category_fields=[[sg.Text('Category name(*)',font=('Heebo Light',11))],[sg.Input(key='-INPUT_CATEGORY_NAME-',font=('Heebo Light',11))],[sg.Text('Transaction Type(*)',font=('Heebo Light',11))],[sg.Combo(['Expense','Income'],key='-COMBO_TRANSACTION_TYPE-',font=('Heebo Light',11))],[sg.Text('Description(*)',font=('Heebo Light',11))],[sg.Input(key='-INPUT_CATEGORY_DESCRIPTION-',font=('Heebo Light',11))]]
    record_category_layout=[[sg.Frame('Data form',record_category_fields)],[sg.Frame('Button',record_category_buttons)]]
    record_category_wdw=sg.Window('Record a New Category',record_category_layout)
    return record_category_wdw


def main_window(my_list,headers,file_path):
    menu_def=[['Tools',['Record an Expense','Record an Income','Record a Category','Exit']]]

    if actions_transactions.import_file(my_list,file_path)==None:
        record_table=sg.Table(values="",headings=["TYPE","CATEGORY","DESCRIPTION","DATE","AMOUNT"],auto_size_columns=True,font=('Heebo Light',11),justification='center',key='-TABLE-')
        my_list=[]
    else:
        my_list=[]
        if file_handle.read_file(file_path):
            record_table=sg.Table(values="",headings=["TYPE","CATEGORY","DESCRIPTION","DATE","AMOUNT"],auto_size_columns=True,font=('Heebo Light',11),justification='center',key='-TABLE-')
        else:
            record_table=sg.Table(values=data_handle.structuring_file_to_import(actions_transactions.import_file(my_list,file_path),headers),auto_size_columns=True,font=('Heebo Light',11),justification='center',headings=["TYPE","CATEGORY","DESCRIPTION","DATE","AMOUNT"],key='-TABLE-')
    
    frame_buttons_layout=[[sg.Button('Record Expense',font=('Heebo Light',11)),sg.Button('Record Income',font=('Heebo Light',11)),sg.Button('Record Category',font=('Heebo Light',11))]]
    frame_layout=[[sg.Text('Main Transactions Table',justification='center',font=('Heebo Bold',12))],[record_table]]

    layout=[[sg.Menu(menu_def)],[sg.Frame('Transaction Journal',frame_layout,size=(550,300))],[sg.Frame('Buttons',frame_buttons_layout,size=(550,70))]]
    main_wdw=sg.Window('Financial Management APP',layout,size=(600,450))
    return main_wdw


def gui_transaction_handler(wdw,wdw1,my_list,headers,file_path,file_path_category):
            my_list=[]
            while True:
                ev2,val2=wdw.Read()
                if ev2=='-INPUT_AMOUNT-' and len(val2['-INPUT_AMOUNT-'])>0:
                    formatted_value=data_handle.format_currency(val2['-INPUT_AMOUNT-'])
                    wdw['-INPUT_AMOUNT-'].update(formatted_value)
                    if val2['-INPUT_AMOUNT-'][-1] not in ('0123456789'):
                        wdw['-INPUT_AMOUNT-'].update(val2['-INPUT_AMOUNT-'][:-1])
                if ev2 in (sg.WIN_CLOSED,None):
                    wdw.Close()
                    win2_active=False
                    break
                if ev2=='Record':
                    str_type=val2['-INPUT_TYPE-']
                    str_category=val2['-INPUT_CATEGORY-']
                    str_description=val2['-INPUT_DESCRIPTION-']
                    str_date=val2['-DATE-']
                    if val2['-INPUT_AMOUNT-']=="":
                        int_amount=0
                    else:
                        int_amount=float(val2['-INPUT_AMOUNT-'].replace("₵",''))
                    if actions_transactions.input_transaction(my_list,str_type,str_category,str_description,str_date,int_amount)==None:
                        sg.popup_error("Transaction cannot be recorded. There are some missing required values (*)")
                    else:
                        if data_handle.filter_csv(file_path_category,str_type)!=None:
                            if data_handle.find_category(str_category,data_handle.filter_csv(file_path_category,str_type))==False:
                                sg.popup_ok("Category cannot be added, it does not exist. Please add category in Record Category Button")
                                my_list=[]
                            else:
                                print(my_list)
                                actions_transactions.import_file(my_list,file_path)
                                file_handle.export_file(data_handle.structuring_file_to_export(my_list,headers),headers,file_path)
                                wdw1['-TABLE-'].update(values=data_handle.structuring_file_to_import(my_list,headers))
                                sg.popup_ok("Transaction successfully recorded!!!")
                                my_list=[]
                        else:
                                sg.popup_error("File database_categories does not exist. Please first create a New Category")


def main_gui(my_list,category_list):
    headers_category=('Name','Transaction Type','Description')
    file_path_categories="C:/Users/default.LAPTOP-SHSSKNRP/OneDrive/INVERSIONES/Escritorio/Programas/Semana10/DUAD_My-Tech-Transformation-Journal/Semana17/database_categories.csv"

    headers_transactions=('Type','Category','Description','Date','Amount')
    file_path_transactions="C:/Users/default.LAPTOP-SHSSKNRP/OneDrive/INVERSIONES/Escritorio/Programas/Semana10/DUAD_My-Tech-Transformation-Journal/Semana17/database.csv"
    

    sg.theme('LightGrey1')
    window1=main_window(my_list,headers_transactions,file_path_transactions)
    win2_active=False
    win3_active=False
    win4_active=False
    while True:
        ev1,val1=window1.Read(timeout=100) 
        if ev1==sg.WIN_CLOSED or ev1=='Exit':
            break
        #Record an Expense
        if ev1=='Record Expense' or ev1=='Record an Expense':
            window2=record_expense_window()
            gui_transaction_handler(window2,window1,my_list,headers_transactions,file_path_transactions,file_path_categories)
        #Record an Income
        if ev1=='Record Income' or ev1=='Record an Income':
            window4=record_income_window()
            gui_transaction_handler(window4,window1,my_list,headers_transactions,file_path_transactions,file_path_categories)
        #Record a Category
        if ev1=='Record Category':
            win3_active=True
            if win2_active:
                window2.Hide()
            if win4_active:
                window4.Hide()
            window3=record_category_window()
            while True:
                ev3,val3=window3.Read()
                if ev3=='Record':
                    str_category_name=val3['-INPUT_CATEGORY_NAME-']
                    str_transaction_type=val3['-COMBO_TRANSACTION_TYPE-']
                    str_description=val3['-INPUT_CATEGORY_DESCRIPTION-']
                    if actions_categories.input_category(category_list,str_category_name,str_transaction_type,str_description)==None:
                        sg.popup_error("Category cannot be added. There are some missing required values (*)")
                    else:
                        if data_handle.filter_csv(file_path_categories,str_transaction_type)!=None:
                            if data_handle.find_category(str_category_name,data_handle.filter_csv(file_path_categories,str_transaction_type))==True: 
                                sg.popup_error("Categories names are repeated, this category name cannot be added")
                                category_list=[]
                        sg.popup_ok("Category successfully created!!!")
                        actions_categories.import_file(category_list,file_path_categories)
                        file_handle.export_file(data_handle.structuring_file_to_export(category_list,headers_category),headers_category,file_path_categories)
                        category_list=[]
                if ev3 in (sg.WIN_CLOSED,None):
                    window3.Close()
                    break