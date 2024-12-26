from xml.dom import minidom

# Đọc file XML
doc = minidom.parse('sample.xml')

# Lấy tất cả các phần tử "staff"
staff_nodes = doc.getElementsByTagName('staff')

# In ra tên của từng nhân viên
for staff in staff_nodes:
    staff_name = staff.getElementsByTagName('name')[0].firstChild.nodeValue
    print("Staff Name:", staff_name)
