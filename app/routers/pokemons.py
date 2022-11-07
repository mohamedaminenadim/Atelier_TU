from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter,  Depends
from app import actions, schemas
from app.utils.utils import get_db

router = APIRouter()


@router.get("/", response_model=List[schemas.Pokemon])
def get_pokemons(skip: int = 0, limit: int = 100, database: Session = Depends(get_db)):
    """
        Return all pokemons
        Default limit is 100
    """
    pokemons = actions.get_pokemons(database, skip=skip, limit=limit)
    return pokemons

@router.get("/battle", response_model = List[schemas.Pokemon])
def fight_pokemons(P1: int, P2: int):
    fight_init = actions.initiate_duel(P1, P2)
    return fight_init