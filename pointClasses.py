import numpy as np
from typing import Union, Iterable
from numpy.typing import ArrayLike
from abc import ABC, abstractmethod

class Point:
    """
    Clase que representa un punto en un espacio de dimensiones N.

    Atributos
    ----------
    __coords_dictionary : dict
        Diccionario estático que mapea las coordenadas 'x', 'y', 'z' a su correspondiente índice en un array.

    Métodos
    -------
    __init__(*args: Iterable)
        Constructor de la clase. Inicializa el punto con las coordenadas proporcionadas.

    __str__() -> str
        Representación en cadena de caracteres del punto.

    get_space_dimension() -> int
        Devuelve la dimensión del espacio en el que se encuentra el punto.

    get_graphable() -> bool
        Devuelve si el punto es graficable o no. Un punto es graficable si su dimensión es 1, 2 o 3.

    get_coordinates() -> ArrayLike
        Devuelve las coordenadas del punto.

    set_coordinates(*args: Iterable)
        Establece las coordenadas del punto.

    get_coordinate(coordinate: Union[str, int]) -> float
        Devuelve una coordenada específica del punto.
    """
    __coords_dictionary: dict[str, int] = {"x": 0, "y": 1, "z": 2}

    def __init__(self, *args: Iterable) -> None:
        """
        Constructor de la clase. Inicializa el punto con las coordenadas proporcionadas.

        Parámetros
        ----------
        *args : Iterable
            Las coordenadas del punto.
        """
        self.__ndim: int = len(args)
        self.__values: ArrayLike = np.array(args)
        self.__graphable: bool = True
        if (self.__ndim == 0) or (self.__ndim > 3) :
            self.__graphable = False

    def __str__(self) -> str:
        """
        Representación en cadena de caracteres del punto.

        Devoluciones
        ----------
        str
            Cadena de caracteres que representa el punto.
        """
        return f"{self.get_space_dimension()}D point at {self.get_coordinates()}"

    def get_space_dimension(self) -> int:
        """
        Devuelve la dimensión del espacio en el que se encuentra el punto.

        Devoluciones
        ----------
        int
            Dimensión del espacio en el que se encuentra el punto.
        """
        return self.__ndim

    def get_graphable(self) -> bool:
        """
        Devuelve si el punto es graficable o no. Un punto es graficable si su dimensión es 1, 2 o 3.

        Devoluciones
        ----------
        bool
            Verdadero si el punto es graficable, falso en caso contrario.
        """
        return self.__graphable    

    def get_coordinates(self) -> ArrayLike:
        """
        Devuelve las coordenadas del punto.

        Devoluciones
        ----------
        ArrayLike
            Coordenadas del punto.
        """
        return self.__values        
        
    def set_coordinates(self, *args: Iterable) -> None:
        """
        Establece las coordenadas del punto.

        Parámetros
        ----------
        *args : Iterable
            Las coordenadas del punto.
        """
        self.__ndim = len(args)
        self.__values = np.array(args)
        self.__graphable = True
        if (self.__ndim == 0) or (self.__ndim > 3) :
            self.__graphable = False

    def get_coordinate(self, coordinate: Union[str, int]) -> float:
        """
        Devuelve una coordenada específica del punto.

        Parámetros
        ----------
        coordinate : Union[str, int]
            Coordenada a obtener. Puede ser un entero (índice de la coordenada) 
            o una cadena de caracteres ('x', 'y', 'z').

        Devoluciones
        ----------
        float
            Valor de la coordenada solicitada.

        Lanza
        ----------
        ValueError
            Si el argumento 'coordinate' no es de tipo int o str.
        Exception
            Si la coordenada solicitada no es válida para la dimensión del punto.
        """
        if type(coordinate) == str:
            try:
                coordinate = coordinate.lower()
                return self.__values[Point.__coords_dictionary[coordinate]]
            except IndexError:
                raise Exception(f"The entered argument '{coordinate}' is not a valid coordinate for a point of {self.__ndim} dimensions")
            except KeyError:
                raise Exception(f"The entered argument '{coordinate}' is not a valid coordinate. Try a number or (X,Y,Z)")   
            except Exception as err:
                print(f"Unexpected {err=}, {type(err)=}")
                raise
        if type(coordinate) == int:
            try:
                return self.__values[coordinate]
            except IndexError:
                raise Exception(f"The entered argument '{coordinate}' is not a valid coordinate for a point of {self.__ndim } dimensions")
            except Exception as err:
                print(f"Unexpected {err=}, {type(err)=}")
                raise   
        raise ValueError(f"The entered argument '{coordinate}' is not of type int or str")

class Distancia(ABC):
    """
    Clase abstracta que representa un segmento de línea entre dos puntos.

    Métodos
    -------
    __str__() -> str
        Representación en cadena de caracteres del segmento de línea.

    get_start_point() -> Point
        Devuelve el punto de inicio del segmento de línea.

    get_end_point() -> Point
        Devuelve el punto final del segmento de línea.

    get_distance(distanceType: str) -> float
        Método abstracto para calcular la distancia entre los dos puntos del segmento de línea.
    """
    def __str__(self) -> str:
        """
        Representación en cadena de caracteres del segmento de línea.

        Devoluciones
        ----------
        str
            Cadena de caracteres que representa el segmento de línea.
        """
        return f"Line segment between {self.get_start_point()} and {self.get_end_point()}"

    def get_start_point(self) -> Point:
        """
        Devuelve el punto de inicio del segmento de línea.

        Devoluciones
        ----------
        Point
            Punto de inicio del segmento de línea.
        """
        return self.__start_point

    def get_end_point(self) -> Point:
        """
        Devuelve el punto final del segmento de línea.

        Devoluciones
        ----------
        Point
            Punto final del segmento de línea.
        """
        return self.__end_point

    @abstractmethod
    def get_distance(self, distanceType: str) -> float:
        """
        Método abstracto para calcular la distancia entre los dos puntos del segmento de línea.

        Parámetros
        ----------
        distanceType : str
            Tipo de distancia a calcular.

        Devoluciones
        ----------
        float
            Distancia entre los dos puntos del segmento de línea.

        Lanza
        ----------
        NotImplementedError
            Si el método no ha sido
