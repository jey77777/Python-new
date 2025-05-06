import os 
import shutil 
import datetime
import schedule 
import time

source_dir = "C:/Users/admin/Pictures/Screenshots"
destionation_dir = "C:/Users/admin/Pictures/Backups"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to {dest_dir}")
    except FileExistsError:
        print(f"Folder already existrs in: {dest}")


schedule.every().day.at("15:05").do(lambda: copy_folder_to_directory(source_dir, destionation_dir))

while True:
    schedule.run_pending()
    time.sleep(60)