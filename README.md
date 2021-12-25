# Sleep Parser

Data in the Sleep as Android app comes in a CSV file that is very difficult to process with the aim of examining it because each sleep record is of variable length. It's made up of header rows and values rows.

This project is designed to process sleep data in its raw format and output it into a more friendly format.

Right now, this just takes a CSV file from the Sleep as Android app and converts it into a JSON file, but future goals are to allow for more options and move on to sleep data from other systems, including CPAP machines.

State at 26th December 2021: The MVP is almost done, after which a proper versioning process will be put in place. It currently outputs a monthly JSON file for Sleep as Android CSV files, but if there is any noise recording it will simply exclude that row from the output.

## Screenshots

Original Sleep as Android CSV file:

![Screenshot 2021-12-26 061759](https://user-images.githubusercontent.com/8345824/147394570-478f1101-c38f-4848-8f9b-4375c1f4519f.png)

![Screenshot 2021-12-26 061830](https://user-images.githubusercontent.com/8345824/147394598-552ac2f0-995e-4c9e-af16-b165f844764a.png)

Script output:

![Screenshot 2021-12-26 062027](https://user-images.githubusercontent.com/8345824/147394613-7ad206b4-5ebd-4eb9-b874-7f8f223d640f.png)

Resulting JSON file:

![Screenshot 2021-12-26 061838](https://user-images.githubusercontent.com/8345824/147394626-43edf7bf-4f0e-4740-81e0-e597369ac15a.png)

![Screenshot 2021-12-26 061844](https://user-images.githubusercontent.com/8345824/147394636-806b77da-6ddf-4e58-84c5-0a1c9bb648f2.png)

## Technologies

**Language:** Python 3.9.7

**Handles files:** CSV, JSON

## Badges

![Top Language](https://img.shields.io/github/languages/top/GwynHannay/sleep-parser)

![Last Commit](https://img.shields.io/github/last-commit/GwynHannay/sleep-parser)
