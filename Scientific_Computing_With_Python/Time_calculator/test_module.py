import unittest
from time_calculator import add_time
class UnitTests(unittest.TestCase):
  def test_same_day_zone(self):
    self.assertEqual(add_time("3:00 PM", "3:00"), "6:00 PM")

  def test_with_days(self):
    self.assertEqual(add_time("3:00 PM", "3:00", "Wednesday"), "6:00 PM, Wednesday")

  def test_with_lower_days(self):
    self.assertEqual(add_time("3:00 PM", "3:00", "wednesday"), "6:00 PM, Wednesday")
    
  def test_with_next_day(self):
    self.assertEqual(add_time("11:10 PM", "4:30"), "3:40 AM (next_day)")

  def test_with_week_day_later(self):
    self.assertEqual(add_time("11:43 PM", "48:20", "tueSday"), "12:03 AM, Friday (3 days later)")

  def test_with_days_later(self):
    self.assertEqual(add_time("11:43 PM", "148:20"), "4:03 AM (7 days later)")

  def test_with_week_daylater(self):
    self.assertEqual(add_time("11:43 PM", "4448:20", "monday"), "8:03 AM, Friday (186 days later)")
  
  def test_next_day_zone(self):
    self.assertEqual(add_time("12:43 AM", "00:20"), "1:03 PM")

      
if __name__ == '__main__':
    unittest.main()
