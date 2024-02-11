import folium

from django.shortcuts import render

from catalog.models import BankProtectionStructures


def main_map(request):
    azov_sea_map = {'latitude': 46.190629, "longitude": 36.822734}
    m = folium.Map(location=[azov_sea_map['latitude'], azov_sea_map['longitude']], zoom_start=7)
    protection_objects = BankProtectionStructures.objects.all()
    for structure in protection_objects:
        build_date = structure.build_date if structure.build_date is not None else 'Не указано'
        repair_date = structure.last_repair_date if structure.last_repair_date is not None else 'Не указано'
        structure_popup = f"""
        {structure.name}
        Состояние: {structure.mark}/10
        Прогноз: {structure.prognosis}
        Строительство: {build_date}
        Ремонт: {repair_date}
        Подробная информация
        """
        folium.Marker(location=(structure.latitude, structure.longitude),
                      popup=structure_popup).add_to(m)
    folium.LayerControl().add_to(m)
    m = m._repr_html_()
    context = {
        "map": m,
    }
    return render(request, 'main.html', context)

