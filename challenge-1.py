#!/usr/bin/env python3
import itertools
import numpy


def combinations_list_comprehension(entry_list, r):
    return numpy.prod(list([combination for combination in itertools.combinations(entries_list, r) if sum(list(combination)) == 2020]))


def combinations_r_2(entry_list):
    combinations_obj = itertools.combinations(entry_list, 2)
    for combination in combinations_obj:
        if (combination[0] + combination[1] == 2020):
            print(f"combination_r_2: {combination[0]} + {combination[1]} = 2020")
            return combination[0] * combination[1]
    

def combinations_r_3(entry_list):
    combinations_obj = itertools.combinations(entry_list, 3)
    for combination in combinations_obj:
        if (combination[0] + combination[1] + combination[2] == 2020):
            print(f"combinations_r_3: {combination[0]} + {combination[1]} + {combination[2]} = 2020")
            return combination[0] * combination[1] * combination[2]


def sum_of_two_numbers(entry_list):
    for counter, value in enumerate(entry_list):
        for entry in entry_list[counter+1:]:
            if (value + entry == 2020):
                print(f"sum_of_two_numbers: {value} + {entry} = 2020")
                return value * entry

    
def sum_of_three_numbers(entry_list):
    for counter, entry1 in enumerate(entry_list):
        for counter2, entry2 in enumerate(entry_list[counter+1:]):
            for entry3 in entry_list[counter2+1:]:
                if (entry1 + entry2 + entry3 == 2020):
                    print(f"sum_of_three_numbers: {entry1} + {entry2} + {entry3} = 2020")
                    return entry1 * entry2 * entry3


if __name__ == "__main__":
    entries_list = [
        1834,
        1546,
        1119,
        1870,
        1193,
        1198,
        1542,
        1944,
        1817,
        1249,
        1361,
        1856,
        1258,
        1425,
        1835,
        1520,
        1792,
        1130,
        2004,
        1366,
        1549,
        1347,
        1507,
        1699,
        1491,
        1557,
        1865,
        1948,
        1199,
        1229,
        1598,
        1756,
        1643,
        1306,
        1838,
        1157,
        1745,
        1603,
        1972,
        1123,
        1963,
        1759,
        1118,
        1526,
        1695,
        1661,
        1262,
        1117,
        1844,
        1922,
        1997,
        1630,
        1337,
        1721,
        1147,
        1848,
        1476,
        1975,
        1942,
        1569,
        1126,
        1313,
        1449,
        1206,
        1722,
        1534,
        1706,
        1596,
        1700,
        1811,
        906,
        1666,
        1945,
        1271,
        1629,
        1456,
        1316,
        1636,
        1884,
        1556,
        1317,
        1393,
        1953,
        1658,
        2005,
        1252,
        1878,
        1691,
        60,
        1872,
        386,
        1369,
        1739,
        1460,
        1267,
        1935,
        1992,
        1310,
        1818,
        1320,
        1437,
        1486,
        1205,
        1286,
        1670,
        1577,
        1237,
        1558,
        1937,
        1938,
        1656,
        1220,
        1732,
        1647,
        1857,
        1446,
        1516,
        1450,
        1860,
        1625,
        1377,
        1312,
        1588,
        1895,
        1967,
        1567,
        1582,
        1428,
        1415,
        1731,
        1919,
        1651,
        1597,
        1982,
        1576,
        1172,
        1568,
        1867,
        1660,
        1754,
        1227,
        1121,
        1733,
        537,
        1809,
        1322,
        1876,
        1665,
        1124,
        1461,
        1888,
        1368,
        1235,
        1479,
        1529,
        1148,
        1996,
        1939,
        1340,
        1531,
        1438,
        1897,
        1152,
        1321,
        1770,
        897,
        1750,
        1111,
        1772,
        1615,
        1798,
        1359,
        1470,
        1610,
        1362,
        1973,
        1892,
        1830,
        599,
        1341,
        1681,
        1572,
        1873,
        42,
        1246,
        1447,
        1800,
        1524,
        1214,
        1784,
        1664,
        1882,
        1989,
        1797,
        1211,
        1170,
        1854,
        1287,
        1641,
        1760
    ]
    combination_comprehension_r_2 = combinations_list_comprehension(entries_list, 2)
    combination_comprehension_r_3 = combinations_list_comprehension(entries_list, 3)
    combination_r_2_result = combinations_r_2(entries_list)
    combination_r_3_result = combinations_r_3(entries_list)
    sum_of_two_result = sum_of_two_numbers(entries_list)
    sum_of_three_result = sum_of_three_numbers(entries_list)
    print("combination_comprehension_r_2 multiplied: ", combination_comprehension_r_2)
    print("combination_comprehension_r_3 multiplied: ", combination_comprehension_r_3)
    print("combination_r_2_result multiplied: ", combination_r_2_result)
    print("combination_r_3_result multiplied: ", combination_r_3_result)