#Answers to Quiz 2
## Shruti Jadhav

1a) The 2 tools picked to compare are: Search, Writing

Base level search:
AI search (ChatGPT)- 2.9 Wh per query
Basic search (Google)- 0.3 Wh per query

After settings
Setting 1: small model size, low batch size, local cloud distance: 1 Wh  
Setting 2: huge model size, low batch size, local cloud distance: 5.2 Wh  
Setting 3: huge model size, low batch size, large cloud distance: 8.5 Wh


Base level Writing:
AI writing assistant- 1.5 Wh per session
Basic text editor- 0.1 Wh per session

After settings
Setting 1: small model size, low batch size, local cloud distance: 0.5 Wh  
Setting 2: huge model size, low batch size, local cloud distance: 2.7 Wh  
Setting 3: huge model size, low batch size, large cloud distance: 4.4 Wh

1b) Average energy difference across the settings for the models above is between 3 to 5 Wh. 
On average the LLM consumes higher energy due to its huge model size with about a jump of average 3 Wh from small to huge LLM model.

Q2.b.c.i. The cleaning I did for the "original_recipe1" is deleting the extra information about the author in the beginning and the license and number at the beginning, and options such as "save PDF"
I had to do less cleaning for "original_recipe2" because it had no such things as "about the author" so the only thing I deleted here is options such as "save PDF" and extra numbers and license floating on top.

Q2.b.c.iii. Three prompts used to get the full R3 file are:
1) For the given text file, provide a complete R3 json file.
2) Output a R3 jason file for this recipe.
3) Provide R3 json.

Q2.b.c.iv: 2 prompts for partial approach
1) provide ingredients in R3 json
2) provide recipe method in R3 json
This case the json files are combined using a simple copy paste approach as mentioned during class time