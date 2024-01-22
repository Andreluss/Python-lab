if __name__ == '__main__':
    dane_full = [1, "to", 23, "nie", [12, [], [[2]], "było", -12, "trudne", False, [1, 2, [3]]]]

    print()



    def count_sum(pos, dane):
        if not(pos < len(dane)):
            return 0

        x = 0
        if type(dane[pos]) == int:
            x += dane[pos]
        elif type(dane[pos]) == list:
            x += count_sum(0, dane[pos])

        x += count_sum(pos+1, dane)

        return x


    print(count_sum(0, dane_full))



