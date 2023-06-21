from flask import Flask, render_template, request

from bs4 import BeautifulSoup
import requests
import csv


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def homepage():
    """This is where the magic happens"""
    global counter

    if request.method == 'POST':
        logins_list = request.values.getlist("login[]")
        print(f"People: {logins_list}")

        input_include_list = request.form.get("include")
        input_exclude_list = request.form.get("exclude")

        per_page = int(request.form.get("per_page"))
        print(per_page)

        include_list = []
        exclude_list = []

        if input_include_list != "":
            temp = input_include_list.split(",")
            for i in temp:
                include_list.append(i.strip())

        if input_exclude_list != "":
            temp = input_exclude_list.split(",")
            for i in temp:
                exclude_list.append(i.strip())


        print(f"Include: {include_list}")
        print(f"Exclude: {exclude_list}")

        anime_list = main(logins_list)

        filtered_list = []


        if input_include_list != "" and input_exclude_list != "":
            for anime in anime_list:
                if all(tag in anime[1][4] for tag in include_list) and all(tag not in anime[1][4] for tag in exclude_list):
                    filtered_list.append(anime)
        elif input_include_list != "":
            for anime in anime_list:
                if all(tag in anime[1][4] for tag in include_list):
                    filtered_list.append(anime)
        elif input_exclude_list != "":
            for anime in anime_list:
                if all(tag not in anime[1][4] for tag in exclude_list):
                    filtered_list.append(anime)
        else:
            filtered_list = anime_list

        shorted_filtered_list = filtered_list[:per_page]

        return render_template("index.html", logins=logins_list, anime_list=shorted_filtered_list, include_list=include_list, exclude_list=exclude_list)

    else:
        return render_template("index.html")


    #         symbol = request.form.get("symbol")
    #  if add button is pressed, add another text box
    #  if submit button is pressed, get values from text boxes



# TODO:
# make a button for adding more input boxes for each user (also deleting them?) X
# make submit button x
# recieve info x
# get their anime-planet info and print a table x
# sort and filter
# reroute request to client







# Functionality:

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/50.0.2661.102 Safari/537.36'}

title_list = []

# title: [how many people have seen it, rating (1-5)
anime_dict = dict()

# logins_list = ["Dominik", "Szarakpl"]


def main(logins_list):
    read_csv()
    for i in logins_list:
        read_pages(i, 1, 0)

    # name = input("Please input second Anime-planet.com login: ")
    # read_pages(name, 1, 0)

    sorted_dict = sorted(anime_dict.items(), key=lambda x: (x[1][0], -x[1][1]))  # this outputs a tuple

    counter = 0

    for i in sorted_dict:
        x = i[1][4].replace("[","").replace("]","").split(",")

        pretty_tags = []

        for i in x:
            y = i.strip().strip("'")
            pretty_tags.append(y)

        sorted_dict[counter][1][4] = pretty_tags
        counter += 1

    return sorted_dict



    # counter = 0
    # for i in sorted_dict:
    #     if counter == 20:
    #         break
    #     print(f"{i[0]}, {i[1][0]}, {i[1][1]}")
    #     counter += 1

    # for key, value in sorted_dict[0].items():
    #     print(key, value)

    # I can sort it in html later on


def read_csv():
    with open('anime.csv', 'r', encoding="utf8") as csvfile:
        anime_reader = csv.reader(csvfile)
        for row in anime_reader:
            anime_dict[row[1]] = [0, float(row[5]), row[2], row[4], row[6]]


def read_pages(name, page_number, anime_id):
    url = f"https://www.anime-planet.com/users/{name}" \
          f"/anime/watched?sort=average&order=desc&mylist_view=list&per_page=560&page={page_number}"
    page = requests.get(url, headers=headers)
    watched_list_soup = BeautifulSoup(page.text, "html.parser")
    lists = watched_list_soup.find_all("a", class_="tooltip")
    for item in lists:
        if item.text == "":
            pass
        else:
            anime_id += 1
            # print(f"{anime_id}. {item.text}")
            # title_list.append(item.text)
            if item.text in anime_dict:
                anime_dict[item.text][0] += 1

    if anime_id % 560 == 0:
        page_number += 1
        read_pages(name, page_number, anime_id)



# TODO:
# split the sorted dict to be only 20 items long X
# feed those items into website X