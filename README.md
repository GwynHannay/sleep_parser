# Sleep Parser
![Top Language](https://img.shields.io/github/languages/top/GwynHannay/sleep-parser)
![Licence](https://img.shields.io/github/license/GwynHannay/sleep-parser)
![Last Commit](https://img.shields.io/github/last-commit/GwynHannay/sleep-parser)
![Latest Release](https://img.shields.io/github/v/release/GwynHannay/sleep-parser)
![Total Downloads](https://img.shields.io/github/downloads/GwynHannay/sleep-parser/total)

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

![image](https://user-images.githubusercontent.com/8345824/147508151-0ae09139-b077-43f2-9847-fc5520f694c8.png)

## Usage

Using this is easy! From the main folder of this repository, simply create the path ``/sleep-as-android/csv/`` and place your ``sleep-export.csv`` file there.

![image](https://user-images.githubusercontent.com/8345824/147394736-d648f4a6-b686-4da8-ad2a-02ef9ecf518e.png)

Alternatively, you can change the relative file path in ``main.py``. You can do this for the location of the CSV file, and specify where the JSON files should go as well (don't include a forward slash after the directory name).

![image](https://user-images.githubusercontent.com/8345824/147508805-0a2c6d10-c7fa-4ef0-a51c-cb1c57627e88.png)

## Release History

* 1.0.4
   * FIX: Time zones are now added when converting Unix timestamps into datetimes for events.
* 1.0.3
   * CHANGE: Raise an exception if the CSV file is not detected as being a valid Sleep as Android export.
* 1.0.2
    * FIX: Errors when running on a web server caused by attempt to subscript types such as `dict[str, str].`
    * ADD: Ability to specify output directory for JSON files.
* 1.0.1
    * CHANGE: Update of README.
* 1.0.0
    * Original project launch.

## General Information

**Language:** Python 3.9.7

**Handles files:** CSV, JSON

Distributed under the GNU GPL v3 license. See ``LICENSE`` for more information.
