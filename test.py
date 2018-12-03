from clooney_model.run import get_result
import os

resultsrows = [['image name' , 'label']]
    

for imgname in os.listdir(os.path.join("uploads")):
    score  = get_result(f"uploads/{imgname}")
    resultsrows.append([imgname , score])
print(resultsrows)    


        