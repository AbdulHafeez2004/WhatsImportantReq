from string import punctuation
from spacy.lang.en.stop_words import STOP_WORDS
import spacy
from heapq import nlargest
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Summary


# Create your views here.


def index(request):

    my_summary = None
    if request.method == 'POST':
        full_text = request.POST['full_text']

        if full_text.isnumeric() == True or len(full_text.split()) < 40:
            messages.error(
                request, "There is a problem with your text, it's either completely numeric or too short. Check it and try again.")

        else:
            stopwords = list(STOP_WORDS)

            nlp = spacy.load("en_core_web_sm")

            text = full_text

            doc = nlp(text)

            tokens = [token.text for token in doc]
            # print(tokens)

            # punctuation = punctuation + '\n'

            word_frequencies = {}

            for word in doc:
                if word.text.lower() not in stopwords:
                    if word.text.lower() not in punctuation:
                        if word.text not in word_frequencies.keys():
                            word_frequencies[word.text] = 1
                        else:
                            word_frequencies[word.text] += 1

            # print(word_frequencies)

            max_frequency = max(word_frequencies.values())

            max_frequency

            for word in word_frequencies.keys():
                word_frequencies[word] = word_frequencies[word]/max_frequency
            # print(word_frequencies)

            sentence_tokens = [sent for sent in doc.sents]
            # print(sentence_tokens)

            sentence_scores = {}
            for sent in sentence_tokens:
                for word in sent:
                    if word.text.lower() in word_frequencies.keys():
                        if sent not in sentence_scores.keys():
                            sentence_scores[sent] = word_frequencies[word.text.lower(
                            )]

                        else:
                            sentence_scores[sent] += word_frequencies[word.text.lower()]

            sentence_scores

            select_length = int(len(sentence_tokens)*0.3)
            select_length

            summary = nlargest(select_length, sentence_scores,
                               key=sentence_scores.get)
            summary

            final_summary = [word.text for word in summary]
            final_summary

            summary = ''.join(final_summary)

            # your_summary = Summary.objects.create(
            #     full_text=full_text, summary=summary)
            # your_summary.save()

            messages.info(request, full_text)
            messages.success(request, summary)

    return render(request, 'index.html')


def result(request):
    return render(request, 'result.html')


# C:\Users\abdul\OneDrive\Desktop\extractor>
# -*- coding: utf-8 -*-
"""text-summarization.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BJQWKue-7iU_DHkBNjW8b5OlaHRCstR8
"""


# stopwords = list(STOP_WORDS)
# nlp = spacy.load('en_core_web_sm')

# text = """
# Nestled on the vibrant coastline of West Africa, Lagos, Nigeria, is a destination that tantalizes the senses and captures the essence of African culture. Boasting a rich and iconic history, a bustling metropolis, and its diverse traditions, this captivating city has emerged as a hidden gem for intrepid travelers seeking a unique and unforgettable experience. From its busy markets and mouthwatering cuisine to its breathtaking beaches and pulsating nightlife, Lagos has something to offer every explorer. In this article, we embark on a journey to unravel the wonders of Lagos and delve into the reasons why it should be at the top of your travel bucket list.

# Lagos presents an intriguing blend of ancient history and modern development. With roots dating back to the precolonial era, the city showcases its heritage through landmarks like the National Museum, which houses a remarkable collection of Nigerian art and artifacts. Exploring the iconic Badagry Slave Route offers a sobering glimpse into the transatlantic slave trade's impact on the region's past.
# But Lagos is not just a city stuck in history; it pulsates with contemporary vibrancy. The impressive skyline is gifted with architectural marvels such as the Nigerian National Theatre and the Lekki Conservation Centre, a haven for nature enthusiasts. Additionally, the Eko Atlantic City, an ambitious urban development project, showcases the city's ambition and progress. This harmonious fusion of history and modernity makes Lagos a captivating destination for travelers seeking a multifaceted experience.

# Lagos epitomizes Nigeria's cultural diversity, with over 250 ethnic groups residing in the region. The city acts as a cultural tapestry, where vibrant traditions and customs are intertwined. A visit to the Nike Art Gallery provides an immersive experience of Nigeria's artistic heritage, with its vast collection of contemporary African art.
# Lagos is renowned for its effervescent music scene, especially Afrobeat, a genre popularized by the legendary Fela Kuti. Travelers can groove to the pulsating rhythms at various live music venues, such as the New Afrika Shrine. The annual Lagos Carnival showcases the city's exuberance, with flamboyant parades and colorful costumes that ignite the streets.

# Moreover, Lagos is a gastronomic delight, boasting a diverse culinary landscape. From street-side delicacies like suya (spicy skewered meat) to the flavorful jollof rice and mouthwatering seafood, Lagos offers an explosion of flavors that will leave taste buds wanting more.

# Lagos is blessed with stunning beaches along its coastline, providing an idyllic escape from the city's hustle and bustle. Tarkwa Bay and Elegushi Beach offer serene settings for relaxation, water sports, and picnics. The renowned Lekki Peninsula boasts a stretch of golden sands and crystal-clear waters, perfect for sunbathing and surfing enthusiasts.
# For nature lovers, the Lekki Conservation Centre is a must-visit destination. Spanning over 78 acres, it is home to a diverse species of wildlife, including monkeys, crocodiles, and exotic bird species. Visitors can explore the elevated canopy walkway, which provides breathtaking views of the lush greenery in the area.

# When the sun sets, Lagos comes alive with its vibrant nightlife scene. The city offers an eclectic mix of bars, clubs, and lounges catering to various tastes. Victoria Island and Ikoyi are known for their upscale establishments,while areas like Allen Avenue and Surulere and Jibowu offer a more laid-back atmosphere with live music venues and pubs.
# """

# doc = nlp(text)

# tokens = [token.text for token in doc]
# print(tokens)

# punctuation = punctuation + '\n'
# punctuation

# word_frequencies = {}

# for word in doc:
#     if word.text.lower() not in stopwords:
#         if word.text.lower() not in punctuation:
#             if word.text not in word_frequencies.keys():
#                 word_frequencies[word.text] = 1
#             else:
#                 word_frequencies[word.text] += 1

# print(word_frequencies)

# max_frequency = max(word_frequencies.values())

# max_frequency

# for word in word_frequencies.keys():
#     word_frequencies[word] = word_frequencies[word]/max_frequency
# print(word_frequencies)

# sentence_tokens = [sent for sent in doc.sents]
# print(sentence_tokens)

# sentence_scores = {}
# for sent in sentence_tokens:
#     for word in sent:
#         if word.text.lower() in word_frequencies.keys():
#             if sent not in sentence_scores.keys():
#                 sentence_scores[sent] = word_frequencies[word.text.lower()]

#             else:
#                 sentence_scores[sent] += word_frequencies[word.text.lower()]

# sentence_scores


# select_length = int(len(sentence_tokens)*0.3)
# select_length

# summary = nlargest(select_length, sentence_scores, key=sentence_scores.get)
# summary

# final_summary = [word.text for word in summary]
# final_summary

# summary = ''.join(final_summary)

# print(summary)
