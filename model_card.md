# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  MyMusic 1.0

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

its a system that suggests songs based on the users favorite genre mood and energy level. it assumes that songs matching these preferences are likely to be enjoyed by the user. Its designed for experimentation.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Songs earn points and the system recommends based on higher points. 



---

## 4. Data  

Describe the dataset the model uses.  

the model inclsuded 15 songs with different types of music. 

---

## 5. Strengths  

Where does your system seem to work well  
It actually recommends based on perferences instead of throwing random songs. 
---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

during my experiment i noticed that the recommender gives alot of importance to energy levels. When i doubled energy weight and reduced genres weight the recommendation scores changed but the rankings stayed the same for all 3 profiles. This shos that changing the weight doesnt improve recommendations. One limitation is that the system may recommend songs with similar energy levels even if they do not match the users prefered genre. 
---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

I tested 3 different user profiles. each profile recieved 5 song recommendations based on genre mood and energy. I was surprised that doubling the energy weight and reducing the genre weight changed the scores but not the rankings. this showed me that adjusting the score weights does not always change recommendations. 
i noticed that each profile recieved a differnet top recommendation. This suggests that the recommender can distinguish between the 3 profiles but the experiment did not demonstrate an imporvement in recommendation quality. 

---

## 8. Future Work  

Ideas for how you would improve the model next.  

i would like to add more songs and genres. 

---

## 9. Personal Reflection  

 this project helped me understand how music recommendations work. 

 i learned that while github can help me with writing code i still need to verify the code, understand the logic and identify weaknesses. 