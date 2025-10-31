from salvar import salvar
from extract import (
    get_aircraft_types,
    get_airlines,
    get_destinations,
    get_flights_agendado_hoje,
)
from transformar import (
    transformar_aircraft_types,
    transformar_airlines,
    transformar_destinations,
    transformar_flights,
)


def main_etl():
    # Extract
    flights_paginas = get_flights_agendado_hoje()
    aircraft_types_paginas = get_aircraft_types()
    destinations_paginas = get_destinations()
    airlines_paginas = get_airlines()

    # Transform
    flights = transformar_flights(flights_paginas)
    aircraft_types = transformar_aircraft_types(aircraft_types_paginas)
    destinations = transformar_destinations(destinations_paginas)
    airlines = transformar_airlines(airlines_paginas)

    # Load
    salvar(
        "../",
        [
            flights,
            aircraft_types,
            destinations,
            airlines,
        ],
        [
            "flights",
            "aircraft_types",
            "destinations",
            "airlines",
        ],
    )
   

if __name__ == "__main__":
    main_etl()
