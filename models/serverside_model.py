from fastapi import Query
from fastapi import Request
import json

class ComponentServerSide:
    def __init__(
        self,
        limit: int = Query(None, ge=1),
        skip: int = Query(0, ge=0),
        sort_type: str = Query("asc"),
        sort_by: str = Query(None)
    ):
        self.limit = limit
        self.skip = skip
        self.sort_type = sort_type
        self.sort_by = sort_by
        


    def __str__(self):
          return f"<limit ={self.limit} skip={self.skip} sort_by={self.sort_by}  sort_type={self.sort_type} >"