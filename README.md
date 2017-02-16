# nagios-plugins

check_nfs.py
------------ 
Performs a check for missing nfs mount points. It queries /proc/mounts and /etc/fstab.
It then compares the information from both files and identifies if mount points are missing.

