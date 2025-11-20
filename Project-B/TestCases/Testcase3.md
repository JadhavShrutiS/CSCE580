# AI Testcase (TC) Review 3
_ // This file has a human-written review that the 4 models must evaluate its sentiment

### 1. TC-identifier: 
_ // T3-Review 3, High

### 2. TC-name: 
_ // Review sentiment deciphering- hard level._

### 3. TC-objective: 
-// Objective of the test case is to check what sentiment the trained models provide for a certain review, high complexity.

### 4. TC-input: 
_ // review: "Cannot understand the 1 out of 10 harsh review. 1 means its the worst film you have ever seen which this is not. Presumably its either because they were  offended by the film being directed, written and acted by a woman who was married to Elon Musk and is giving it the silver spoon brush off or either offended at a Scottish movie with mostly English actors in it, who knows but the film is worth a watch with your partner as it is most definitely not just a womans movie as I quite enjoyed it and am a bit of an old romantic at heart myself.Its not going to win any oscars but it has some moments of comedy magic in that typical Glasgow way which only us Weegies can fully appreciate. Not a bad effort at all from Talulah Riley at all, its just a shame that people want to bash her because she is the ex of Elon Musk which is a shame as she certainly has acting talent that is for sure and for her first directorial debut it was not half bad."

### 5. TC-reference-output: 
_ // Reference output is the Classical Machine Learning, SVM output: negative
-// Outputs of all models provided in the code, at the end

### 6. TC-harm-risk-info: 
_ // HC1-incorrect-info, HC3-unstable-extrauserinfo, HC4-incomprehensible-ai.

### 7. TC-other-info: 
_ // Humans that create the reviews will have the best idea on the sentiment of the review and what they are trying to portray.
-//The SVM output in this case is actually incorrect, and in reality should be compared with the ground truth of positive sentiment for this
