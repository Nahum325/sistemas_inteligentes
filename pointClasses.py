import numpy as np
from typing import Union, Iterable
from numpy.typing import ArrayLike
from abc import ABC, abstractmethod

class Point:
    __coords_dictionary: dict[str, int] = {"x": 0, "y": 1, "z": 2}

    def __init__(self, *args: Iterable) -> None:
        self.__ndim: int = len(args)
        self.__values: ArrayLike = np.array(args)
        self.__graphable: bool = True
        if (self.__ndim == 0) or (self.__ndim > 3) :
            self.__graphable = False

    def __str__(self) -> str:
        return f"{self.get_space_dimension()}D point at {self.get_coordinates()}"

    def get_space_dimension(self) -> int:
        return self.__ndim

    def get_graphable(self) -> bool:
        return self.__graphable    

    def get_coordinates(self) -> ArrayLike:
        return self.__values        
        
    def set_coordinates(self, *args: Iterable) -> None:
        self.__ndim = len(args)
        self.__values = np.array(args)
        self.__graphable = True
        if (self.__ndim == 0) or (self.__ndim > 3) :
            self.__graphable = False

    def get_coordinate(self, coordinate: Union[str, int]) -> float:
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
    def __str__(self) -> str:
        return f"Line segment between {self.get_start_point()} and {self.get_end_point()}"

    def get_start_point(self) -> Point:
        return self.__start_point

    def get_end_point(self) -> Point:
        return self.__end_point

    @abstractmethod
    def get_distance(self, distanceType: str) -> float:
        pass

class DistanciaManhattan(Distancia):
    def __init__(self, start_point: Point, end_point: Point) -> None:                
        if type(start_point) == type(end_point) == Point:
            if start_point.get_space_dimension() == end_point.get_space_dimension():
                self.__start_point: Point = start_point
                self.__end_point: Point = end_point
            else:
                raise ValueError(f"Can't create a segment between a point of {start_point.get_space_dimension()} dimensions and a point of {end_point.get_space_dimension()} dimensions.")                
        else:
            raise TypeError("One of the arguments is not a point.")
            
    def get_distance(self, distanceType: str) -> float:
        try:
            distanceType = distanceType.lower()
            distance_function = lambda start, end: sum(abs(st - en) for st, en in zip(start, end))
            return distance_function(self.__start_point.get_coordinates(), self.__end_point.get_coordinates())
        except KeyError:
            raise KeyError(f"{distanceType} is not a valid type of distance.")
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise

class DistanciaEuclidiana(Distancia):
    def __init__(self, start_point: Point, end_point: Point) -> None:                
        if type(start_point) == type(end_point) == Point:
            if start_point.get_space_dimension() == end_point.get_space_dimension():
                self.__start_point: Point = start_point
                self.__end_point: Point = end_point
            else:
                raise ValueError(f"Can't create a segment between a point of {start_point.get_space_dimension()} dimensions and a point of {end_point.get_space_dimension()} dimensions.")                
        else:
            raise TypeError("One of the arguments is not a point.")
            
    def get_distance(self, distanceType: str) -> float:
        try:
            distanceType = distanceType.lower()
            distance_function = lambda start, end: (sum((st - en)**2 for st, en in zip(start, end))) ** (1/2)
            return distance_function(self.__start_point.get_coordinates(), self.__end_point.get_coordinates())
        except KeyError:
            raise KeyError(f"{distanceType} is not a valid type of distance.")
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise

class DistanciaMinkowski(Distancia):
    def __init__(self, start_point: Point, end_point: Point) -> None:                
        if type(start_point) == type(end_point) == Point:
            if start_point.get_space_dimension() == end_point.get_space_dimension():
                self.__start_point: Point = start_point
                self.__end_point: Point = end_point
            else:
                raise ValueError(f"Can't create a segment between a point of {start_point.get_space_dimension()} dimensions and a point of {end_point.get_space_dimension()} dimensions.")                
        else:
            raise TypeError("One of the arguments is not a point.")
            
    def get_distance(self, distanceType: str) -> float:
        try:
            distanceType = distanceType.lower()
            distance_function = lambda start, end, p: sum(abs(st - en) ** p for st, en in zip(start, end)) ** (1/p)
            return distance_function(self.__start_point.get_coordinates(), self.__end_point.get_coordinates())
        except KeyError:
            raise KeyError(f"{distanceType} is not a valid type of distance.")
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise       