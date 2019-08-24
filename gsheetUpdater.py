# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.0.5
import gspread
from oauth2client.service_account import ServiceAccountCredentials

api_urls = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', api_urls)
worksheet_name = "meat-fridge"

def open_worksheet():
    gc = gspread.authorize(creds)
    sheet = gc.open('meat-fridge').sheet1
    return sheet

def find_last_row(worksheet):
    rows = worksheet.col_values(1)
    
    return len(rows)

def update_record(time,temp,humidity):
    
    worksheet = open_worksheet()
    empty_row = find_last_row(worksheet) + 1
    
    worksheet.update_cell(empty_row, 1, time)
    worksheet.update_cell(empty_row, 2, temp)
    worksheet.update_cell(empty_row, 3, humidity)
