import csv
import pandas as pd

book_file = open('100_books.txt', 'r')
file_list = book_file.readlines()

cleaned_list = [item.replace("\n", "").replace(" â€", "").replace("Want to Read", "").replace("Rate this book", "") \
    .replace("1 of 5 stars", "").replace("2 of 5 stars", "").replace("5 of 5 stars", "").replace("3 of 5 stars", "") \
    .replace("4 of 5 stars", "").replace("really liked it", "").replace("rating” ", "rating ") for item in file_list] # Cleaning

cleaned_list2 = list(filter(None, cleaned_list)) # Remove empty values

cleaned_list3 = [i.split(', and ') for i in cleaned_list2]
#print(cleaned_list3)

title_list = []
author_list = []
avg_and_num_rating = [] # Split these into 2 diffrent elements
num_ratings = []

counter = 0

# Title list
for i in cleaned_list3:
    if counter == 1:
        title_list.append(i)
    counter += 1
    if counter == 5:
        counter = 0

#Author list
for i in cleaned_list3:
    if counter == 2:
        author_list.append(i)
    counter += 1
    if counter == 5:
        counter = 0

#Avg rating list
for i in cleaned_list3:
    if counter == 3:
        avg_and_num_rating.append(i)
    counter += 1
    if counter == 5:
        counter = 0

avg = avg_and_num_rating[0][0].split()
avg = avg[0]

print(avg)

#print(avg_and_num_rating)

# clean_avg_num_rating = [i.replace("rating” ", "rating ") for i in avg_and_num_rating]

# print(clean_avg_num_rating)

#print(avg_rating)

# for i in cleaned_list3:
#     print(i)

# avg_and_num_rating_string = avg_and_num_rating.join(',')

# avg_and_num_rating2 = [l.split('###') for l in ''.join(avg_and_num_rating)]



book_file.close()



#--------------------------------------------
# Playing with CSV files
# with open("100_clean_books.csv", "w", newline="") as clean_file:
#     writer = csv.writer(clean_file)
#     writer.writerow(["Rank", "Title", "Author", "Avg rating", "Ratings", "Score"])
#     writer.writerow(["1", "A Game of Thrones (A Song of Ice and Fire #1)", "by George R.R. Martin", 4.44, 2083888, 676923])

#-------------------------------------------
    # for j in i:
    #     if j == 'by':
    #         # print("yes") # Test if the for loop works
    #         author_list.append(i)
    #     if j
# print(author_list)

    # per_page += 1
    # counter += 1
# counter = 1
# counter+=1
# for i in cleaned_list:
#     cleaned_list = cleaned_list.replace(i, "")
# cleaned_list = [item.replace("â€", "") for item in file_list]
# for i in file_list:
#     file_list.replace("\n", "")
# per_page = 1
# counter = 1
# while per_page != 100:
# print(book_file.readlines())

# # cleaned_list3 = [i.split('" ') for i in cleaned_list3]
#print(cleaned_list2)

# k = 1# k+1
    # if i == int:
    #     title_list.append(i)
# title_list = [title_list.append(i)]
# string_c_list = " ".join(cleaned_list3)
# print(string_c_list)


