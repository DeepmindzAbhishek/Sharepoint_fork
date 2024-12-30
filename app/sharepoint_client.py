from office365.sharepoint.client_context import ClientContext
from config import SHAREPOINT_CLIENT_ID, SHAREPOINT_CLIENT_SECRET, SHAREPOINT_SITE_URL, SHAREPOINT_TENANT_ID


def get_sharepoint_client():
    ctx = ClientContext(SHAREPOINT_SITE_URL).with_client_credentials(
        SHAREPOINT_CLIENT_ID, SHAREPOINT_CLIENT_SECRET
    )
    return ctx

def create_item(list_name, data):
    ctx = get_sharepoint_client()
    list_obj = ctx.web.lists.get_by_title(list_name)
    item = list_obj.add_item(data).execute_query()
    return item.properties


def read_items(list_name):
    ctx = get_sharepoint_client()
    list_obj = ctx.web.lists.get_by_title(list_name)
    items = list_obj.items.get().execute_query()
    return [item.properties for item in items]

def update_item(list_name, item_id, data):
    ctx = get_sharepoint_client()
    list_obj = ctx.web.lists.get_by_title(list_name)
    item = list_obj.get_item_by_id(item_id)
    for key, value in data.items():
        item.set_property(key, value)
    item.update().execute_query()
    return item.properties

def delete_item(list_name, item_id):
    ctx = get_sharepoint_client()
    list_obj = ctx.web.lists.get_by_title(list_name)
    item = list_obj.get_item_by_id(item_id)
    item.delete_object().execute_query()
    return {"message": "Item deleted successfully"}