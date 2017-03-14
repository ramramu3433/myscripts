from selenium import webdriver
import unittest

class test(unittest.TestCase):
   def testing(self):
      self.driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true' ])
      self.driver.set_window_size(1120, 550)
      self.driver.get("https://testl.prosol-envtd.isdcs.co.za/")
#print driver.title
#   def titletest(self):
      self.assertIn('form',self.driver.title)
#   def urltest(self):  
      self.driver.find_element_by_name('name').send_keys("janakiraman")
      #self.driver.find_element_by_xpath("//form[input/@name='name']").send_keys("janakiraman")
      self.driver.find_element_by_name('phone').send_keys("9176724389")
      self.driver.find_element_by_xpath("//form[button]").click()
      self.assertIn("https://testl.prosol-envtd.isdcs.co.za/", self.driver.current_url)
      self.driver.quit()


if __name__=='__main__':
  unittest.main()
