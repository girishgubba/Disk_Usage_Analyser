import wmi
import pandas as pd
key = wmi.WMI()
drive_name = []
free_space = []
total_size = []
for drive in key.Win32_LogicalDisk():
    drive_name.append(drive.Caption)
    free_space.append(round(int(drive.FreeSpace ) /1e+9, 2))
    total_size.append(round(int(drive.Size ) /1e+9, 2))
    print("================")
    print("Drive Name :", drive.Caption +"\n================","\nFree Space Available in GB : \n", round(int(drive.FreeSpace ) /1e+9, 2),"\nTotal Size in GB :\n", round(int(drive.Size ) /1e+9, 2))
size_dict = {'Directory Name': drive_name,
             'Free Space (in GB)': free_space,
             'Total Size (in GB)': total_size}
data_frame = pd.DataFrame(size_dict)
data_frame.to_csv("disk_usage.csv")