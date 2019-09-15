import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class WwOrgSearch(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome("/Users/lokgayak/PycharmProjects/Hello_Aadhu/chromedriver")

    def test_search_in_ww_org(self):
        driver = self.driver
        driver.get("https://www.weightwatchers.com/us/")
        self.assertIn("WW (Weight Watchers): Weight Loss & Wellness Help", driver.title)
        driver.find_element_by_link_text("Find a Studio").click()
        time.sleep(5)
        # self.assertIn("Find WW Studios & Meetings Near You | WW USA", driver.title)
        elem1 = driver.find_element_by_id("meetingSearch")
        elem1.clear()
        elem1.send_keys("10011")
        elem1.send_keys(Keys.RETURN)
        assert "No Result Found" not in driver.page_source

        for dev in driver.find_elements_by_class_name("meeting-locations-list"):
            temp = driver.find_element_by_class_name("location__name")
            val_1 = temp.text
            # print(val_1)
            temp.click()
            temp1 = driver.find_element_by_class_name("location__name")
            val_2 = temp1.text
            # print(val_2)
            if val_1 == val_2:
                print("MATCHED, Displayed location name/title matches with the name of the first searched result")
            else:
                print("Mismatched, Displayed location name/title matches with the name of the first searched result")

        x = driver.find_elements_by_xpath("/html/body/div[3]/div/div[2]/div/div/ui-view/ui-view/div[1]/div[2]/div/div/div[2]/div[1]/hours-list/ul")
        for i in x:
            current_log = i.find_elements_by_xpath("/html/body/div[3]/div/div[2]/div/div/ui-view/ui-view/div[1]/div[2]/div/div/div[2]/div[1]/hours-list")
            for j in current_log:
                curr_day = j.find_element_by_css_selector("#content > div > div > ui-view > ui-view > div.meeting-detail > div.meeting-detail-bottom-container.container-fluid > div > div > div.meeting-detail-bottom-bottom.meeting-detail-bottom-bottom--no-cancellations.meeting-detail-bottom-bottom--has-hours.meeting-detail-bottom-bottom--no-leaders.meeting-detail-bottom-bottom--has-notes > div.meeting-hours.meeting-detail-bottom-section.meeting-hours--count-7 > hours-list > ul > li:nth-child(1) > div").text
                print("TODAY’s hours of operation - ")
                print(curr_day)
        current_day = curr_day.split('\n')

        #Print meeting scheduled for a person on current day
        a = driver.find_elements_by_class_name("schedule-detailed-day")
        for i in a:
            cd = i.find_element_by_class_name("schedule-detailed-day-label").text
            # print(cd)
            if cd == current_day[0]:
                y = i.find_elements_by_class_name("schedule-detailed-day-meetings")
                for b in y:
                    z = b.find_elements_by_class_name("schedule-detailed-day-meetings-item")
                    temp = []
                    count = 0
                    for k in z:
                        # count = 0
                        leader = k.find_element_by_class_name("schedule-detailed-day-meetings-item-leader").text
                        temp.append(leader)
                    # c = 0
                    temp_c = []
                    print("Number of meeting the each person(under the scheduled time) has on current day of the week - ")
                    for c in range(0, len(temp)):
                        if temp[c] not in temp_c:
                            temp_c.append(temp[c])
                            count_l = temp.count(temp[c])
                            print(temp[c], count_l)
                            # print(count_l)

        #printMeeting(day) for a person
        selected_day = input("Please enter a day of week(Format - MON, TUE, WED, THU, FRI, SAT or SUN) to get the number of meeting scheduled for a person: \n")
        a = driver.find_elements_by_class_name("schedule-detailed-day")
        for i in a:
            cd = i.find_element_by_class_name("schedule-detailed-day-label").text
            # print(cd)
            if cd == selected_day:
                y = i.find_elements_by_class_name("schedule-detailed-day-meetings")
                for b in y:
                    z = b.find_elements_by_class_name("schedule-detailed-day-meetings-item")
                    temp = []
                    count = 0
                    for k in z:
                        # count = 0
                        leader = k.find_element_by_class_name("schedule-detailed-day-meetings-item-leader").text
                        temp.append(leader)
                    # c = 0
                    temp_c = []
                    print("Number of meeting the each person(under the scheduled time) has on selected day of the week - ")
                    for c in range(0, len(temp)):
                        if temp[c] not in temp_c:
                            temp_c.append(temp[c])
                            count_l = temp.count(temp[c])
                            print(temp[c], count_l)
                            # print(count_l)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
