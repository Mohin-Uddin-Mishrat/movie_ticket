class Star_Cinema:
    hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.hall_list.append(hall)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.__entry_show_counter = 0
        self.__initialize_seats()

        Star_Cinema.entry_hall(self)

    def __initialize_seats(self):
        for row in range(1, self.__rows + 1):
            self.__seats[row] = ['0'] * self.__cols

    def __generate_show_id(self):
        self.__entry_show_counter += 1
        return f'Show{self.__entry_show_counter}'

    def entry_show(self, movie_name, time):
        show_id = self.__generate_show_id()
        show_info = (show_id, movie_name, time)
        self.__show_list.append(show_info)

        self.__seats[show_id] = [['0'] * self.__cols for _ in range(1, self.__rows + 1)]

    def book_seats(self, show_id, seat_list):
        if show_id not in self.__seats:
            raise ValueError("invalid show ID")

        seats = self.__seats[show_id]

        for row, col in seat_list:
            if 1 <= row <= self.__rows and 1 <= col <= self.__cols:
                if seats[row-1][col-1] == 'Booked':
                    raise ValueError(f"Seat ({row}, {col}) is already booked")
                else:
                    seats[row-1][col-1] = 'Booked'
            else:
                raise ValueError(f"invalid seat ({row}, {col})")

    def view_show_list(self):
        return self.__show_list

    def view_available_seats(self, show_id):
        if show_id not in self.__seats:
            raise ValueError("invalid show ID")

        seats = self.__seats[show_id]
        available_seats = []

        for row in range(1, self.__rows + 1):
            for col in range(1, self.__cols + 1):
                if seats[row-1][col-1] == '0':
                    available_seats.append((row, col))

        return available_seats


class Counter:
    def __init__(self):
        self.__hall_info = []

    def view_all_shows(self):
        for hall in Star_Cinema.hall_list:
            hall_info = (hall._Hall__hall_no, hall.view_show_list())
            self.__hall_info.append(hall_info)
        return self.__hall_info

    def view_available_seats(self, hall_no, show_id):
        for hall in Star_Cinema.hall_list:
            if hall._Hall__hall_no == hall_no:
                return hall.view_available_seats(show_id)

    def book_tickets(self, hall_no, show_id, seat_list):
        for hall in Star_Cinema.hall_list:
            if hall._Hall__hall_no == hall_no:
                hall.book_seats(show_id, seat_list)
