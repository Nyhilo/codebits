# Takes either a single Serial Number or a file with a list of Serial Numbers as input.
# Outputs Computer Name associated with Serial Number or
# creates a new file with list of Names that correlate to the Serial Numbers
#
# Type 'py QuerySN.py --help' for information.
#
# Jacob Cloward 6/27/18

import MySQLdb
from _mysql_exceptions import OperationalError

def query_file(filename, HOST, USER, PSWD, DATABASE):
    sn_list = []
    try:
        with open(filename, 'r') as file:
            sn_list = file.readlines()
            sn_list = map(lambda s: s.strip(), sn_list)
    except FileNotFoundError:
        print("Error: File does not exist.")
        return None

    try:
        db = MySQLdb.connect(HOST, USER, PSWD, DATABASE)
    except _mysql_exceptions.OperationalError as err:
        print(err)
        return None

    cursor = db.cursor()
    query = ""
    outlist = []

    for serial_number in sn_list:
        query = 'SELECT NAME FROM MACHINE WHERE BIOS_SERIAL_NUMBER = "{}"'.format(serial_number)
        values_returned = cursor.execute(query)

        if values_returned == 0:
            outlist.append("No Entry Found")

        elif values_returned == 1:
            outlist.append( cursor.fetchone()[0])

        elif values_returned <= 5:
            outstring = ""
            data = cursor.fetchall()
            for item in data:
                outstring += item[0] + ", "
            outlist.append( outstring)

        else:
            outlist.append("Query Error: Recieved {} results.".format(values_returned))

    print("{} items sent to ouput.".format(len(outlist)))
    db.close()
    return outlist


def query_SN(serial_number, HOST, USER, PSWD, DATABASE):
    try:
        db = MySQLdb.connect(HOST, USER, PSWD, DATABASE)
    except _mysql_exceptions.OperationalError as err:
        print(err)
        return None

    cursor = db.cursor()
    query = 'SELECT NAME FROM MACHINE WHERE BIOS_SERIAL_NUMBER = "{}"'.format(serial_number)
    values_returned = cursor.execute(query)
    outstring = ""

    if values_returned == 0:
        outstring = "No Entry Found"

    elif values_returned == 1:
        outstring = cursor.fetchone()[0]

    elif values_returned <= 5:
        data = cursor.fetchall()

        for item in data:
            outstring += item[0] + ", "

    else:   # Less than 0 FOR SOME REASON. and > 5
        outstring = "Query Error: Recieved {} results.".format(values_returned)

    db.close()
    return outstring


def query_drives(filename, HOST, USER, PSWD, DATABASE):
    import re

    sn_list = []
    try:
        with open(filename, 'r') as file:
            sn_list = file.readlines()
            sn_list = map(lambda s: s.strip(), sn_list)
    except FileNotFoundError:
        print("Error: File does not exist.")
        return None

    try:
        db = MySQLdb.connect(HOST, USER, PSWD, DATABASE)
    except _mysql_exceptions.OperationalError as err:
        print(err)
        return None

    cursor = db.cursor()
    query = ""
    outlist = []
    regex = re.compile(r'(Total: )(\d+(?:\.\d+)?)\s*([kmgtp]?b)', re.IGNORECASE)

    for serial_number in sn_list:
        query = 'SELECT NAME FROM MACHINE_DISKS WHERE ID IN ( SELECT ID FROM MACHINE WHERE BIOS_SERIAL_NUMBER = "{}" )'.format(serial_number)
        values_returned = cursor.execute(query)

        drive_sizes = []
        drive_types = []

        if values_returned == 0:
            outlist = [["No Entry Found","No Entry Found"]]

        elif values_returned == 1:
            fetched = cursor.fetchone()[0]
            total, value, unit = regex.findall(fetched)[0]
            drive_sizes.append(str(value) + unit)

            if unit == "GB":
                if value > 300:
                    drive_types.append("HDD")
                elif value <= 300 and value > 100:
                    drive_types.append("SDD")
                else:
                    drive_types.append("Small Volume")

            elif unit == "KB" or unit == "B":
                drive_types.append("Small Volume")
            else:   # Larger than GB
                drive_types.append("HDD")

            outlist = [drive_sizes[0], drive_types[0]]

        elif values_returned <= 5:
            fetched = cursor.fetchall()
            totals = values = units = []

            for item in fetched:
                l = regex.findall(item[0])[0]
                print(l)
                print(l[1])
                totals.append(l[0])
                values.append(l[1])
                units.append(l[2])
                print("ts", totals)
                print("vs", values)

            print("totals", totals)
            print("values", values)
            print("units", units)
            for index in range(len(totals)):

                drive_sizes.append(str(values[index]) + units[index])

                if units[index] == "GB":
                    if float(values[index]) > 300:
                        drive_types.append("HDD")
                    elif float(values[index]) <= 300 and float(values[index]) > 100:
                        drive_types.append("SDD")
                    else:
                        drive_types.append("Small Volume")

                elif units[index] == "KB" or units[index] == "B":
                    drive_types.append("Small Volume")
                else:   # Larger than GB
                    drive_types.append("HDD")

            for i in range(len(drive_sizes)):
                drives = "' ".join(drive_sizes)
                has_SSD = "SSD" if "SSD" in drive_types else "No SSD"
                outlist.append([drives, has_SSD])

        else:
            outlist = [["Query Error: Recieved {} results.".format(values_returned), "Error"]]


    print("{} items sent to output.".format(len(outlist)))
    db.close()
    return outlist


def query_all(filename, HOST, USER, PSWD, DATABASE):
    sn_list = []
    try:
        with open(filename, 'r') as file:
            sn_list = file.readlines()
            sn_list = map(lambda s: s.strip(), sn_list)
    except FileNotFoundError:
        print("Error: File does not exist.")
        return None

    name_list = query_file(filename, HOST, USER, PSWD, DATABASE)
    drive_list = query_drives(filename, HOST, USER, PSWD, DATABASE)



def main():
    import sys
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("-i","--ip", dest="HOST", metavar="ipaddress",
                        help="Host IP or server name for the database", required=True)
    parser.add_argument("-u","--user", dest="USER", metavar="user",
                        help="Username for the server", required=True)
    parser.add_argument("-p","--password", dest="PSWD", metavar="password",
                        help="Password for the server", required=True)
    parser.add_argument("-d","--database", dest="DATABASE", metavar="database",
                        help="Database being accessed on the server", required=True)
    parser.add_argument("-f","--file", dest="filename", metavar="fileName", default=False,
                        help="File containing list of serial numbers to be queried")
    parser.add_argument("-s","--serial", dest="serial_number", metavar="serialNumber", default=False,
                        help="Serial number to be queried")

    args = parser.parse_args()


    if args.filename:
        data = query_file(filename, args.HOST, args.USER, args.PSWD, args.DATABASE)

        if data != None:
            with open(filename + "-output.txt", 'w') as file:
                for item in data:
                    file.write(item + "\n")
    elif args.serial_number:
        print(query_SN(args.serial_number, args.HOST, args.USER, args.PSWD, args.DATABASE))
    else:
        print("Please enter either a serial number or list of serial numbers.\n" +
                "Type 'py QuerySN.py --help' for more information.")


if __name__ == '__main__':
    main()
