#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics:"""

import sys

if __name__ == '__main__':

    file_size, count = 0, 0
    status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    statistics = {x: 0 for x in status_codes}

    def show_stats(statistics: dict, file_size: int) -> None:
        print("File size: {:d}".format(file_size))
        for x, y in sorted(statistics.items()):
            if y:
                print("{}: {}".format(x, y))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in statistics:
                    statistics[status_code] += 1
            except BaseException:
                pass
            try:
                file_size += int(data[-1])
            except BaseException:
                pass
            if count % 10 == 0:
                show_stats(statistics, file_size)
        show_stats(statistics, file_size)
    except KeyboardInterrupt:
        show_stats(statistics, file_size)
        raise
