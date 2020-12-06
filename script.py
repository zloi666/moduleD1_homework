from trello import TrelloApi


USER = "zloi666"
KEY= "654febea302c9ad2dd3cd24099454674"
TOKEN = "8e2f78ff7fc353b5ad7f0b0d1f3fb7d9fa5aca36ada45e895afa6a096a5cfd54"

BOARD_ID = "5fcb8a4cbcd3b125d6c9c269"

trl = TrelloApi(KEY, TOKEN)

# response = trl.boards.new("testapi2")

cols = trl.boards.get_list(BOARD_ID)

for col in cols:
    if col["name"] == "To Do":
        id = col["id"]

card = trl.cards.new("first card", id)
