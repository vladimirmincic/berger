column = ""

# Enter names of teams
ekipa_1 = "aaaaaaaaaa"
ekipa_2 = "bbbbbbbbbb"
ekipa_3 = "cccccccccc"
ekipa_4 = "dddddddddd"
ekipa_5 = "eeeeeeeeee"
ekipa_6 = "ffffffffff"
ekipa_7 = "gggggggggg"
ekipa_8 = "hhhhhhhhhh"
ekipa_9 = "iiiiiiiiii"
ekipa_10 = "jjjjjjjjjj"
ekipa_11 = "kkkkkkkkkk"
ekipa_12 = "llllllllll"
ekipa_13 = "mmmmmmmmmm"
ekipa_14 = "nnnnnnnnnn"

def get_rounds_data(rounds):
    if rounds == 4:
        return [
            [column],
            ["Kolo 1", f"{ekipa_1}-{ekipa_4}", f"{ekipa_2}-{ekipa_3}"],
            ["Kolo 2", f"{ekipa_4}-{ekipa_3}", f"{ekipa_1}-{ekipa_2}"],
            ["Kolo 3", f"{ekipa_2}-{ekipa_4}", f"{ekipa_3}-{ekipa_1}"]
        ]
    if rounds == 6:
        return [
            [column],
            ["Kolo 1", f"{ekipa_1}-{ekipa_6}", f"{ekipa_2}-{ekipa_5}", f"{ekipa_3}-{ekipa_4}"],
            ["Kolo 2", f"{ekipa_6}-{ekipa_4}", f"{ekipa_5}-{ekipa_3}", f"{ekipa_1}-{ekipa_2}"],
            ["Kolo 3", f"{ekipa_2}-{ekipa_6}", f"{ekipa_3}-{ekipa_1}", f"{ekipa_4}-{ekipa_5}"],
            ["Kolo 4", f"{ekipa_6}-{ekipa_5}", f"{ekipa_1}-{ekipa_4}", f"{ekipa_2}-{ekipa_3}"],
            ["Kolo 5", f"{ekipa_3}-{ekipa_6}", f"{ekipa_4}-{ekipa_2}", f"{ekipa_5}-{ekipa_1}"],
        ]
    if rounds == 8:
        return [
            [column],
            ["Kolo 1", f"{ekipa_1}-{ekipa_8}", f"{ekipa_2}-{ekipa_7}", f"{ekipa_3}-{ekipa_6}", f"{ekipa_4}-{ekipa_5}"],
            ["Kolo 2", f"{ekipa_8}-{ekipa_5}", f"{ekipa_6}-{ekipa_4}", f"{ekipa_7}-{ekipa_3}", f"{ekipa_1}-{ekipa_2}"],
            ["Kolo 3", f"{ekipa_2}-{ekipa_8}", f"{ekipa_3}-{ekipa_1}", f"{ekipa_4}-{ekipa_7}", f"{ekipa_5}-{ekipa_6}"],
            ["Kolo 4", f"{ekipa_8}-{ekipa_6}", f"{ekipa_7}-{ekipa_5}", f"{ekipa_1}-{ekipa_4}", f"{ekipa_2}-{ekipa_3}"],
            ["Kolo 5", f"{ekipa_3}-{ekipa_8}", f"{ekipa_4}-{ekipa_2}", f"{ekipa_5}-{ekipa_1}", f"{ekipa_6}-{ekipa_7}"],
            ["Kolo 6", f"{ekipa_8}-{ekipa_7}", f"{ekipa_1}-{ekipa_6}", f"{ekipa_2}-{ekipa_5}", f"{ekipa_3}-{ekipa_4}"],
            ["Kolo 7", f"{ekipa_4}-{ekipa_8}", f"{ekipa_5}-{ekipa_3}", f"{ekipa_6}-{ekipa_2}", f"{ekipa_7}-{ekipa_1}"],
        ]
    if rounds == 10:
        return [
            [column],
            ["Kolo 1", f"{ekipa_1}-{ekipa_10}", f"{ekipa_2}-{ekipa_9}", f"{ekipa_3}-{ekipa_8}", f"{ekipa_4}-{ekipa_7}", f"{ekipa_5}-{ekipa_6}"],
            ["Kolo 2", f"{ekipa_10}-{ekipa_6}", f"{ekipa_7}-{ekipa_5}", f"{ekipa_8}-{ekipa_4}", f"{ekipa_9}-{ekipa_3}", f"{ekipa_1}-{ekipa_2}"],
            ["Kolo 3", f"{ekipa_2}-{ekipa_10}", f"{ekipa_3}-{ekipa_1}", f"{ekipa_4}-{ekipa_9}", f"{ekipa_5}-{ekipa_8}", f"{ekipa_6}-{ekipa_7}"],
            ["Kolo 4", f"{ekipa_10}-{ekipa_7}", f"{ekipa_8}-{ekipa_6}", f"{ekipa_9}-{ekipa_5}", f"{ekipa_1}-{ekipa_4}", f"{ekipa_2}-{ekipa_3}"],
            ["Kolo 5", f"{ekipa_3}-{ekipa_10}", f"{ekipa_4}-{ekipa_2}", f"{ekipa_5}-{ekipa_1}", f"{ekipa_6}-{ekipa_9}", f"{ekipa_7}-{ekipa_8}"],
            ["Kolo 6", f"{ekipa_10}-{ekipa_8}", f"{ekipa_9}-{ekipa_7}", f"{ekipa_1}-{ekipa_6}", f"{ekipa_2}-{ekipa_5}", f"{ekipa_3}-{ekipa_4}"],
            ["Kolo 7", f"{ekipa_4}-{ekipa_10}", f"{ekipa_5}-{ekipa_3}", f"{ekipa_6}-{ekipa_2}", f"{ekipa_7}-{ekipa_1}", f"{ekipa_8}-{ekipa_9}"],
            ["Kolo 8", f"{ekipa_10}-{ekipa_9}", f"{ekipa_1}-{ekipa_8}", f"{ekipa_2}-{ekipa_7}", f"{ekipa_3}-{ekipa_6}", f"{ekipa_4}-{ekipa_5}"],
            ["Kolo 9", f"{ekipa_5}-{ekipa_10}", f"{ekipa_6}-{ekipa_4}", f"{ekipa_7}-{ekipa_3}", f"{ekipa_8}-{ekipa_2}", f"{ekipa_9}-{ekipa_1}"],
        ]
    if rounds == 12:
        return [
            [column],
            ["Kolo 1", f"{ekipa_1}-{ekipa_12}", f"{ekipa_2}-{ekipa_11}", f"{ekipa_3}-{ekipa_10}", f"{ekipa_4}-{ekipa_9}", f"{ekipa_5}-{ekipa_8}", f"{ekipa_6}-{ekipa_7}"],
            ["Kolo 2", f"{ekipa_12}-{ekipa_7}", f"{ekipa_8}-{ekipa_6}", f"{ekipa_9}-{ekipa_5}", f"{ekipa_10}-{ekipa_4}", f"{ekipa_11}-{ekipa_3}", f"{ekipa_1}-{ekipa_2}"],
            ["Kolo 3", f"{ekipa_2}-{ekipa_12}", f"{ekipa_3}-{ekipa_1}", f"{ekipa_4}-{ekipa_11}", f"{ekipa_5}-{ekipa_10}", f"{ekipa_6}-{ekipa_9}", f"{ekipa_7}-{ekipa_8}"],
            ["Kolo 4", f"{ekipa_12}-{ekipa_8}", f"{ekipa_9}-{ekipa_7}", f"{ekipa_10}-{ekipa_6}", f"{ekipa_11}-{ekipa_5}", f"{ekipa_1}-{ekipa_4}", f"{ekipa_2}-{ekipa_3}"],
            ["Kolo 5", f"{ekipa_3}-{ekipa_12}", f"{ekipa_4}-{ekipa_2}", f"{ekipa_5}-{ekipa_1}", f"{ekipa_6}-{ekipa_11}", f"{ekipa_7}-{ekipa_10}", f"{ekipa_8}-{ekipa_9}"],
            ["Kolo 6", f"{ekipa_12}-{ekipa_9}", f"{ekipa_10}-{ekipa_8}", f"{ekipa_11}-{ekipa_7}", f"{ekipa_1}-{ekipa_6}", f"{ekipa_2}-{ekipa_5}", f"{ekipa_3}-{ekipa_4}"],
            ["Kolo 7", f"{ekipa_4}-{ekipa_12}", f"{ekipa_5}-{ekipa_3}", f"{ekipa_6}-{ekipa_2}", f"{ekipa_7}-{ekipa_1}", f"{ekipa_8}-{ekipa_11}", f"{ekipa_9}-{ekipa_10}"],
            ["Kolo 8", f"{ekipa_12}-{ekipa_10}", f"{ekipa_11}-{ekipa_9}", f"{ekipa_1}-{ekipa_8}", f"{ekipa_2}-{ekipa_7}", f"{ekipa_3}-{ekipa_6}", f"{ekipa_4}-{ekipa_5}"],
            ["Kolo 9", f"{ekipa_5}-{ekipa_12}", f"{ekipa_6}-{ekipa_4}", f"{ekipa_7}-{ekipa_3}", f"{ekipa_8}-{ekipa_2}", f"{ekipa_9}-{ekipa_1}", f"{ekipa_10}-{ekipa_11}"],
            ["Kolo 10", f"{ekipa_12}-{ekipa_11}", f"{ekipa_1}-{ekipa_10}", f"{ekipa_2}-{ekipa_9}", f"{ekipa_3}-{ekipa_8}", f"{ekipa_4}-{ekipa_7}", f"{ekipa_5}-{ekipa_6}"],
            ["Kolo 11", f"{ekipa_6}-{ekipa_12}", f"{ekipa_7}-{ekipa_5}", f"{ekipa_8}-{ekipa_4}", f"{ekipa_9}-{ekipa_3}", f"{ekipa_10}-{ekipa_2}", f"{ekipa_11}-{ekipa_1}"],
        ]
    if rounds == 14:
        return [
            [column],
            ["Kolo 1", f"{ekipa_1}-{ekipa_14}", f"{ekipa_2}-{ekipa_13}", f"{ekipa_3}-{ekipa_12}", f"{ekipa_4}-{ekipa_11}", f"{ekipa_5}-{ekipa_10}", f"{ekipa_6}-{ekipa_9}", f"{ekipa_7}-{ekipa_8}"],
            ["Kolo 2", f"{ekipa_14}-{ekipa_8}", f"{ekipa_9}-{ekipa_7}", f"{ekipa_10}-{ekipa_6}", f"{ekipa_11}-{ekipa_5}", f"{ekipa_12}-{ekipa_4}", f"{ekipa_13}-{ekipa_3}", f"{ekipa_1}-{ekipa_2}"],
            ["Kolo 3", f"{ekipa_2}-{ekipa_14}", f"{ekipa_3}-{ekipa_1}", f"{ekipa_4}-{ekipa_13}", f"{ekipa_5}-{ekipa_12}", f"{ekipa_6}-{ekipa_11}", f"{ekipa_7}-{ekipa_10}", f"{ekipa_8}-{ekipa_9}"],
            ["Kolo 4", f"{ekipa_14}-{ekipa_9}", f"{ekipa_10}-{ekipa_8}", f"{ekipa_11}-{ekipa_7}", f"{ekipa_12}-{ekipa_6}", f"{ekipa_13}-{ekipa_5}", f"{ekipa_1}-{ekipa_4}", f"{ekipa_2}-{ekipa_3}"],
            ["Kolo 5", f"{ekipa_3}-{ekipa_14}", f"{ekipa_4}-{ekipa_2}", f"{ekipa_5}-{ekipa_1}", f"{ekipa_6}-{ekipa_13}", f"{ekipa_7}-{ekipa_12}", f"{ekipa_8}-{ekipa_11}", f"{ekipa_9}-{ekipa_10}"],
            ["Kolo 6", f"{ekipa_14}-{ekipa_10}", f"{ekipa_11}-{ekipa_9}", f"{ekipa_12}-{ekipa_8}", f"{ekipa_13}-{ekipa_7}", f"{ekipa_1}-{ekipa_6}", f"{ekipa_2}-{ekipa_5}", f"{ekipa_3}-{ekipa_4}"],
            ["Kolo 7", f"{ekipa_4}-{ekipa_14}", f"{ekipa_5}-{ekipa_3}", f"{ekipa_6}-{ekipa_2}", f"{ekipa_7}-{ekipa_1}", f"{ekipa_8}-{ekipa_13}", f"{ekipa_9}-{ekipa_12}", f"{ekipa_10}-{ekipa_11}"],
            ["Kolo 8", f"{ekipa_14}-{ekipa_11}", f"{ekipa_12}-{ekipa_10}", f"{ekipa_13}-{ekipa_9}", f"{ekipa_1}-{ekipa_8}", f"{ekipa_2}-{ekipa_7}", f"{ekipa_3}-{ekipa_6}", f"{ekipa_4}-{ekipa_5}"],
            ["Kolo 9", f"{ekipa_5}-{ekipa_14}", f"{ekipa_6}-{ekipa_4}", f"{ekipa_7}-{ekipa_3}", f"{ekipa_8}-{ekipa_2}", f"{ekipa_9}-{ekipa_1}", f"{ekipa_10}-{ekipa_13}", f"{ekipa_11}-{ekipa_12}"],
            ["Kolo 10", f"{ekipa_14}-{ekipa_12}", f"{ekipa_13}-{ekipa_11}", f"{ekipa_1}-{ekipa_10}", f"{ekipa_2}-{ekipa_9}", f"{ekipa_3}-{ekipa_8}", f"{ekipa_4}-{ekipa_7}", f"{ekipa_5}-{ekipa_6}"],
            ["Kolo 11", f"{ekipa_6}-{ekipa_14}", f"{ekipa_7}-{ekipa_5}", f"{ekipa_8}-{ekipa_4}", f"{ekipa_9}-{ekipa_3}", f"{ekipa_10}-{ekipa_2}", f"{ekipa_11}-{ekipa_1}", f"{ekipa_12}-{ekipa_13}"],
            ["Kolo 12", f"{ekipa_14}-{ekipa_13}", f"{ekipa_1}-{ekipa_12}", f"{ekipa_2}-{ekipa_11}", f"{ekipa_3}-{ekipa_10}", f"{ekipa_4}-{ekipa_9}", f"{ekipa_5}-{ekipa_8}", f"{ekipa_6}-{ekipa_7}"],
            ["Kolo 13", f"{ekipa_7}-{ekipa_14}", f"{ekipa_8}-{ekipa_6}", f"{ekipa_9}-{ekipa_5}", f"{ekipa_10}-{ekipa_4}", f"{ekipa_11}-{ekipa_3}", f"{ekipa_12}-{ekipa_2}", f"{ekipa_13}-{ekipa_1}"],
        ]
    return []
