from textnode import TextNode, TextType


def main():
    text_node = TextNode(
        "Sérgio Paulo",
        TextType.BOLD_TEXT    
    )
    print(text_node)
    
main()