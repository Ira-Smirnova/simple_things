import doctest

class LightDevice:
    _identify_list = [] #предполагается ограничение изменения списка идентификационных номеров (и самих идентификационных номеров) для пользователя
    COLOR_DICT = {
        'white': '#ffffff',
        'red': '#ff0000',
        'green': '#00ff00',
        'blue': '#0000ff',
        'yellow': '#ffff00',
        'navy': '#000080',
        'orange_red': '#ff4500',
        'fuchsia': '#ff00ff'
    }
    RGB_DICT ={
        'white': (255, 255, 255),
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'yellow': (255, 255, 0),
        'navy': (233, 150, 122),
        'orange_red': (255, 69, 0),
        'fuchsia': (255, 0, 255)
    }

    def __init__(self, identify_number: int, on: bool = False, color: str = 'white'):
        """
        Создание и подготовка к работе объекта Световой прибор

        :param identify_number: Идентификационный номер прибора
        :param on: Индикатор включения прибора (True-включён в текущий момент; False-выключен)
        :param color: Индикатор цвета света прибора (хранится после инициализации в формате HEX-кода цвета, но взаимодействие реализовано через стандартные названия)

        Примеры:
        >>> lite_1 = LightDevice(987, False, 'blue')
        >>> lite_2 = LightDevice(986)
        """
        if not isinstance(identify_number, int):
            raise TypeError('Идентификационный номер прибора должен быть типа int')
        if identify_number in LightDevice._identify_list:
            raise ValueError('Идентификационный номер прибора должен быть уникален')
        self._identify_number = identify_number
        LightDevice._identify_list.append(identify_number)

        if not isinstance(on, bool):
            raise TypeError('Индикатор включения прибора должен быть типа Bool')
        self.on = on

        if not isinstance(color, str):
            raise TypeError('Индикатор цвета света прибора должен быть типа str')
        self.color = LightDevice.COLOR_DICT.get(color)

    @property
    def identify_number(self) -> int:
        """Геттер для получения идентификационного номера светового прибора.
        Идентификационный номер прибора сделан protected атрибутом,
        так как данные номера используются для внутреннего учёта оборудования;
        и внешнее вмешательство может нарушить систему учёта"""
        return self._identify_number

    def __str__(self):
        return f"Световой прибор {self.__class__.__name__} номер {self._identify_number}"

    def __repr__(self):
        name_color = next(name_color for name_color, value in LightDevice.COLOR_DICT.items() if value == self.color)
        return f"{self.__class__.__name__}(identify_number={self._identify_number!r}, on={self.on!r}, color='{name_color}')"

    def turn_on(self) -> None:
        """
        Метод, который включает прибор

        Примеры:
        >>> lite_4 = LightDevice(705)
        >>> lite_4.turn_on()
        """
        if self.on:
            raise ValueError(f'Световой прибор номер {self._identify_number} уже включён!')
        self.on = True

    def turn_off(self) -> None:
        """
        Метод, который включает прибор

        Примеры:
        >>> lite_5 = LightDevice(705, True)
        >>> lite_5.turn_off()
        """
        if not self.on:
            raise ValueError(f'Световой прибор номер {self._identify_number} уже выключен!')
        self.on = False

    def change_color(self, color: str) -> None:
        """
        Метод, который изменяет цвет света прибора

        :param color: новое значение цвета света прибора

        Примеры:
        >>> lite_3 = LightDevice(802) #color: 'white' = '#ffffff'
        >>> lite_3.change_color('red') #color: 'red' = '#ff0000'
        """
        if color not in LightDevice.COLOR_DICT:
            raise ValueError('Цвет с таким названием не может быть использован')
        self.color = LightDevice.COLOR_DICT.get(color)

class LampSpotlight(LightDevice):
    def __init__(self, identify_number: int, on: bool = False, color: str = 'white', color_filter: str = 'white'):
        """
        Создание и подготовка к работе объекта Ламповый прожектор

        :param identify_number: Идентификационный номер прибора
        :param on: Индикатор включения прибора
        :param color: Индикатор цвета света прибора
        :param color_filter: Индикатор цвета фильтра прибора (в ламповых прожекторах цвет света прибора изменяется с помощью фильтра)

        Примеры:
        >>> lite_6 = LampSpotlight(402)
        >>> lite_7 = LampSpotlight(605, True, 'green', 'green')
        """
        super().__init__(identify_number, on, color)
        if not isinstance(color_filter, str):
            raise TypeError('Цвет фильтра должен быть типа str')
        if color_filter != color:
            raise ValueError('Цвет фильтра должен совпадать с цветом света')
        self.color_filter = color_filter

    def __repr__(self):
        name_color = next(name_color for name_color, value in LightDevice.COLOR_DICT.items() if value == self.color)
        return f"{self.__class__.__name__}(identify_number={self._identify_number!r}, on={self.on!r}, color='{name_color}', color_filter='{self.color_filter!r}')"

    def change_color(self, color_filter: str) -> None:
        """
        Метод, который изменяет цвет света прибора
        Перегружен в дочернем классе Ламповый прожектор, так как изменение цвета в непрограммируемых ламповых прожекторах осуществляется только через смену фильтра

        :param color_filter: Индикатор цвета фильтра прибора

        Примеры:
        >>> lite_8 = LampSpotlight(305)
        >>> lite_8.change_color('red')
        """
        if color_filter not in LightDevice.COLOR_DICT:
            raise ValueError('Фильтр с таким названием не может быть использован')
        self.color_filter = color_filter
        self.color = LightDevice.COLOR_DICT.get(color_filter)

class RGBSpotlight(LightDevice):
    def __init__(self, identify_number: int, on: bool = False, color: str = 'white', red: int = 255, green: int = 255, blue: int = 255):
        """
        Создание и подготовка к работе объекта RGB прожектор

        :param identify_number: Идентификационный номер прибора
        :param on: Индикатор включения прибора
        :param color: Индикатор цвета света прибора

        Индикатор присутствия не запрашиваются у пользователя при инициализации прибора, так как они напрямую связаны с цветом света
        :param red: Индикатор присутствия красного цвета в цвете света прибора
        :param green: Индикатор присутствия зелёного цвета в цвете света прибора
        :param blue: Индикатор присутствия синего цвета в цвете света прибора

        Примеры:
        >>> lite_9 = RGBSpotlight(100)
        """
        super().__init__(identify_number, on, color)
        if not (isinstance(red, int) and isinstance(green, int) and isinstance(blue, int)):
            raise TypeError('Значения индикаторов присутствия цвета должны быть типа int')
        if LightDevice.RGB_DICT.get(color)[0] != red:
            raise ValueError('Недопустимое сочетание Индикатора цвета света прибора и Индикатор присутствия красного')
        if LightDevice.RGB_DICT.get(color)[1] != green:
            raise ValueError('Недопустимое сочетание Индикатора цвета света прибора и Индикатор присутствия зелёного')
        if LightDevice.RGB_DICT.get(color)[2] != blue:
            raise ValueError('Недопустимое сочетание Индикатора цвета света прибора и Индикатор присутствия синего')
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self):
        name_color = next(name_color for name_color, value in LightDevice.COLOR_DICT.items() if value == self.color)
        return f'{self.__class__.__name__}(identify_number={self._identify_number!r}, on={self.on!r}, color={name_color}, red={self.red!r}, green={self.green!r}, blue={self.blue!r})'


    def change_color(self, red: int, green: int, blue:int) -> None:
        """
        Метод, который изменяет цвет света прибора
        Перегружен в дочернем классе RGB прожектор, так как для программируемых световых приборов цвет задаётся через изменение значений параметров rgb

        :param red: Индикатор присутствия красного цвета в цвете света прибора
        :param green: Индикатор присутствия зелёного цвета в цвете света прибора
        :param blue: Индикатор присутствия синего цвета в цвете света прибора

        Примеры:
        >>> lite_10 = RGBSpotlight(102)
        >>> lite_10.change_color(0, 255, 0)
        """
        if not (isinstance(red, int) and isinstance(green, int) and isinstance(blue, int)):
            raise TypeError('Значения индикаторов присутствия цвета должны быть типа int')
        error_change = True
        for color, rgb_list in LightDevice.RGB_DICT.items():
            if rgb_list[0] == red and rgb_list[1] == green and rgb_list[2] == blue:
                self.red =red
                self.green = green
                self.blue = blue
                self.color = LightDevice.COLOR_DICT.get(color)
                error_change = False
        if error_change:
            raise ValueError('Такое сочетание цветовых компонент на данный момент не может быть реализовано')

if __name__ == "__main__":
    doctest.testmod()
    pass
