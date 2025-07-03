---
title: See Future Payments
---
Future payments can be entered into portfolio performance but the transactions cannot be seen before the current date. Utilities changing the Operating System date to the future allow these payments to be seen.

* Linux - [faketime](https://www.systutorials.com/docs/linux/man/1-faketime/): manipulate the system time for a given command

eg: `$ faketime -f '-2y' /bin/bash -c '/home/$USER/Pfad/zu/PP/PortfolioPerformance'`

... shows a 2-year-old inventory donut chart.

* Windows - [RunAsDate](https://www.nirsoft.net/utils/run_as_date.html): Run a program with the specified date/time
