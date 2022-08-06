class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self, 
                training_type: str, 
                duration: float, 
                distance: float, 
                speed: float, 
                calories: float,
                ) -> None:
        self.training_type = training_type
        self.duration = "%.3f" % duration
        self.distance = "%.3f" % distance
        self.speed = "%.3f" % speed
        self.calories = "%.3f" % calories 
        
    def get_message(self) -> str:
        self.message: str = (f'Тип тренировки: {self.training_type}; \n' 
                        f'Длительность: {self.duration} ч.; \n'
                        f'Дистанция: {self.distance} км; \n'
                        f'Ср. скорость: {self.speed} км/ч; \n'
                        f'Потрачено ккал: {self.calories}.'
                        )
        return self.message 

class Training:
    """Базовый класс тренировки."""
    LEN_STEP:float = 0.65
    M_IN_KM: int = 1000

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        self.distant_km: float
        distant_km = self.action * self.LEN_STEP / self.M_IN_KM
        return distant_km

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        s_speed = self.distant_km / self.duration
        return s_speed
    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""

        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        show_message = InfoMessage(type(self).__name__,
                                   self.duration,
                                   self.get_distance(),
                                   self.get_mean_speed(),
                                   self.get_spent_calories()
                                   )
        return show_message

class Running(Training):
    """Тренировка: бег."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        super().__init__(action, duration, weight)
        self.duration = duration * 60

    def get_spent_calories(self) -> float:
        self.coeff_calorie_1: int = 18
        self.coeff_calorie_2: int = 20
        return ((self.coeff_calorie_1 * super().get_mean_speed() 
                - self.coeff_calorie_2) * self.weight / self.M_IN_KM 
                * self.duration
                ) 

class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float,
                 ) -> None:
        super().__init__(action, duration, weight)
        self.height = height
        self.duration = duration * 60

    def get_spent_calories(self) -> float:
        self.coeff_calorie_1: float = 0.035
        self.coeff_calorie_2: float = 0.029
        return ((self.coeff_calorie_1 * self.weight 
                + (super().get_mean_speed()**2 // self.height) * self.coeff_calorie_2
                * self.weight) * self.duration
                )


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP: float = 1.38

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: int,
                 ) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        return (self.length_pool * self.count_pool 
                / self.M_IN_KM / self.duration
                )

    def get_spent_calories(self) -> float:
        self.coeff_calories_1: float = 1.1
        self.coeff_calories_2: int = 2 
        return ((self.get_mean_speed() + self.coeff_calories_1) 
                * self.coeff_calories_2 * self.weight
                )


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    training_type = {'SWM': Swimming, 
                     'RUN': Running,
                     'WLK': SportsWalking
                    }
    return training_type[workout_type](*data)

def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    return print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

