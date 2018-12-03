from clooney_model.run import get_result , get_batch
import os


def test1():
    resultsrows = [['image name' , 'label']]
        

    for imgname in os.listdir(os.path.join("uploads")):
        score  = get_result(f"uploads/{imgname}")
        resultsrows.append([imgname , score])
    print(resultsrows)    

def test_batch():
    return get_batch()


print(test_batch())
print(test_batch())
        