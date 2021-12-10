# Sleep Parser

Data in the Sleep as Android app comes in a CSV file that is very difficult to process with the aim of examining it because each sleep record is of variable length. It's made up of header rows and values rows.

This project is designed to process sleep data in its raw format and output it into a more friendly format.

Right now, this just takes a CSV file from the Sleep as Android app and converts it into a JSON file, but future goals are to allow for more options and move on to sleep data from other systems, including CPAP machines.

State at 11th December 2021: This is very much a WIP, so please excuse all the random crap and comments. After the MVP is done, a proper versioning process will be put in place.

## Technologies

**Language:** Python 3.9.7

**Handles files:** CSV, JSON

## Badges

![Top Language](https://img.shields.io/github/languages/top/GwynHannay/sleep-parser)

![Last Commit](https://img.shields.io/github/last-commit/GwynHannay/sleep-parser)