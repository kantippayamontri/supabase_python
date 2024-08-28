from dotenv import load_dotenv

load_dotenv()

# TODO: connection with hosted supabase
import os
from supabase import create_client, Client
from datetime import datetime, timedelta

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# TODO: crud operation
# select data
data = supabase.table("todo").select("*").execute()
print(data)
print(len(data.data))

data = supabase.table("todo").select("id, name").execute()
print(data)
print(len(data.data))

data = (
    supabase.table("todo").select("id, name").eq("name", "item 1").execute()
)  # add filter name=item?
print(data)
print(len(data.data))

# # insert data
# create_at = datetime.now() - timedelta(hours=2)
# data = (
#     supabase.table("todo")
#     .insert({"name": "item3", "created_at": str(create_at)})
#     .execute()
# )

# # update data
# data = (
#     supabase.table("todo")
#     .update(
#         {
#             "name": "todo update 3", # only update name
#         }
#     )
#     .eq("id", 3) # filter to update at id=3
#     .execute()
# )

# data = (
#     supabase.table("todo")
#     .update(
#         {
#             "name": "todo update 4",
#         }
#     )
#     .eq("id", 4)
#     .execute()
# )

# # try to update id=6 not exist in the table -> nothing happen
# data = (
#     supabase.table("todo")
#     .update(
#         {
#             "name": "todo update 6", 
#         }
#     )
#     .eq("id", 6) 
#     .execute()
# )

# delete data 
# data = supabase.table("todo").delete().eq("id", 3).execute()