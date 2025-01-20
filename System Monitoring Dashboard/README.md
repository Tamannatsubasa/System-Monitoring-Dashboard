# System-Monitoring-Dashboard
The idea is to create a small dashboard that shows how healthy your computer system is.

What Is the Goal of This Project?

A few things that this dashbboard will show:
CPU Usage: How much of the computer's processing power is being used.
Memory Usage: How much RAM is being used.
Disk Usage: How much of the hard drive is full.
The following will be displayed as numbers and charts.

How I Built It

Python code programmed to:
Collect System Information: Use a psutil library to gather data about computer, like CPU, memory, and disk usage.
Create Charts: Use matplotlib.
Display It on a Webpage: Use Flask to create a small website where the data and chart will be shown.
