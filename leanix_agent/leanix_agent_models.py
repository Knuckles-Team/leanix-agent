#!/usr/bin/python
               
from typing import Optional, Any, List
from pydantic import BaseModel, ConfigDict, Field
import requests


class Response(BaseModel):
    """
    Standard Response Wrapper.
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)
    response: requests.Response
    data: Any = None


class BaseModelWrapper(BaseModel):
    """
    Base Model wrapping common functionalities such as extracting nested API parameters
    from the root attributes.
    """

    model_config = ConfigDict(populate_by_name=True)

    @property
    def api_parameters(self) -> dict:
        """
        Convert the Pydantic model to a dictionary suitable for passing as API arguments or params.
        Can be customized to exclude specific internal fields like IDs that are passed in the URL.
        """
        return self.model_dump(exclude_none=True, by_alias=True)


class FactSheetModel(BaseModelWrapper):
    """
    Input model for querying FactSheets.
    """

    id: Optional[str] = Field(None, description="The unique ID of the FactSheet.")
    type: Optional[str] = Field(
        None, description="The type of the FactSheet. Example: Application, ITComponent"
    )
    page_size: Optional[int] = Field(
        40, description="Number of results to return per page.", alias="pageSize"
    )
    cursor: Optional[str] = Field(None, description="Pagination cursor.")

    @property
    def api_parameters(self) -> dict:
        return self.model_dump(exclude_none=True, exclude={"id"}, by_alias=True)


class FactSheetResponse(BaseModel):
    """
    Output model parsed from the JSON response for a FactSheet.
    """

    model_config = ConfigDict(extra="allow")
    id: str
    name: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None


class FactSheetListResponse(BaseModel):
    """
    Output model for a paginated list of FactSheets.
    """

    model_config = ConfigDict(extra="allow")
    data: List[FactSheetResponse]
