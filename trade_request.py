from sys import argv


def gen_line(item, buffer):
    padded_line = item.ljust(buffer)
    return f"[H] {padded_line} [W] (wants)"


def gen_code_block(items):
    code_block_start = '```css\n'
    code_block_end = '\n```'
    item_field_len = max([len(item) for item in items]) + 3
    padded_items = "\n".join([gen_line(item, item_field_len) for item in items])

    return f"{code_block_start}{padded_items}{code_block_end}"

def main(items):

    items_to_trade = items
    print(gen_code_block(items_to_trade))

if __name__ == '__main__':
    if len(argv) < 1:
        raise ValueError("Must provide at least one argument")
    main(argv)