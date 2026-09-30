screen music_puzzle(puzzle):

    modal True

    default chosen = []
    default hovered_item = None

    for item in puzzle["items"]:

        imagebutton:

            if item["id"] in chosen:
                idle At(Transform(item["image"], zoom=0.5), outline_white_thick)
                hover At(Transform(item["image"], zoom=0.5), outline_white_thick)
                action NullAction()

            elif hovered_item == item["id"]:
                idle At(Transform(item["image"], zoom=0.5), outline_white_thin)
                hover At(Transform(item["image"], zoom=0.5), outline_white_thin)
                action SetScreenVariable("chosen", chosen + [item["id"]])

            else:
                idle Transform(item["image"], zoom=0.5)
                hover Transform(item["image"], zoom=0.5)
                action SetScreenVariable("chosen", chosen + [item["id"]])

            hovered SetScreenVariable("hovered_item", item["id"])
            unhovered SetScreenVariable("hovered_item", None)

            focus_mask True

            xpos item["x"]
            ypos item["y"]
            xanchor 0
            yanchor 0

define scene1_puzzle = {
    "items": [
        {"id": "piano", "image": "images/piano.png", "x": 300, "y": 450},
        {"id": "drums", "image": "images/drums.png", "x": 1150, "y": 500}
    ]
}