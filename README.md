# Sleep Parser
![Top Language](https://img.shields.io/github/languages/top/GwynHannay/sleep-parser)
![Last Commit](https://img.shields.io/github/last-commit/GwynHannay/sleep-parser)

Data in the Sleep as Android app comes in a CSV file that is very difficult to process with the aim of examining it because each sleep record is of variable length. It's made up of header rows and values rows.

This project is designed to process sleep data in its raw format and output it into a more friendly format.

Right now, this just takes a CSV file from the Sleep as Android app and converts it into a JSON file, but future goals are to allow for more options and move on to sleep data from other systems, including CPAP machines.

## Screenshots

_Original Sleep as Android CSV file:_

![Screenshot 2021-12-26 061759](https://user-images.githubusercontent.com/8345824/147394570-478f1101-c38f-4848-8f9b-4375c1f4519f.png)

![Screenshot 2021-12-26 061830](https://user-images.githubusercontent.com/8345824/147394598-552ac2f0-995e-4c9e-af16-b165f844764a.png)

_Script output:_

![Screenshot 2021-12-26 062027](https://user-images.githubusercontent.com/8345824/147394613-7ad206b4-5ebd-4eb9-b874-7f8f223d640f.png)

_Resulting JSON file:_

![Screenshot 2021-12-26 061838](https://user-images.githubusercontent.com/8345824/147394626-43edf7bf-4f0e-4740-81e0-e597369ac15a.png)

![Screenshot 2021-12-26 061844](https://user-images.githubusercontent.com/8345824/147394636-806b77da-6ddf-4e58-84c5-0a1c9bb648f2.png)

## Usage

Using this is easy! From the main folder of this repository, simply create the path ``/sleep-as-android/csv/`` and place your ``sleep-export.csv`` file there.

![image](https://user-images.githubusercontent.com/8345824/147394736-d648f4a6-b686-4da8-ad2a-02ef9ecf518e.png)

Alternatively, you can change the relative file path in ``main.py``.

![image](https://user-images.githubusercontent.com/8345824/147394742-adc1ef36-2489-459b-a76f-c8f82400290e.png)

## Updates

**26th December 2021:** The MVP is almost done, after which a proper versioning process will be put in place. It currently outputs a monthly JSON file for Sleep as Android CSV files, but if there is any noise recording it will simply exclude that row from the output.

## Technologies

**Language:** Python 3.9.7

**Handles files:** CSV, JSON

Distributed under the GNU GPL v3 license. See ``LICENSE`` for more information.
