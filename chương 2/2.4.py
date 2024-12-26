from xml.dom import minidom

# Đọc và phân tích file XML
doc = minidom.parse('sample.xml')

# Lấy tên công ty
company_name = doc.getElementsByTagName('name')[0].firstChild.nodeValue
print("Company Name:", company_name)

# Lấy thông tin các nhân viên
staff_nodes = doc.getElementsByTagName('staff')
for staff in staff_nodes:
    staff_name = staff.getElementsByTagName('name')[0].firstChild.nodeValue
    staff_salary = staff.getElementsByTagName('salary')[0].firstChild.nodeValue
    print(f"Staff: {staff_name}, Salary: {staff_salary}")
