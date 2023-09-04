# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

import re

def parse_fdisk_output(output):
  """
  Parse the output of the fdisk -l command.

  Args:
    output: The output of the fdisk -l command.

  Returns:
    A list of dictionaries, where each dictionary represents a partition.
  """
  partitions = []
  for line in output.splitlines():
    if line.startswith("Disk /dev/"):
      continue
    match = re.match(r"^(\S+) (\d+-\d+) (\d+-\d+) (.*)$", line)
    if match:
      partitions.append({
        "device": match.group(1),
        "start": match.group(2),
        "end": match.group(3),
        "type": match.group(4),
      })
  return partitions


def read_text(text: str):

    lines = text.split("\n")
    pos = -1
    last_disk = {}
    disks = []
    for line in lines:
        if line.startswith("Disk /"):
            pos = pos + 1
            fields = line.split(" ")
            last_disk = {'name': fields[1]}
            disks.append(last_disk)


            continue

        if line.startswith("Disk model"):
            detail = disks[pos]
            detail['model'] = line.split(":")[1]
            disks[pos] = detail
    print(disks)



if __name__ == '__main__':
    with open('fdisk_output.txt', 'r') as diskoutput:
        read_text(diskoutput.read())
