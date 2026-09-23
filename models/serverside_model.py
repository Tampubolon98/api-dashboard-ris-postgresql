from fastapi import Query
from fastapi import Request
import json

class ComponentServerSide:
    def __init__(
        self,
        limit: int = Query(10, ge=1),
        skip: int = Query(0, ge=0),
        sort_type: str = Query("asc"),
        sort_by: str = Query(None),
        search: str = "",
        status: str = Query(None),
    ):
        self.limit = limit
        self.skip = skip
        self.sort_type = sort_type
        self.search = search
        self.sort_by = sort_by
        self.status = status
        


    def __str__(self):
          return f"<limit ={self.limit} skip={self.skip} sort_by={self.sort_by}  sort_type={self.sort_type} search={self.search}  status={self.status} >"