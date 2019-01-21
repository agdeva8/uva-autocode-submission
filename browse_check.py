from selenium import webdriver
import getpass
import string

problem_id = raw_input('problem id: ')
uva = webdriver.PhantomJS()

uva.get("https://uva.onlinejudge.org")

print "uva opened"

wrongPass = False;
for i in range(3):
    username=raw_input("username: ")
    username_dialog = uva.find_element_by_id('mod_login_username')
    username_dialog.send_keys(username)

    password = getpass.getpass(prompt='Password: ')
    password_dialog = uva.find_element_by_id('mod_login_password')
    password_dialog.send_keys(password)

    login_button = uva.find_element_by_name('Submit')
    login_button.click()
    try:
        uva.find_element_by_class_name('error')
        if(i==2):
            wrongPass=True;
            break;
        print "wrong password or id"
        continue;
    except:
        print "proceeding"
        break;

if(wrongPass):
    raise ValueError("3 incorrect password attempts")
    
page_margin = uva.find_element_by_xpath("/html/body/div[@id='page_margins']/div[@id='page']/div[@id='main']/div[@id='col1']/div[@id='col1_content']")
quick_submit = page_margin.find_element_by_xpath("//div[@class='moduletable']/table/tbody/tr/td/a[@href='https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=25']")
quick_submit.click()

prob_id_dialog = uva.find_element_by_name('localid')
prob_id_dialog.send_keys(problem_id)

lang_button = uva.find_element_by_name('language')
cpp_button = lang_button.find_element_by_xpath('//input[@value=5]')
cpp_button.click()

choose_file_button = uva.find_element_by_xpath("//input[@name='codeupl']")
problem_path = "/home/deva/comptetive_prog/uva/p"+str(problem_id)+".cpp"
choose_file_button.send_keys(problem_path)

submit_button = uva.find_element_by_xpath("//input[@value='Submit']")
submit_button.click();

print "code submitted"
uva.close()

uhunt = webdriver.PhantomJS()
uhunt.get("https://uhunt.onlinejudge.org")

print "uhunt opened"

uhunt.find_element_by_id("u_input").send_keys(username)
uhunt.find_element_by_xpath("//input[@value='Submit']").click()
user_stats = uhunt.find_element_by_xpath("//div[@ng-controller='StatisticsCtrl']").text
user_stat3 = user_stats.replace("\n| discuss","").replace("\ndiscuss\n","\n").replace("\nSolved","\n\nSolved")
user_stat2 = user_stat3.split('\n')[3:-3]
print "got stats"
print "stats are"
print

for i in user_stat2:
    print i

uhunt.close()