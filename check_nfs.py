#!/usr/bin/python

#
# Author: Yuri Medvinsky
# Date: 2-16-2017
# Info: Nagios Check
#  check_nfs.py checks for missing nfs mount points. It queries /proc/mounts and /etc/fstab. 
#  It then compares the information from both files and identifies if mount points are missing.
#

import sys



# Just read file and return output to 'file_out'

def ReadFile(file):

  # Create array to hold file info
  file_out = []

  fo = open(file, 'r')
  file_read = fo.readlines()
  for line in file_read:
    if line.startswith('#'):
      continue
    else:
      file_out.append(line)
    fo.close()

  return file_out






def main():

  # Declare variables
  file_etc_fstab = '/etc/fstab'
  file_proc_mounts = '/proc/mounts'


  # Declare hash
  holds_mount_info = {}



  # Process /etc/fstab
  file_out_etc_fstab = ReadFile(file_etc_fstab)


  # Find 'nfs' mount point in fstab file
  for line in file_out_etc_fstab:
    line = line.split()                         # Remove newline (\n)
    if 'nfs' in line:                           # Search for 'nfs' in line
      try:
        holds_mount_info[str(line[0])] += 1     # If duplicate nfs line is found increment value by 1
      except KeyError:
        holds_mount_info[str(line[0])] = 1      # If new nfs line is found then assign value of 1





  # Process /proc/mounts
  file_out_proc_mounts = ReadFile(file_proc_mounts)

  for line in file_out_proc_mounts:
    line = line.split()                         # Remove newline (\n)
    if 'nfs' in line:                           # Search for 'nfs' in line
      try:
        holds_mount_info[str(line[0])] += 1     # If duplicate nfs line is found increment value by 1
      except KeyError:
        holds_mount_info[str(line[0])] = 1      # If new nfs line is found then assign value of 1






  # If holds_mount_info value of the key is 1. Then required mount point does NOT exists
  # If holds_mount_info value of the key is 2. Then required mount point exists


  # See if required mount points are not mounted by testing for value of 1
  if 1 in holds_mount_info.values():
    
    # Loop through hash and find value that is equal to 1, Generate Critical Alert
    for k,v in holds_mount_info.items():
      if v == 1:
        print "Critical - NFS %s is Not Mounted" % k
        sys.exit(2)
    

  # See if required mount points are mounted by testing for value of 2 
  if 2 in holds_mount_info.values(): 
    print "OK - NFS Partitions Mounted" 
    sys.exit(0)
  else:
    print "Unknown"
    sys.exit(3) 



if __name__ == "__main__":
  main()
