import os
import datetime
print("\x1B[9m \x1B[40m \x1B[32m")
os.system("git remote remove upstream")

def fileing(i):
    with open("Readme.md","w") as file:
       file.write("\n ## itsfelipeh \n {} \n".format(i))
       file.close()

def load():
    start_date = datetime.date(2018, 1, 1)
    end_date = datetime.date(2018, 12, 31)
    delta = datetime.timedelta(days=1)
    while (start_date <= end_date):
        start_date +=delta
        mydate = start_date.strftime('%a %d %b %Y')
        print(mydate) 
        fileing(mydate)
        os.system("git add .")
        os.system("git commit --date=\"{} 10:00 2022 +0500\" -m hack-git-commit".format(mydate))

load()

os.system("git push -f origin master")