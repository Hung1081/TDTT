def spell_integer(n: int) -> str:
    """Chuyển số nguyên sang chữ tiếng Việt (hỗ trợ âm và dương)."""
    if n == 0:
        return "không"
    if n < 0:
        return "âm " + spell_integer(-n)

    units = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    suffixes = ["", "nghìn", "triệu", "tỷ", "nghìn tỷ", "triệu tỷ"]

    def three_digits_to_words(num: int, is_first_group: bool) -> str:
        hundreds = num // 100
        tens = (num % 100) // 10
        ones = num % 10
        parts = []

        if hundreds:
            parts.append(units[hundreds] + " trăm")

        if tens == 0:
            if ones != 0:
                if hundreds:
                    parts.append("lẻ")
                parts.append(units[ones])
        elif tens == 1:
            parts.append("mười")
            if ones == 1:
                parts.append("một")
            elif ones == 4:
                parts.append("bốn")
            elif ones == 5:
                parts.append("lăm")
            elif ones != 0:
                parts.append(units[ones])
        else:
            parts.append(units[tens] + " mươi")
            if ones == 1:
                parts.append("mốt")
            elif ones == 4:
                parts.append("bốn")
            elif ones == 5:
                parts.append("lăm")
            elif ones != 0:
                parts.append(units[ones])

        return " ".join(parts).strip()

    groups = []
    temp = n
    while temp > 0:
        groups.append(temp % 1000)
        temp //= 1000

    result_parts = []
    highest = len(groups) - 1
    for i in range(highest, -1, -1):
        group = groups[i]
        if group == 0:
            # only say zero group if there is a nonzero lower group
            if i > 0 and any(g != 0 for g in groups[:i]):
                result_parts.append("không " + suffixes[i])
            continue

        group_words = three_digits_to_words(group, is_first_group=(i == highest))
        if suffixes[i]:
            result_parts.append((group_words + " " + suffixes[i]).strip())
        else:
            result_parts.append(group_words)

    return " ".join(result_parts).strip()


def main():
    try:
        text = input("Nhập số nguyên: ")
        n = int(text.strip())
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")
        return

    print(spell_integer(n))


if __name__ == "__main__":
    main()