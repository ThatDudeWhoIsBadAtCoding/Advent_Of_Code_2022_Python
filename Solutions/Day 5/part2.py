def extract_crates(text, depth, crate_array):
    crate_array = [] if not crate_array else crate_array
    curr_stack = []

    for line in text:
        line = line.removesuffix("\n")
        if line.startswith("["):
            try:
                if line[depth] != " ":
                    curr_stack.append(line[depth])
            except IndexError:
                return crate_array

    crate_array.append(curr_stack)

    return extract_crates(text, depth + 4, crate_array)


def decode_instruction(instruction):
    decoded_instruction = {"start": None, "move_to": None, "number": None}
    instruction = instruction.split(" ")
    decoded_instruction["start"] = int(instruction[3])
    decoded_instruction["move_to"] = int(instruction[-1])
    decoded_instruction["number"] = int(instruction[1])
    return decoded_instruction


def follow_instruction(instruction, crates):
    start = instruction["start"] - 1
    move = instruction["move_to"] - 1
    number = instruction["number"]
    crates_to_move = crates[start][:(number)]
    crates[start] = crates[start][(number):]
    crates_to_move.reverse()
    for i in crates_to_move:
        crates[move].insert(0, i)
    return crates


with open("Day 5/crates.txt", "r+") as Crate_File:
    text = Crate_File.readlines()
    instructions = text[10:]
    crates = extract_crates(text, 1, False)
    for instruction in instructions:
        instruction = decode_instruction(instruction.removesuffix("\n"))
        crates = follow_instruction(instruction, crates)
message = ""
for stack in crates:
    if len(stack) <= 0:
        continue
    message += stack[0]
print(message)
