#!/usr/bin/env python3
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Prosty program dodający dwie liczby"
    )
    parser.add_argument(
        "a",
        type=float,
        help="Pierwsza liczba (całkowita lub zmiennoprzecinkowa)"
    )
    parser.add_argument(
        "b",
        type=float,
        help="Druga liczba (całkowita lub zmiennoprzecinkowa)"
    )
    args = parser.parse_args()

    wynik = args.a + args.b
    print(wynik)

if __name__ == "__main__":
    main()
