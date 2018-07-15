# DataDog ACPI check

Just a quick check I created to make sure my server (a repurposed laptop) hadn't
been unplugged.

## Installation

1. Run `sudo ./install.sh` to place the check script and config in the correct place
2. Create a new monitor in the DataDog web UI. 
3. Set the critical threshold to "below or equal to 0"

## How it works

The script reads the value of `/sys/bus/acpi/drivers/ac/ACPI0003:00/power_supply/AC/online` and 
outputs it as a metric. If the server is on AC power, it will equal 1. If unplugged, it will 
be 0.


