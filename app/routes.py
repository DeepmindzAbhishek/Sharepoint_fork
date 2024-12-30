from fastapi import APIRouter, HTTPException
from app.sharepoint_client import create_item, update_item, delete_item, read_items


router = APIRouter()

@router.post("/create")
async def create_item_in_sharepoint(list_name: str, data: dict):
    try:
        created_item = create_item(list_name, data)
        return {"message": "Item created successfully", "item": created_item}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to create item")
    

@router.get("/read")
async def read_items_in_sharepoint(list_name: str):
    try:
        items = read_items(list_name)
        return {"message": "Items read successfully", "items": items}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to read items")
    

@router.put("/update")
async def update_item_in_sharepoint(list_name: str, item_id: int, data: dict):
    try:
        updated_item = update_item(list_name, item_id, data)
        return {"message": "Item updated successfully", "item": updated_item}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to update item")
    

@router.delete("/delete")
async def delete_item_in_sharepoint(list_name: str, item_id: int):
    try:
        deleted_item = delete_item(list_name, item_id)
        return {"message": "Item deleted successfully", "item_id": item_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to delete item")

