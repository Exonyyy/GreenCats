def get_prognosis(statistic_files: list, parsed_data: dict, current_status: int, material_info: str):
    const = 1.6

    materials = {
        'Бетон': 1.4,
        'Песок': 0.8,
        'Гранитная кладка': 2.1,
        'Сталь': 1.6,
        'Древесина': 2.4,
    }

    weather = {
        'Ясно': 1,
        'Пассмурно': 1.2,
        'Дождь': 1.4,
        'Снег': 1.3,
    }

    wind = (
        (i/10 for i in range(0, 201)),
        (i/10 for i in range(201, 401)),
        (i / 10 for i in range(401, 601)),
        (i / 10 for i in range(601, 801)),
        (i / 10 for i in range(801, 1001)),
        (i / 10 for i in range(1001, 1201)),
        (i / 10 for i in range(1201, 1401)),
        (i / 10 for i in range(1401, 1601)),
        (i / 10 for i in range(1601, 1801)),
    )



