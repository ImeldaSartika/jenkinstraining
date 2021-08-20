from selenium import webdriver

def test_setup():
	global driver
	driver = webdriver.Chrome(executable_path="C:/driver/chromedriver.exe")
	driver.maximize_window();

def test_form_entry():
	driver.get("http://localhost/form.php")
	driver.find_element_by_name("nip").send_keys("12345")
	driver.find_element_by_name("nama").send_keys("Imelda Sartika")
	driver.find_element_by_name("nik").send_keys("18022586")
	driver.find_element_by_name("alamat").send_keys("Tangerang")
	driver.find_element_by_name("perusahaan").send_keys("PT Sumber Alfaria Trijaya")
	driver.find_element_by_name("tanggal").send_keys("20/08/2021")
	driver.find_element_by_name("divisi").send_keys("IT Back Office")
	driver.find_element_by_name("posisi").send_keys("Programmer")
	driver.find_element_by_name("gaji").send_keys("1000000")
	driver.find_element_by_name("atasan").send_keys("ADN")
	driver.find_element_by_name("submit").click()

def test_cleanup():
	driver.close()
	driver.quit()
	print("Test Selesai...")