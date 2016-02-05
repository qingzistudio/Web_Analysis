# Web_Analysis
Including all tasks to extract information from website, quantitative analytic technologies across multiple business domains,and sentiment analysis
=================================================================================

## Grasp information from websites

##### File - Douban_Pageselecting.py

I planed to grasp moive information from douban.com according to the rates, then listed the output that combines web addresses of moives and rates. 

##### File - Get_August_Customer_Reviews.py

The objective of the program is to grasp customers' reviews which wrote at August.

##### File - Frequency_A_Author_Is_Quoted.py

How many times are one author quoted under a post? 

##### File - Reviews_More_Than_1000.py

Collected at least 1000 TV reviews from a websites, like Amazon or Bestbuy, then stored all the reviews in a single file.

Steps:
1. List all links with the amount of reviews are more than 400. Select_Reviews_More_Than_400.py designs a step that collects all addresses and products.

2. Write down 3 functions to grab information like the full reviews, rates and submission dates. 

3. Use a loop for traversing the 3 links and append newly grabbing information to each list.

Problems:
1. The overrate and customer’s rates share the same HTML tag on each review page

2. If a customers wrote down 2 or more paragraphs, more details will be involved in our processing.

3. Lists(ratinglist, reviewslist, datelist) should be preprocessed before write into a txt file: a encoding problem (\xa3); duplicated information; useless information

## Sentiment Analysis

##### File - Tokenize_Sentences_Into_Trigram.py

The most important part of sentiment analysis is to detect pattern behind the content, which can input from local computer, or automatically grasp from websites. The first step is to prepocess the origin dataset, like converting to lower case, avoiding some words, and then we will split our articles into sentences for further explore. After retrieving sentence sets, we will tokenize the sentences into single words, bigrams or trigrams, generally, they are called features. 

My work is to tokenize sentences and to select trigrams that are organized by at least 2 nones. 


				
				
