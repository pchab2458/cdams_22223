# **************** #
# GLOBAL VARIABLES #
# **************** #

import os

# APPLICATION DETAIL
app_name = 'Apartment Management System (AMS): CDAMS_REV2'
app_version = 'cdams_rev2: 10 Feb 23'

# APARTMENT DETAIL
apartment_name_thai = 'ชลลดา อพาร์ตเมนต์'
apartment_name_eng = 'Chollada Apartment'

# apartment_address_thai = '3/44 ซอย เธียรสวน 1, ถนน พหลโยธิน, เขต สายไหม, กรุงเทพมหานคร 10220, Tel: 5522494, HP: 089-8814303'
apartment_address_thai = '3/44 ซอย พหลโยธิน 54 แยก 6, แขวง คลองถนน, เขต สายไหม, กรุงเทพมหานคร 10220, โทร. 089-8814303'
apartment_address_eng = 'Chollada Apartment 3/44 Soi Phahonyothin 54 Thiansuan 1, Klongthanon, Sai Mai, Bangkok 10220, HP: 089-8814303'

# SMS MESSAGE APP DATA ***********************************************************************************************

Account_SID = "ACc0952101a0fc649b2c9646f9ff79ac2a"
Auth_Token = "cfdaf8c4f098369aa9977692ec0ce5ad"
Sending_Phone_No = "+12532017565"
# Sending_Phone_No = "Chollada-AT"

SMS_TO_ALL_ROOMS = True

# ********************************************************************************************************************

# ROOM ACCESSORY DISCOUNT
RM_ACC_DISC = 0

# LATE_FEE PARAMETERS:

LATE_DAY_MAX = 6
LATE_FEE_PER_DAY = 50  # TRUN OFF 50*0: TURN ON: 50

# COMMON SERVICE CHARGE (5 B/UNIT)
COMMOM_SERVICE_CPU = 5 * 0 # O: TRUN OFF 1: TURN ON

# BANK INFO. ********************************************************************************************************

# bank_info = 'สามารถเลือกชำระโดยโอนเข้าบัญชี นาย ปรีชา บุตรวิชา ธนาคารกรุงเทพ เลขที่บัญชี 935-002324-9'
# bank_info = ' สามารถเลือกชำระโดยโอนเข้าบัญชี นาง ชลลดา บุตรวิชา ธนาคารกสิกรไทย บัญชี 023-2-97733-7, ธนาคารกรุงเทพ บัญชี 935-002324-9'
# bank_info = ' (สามารถเลือกชำระโดยโอนเข้าบัญชี นาง ชลลดา บุตรวิชา ธนาคารกรุงเทพ เลขที่บัญชี 935-002324-9)'
# bank_info = ' (ชำระเป็นเงินสด หรือเลือกชำระโดยโอนเข้าบัญชี นาง ชลลดา บุตรวิชา ธนาคารกรุงเทพ เลขที่บัญชี 935-002324-9)'

# bank_info = ' (ชำระเป็นเงินสด หรือโอนเข้าบัญชี นาง ชลลดา บุตรวิชา ธนาคารกรุงเทพ เลขบัญชี 935-00232
bank_info = ' (ชำระเป็นเงินสด หรือโอนเข้าบัญชี นาย ธีรวุฒิ บุตรวิชา ธนาคารไทยพาณิชย์(SCB) เลขบัญชี 026-463996-8)'

bank_info_2 = ' (ชำระเป็นเงินสด หรือโอนเข้าบัญชี นาง ชลลดา บุตรวิชา ธนาคารกรุงเทพ เลขบัญชี 935-002324-9) จ่ายหลังกำหนด จะมีค่าปรับ 50 บาท/วัน โดยจะถูกรวมในค่าเช่าของเดือนถัดไป '

# *******************************************************************************************************************

# excel_file_path = "C:\\Users\\pboot\\cdams_excel"

# excel_file_new_ac = "new_account.xlsx"
# excel_file_ew_con = "elec_water_consumption.xlsx"



# Excel Files to be uploaded to PythonAnywher: **********************************************************************

excel_file_path = "C:\\Users\\pboot\\cdams_excel"
excel_file_new_ac = "new_account.xlsx"
excel_file_ew_con = "elec_water_consumption.xlsx"

