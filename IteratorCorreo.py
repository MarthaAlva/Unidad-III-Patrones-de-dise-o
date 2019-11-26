#Iterator

from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List

class correo_Orden(Iterator):
    _posicion:int = None
    _reversa: bool = False

    def __init__(self, collection: Folio , reversa: bool = False) -> None:
        self._collection  = collection
        self._reversa = reversa
        self._posicion = -1 if reversa else 0

    def __next__(self):
        try:
            valor = self._collection[self._posicion]
            self._posicion += -1 if self._reversa else 1
        except IndexError:
            raise StopIteration()

        return valor
    
class FolioClasificacion(Iterable):

    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection
    def __iter__(self) -> correo_Orden:
        
        return correo_Orden(self._collection)

    def get_revez_iterator(self) -> correo_Orden:
        return correo_Orden(self._collection, True)

    def agregar_folioCorreo(self, item: Any):
        self._collection.append(item)


if __name__ == "__main__":
    folio  = FolioClasificacion()
    folio.agregar_folioCorreo("F515")
    folio.agregar_folioCorreo("E88")
    folio.agregar_folioCorreo("D777")
    folio.agregar_folioCorreo("M557")
    folio.agregar_folioCorreo("H715")
    folio.agregar_folioCorreo("MB22")
    folio.agregar_folioCorreo("MM28")

    print("Folios superiores:")
    print("\n".join(folio))
    print("")

    print("Folios inversos:")
    print("\n".join(folio.get_revez_iterator()), end="")

    
