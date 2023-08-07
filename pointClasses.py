__author__ = "Pinkie Pie"

import numpy as np
from typing import Union, Iterable
from numpy.typing import ArrayLike
from abc import ABC, abstractmethod

class Point:
    """
    Clase que representa un punto en un espacio de hasta tres dimensiones.
    Si el punto tiene más de tres dimensiones o ninguna, no será graficable.

    Atributos
    ---------
    _coords_dictionary: dict[str, int]
        Un diccionario que mapea las coordenadas "x", "y", "z" a los índices 0, 1, 2 respectivamente.
    _ndim: int
        Número de dimensiones del punto.
    _values: ArrayLike
        Un array de numpy que almacena las coordenadas del punto.
    _graphable: bool
        Variable que indica si el punto es graficable o no.

    Métodos
    -------
    __init__(*args: Iterable) -> None:
        Inicializa el punto con las coordenadas proporcionadas.

    __str__() -> str:
        Devuelve una representación de cadena del punto.

    get_space_dimension() -> int:
        Devuelve el número de dimensiones del punto.

    get_graphable() -> bool:
        Devuelve si el punto es graficable o no.

    get_coordinates() -> ArrayLike:
        Devuelve las coordenadas del punto.

    set_coordinates(*args: Iterable) -> None:
        Establece las coordenadas del punto.

    get_coordinate(coordinate: Union[str, int]) -> float:
        Devuelve una coordenada específica del punto.
    """
    _coords_dictionary: dict[str, int] = {"x": 0, "y": 1, "z": 2}

    def __init__(self, *args: Iterable) -> None:
        """
        Inicializa el punto con las coordenadas proporcionadas.
        Si no se proporciona ninguna coordenada o si se proporcionan más de tres, el punto no será graficable.

        Parámetros
        ----------
        *args: Iterable
            Las coordenadas del punto.
        """
        self._ndim: int = len(args)
        self._values: ArrayLike = np.array(args)
        self._graphable: bool = True
        if (self._ndim == 0) or (self._ndim > 3) :
            self._graphable = False

    def __str__(self) -> str:
        """
        Devuelve una representación de cadena del punto.
        """
        return f"{self.get_space_dimension()}D point at {self.get_coordinates()}"

    def get_space_dimension(self) -> int:
        """
        Devuelve el número de dimensiones del punto.
        """
        return self._ndim

    def get_graphable(self) -> bool:
        """
        Devuelve si el punto es graficable o no.
        """
        return self._graphable    

    def get_coordinates(self) -> ArrayLike:
        """
        Devuelve las coordenadas del punto.
        """
        return self._values        
        
    def set_coordinates(self, *args: Iterable) -> None:
        """
        Establece las coordenadas del punto.
        Si no se proporciona ninguna coordenada o si se proporcionan más de tres, el punto no será graficable.

        Parámetros
        ----------
        *args: Iterable
            Las nuevas coordenadas del punto.
        """
        self._ndim = len(args)
        self._values = np.array(args)
        self._graphable = True
        if (self._ndim == 0) or (self._ndim > 3) :
            self._graphable = False

    def get_coordinate(self, coordinate: Union[str, int]) -> float:
        """
        Devuelve una coordenada específica del punto.

        Parámetros
        ----------
        coordinate: Union[str, int]
            Si es una cadena, debe ser "x", "y" o "z".
            Si es un entero, debe ser el índice de la coordenada en el array.

        Lanza
        -----
        ValueError
            Si 'coordinate' no es un entero o una cadena.
        Exception
            Si 'coordinate' no es una coordenada válida.
        """
        if type(coordinate) == str:
            try:
                coordinate = coordinate.lower()
                return self._values[Point._coords_dictionary[coordinate]]
            except IndexError:
                raise Exception(f"El argumento ingresado '{coordinate}' no es una coordenada válida para un punto de {self._ndim} dimensiones")
            except KeyError:
                raise Exception(f"El argumento ingresado '{coordinate}' no es una coordenada válida. Prueba con un número o (X,Y,Z)")   
            except Exception as err:
                print(f"Inesperado {err=}, {type(err)=}")
                raise
        if type(coordinate) == int:
            try:
                return self._values[coordinate]
            except IndexError:
                raise Exception(f"El argumento ingresado '{coordinate}' no es una coordenada válida para un punto de {self._ndim } dimensiones")
            except Exception as err:
                print(f"Inesperado {err=}, {type(err)=}")
                raise   
        raise ValueError(f"El argumento ingresado '{coordinate}' no es de tipo int o str")



class Distancia(ABC):
    """
    Clase abstracta que representa un segmento de línea entre dos puntos en un espacio.

    Atributos
    ---------
    __start_point: Point
        El punto inicial del segmento de línea.
    __end_point: Point
        El punto final del segmento de línea.

    Métodos
    -------
    __str__() -> str:
        Devuelve una representación de cadena del segmento de línea.

    get_start_point() -> Point:
        Devuelve el punto inicial del segmento de línea.

    get_end_point() -> Point:
        Devuelve el punto final del segmento de línea.

    get_distance() -> float:
        Método abstracto para calcular la distancia entre los dos puntos.
    """
    def __str__(self) -> str:
        """
        Devuelve una representación de cadena del segmento de línea.
        """
        return f"Segmento de línea entre {self.get_start_point()} y {self.get_end_point()}"

    def get_start_point(self) -> Point:
        """
        Devuelve el punto inicial del segmento de línea.
        """
        return self.__start_point

    def get_end_point(self) -> Point:
        """
        Devuelve el punto final del segmento de línea.
        """
        return self.__end_point

    @abstractmethod
    def get_distance(self) -> float:
        """
        Método abstracto para calcular la distancia entre los dos puntos.
        Este método debe ser implementado por cualquier subclase de Distancia.
        """
        pass


class Distancia(ABC):
    """
    Clase abstracta que representa un segmento de línea entre dos puntos en un espacio.

    Atributos
    ---------
    __start_point: Point
        El punto inicial del segmento de línea.
    __end_point: Point
        El punto final del segmento de línea.

    Métodos
    -------
    __str__() -> str:
        Devuelve una representación de cadena del segmento de línea.

    get_start_point() -> Point:
        Devuelve el punto inicial del segmento de línea.

    get_end_point() -> Point:
        Devuelve el punto final del segmento de línea.

    get_distance() -> float:
        Método abstracto para calcular la distancia entre los dos puntos.
    """
    def __str__(self) -> str:
        """
        Devuelve una representación de cadena del segmento de línea.
        """
        return f"Segmento de línea entre {self.get_start_point()} y {self.get_end_point()}"

    def get_start_point(self) -> Point:
        """
        Devuelve el punto inicial del segmento de línea.
        """
        return self.__start_point

    def get_end_point(self) -> Point:
        """
        Devuelve el punto final del segmento de línea.
        """
        return self.__end_point

    @abstractmethod
    def get_distance(self) -> float:
        """
        Método abstracto para calcular la distancia entre los dos puntos.
        Este método debe ser implementado por cualquier subclase de Distancia.
        """
        pass


class DistanciaEuclidiana(Distancia):
    """
    Clase que representa un segmento de línea entre dos puntos en un espacio y calcula la distancia Euclidiana entre ellos.

    Hereda de la clase Distancia.

    Métodos
    -------
    __init__(start_point: Point, end_point: Point) -> None:
        Inicializa el segmento de línea con los puntos de inicio y fin proporcionados.

    get_distance() -> float:
        Calcula y devuelve la distancia Euclidiana entre los puntos de inicio y fin.
    """
    def __init__(self, start_point: Point, end_point: Point) -> None: 
        """
        Inicializa el segmento de línea con los puntos de inicio y fin proporcionados.

        Parámetros
        ----------
        start_point: Point
            El punto inicial del segmento de línea.
        end_point: Point
            El punto final del segmento de línea.

        Lanza
        -----
        ValueError
            Si los puntos de inicio y fin no tienen la misma dimensión.
        TypeError
            Si uno de los argumentos no es un objeto de la clase Point.
        """
        if type(start_point) == type(end_point) == Point:
            if start_point.get_space_dimension() == end_point.get_space_dimension():
                self.__start_point: Point = start_point
                self.__end_point: Point = end_point
            else:
                raise ValueError(f"No se puede crear un segmento entre un punto de {start_point.get_space_dimension()} dimensiones y un punto de {end_point.get_space_dimension()} dimensiones.")                
        else:
            raise TypeError("Uno de los argumentos no es un punto.")
            
    def get_distance(self) -> float:
        """
        Calcula y devuelve la distancia Euclidiana entre los puntos de inicio y fin.

        Lanza
        -----
        Exception
            Si ocurre un error inesperado al calcular la distancia.
        """
        try:
            distance_function = lambda start, end: (sum((st - en)**2 for st, en in zip(start, end))) ** (1/2)
            return distance_function(self.__start_point.get_coordinates(), self.__end_point.get_coordinates())
        except Exception as err:
            print(f"Inesperado {err=}, {type(err)=}")
            raise


class DistanciaCamberra(Distancia):
    """
    Clase que representa un segmento de línea entre dos puntos en un espacio y calcula la distancia de Camberra entre ellos.

    Hereda de la clase Distancia.

    Métodos
    -------
    __init__(start_point: Point, end_point: Point) -> None:
        Inicializa el segmento de línea con los puntos de inicio y fin proporcionados.

    get_distance() -> float:
        Calcula y devuelve la distancia de Camberra entre los puntos de inicio y fin.
    """
    def __init__(self, start_point: Point, end_point: Point) -> None: 
        """
        Inicializa el segmento de línea con los puntos de inicio y fin proporcionados.

        Parámetros
        ----------
        start_point: Point
            El punto inicial del segmento de línea.
        end_point: Point
            El punto final del segmento de línea.

        Lanza
        -----
        ValueError
            Si los puntos de inicio y fin no tienen la misma dimensión.
        TypeError
            Si uno de los argumentos no es un objeto de la clase Point.
        """
        if type(start_point) == type(end_point) == Point:
            if start_point.get_space_dimension() == end_point.get_space_dimension():
                self.__start_point: Point = start_point
                self.__end_point: Point = end_point
            else:
                raise ValueError(f"No se puede crear un segmento entre un punto de {start_point.get_space_dimension()} dimensiones y un punto de {end_point.get_space_dimension()} dimensiones.")                
        else:
            raise TypeError("Uno de los argumentos no es un punto.")
            
    def get_distance(self) -> float:
        """
        Calcula y devuelve la distancia de Camberra entre los puntos de inicio y fin.

        Lanza
        -----
        Exception
            Si ocurre un error inesperado al calcular la distancia.
        """
        try:
            distance_function = lambda start, end: sum(abs(st - en) / (abs(st) + abs(en)) for st, en in zip(start, end))
            return distance_function(self.__start_point.get_coordinates(), self.__end_point.get_coordinates())
        except Exception as err:
            print(f"Inesperado {err=}, {type(err)=}")
            raise
