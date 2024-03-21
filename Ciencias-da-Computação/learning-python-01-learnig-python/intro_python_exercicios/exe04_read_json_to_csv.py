import json
import csv


def retrieve_books(file):
    with open(file) as file:
        return json.load(file)


def count_books_by_categories(books):
    categories = {}
    for book in books:
        for category in book["categories"]:
            if not categories.get(category):
                categories[category] = 1
            categories[category] += 1
    return categories


def calculate_percentage_by_category(book_count_by_categpry, total_books):
    return [
        [category, num_books / total_books]
        for category, num_books in book_count_by_categpry.items()
    ]


def write_csv_report(file, header, rows):
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(rows)


if __name__ == "__main__":
    books = retrieve_books("books_json_format.json")

    count_books = count_books_by_categories(books)

    calculate_percentage = calculate_percentage_by_category(count_books, len(books))

    header = ["categories", "percentage"]
    with open("report_csv.csv", "w") as file:
        write_csv_report(file, header, calculate_percentage)
