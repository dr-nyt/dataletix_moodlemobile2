from tempfile import mkstemp
from shutil import move
from os import fdopen, remove
import os
import subprocess
import json
import re

class Setup():
    def __init__(self):
        self.meta_data = []
        self.app_name = 'Hana App'
        self.unique_id = 'com.hana.app'
        self.version = '0.0.1'
        self.version_code = '1'
        self.app_description = 'Official app provided by Hana.'
        self.theme_color = '#ffff'
        self.author_name = "Hana Mobile Team"
        self.author_email = "support@hana.com"
        self.author_website = "http://www.hanainc.com"
        self.site_url = "moodlesite.hana.com"
        self.privacy_policy = 'none'

        self.meta_data.append(self.app_name)
        self.meta_data.append(self.unique_id)
        self.meta_data.append(self.version)
        self.meta_data.append(self.version_code)
        self.meta_data.append(self.app_description)
        self.meta_data.append(self.theme_color)
        self.meta_data.append(self.author_name)
        self.meta_data.append(self.author_email)
        self.meta_data.append(self.author_website)
        self.meta_data.append(self.site_url)
        self.meta_data.append(self.privacy_policy)

        self.langs = []
        core_cannotconnect = "Cannot connect: Verify that you have correctly typed the URL and that your site uses Moodle 2.4 or later."
        core_login_checksiteversion = "Check that your site uses Moodle 2.4 or later."
        core_course_activitynotyetviewablesiteupgradeneeded = "Your organisation's Moodle installation needs to be updated."
        core_course_askadmintosupport = "Contact the site administrator and tell them you want to use this activity with the Moodle Mobile app."
        core_login_connecttomoodle = "Connect to Moodle"
        core_login_connecttomoodleapp = "You are trying to connect to a regular Moodle site. Please download the official Moodle app to access this site."
        core_login_connecttoworkplaceapp = "You are trying to connect to a Moodle Workplace site. Please download the Moodle Workplace app to access this site."
        core_login_erroraccesscontrolalloworigin = "The cross-origin call you're trying to perform has been rejected. Please check https://docs.moodle.org/dev/Moodle_Mobile_development_using_Chrome_or_Chromium",
        core_login_helpmelogin = "<p>There are many thousands of Moodle sites around the world. This app can only connect to Moodle sites that have specifically enabled Mobile app access.</p><p>If you can't connect to your Moodle site then you need to contact your site administrator and ask them to read <a href=\"http://docs.moodle.org/en/Mobile_app\" target=\"_blank\">http://docs.moodle.org/en/Mobile_app</a></p><p>To test the app in a Moodle demo site type <i>teacher</i> or <i>student</i> in the <i>Site address</i> field and click the <b>Connect button</b>.</p>"
        core_login_invalidmoodleversion = "Invalid Moodle version. The minimum version required is 2.4."
        core_login_legacymoodleversion = "You are trying to connect to an unsupported Moodle version. Please download the Moodle Classic app to access this Moodle site."
        core_login_legacymoodleversiondesktop = "You are trying to connect to <b>{{$a}}</b>.<br><br>This site is running an outdated unsupported version of Moodle which will not work with this Moodle Desktop App.<br><br>If this is your site please contact your local moodle partner to get assistance to update it.<br><br>See <a href=\"https://moodle.com/contact\">our contact page</a> to submit a request for assistance."
        core_login_newsitedescription = "Please enter the URL of your Moodle site. Note that it might not be configured to work with this app."
        core_login_siteurlrequired = "Site URL required i.e <i>http://www.yourmoodlesite.org</i>"
        assets_mimetypes_application_vnd_moodle_backup = "Moodle backup"

        self.langs.append(core_cannotconnect)
        self.langs.append(core_login_checksiteversion)
        self.langs.append(core_course_activitynotyetviewablesiteupgradeneeded)
        self.langs.append(core_course_askadmintosupport)
        self.langs.append(core_login_connecttomoodle)
        self.langs.append(core_login_connecttomoodleapp)
        self.langs.append(core_login_connecttoworkplaceapp)
        self.langs.append(core_login_erroraccesscontrolalloworigin)
        self.langs.append(core_login_helpmelogin)
        self.langs.append(core_login_invalidmoodleversion)
        self.langs.append(core_login_legacymoodleversion)
        self.langs.append(core_login_legacymoodleversiondesktop)
        self.langs.append(core_login_newsitedescription)
        self.langs.append(core_login_siteurlrequired)
        self.langs.append(assets_mimetypes_application_vnd_moodle_backup)

        self.temp_langs = self.langs.copy()
    
    def main_menu(self):
        print("""
        ////////////////////////////////////////////////////////////////
        ////////////////////////////////////////////////////////////////
        ////                                                        ////
        ////        ███████╗███████╗████████╗██╗   ██╗██████╗       ////
        ////        ██╔════╝██╔════╝╚══██╔══╝██║   ██║██╔══██╗      ////
        ////        ███████╗█████╗     ██║   ██║   ██║██████╔╝      ////
        ////        ╚════██║██╔══╝     ██║   ██║   ██║██╔═══╝       ////
        ////        ███████║███████╗   ██║   ╚██████╔╝██║           ////
        ////        ╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝           ////
        ////                                                        ////
        ////////////////////////////////////////////////////////////////
        ////////////////////////////////////////////////////////////////""")
        while(True):
            print("")
            print("[NOTICE] Make sure to run this script in administration!")
            print("Please select one of the following options:")
            print("[1] Setup a new build.")
            print("[2] Recompile this build.")
            print("[3] Reset Project to default settings.")
            ans = input('> ')

            if(ans == "1"):
                print("")
                print("Would you like to reset the project files? (recommended)")
                print("The following files will be affected:")
                print("config.xml")
                print('src/config.json')
                print('package.json')
                print('google-services.json')
                while(True):
                    y = input('(Y/n) > ')

                    if(y.lower() == "y" or y.lower() == "yes"):
                        self.reset_project()
                        break
                    elif(y.lower() == "n" or y.lower() == "no"):
                        break

                app_name = input(f'App Name ({self.app_name}): ')
                unique_id = input(f'App Unique ID ({self.unique_id}): ')
                version = input(f'App Version ({self.version}): ')
                version_code = input(f'App Version Code ({self.version_code}): ')
                app_description = input(f'App Description ({self.app_description}): ')
                theme_color = input(f'App Theme Color ({self.theme_color}): ')
                author_name = input(f'Author Name ({self.author_name}): ')
                author_email = input(f'Author Email ({self.author_email}): ')
                author_website = input(f'Author Website ({self.author_website}): ')
                site_url = input(f'Pre-set Site URL (optional) ({self.site_url}): ')
                privacy_policy = input(f'Privacy Policy (optional) ({self.privacy_policy}): ')

                self.set_meta_data(app_name, 0)
                self.set_meta_data(unique_id, 1)
                self.set_meta_data(version, 2)
                self.set_meta_data(version_code, 3)
                self.set_meta_data(app_description, 4)
                self.set_meta_data(theme_color, 5)
                self.set_meta_data(author_name, 6)
                self.set_meta_data(author_email, 7)
                self.set_meta_data(author_website, 8)
                self.set_meta_data(site_url, 9)
                self.set_meta_data(privacy_policy, 10)

                self.controller()

                print('')
                print('[Notice] If any errors occured then open an issue on the github repository: https://github.com/dr-nyt/dataletix_moodlemobile2/issues')
                print('[Notice] If no errors occured then you can now find your android project in platforms/android folder. Open it in Android Studio and enjoy!')
                input('> ')
                break
            
            elif(ans == "2"):
                os.system('ionic cordova prepare android')

                print('')
                print('[Notice] If any errors occured then open an issue on the github repository: https://github.com/dr-nyt/dataletix_moodlemobile2/issues')
                print('[Notice] If no errors occured then you can now find your android project in platforms/android folder. Open it in Android Studio and enjoy!')
                input('> ')
                break

            elif(ans == "3"):
                self.reset_project()
                print("[NOTICE] Reset complete!")
                
            else:
                print("[Error] Invalid choice!")
                continue

    def controller(self):
        self.set_meta_data('meta_data', 'set')

        while(True):
            ans = input('Would you like to change the in-app texts related to moodle? (y/n): ')

            if(ans == "y" or ans == "yes"):
                self.lang_replacement()
                break

            elif(ans == 'n' or ans == "no"):
                break

        self.config_xml()
        self.config_json()
        self.bmma_scss()
        self.package_json()
        self.google_services_json()

        print("")
        print("[IMPORTANT NOTICE] Please replace all img resources in the resources/android folder before you continue!")
        while(True):
            x = input('Have you replaced all image resources? (y/n): ')
            if(x == 'y' or x == 'yes'):
                break
        
        self.exec_cmd()
        
    def set_meta_data(self, rep, index):
        if(index == 'set'):
            self.app_name = self.meta_data[0]
            self.unique_id = self.meta_data[1]
            self.version = self.meta_data[2]
            self.version_code = self.meta_data[3]
            self.app_description = self.meta_data[4]
            self.theme_color = self.meta_data[5]
            self.author_name = self.meta_data[6]
            self.author_email = self.meta_data[7]
            self.author_website = self.meta_data[8]
            self.site_url = self.meta_data[9]
            self.privacy_policy = self.meta_data[10]
        elif(rep != ""):
            self.meta_data[index] = rep
    
    def lang_replacement(self):
        for i in range(len(self.temp_langs)):
            print(f'Sample Text: {self.temp_langs[i]}')
            rep = input('(Replacement Text): ')
            if(rep != ""):
                self.temp_langs[i] = rep
    
    def reset_project(self):
        print('[Notice] Preparing files...')
        self.reset_file('config.xml')
        print('[Notice] Reset config.xml')
        self.reset_file('src/config.json')
        print('[Notice] Reset config.json')
        self.reset_file('package.json')
        print('[Notice] Reset package.json')
        self.reset_file('google-services.json')
        print('[Notice] Reset google-services.json')

    def reset_file(self, filePath):
        with open('script/backup/' + filePath, "r", encoding="utf8") as f:
            data = f.read()
        with open(filePath, "w", encoding="utf8") as f:
            f.write(re.sub(r"<string>ABC</string>(\s+)<string>(.*)</string>", r"<xyz>ABC</xyz>\1<xyz>\2</xyz>", data))

    def config_xml(self):
        self.replace('config.xml', "com.moodle.moodlemobile", self.unique_id)
        self.replace('config.xml', "3.7.1", self.version)
        self.replace('config.xml', "Moodle official app", self.app_description)
        self.replace('config.xml', "mobile@moodle.com", self.author_name)
        self.replace('config.xml', "http://moodle.com", self.author_website)
        self.replace('config.xml', "Moodle Mobile team", self.author_name)
        self.replace('config.xml', "Moodle", self.app_name)
        print("[Notice] Configured config.xml!")
    
    def config_json(self):
        self.replace_JSON('src/config.json', "app_id", self.unique_id)
        self.replace_JSON('src/config.json', "versioncode", int(self.version_code))
        self.replace_JSON('src/config.json', "versionname", self.version)
        self.replace_JSON('src/config.json', "siteurl", self.site_url)
        self.replace_JSON('src/config.json', "privacypolicy", self.privacy_policy)
        self.replace_JSON('src/config.json', "notificoncolor", self.theme_color)
        self.replace_JSON('src/config.json', "statusbarbgios", self.theme_color)
        self.replace_JSON('src/config.json', "statusbarbgandroid", self.theme_color)
        self.replace_JSON('src/config.json', "appname", self.app_name)
        print("[Notice] Configured config.json!")

    def bmma_scss(self):
        f= open("src\\theme\\bmma.scss","w+")
        f.write(f'$mod-color: {self.theme_color};')
        f.write('$tabs-background: $mod-color !default;')
        f.write('$core-color: $mod-color;')
        f.write('$core-color-init-screen: $mod-color !default;')
        f.write('$core-color-init-screen-alt: $mod-color !default;')
        f.close()
        print("[Notice] Configured bmma.scss!")
    
    def package_json(self):
        self.replace_JSON('package.json', "name", self.app_name.lower().replace(" ", ''))
        self.replace_JSON('package.json', "version", self.version)
        self.replace_JSON('package.json', "description", self.app_description)

        self.replace('package.json', "Moodle Pty Ltd.", self.author_name)
        self.replace('package.json', "mobile@moodle.com", self.author_email)

        print("[Notice] Configured package.json!")
    
    def google_services_json(self):
        self.replace('google-services.json', "com.moodle.moodlemobile", self.unique_id)
        print("[Notice] Configured google-services.json!")
    
    def exec_cmd(self):
        os.system('nvm install 11.12.0')
        os.system('nvm use 11.12.0')
        os.system('npm install -g cordova@8.1.2 ionic')
        os.system('npm install -g gulp')
        os.system('npm install gulp')
        if os.name == 'nt':
            os.system('npm install --global --production windows-build-tools')
        os.system('ionic cordova platform add android@7.1.2')
        os.system('ionic cordova prepare android')
    
    def replace(self, file_path, pattern, subst):
        #Create temp file
        fh, abs_path = mkstemp()
        with fdopen(fh,'w') as new_file:
            with open(file_path, encoding="utf8") as old_file:
                for line in old_file:
                    new_file.write(line.replace(pattern, subst))
        #Remove original file
        remove(file_path)
        #Move new file
        move(abs_path, file_path)
    
    def replace_JSON(self, file_path, key, new_val):
        with open(file_path, 'r', encoding="utf8") as file:
            json_data = json.load(file)
            json_data[key] = new_val
        with open(file_path, 'w') as file:
            json.dump(json_data, file, indent=4)

set = Setup()
set.main_menu()